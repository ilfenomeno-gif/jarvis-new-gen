"""Read-only validation of Astralis prompt metadata, links and source preservation."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote

FIELDS = {
    "schema", "id", "title", "revision", "status", "category", "protocols",
    "domains", "mode", "requires", "sources", "selection",
}
MODES = {
    "consultiva", "verifica_senza_correzione", "esecuzione_su_mandato",
    "consultiva_con_applicazione_autorizzata", "coordinamento_su_mandato",
    "collaudo_su_mandato_senza_correzione", "dipende_dal_mandato",
}
DOMAINS = {"trasversale", "software", "addon_nvda", "utility", "giochi", "scrittura"}
HEADINGS = (
    "## Scopo e condizioni d'uso", "## Scheda operativa", "## Testo da copiare",
    "## Esempio di attivazione", "## Raccordo futuro con Astralis 4",
)
BLOCK_FIELDS = (
    "CONTESTO E VINCOLI ESSENZIALI", "OBIETTIVO", "INPUT", "PERIMETRO OPERATIVO",
    "PROCEDURA", "RISULTATO ATTESO", "CRITERI DI VERIFICA", "LIMITI E ARRESTO",
)


def read_metadata(text):
    if not text.startswith("---\n"):
        raise ValueError("frontmatter assente")
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        raise ValueError("frontmatter non chiuso")
    metadata = {}
    for line in parts[1].strip().splitlines():
        key, separator, value = line.partition(":")
        if not separator or key in metadata:
            raise ValueError(f"campo duplicato o non valido: {key}")
        metadata[key] = json.loads(value.strip())
    return metadata


def local_links(text, parent):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    for target in re.findall(r"\]\(([^)]+)\)", text):
        target = target.strip().strip("<>")
        if re.match(r"^(?:[a-zA-Z][a-zA-Z0-9+.-]*:|#|/)", target):
            continue
        path = unquote(target.partition("#")[0])
        if path:
            yield (parent / path).resolve()


def validate(hub_root, source_root=None):
    catalog = hub_root / "prompts"
    failures, notes, records = [], [], {}
    paths = sorted(catalog.rglob("*.md"))
    if not paths:
        failures.append("Catalogo assente o vuoto")
    for path in paths:
        relative = path.relative_to(catalog).as_posix()
        data = path.read_bytes()
        if data.startswith(b"\xef\xbb\xbf"):
            failures.append(f"BOM: {relative}")
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            failures.append(f"UTF-8 non valido: {relative}")
            continue
        if re.search(r"(?<!\r)\n", text):
            failures.append(f"LF isolato: {relative}")
        text = text.replace("\r\n", "\n")
        if "\ufffd" in text:
            failures.append(f"Carattere sostitutivo: {relative}")
        if len(re.findall(r"^```", text, flags=re.M)) % 2:
            failures.append(f"Blocco Markdown non chiuso: {relative}")
        for target in local_links(text, path.parent):
            if not target.exists():
                failures.append(f"Link non risolto: {relative} -> {target}")
        if path.parent == catalog:
            continue
        try:
            metadata = read_metadata(text)
            if set(metadata) != FIELDS:
                raise ValueError("campi frontmatter diversi dallo schema 2 v3")
            if type(metadata["schema"]) is not int or metadata["schema"] != 2:
                raise ValueError("schema non supportato")
            from genera_indice_prompt import validate_selection
            validate_selection(metadata["selection"])
            for key in ("id", "title", "revision", "status", "category", "mode"):
                if not isinstance(metadata[key], str) or not metadata[key].strip():
                    raise ValueError(f"stringa non valida: {key}")
            for key in ("protocols", "domains", "requires", "sources"):
                if not isinstance(metadata[key], list):
                    raise ValueError(f"lista non valida: {key}")
            for key in ("domains", "requires", "sources"):
                if not all(isinstance(value, str) and value for value in metadata[key]):
                    raise ValueError(f"elementi non validi: {key}")
            if not re.fullmatch(r"AST-P-[A-Z0-9]+(?:-[A-Z0-9]+)*", metadata["id"]):
                raise ValueError("id non valido")
            if not re.fullmatch(r"\d+\.\d+\.\d+", metadata["revision"]):
                raise ValueError("revisione non valida")
            if metadata["id"] in records:
                raise ValueError("id duplicato")
            if metadata["category"] != path.parent.relative_to(catalog).as_posix():
                raise ValueError("categoria diversa dal percorso")
            if metadata["mode"] not in MODES:
                raise ValueError("modalità non riconosciuta")
            if not metadata["domains"] or not set(metadata["domains"]).issubset(DOMAINS):
                raise ValueError("domini non riconosciuti")
            if not metadata["requires"]:
                raise ValueError("capacità non specificate")
            if any(type(p) is not int or not 1 <= p <= 12 for p in metadata["protocols"]):
                raise ValueError("protocolli fuori dalla matrice v3")
            if any(heading not in text for heading in HEADINGS):
                raise ValueError("sezioni operative mancanti")
            blocks = re.findall(r"```text\n(.*?)\n```", text, re.S)
            if len(blocks) != 1 or any(field not in blocks[0] for field in BLOCK_FIELDS):
                raise ValueError("testo copiabile incompleto o duplicato")
            if metadata["id"] not in blocks[0]:
                raise ValueError("identità mancante nel testo copiabile")
            records[metadata["id"]] = metadata
        except (ValueError, TypeError, KeyError) as error:
            failures.append(f"Metadati/struttura {relative}: {error}")

    index_path = catalog / "README.md"
    if index_path.exists():
        index = index_path.read_text(encoding="utf-8")
        index_targets = set(local_links(index, catalog))
        for path in paths:
            if path.parent != catalog and path.resolve() not in index_targets:
                failures.append(f"Prompt assente dall'indice: {path.relative_to(catalog)}")
    else:
        failures.append("Indice README assente")

    inventory_path = hub_root / "docs/report/allegati/catalogo_prompt_20261003/SORGENTI_E_HASH.json"
    if inventory_path.exists():
        inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
        for item in inventory["sources"]:
            mapped_ids = sorted(ident for ident, record in records.items() if item["file"] in record["sources"])
            if mapped_ids != sorted(item["prompts"]):
                failures.append(f"Provenienza incoerente: {item['file']}")
            if item["origin"] == "master_hub":
                original = inventory_path.parent / "ingressi_precedenti" / item["file"]
            elif source_root is not None:
                original = source_root / item["file"]
            else:
                continue
            if not original.exists() or hashlib.sha256(original.read_bytes()).hexdigest() != item["sha256"]:
                failures.append(f"Sorgente/snapshot non preservato: {item['file']}")
        known_sources = {item["file"] for item in inventory["sources"]}
        for record in records.values():
            for source in record["sources"]:
                if source not in known_sources:
                    failures.append(f"Sorgente non inventariata: {source}")
        if source_root is not None:
            actual = {path.name for path in source_root.glob("*.md") if path.name != "README.md"}
            expected = {item["file"] for item in inventory["sources"] if item["origin"] == "storico"}
            if actual != expected:
                failures.append("Inventario storico incompleto o nuove sorgenti da riconciliare")
            notes.append(f"Hash di {len(actual)} sorgenti storiche verificati")
        else:
            notes.append("Sorgenti storiche non disponibili: hash esterni non controllati")
    else:
        failures.append("Inventario di provenienza assente nel Master Hub")
    try:
        from genera_indice_prompt import build_index
        expected_index = build_index(hub_root)
        selection_index = json.loads((catalog / "INDICE_SELEZIONE.json").read_text(encoding="utf-8"))
        if selection_index != expected_index:
            failures.append("Indice di selezione v3 non aggiornato")
        else:
            notes.append("Indice di selezione v3 coerente con criteri e hash dei prompt")
    except (OSError, ValueError, TypeError, KeyError) as error:
        failures.append(f"Indice di selezione: {error}")
    notes.append(f"{len(records)} prompt canonici; {len(paths)} Markdown del catalogo verificati")
    return failures, notes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hub-root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--source-root", type=Path)
    args = parser.parse_args()
    source_root = args.source_root
    if source_root is None:
        candidate = args.hub_root.parent / "istruzioni per ai" / "prompts"
        source_root = candidate if candidate.is_dir() else None
    failures, notes = validate(args.hub_root.resolve(), source_root)
    for note in notes:
        print(f"[INFO] {note}")
    for failure in failures:
        print(f"[FAIL] {failure}")
    print("[FAIL] Catalogo non conforme" if failures else "[PASS] Catalogo conforme documentalmente")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
