"""
Management CLI for connectors and skills.

    python -m core.registry_cli status
    python -m core.registry_cli connect <connector-id>        # prompts for the token
    python -m core.registry_cli grant <connector-id> <scope> [<scope> ...]
    python -m core.registry_cli revoke <connector-id>
    python -m core.registry_cli skill-diff <skill>
    python -m core.registry_cli skill-approve <skill> --reviewer <name>
    python -m core.registry_cli set-tripo-key                 # hidden prompt, for generate_3d_model
    python -m core.registry_cli set-3d-backend auto|local|tripo
    python -m core.registry_cli download-cad-models           # multi-part CAD models for explode_model

Tokens are read with a hidden prompt, never from argv, and stored via SecretStore.
"""
from __future__ import annotations

import argparse
import getpass
import json
import sys
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.connectors import ConnectorError  # noqa: E402
from core.jarvis_runtime import Runtime, build_runtime  # noqa: E402
from core.skills import SkillError  # noqa: E402


def run(argv: list[str], runtime: Runtime, read_token: Callable[[str], str] = getpass.getpass) -> str:
    parser = argparse.ArgumentParser(prog="registry_cli")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status")
    for name in ("connect", "revoke"):
        sub.add_parser(name).add_argument("connector")
    grant = sub.add_parser("grant")
    grant.add_argument("connector")
    grant.add_argument("scopes", nargs="+")
    sub.add_parser("skill-diff").add_argument("skill")
    migrate = sub.add_parser("migrate-api-key")
    migrate.add_argument("--remove-plain", action="store_true")
    sub.add_parser("set-tripo-key")
    backend_cmd = sub.add_parser("set-3d-backend")
    backend_cmd.add_argument("backend", choices=("auto", "local", "tripo"))
    sub.add_parser("download-cad-models")
    approve = sub.add_parser("skill-approve")
    approve.add_argument("skill")
    approve.add_argument("--reviewer", required=True)
    args = parser.parse_args(argv)

    try:
        if args.command == "status":
            return json.dumps({"connectors": runtime.connectors.view(),
                               "skills": runtime.skills.view()}, indent=2, ensure_ascii=False)
        if args.command == "connect":
            descriptor = runtime.connectors.get(args.connector)
            token = "" if descriptor.auth == "none" else read_token(f"Token for {descriptor.name}: ")
            return f"{descriptor.id}: {runtime.connectors.authenticate(descriptor.id, token)}"
        if args.command == "grant":
            runtime.connectors.grant(args.connector, args.scopes)
            return f"{args.connector}: granted {', '.join(args.scopes)}"
        if args.command == "revoke":
            runtime.connectors.revoke(args.connector)
            return f"{args.connector}: revoked (dependent skills moved to review_required)"
        if args.command == "migrate-api-key":
            from core.api_keys import migrate
            from core.jarvis_runtime import BASE_DIR
            result = migrate(BASE_DIR / "config", runtime.secrets, args.remove_plain)
            return result if result.startswith("error:") else f"gemini_api_key: {result}"
        if args.command == "set-3d-backend":
            from core import model_gen
            model_gen.set_backend(args.backend)
            return f"3D backend: {args.backend}"
        if args.command == "set-tripo-key":
            from core.model_gen import SECRET_NAME
            key = read_token("Tripo API key: ").strip()
            if not key:
                return "error: empty key, nothing stored"
            runtime.secrets.set(SECRET_NAME, key)
            return f"{SECRET_NAME}: stored in the SecretStore"
        if args.command == "download-cad-models":
            from core import cad_models
            results = cad_models.download_cad_models()
            lines = [f"{name}: {outcome}" for name, outcome in results.items()]
            try:
                from core import make_pc_cad
                lines.append(f"pc.glb: generated ({make_pc_cad.make_pc_cad().stat().st_size} bytes)")
            except RuntimeError as exc:
                lines.append(f"pc.glb: skipped ({exc})")
            if any(o.startswith("FAILED") for o in results.values()):
                return "error: some models failed\n" + "\n".join(lines)
            return "\n".join(lines) + "\nSaved in assets/viewer3d/models/cad/ (see NOTICE.txt there)."
        if args.command == "skill-diff":
            return json.dumps(runtime.skills.diff(args.skill), indent=2)
        runtime.skills.approve(args.skill, args.reviewer)
        return f"{args.skill}: approved by {args.reviewer}"
    except (ConnectorError, SkillError) as exc:
        return f"error: {exc}"


def main() -> int:
    output = run(sys.argv[1:], build_runtime())
    print(output)
    return 1 if output.startswith("error:") else 0


if __name__ == "__main__":
    raise SystemExit(main())
