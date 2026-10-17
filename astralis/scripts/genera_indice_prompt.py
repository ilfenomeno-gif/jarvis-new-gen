"""Generate or check the derived prompt selection index for Astralis 3.X only."""
import argparse
import hashlib
import json
import re
from pathlib import Path

from verifica_catalogo_prompt import read_metadata

SELECTION_FIELDS = {
    "intents", "use_when", "avoid_when", "materials", "examples", "related",
}


def validate_selection(selection):
    if not isinstance(selection, dict) or set(selection) != SELECTION_FIELDS:
        raise ValueError("criteri di selezione incompleti")
    for key in SELECTION_FIELDS - {"related"}:
        if not isinstance(selection[key], list) or not selection[key]:
            raise ValueError(f"criterio vuoto o non valido: {key}")
        if not all(isinstance(value, str) and value.strip() for value in selection[key]):
            raise ValueError(f"valori non validi: {key}")
    if not isinstance(selection["related"], list):
        raise ValueError("related deve essere una lista")
    for item in selection["related"]:
        if not isinstance(item, dict) or set(item) != {"id", "when"}:
            raise ValueError("relazione incompleta")
        if not all(isinstance(value, str) and value.strip() for value in item.values()):
            raise ValueError("relazione non valida")


def build_index(hub):
    readme = (hub / "README.md").read_text(encoding="utf-8")
    version = re.search(r"(?m)^# Versione:\s*(\d+\.\d+\.\d+)", readme)
    if not version or version.group(1).split(".")[0] != "3":
        raise ValueError("Questo strumento si applica solo a un Master Hub Astralis 3.X")
    entries, seen = [], set()
    for path in sorted((hub / "prompts").rglob("*.md")):
        if path.parent == hub / "prompts":
            continue
        metadata = read_metadata(path.read_text(encoding="utf-8"))
        if metadata.get("schema") != 2:
            raise ValueError(f"Metadati schema 2 richiesti: {path.name}")
        validate_selection(metadata.get("selection"))
        if metadata["id"] in seen:
            raise ValueError(f"Identificativo duplicato: {metadata['id']}")
        seen.add(metadata["id"])
        entries.append({
            key: metadata[key] for key in (
                "id", "title", "revision", "category", "protocols", "domains",
                "mode", "requires", "selection",
            )
        } | {
            "path": path.relative_to(hub / "prompts").as_posix(),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        })
    if not entries:
        raise ValueError("Nessun prompt canonico disponibile")
    for entry in entries:
        for related in entry["selection"]["related"]:
            if related["id"] not in seen or related["id"] == entry["id"]:
                raise ValueError(f"Relazione non risolta o autoreferenziale: {entry['id']}")
    return {
        "schema": 1,
        "applies_to": "ASTRALIS 3.X",
        "framework_baseline": version.group(1),
        "catalog_revision": "1.3.0",
        "source": "frontmatter dei prompt canonici; indice derivato, non modificare a mano",
        "selection_policy": "leggere la scheda v3, valutare obiettivo e materiali, verificare il candidato; nessuna attivazione automatica",
        "prompts": sorted(entries, key=lambda entry: entry["id"]),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hub-root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--check", action="store_true", help="Verifica l'indice senza scrivere")
    args = parser.parse_args()
    try:
        index = build_index(args.hub_root.resolve())
        path = args.hub_root / "prompts/INDICE_SELEZIONE.json"
        if args.check:
            current = json.loads(path.read_text(encoding="utf-8"))
            if current != index:
                raise ValueError("Indice non aggiornato: rigenerare dopo aver modificato i prompt")
            print(f"[PASS] Indice Astralis 3.X aggiornato: {len(index['prompts'])} prompt")
        else:
            content = json.dumps(index, ensure_ascii=False, indent=2) + "\n"
            with path.open("w", encoding="utf-8", newline="\r\n") as handle:
                handle.write(content)
            print(f"[OK] Indice Astralis 3.X generato: {len(index['prompts'])} prompt")
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"[FAIL] {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
