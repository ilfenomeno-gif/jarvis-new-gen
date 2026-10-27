"""
Verifica automatica del piano in IMPLEMENTAZIONE.md.

    Mark-LIV-main\\.venv\\Scripts\\python.exe verifica.py [--fast] [--phase N]

1. Rilegge la checklist e riporta caselle spuntate/aperte per fase.
2. Esegue controlli reali per ogni fase (file, test, import, git).
3. Incrocia: una fase con caselle tutte spuntate deve avere controlli verdi,
   e ogni percorso citato in una casella spuntata deve esistere.
Esce con codice 1 se qualcosa fallisce. --fast salta npm e la suite completa.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
JARVIS = ROOT / "Mark-LIV-main"
EXT = ROOT / "jarvis-vscode-extension"
PLAN = ROOT / "IMPLEMENTAZIONE.md"
VENV_PY = JARVIS / ".venv" / "Scripts" / "python.exe"
PY = str(VENV_PY if VENV_PY.exists() else sys.executable)

sys.path.insert(0, str(JARVIS))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FAST = False
results: list[tuple[int, str, bool, str]] = []


def run(cmd: list[str], cwd: Path, timeout: int = 600) -> tuple[bool, str]:
    try:
        proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout,
                              shell=(cmd[0] == "npm"))
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, str(exc)
    out = (proc.stdout + proc.stderr).strip()
    return proc.returncode == 0, "\n".join(out.splitlines()[-6:])


def check(phase: int, name: str, ok: bool, detail: str = "") -> None:
    results.append((phase, name, bool(ok), detail))
    print(f"  [{'OK' if ok else 'FAIL'}] {name}" + (f"\n        {detail}" if detail and not ok else ""))


def pytest_files(phase: int, name: str, *files: str) -> None:
    ok, out = run([PY, "-m", "pytest", "-q", *[f"tests/{f}" for f in files]], JARVIS)
    check(phase, name, ok, out)


def exists(phase: int, *paths: str) -> None:
    for rel in paths:
        check(phase, f"esiste {rel}", (JARVIS / rel).exists() or (ROOT / rel).exists())


def git_tracked(rel: str) -> bool:
    out = subprocess.run(["git", "ls-files", rel], cwd=ROOT, capture_output=True, text=True).stdout
    return bool(out.strip())


# ------------------------------------------------------------------ fasi
def phase0() -> None:
    pytest_files(0, "test registry azioni", "test_action_loader.py")
    ci = (ROOT / ".github" / "workflows" / "tests.yml").read_text(encoding="utf-8")
    check(0, "CI contiene job jarvis, gev, vscode-extension",
          all(f"{j}:" in ci for j in ("jarvis", "gev", "vscode-extension")))
    main_src = (JARVIS / "main.py").read_text(encoding="utf-8")
    check(0, "main.py usa discover_actions", "discover_actions" in main_src)
    ext = (EXT / "src" / "extension.ts").read_text(encoding="utf-8")
    check(0, "estensione usa SecretStorage", "context.secrets" in ext)
    ok, out = run([PY, "-m", "py_compile", "main.py"], JARVIS)
    check(0, "main.py compila", ok, out)


def phase1() -> None:
    from core.action_loader import discover_actions
    registry = discover_actions(JARVIS / "actions", logger=lambda _m: None)
    check(1, "azioni migrate scoperte", {"weather_report", "send_message", "reminder"} <= registry.names())
    check(1, "risk_class valido per ogni azione",
          all(registry.risk_class(n) in ("read", "write", "destructive") for n in registry.names()))
    main_src = (JARVIS / "main.py").read_text(encoding="utf-8")
    check(1, "main.py senza rami duplicati dei tool migrati",
          not any(f'elif name == "{n}"' in main_src for n in ("weather_report", "send_message", "reminder")))
    check(1, "main.py senza dichiarazioni duplicate dei tool migrati",
          not any(f'"name": "{n}"' in main_src for n in ("weather_report", "send_message", "reminder")))
    pytest_files(1, "test conferma destructive e discovery", "test_action_loader.py")


def phase2() -> None:
    exists(2, "Mark-LIV-main/core/secret_store.py", "Mark-LIV-main/core/audit_log.py")
    for rel in ("config/secrets.json", "config/audit.jsonl", "config/api_keys.json",
                "config/connectors_state.json", "config/skills_state.json"):
        check(2, f"non tracciato da git: {rel}", not git_tracked(f"Mark-LIV-main/{rel}"))
    if sys.platform == "win32":
        from core.secret_store import DpapiBackend
        backend = DpapiBackend()
        blob = backend.protect(b"verifica")
        check(2, "DPAPI cifra e decifra", blob != b"verifica" and backend.unprotect(blob) == b"verifica")
    pytest_files(2, "test SecretStore, scope, audit, revoca", "test_connectors_skills.py")


def phase3() -> None:
    from core.connectors import ConnectorDescriptor
    catalog = sorted((JARVIS / "connectors" / "catalog").glob("*.json"))
    check(3, "catalogo con almeno 5 connettori", len(catalog) >= 5)
    for path in catalog:
        try:
            ConnectorDescriptor.from_dict(json.loads(path.read_text(encoding="utf-8")))
            ok, detail = True, ""
        except Exception as exc:
            ok, detail = False, str(exc)
        check(3, f"descrittore valido: {path.name}", ok, detail)
    pytest_files(3, "test trasporti MCP e runtime", "test_mcp_and_runtime.py")


def phase4() -> None:
    from core.audit_log import AuditLog
    from core.skills import SkillRegistry
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        skills = SkillRegistry(JARVIS / "skills", Path(tmp) / "s.json", AuditLog(Path(tmp) / "a.jsonl"))
        skills.load()
        check(4, "skill caricate senza errori", not skills.errors and bool(skills.view()), str(skills.errors))
        check(4, "nessuna skill attiva senza approvazione", skills.metadata() == [])
    pytest_files(4, "test skill, gate, riferimenti", "test_connectors_skills.py")


def phase5() -> None:
    from core.action_loader import discover_actions
    names = discover_actions(JARVIS / "actions", logger=lambda _m: None).names()
    check(5, "tool use_skill/connectors_status/connector_call scoperti",
          {"use_skill", "connectors_status", "connector_call"} <= names)
    ok, out = run([PY, "-m", "core.registry_cli", "--help"], JARVIS)
    check(5, "registry_cli risponde a --help", ok, out)
    pytest_files(5, "test router e CLI", "test_connectors_skills.py", "test_mcp_and_runtime.py")


def phase6() -> None:
    from core.action_loader import discover_actions
    from core.mcp_server import McpServer
    registry = discover_actions(JARVIS / "actions", logger=lambda _m: None)
    exposed = {t["name"] for t in McpServer(registry).tools()}
    check(6, "server MCP espone solo tool read di default",
          exposed and all(registry.risk_class(n) == "read" for n in exposed))
    pkg = json.loads((EXT / "package.json").read_text(encoding="utf-8"))
    tools = pkg.get("contributes", {}).get("languageModelTools", [])
    check(6, "estensione dichiara il LM Tool jarvis_ask", any(t["name"] == "jarvis_ask" for t in tools))
    check(6, "estensione richiede VS Code >= 1.101", pkg["engines"]["vscode"].lstrip("^") >= "1.101")
    if not FAST:
        ok, out = run(["npm", "test"], EXT)
        check(6, "estensione: compila e npm test", ok, out)
    pytest_files(6, "test MCP server e VoiceTransport", "test_mcp_and_runtime.py")


PHASES = {0: phase0, 1: phase1, 2: phase2, 3: phase3, 4: phase4, 5: phase5, 6: phase6}


# ------------------------------------------------------------------ checklist
def read_plan() -> dict[int, dict]:
    phases: dict[int, dict] = {}
    current = None
    for line in PLAN.read_text(encoding="utf-8").splitlines():
        header = re.match(r"^## Fase (\d)", line)
        if header:
            current = int(header.group(1))
            phases[current] = {"done": 0, "open": 0, "paths": []}
            continue
        if line.startswith("## "):
            current = None
        item = re.match(r"^- \[([ x])\] (.*)", line)
        if current is None or not item:
            continue
        phases[current]["done" if item.group(1) == "x" else "open"] += 1
        if item.group(1) == "x":
            for token in re.findall(r"`([^`]+)`", item.group(2)):
                if " " not in token and re.search(r"[\\/]|\.(py|json|md|ts|yml)$", token) and "config/" not in token \
                        and not token.startswith(("python", "-")):
                    phases[current]["paths"].append(token)
    return phases


def check_plan(phases: dict[int, dict]) -> None:
    print("\n== Coerenza checklist ==")
    for number, info in phases.items():
        print(f"  Fase {number}: {info['done']} spuntate, {info['open']} aperte")
        for token in info["paths"]:
            if "<" in token:
                continue
            bases = [JARVIS, ROOT, EXT, JARVIS / "core", JARVIS / "actions", JARVIS / "plugins", JARVIS / "tests"]
            found = any(
                any(base.glob(token)) if "*" in token else (base / token).exists() for base in bases
            )
            if not found:
                check(99, f"percorso citato in Fase {number} esiste: {token}", False)
    log = PLAN.read_text(encoding="utf-8")
    check(99, "il log verifiche del piano è presente", "## Log verifiche" in log)


def main() -> int:
    global FAST
    parser = argparse.ArgumentParser()
    parser.add_argument("--fast", action="store_true")
    parser.add_argument("--phase", type=int)
    args = parser.parse_args()
    FAST = args.fast

    phases = read_plan()
    print(f"Piano: {PLAN.name}; interprete: {PY}")
    if not shutil.which("git"):
        print("git non trovato")
        return 1
    for number, func in PHASES.items():
        if args.phase is not None and number != args.phase:
            continue
        print(f"\n== Fase {number} ==")
        try:
            func()
        except Exception as exc:
            check(number, f"fase {number} eseguita senza eccezioni", False, repr(exc))
    if args.phase is None:
        check_plan(phases)
        if not FAST:
            ok, out = run([PY, "-m", "pytest", "-q"], JARVIS)
            check(99, "suite JARVIS completa", ok, out)
        ok, out = run(["git", "diff", "--check"], ROOT)
        check(99, "git diff --check", ok, out)

    failed = [r for r in results if not r[2]]
    print(f"\nRisultato: {len(results) - len(failed)}/{len(results)} controlli OK")
    for phase, name, _, _ in failed:
        print(f"  FALLITO (fase {phase}): {name}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
