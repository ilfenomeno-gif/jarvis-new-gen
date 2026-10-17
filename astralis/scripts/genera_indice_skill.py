"""Generate or verify the skill catalog of an Astralis 3.X Master Hub."""
import argparse
import hashlib
import json
import re
from pathlib import Path


def read_skill(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise ValueError(f"Frontmatter mancante: {path}")
    fields = {}
    for line in match.group(1).splitlines():
        key, separator, value = line.partition(":")
        if not separator or key in fields:
            raise ValueError(f"Frontmatter non valido: {path}")
        fields[key] = json.loads(value.strip())
    if set(fields) != {"name", "description", "metadata"}:
        raise ValueError(f"Campi non previsti: {path}")
    name = fields["name"]
    if not isinstance(name, str) or not re.fullmatch(r"astralis-v3-[a-z0-9-]{1,50}", name) or name != path.parent.name:
        raise ValueError(f"Nome non valido: {path}")
    if not isinstance(fields["description"], str) or not fields["description"].strip():
        raise ValueError(f"Descrizione vuota: {path}")
    meta = fields["metadata"]
    required = {"id", "revision", "applies_to", "category", "protocols", "intents", "use_when", "avoid_when", "materials", "prompt_ids", "sources"}
    if not isinstance(meta, dict) or set(meta) != required or meta["applies_to"] != "ASTRALIS 3.X":
        raise ValueError(f"Metadati v3 incompleti: {path}")
    if not isinstance(meta["id"], str) or not re.fullmatch(r"AST-S-[A-Z0-9-]+", meta["id"]):
        raise ValueError(f"ID non valido: {path}")
    if not isinstance(meta["revision"], str) or not re.fullmatch(r"\d+\.\d+\.\d+", meta["revision"]):
        raise ValueError(f"Revisione non valida: {path}")
    if not isinstance(meta["category"], str) or not meta["category"].strip():
        raise ValueError(f"Categoria vuota: {path}")
    if not isinstance(meta["protocols"], list) or not meta["protocols"] or not all(type(v) is int and 1 <= v <= 12 for v in meta["protocols"]):
        raise ValueError(f"Raccordo ai protocolli non valido: {path}")
    for field in ("intents", "use_when", "avoid_when", "materials", "prompt_ids", "sources"):
        values = meta[field]
        if not isinstance(values, list) or not all(isinstance(v, str) and v.strip() for v in values):
            raise ValueError(f"Lista non valida {field}: {path}")
        if field in {"intents", "use_when", "avoid_when", "materials"} and not values:
            raise ValueError(f"Criterio vuoto {field}: {path}")
    return fields


def build_index(hub):
    version = re.search(r"(?m)^# Versione:\s*(\d+\.\d+\.\d+)", (hub / "README.md").read_text(encoding="utf-8"))
    if not version or version.group(1).split(".")[0] != "3":
        raise ValueError("Catalogo applicabile soltanto ad Astralis 3.X")
    # Use canonical prompt metadata, not a potentially stale derived index.
    from genera_indice_prompt import build_index as build_prompts
    prompts = {entry["id"] for entry in build_prompts(hub)["prompts"]}
    root = hub / "skills"
    source_names = {name for p in root.glob("*/SKILL.md") for name in read_skill(p)["metadata"]["sources"]}
    entries, ids = [], set()
    for path in sorted(root.glob("*/SKILL.md")):
        data = read_skill(path)
        meta = data["metadata"]
        if meta["id"] in ids:
            raise ValueError(f"ID duplicato: {meta['id']}")
        ids.add(meta["id"])
        if not set(meta["prompt_ids"]) <= prompts or not set(meta["sources"]) <= source_names:
            raise ValueError(f"Riferimenti non risolti: {path}")
        entries.append({"name": data["name"], "description": data["description"], **meta,
                        "path": path.relative_to(root).as_posix(),
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    if not entries:
        raise ValueError("Catalogo skill vuoto")
    if len(list(root.rglob("SKILL.md"))) != len(entries):
        raise ValueError("Skill annidate non indicizzate: usare una cartella per skill")
    return {"schema": 1, "applies_to": "ASTRALIS 3.X", "framework_baseline": version.group(1),
            "catalog_revision": "1.3.0", "skills": sorted(entries, key=lambda e: e["id"])}


def verify_sources(hub, source_root):
    manifest = json.loads((hub / "skills/PROVENIENZA.json").read_text(encoding="utf-8"))
    root = source_root.resolve()
    for entry in manifest["sources"]:
        path = (root / entry["file"]).resolve()
        if path.parent != root or hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
            raise ValueError(f"Sorgente modificata o percorso non valido: {entry['file']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hub-root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--source-root", type=Path, help="Verifica anche gli hash degli originali")
    args = parser.parse_args()
    try:
        hub = args.hub_root.resolve()
        index = build_index(hub)
        path = hub / "skills/INDICE_SELEZIONE.json"
        if args.check:
            if json.loads(path.read_text(encoding="utf-8")) != index:
                raise ValueError("Indice skill non aggiornato")
        else:
            with path.open("w", encoding="utf-8", newline="\r\n") as handle:
                handle.write(json.dumps(index, ensure_ascii=False, indent=2) + "\n")
        if args.source_root:
            verify_sources(hub, args.source_root)
        print(f"[PASS] Catalogo Astralis 3.X: {len(index['skills'])} skill")
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"[FAIL] {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
