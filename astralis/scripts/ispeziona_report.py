"""Read-only inventory and selective reading of project reports; never infer authority or closure."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


def within(path, root):
    path = path.resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError("Il report deve restare nella radice documentale dichiarata")
    return path


def inspect(path, docs_root):
    path = within(path, docs_root)
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    lines = text.splitlines()
    headings = [{"line": i, "text": line} for i, line in enumerate(lines, 1) if re.match(r"^#{1,6}\s", line)]
    missing = []
    for match in re.finditer(r"\]\(([^)]+)\)", text):
        target = match.group(1).strip().strip("<>")
        if "[" in target or "]" in target or target.startswith(("#", "http:", "https:", "mailto:")):
            continue
        if target.startswith("file:"):
            parts = urlsplit(target)
            if parts.netloc:
                continue  # Do not probe network shares.
            value = unquote(parts.path)
            if re.match(r"^/[A-Za-z]:/", value):
                value = value[1:]
        elif urlsplit(target).scheme and not re.match(r"^[A-Za-z]:[/\\]", target):
            continue
        else:
            value = unquote(target.split("#", 1)[0])
            if not value:
                continue
        # Codex file links may use /C:/path/file.cpp:651. The line suffix is
        # an annotation, not part of the filename; fragments are not checked.
        if re.match(r"^/[A-Za-z]:/", value):
            value = value[1:]
        value = re.sub(r":\d+(?:-\d+)?$", "", value)
        if value.startswith(("\\\\", "//")):
            continue
        resolved = Path(value)
        if not resolved.is_absolute():
            resolved = path.parent / resolved
        if not resolved.exists():
            missing.append({"line": text[:match.start()].count("\n") + 1, "target": target})
    relative = path.relative_to(docs_root.resolve()).as_posix()
    return {"path": relative, "bytes": len(raw), "lines": len(lines),
            "sha256": hashlib.sha256(raw).hexdigest(), "utf8_bom": raw.startswith(b"\xef\xbb\xbf"),
            "location": "archivio" if "archivio" in path.relative_to(docs_root.resolve()).parts else "report_root_or_attachment",
            "heading_count": len(headings), "first_headings": headings[:5], "last_headings": headings[-8:],
            "missing_file_links": missing,
            "authority": "Non determinata: verificare stato datato, contesto, mandato e ambiente corrente"}


def inventory(docs_root):
    root = docs_root.resolve()
    reports = root / "report"
    if not reports.is_dir():
        raise ValueError("docs/report assente: dichiarare la radice documentale effettiva")
    return {"schema": 1, "docs_root": str(root), "mode": "read_only",
            "documents": [inspect(path, root) for path in sorted(reports.rglob("*.md"))]}


def excerpts(path, docs_root, query, limit=8, context=2):
    if not query.strip() or not 1 <= limit <= 30:
        raise ValueError("Query non vuota e limite tra 1 e 30 richiesti")
    lines = within(path, docs_root).read_text(encoding="utf-8-sig").splitlines()
    found = [i for i, line in enumerate(lines) if query.casefold() in line.casefold()]
    return {"match_count": len(found), "truncated": len(found) > limit,
            "excerpts": [{"first_line": max(0, i-context) + 1,
                          "lines": lines[max(0, i-context):i+context+1]} for i in found[:limit]]}


def main():
    # Preserve Unicode headings on Windows terminals and redirected output,
    # independently of the host's legacy console encoding.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs-root", type=Path, required=True)
    parser.add_argument("--report", type=Path, help="Percorso relativo a docs-root")
    parser.add_argument("--query", help="Testo letterale; leggere solo estratti pertinenti")
    parser.add_argument("--limit", type=int, default=8)
    args = parser.parse_args()
    try:
        if args.report:
            path = args.docs_root / args.report
            result = inspect(path, args.docs_root)
            if args.query:
                result["search"] = excerpts(path, args.docs_root, args.query, args.limit)
        else:
            if args.query:
                raise ValueError("La query richiede --report")
            result = inventory(args.docs_root)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, UnicodeError, ValueError) as error:
        print(f"[FAIL] {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
