"""Restricted terminal utilities; arbitrary shell commands are never executed."""
from __future__ import annotations

import re
import time
from datetime import datetime
from pathlib import Path
from typing import Any

MAX_TIMEOUT_SECONDS = 30
MAX_OUTPUT_LENGTH = 4000
TRUNCATION_MARKER = "\n[...output troncato]"

_DENYLIST = (
    ("rm -rf", re.compile(r"\brm\s+-rf\b", re.IGNORECASE)),
    ("del /f /s", re.compile(r"\bdel\s+/f\s+/s\b", re.IGNORECASE)),
    ("format", re.compile(r"\bformat(?:\.com)?\b", re.IGNORECASE)),
    ("shutdown", re.compile(r"\bshutdown(?:\.exe)?\b", re.IGNORECASE)),
    ("reg delete", re.compile(r"\breg\s+delete\b", re.IGNORECASE)),
    (
        "Remove-Item -Recurse -Force",
        re.compile(
            r"\bremove-item\b(?=[\s\S]*-recurse)(?=[\s\S]*-force)",
            re.IGNORECASE,
        ),
    ),
    ("rd /s /q", re.compile(r"\brd\s+/s\s+/q\b", re.IGNORECASE)),
)


def _truncate(value: str) -> str:
    if len(value) <= MAX_OUTPUT_LENGTH:
        return value
    return value[:MAX_OUTPUT_LENGTH] + TRUNCATION_MARKER


def _result(stdout: str = "", stderr: str = "", returncode: int = 0) -> dict[str, Any]:
    return {
        "stdout": _truncate(stdout),
        "stderr": _truncate(stderr),
        "returncode": returncode,
    }


def terminal_run(parameters: dict | None = None, **_context: Any) -> dict[str, Any]:
    values = parameters or {}
    command = values.get("command")
    if not isinstance(command, str) or not command.strip():
        return _result(stderr="command must be a non-empty string", returncode=2)

    for label, pattern in _DENYLIST:
        if pattern.search(command):
            if values.get("confirmed") is True:
                return _result(
                    stderr="Destructive commands are not supported by terminal_run.",
                    returncode=2,
                )
            return {
                "result": "Ask the user for explicit confirmation",
                "matched": label,
            }

    timeout = values.get("timeout", 30)
    if (
        isinstance(timeout, bool)
        or not isinstance(timeout, int)
        or timeout < 1
        or timeout > MAX_TIMEOUT_SECONDS
    ):
        return _result(
            stderr=f"timeout must be an integer between 1 and {MAX_TIMEOUT_SECONDS}",
            returncode=2,
        )

    cwd = values.get("cwd")
    if cwd is not None and not isinstance(cwd, str):
        return _result(stderr="cwd must be a directory path string", returncode=2)
    working_directory = Path(cwd).expanduser() if cwd else Path.cwd()
    if not working_directory.is_dir():
        return _result(stderr="cwd is not an existing directory", returncode=2)

    command = command.strip()
    echo = re.fullmatch(r"echo(?:\s+(.*))?", command, re.IGNORECASE | re.DOTALL)
    if echo:
        output = echo.group(1) or ""
        if len(output) >= 2 and output[0] == output[-1] and output[0] in {"'", '"'}:
            output = output[1:-1]
        return _result(stdout=output + "\n")

    if re.fullmatch(r"(?:pwd|Get-Location)", command, re.IGNORECASE):
        return _result(stdout=str(working_directory.resolve()) + "\n")

    if re.fullmatch(r"Get-Date", command, re.IGNORECASE):
        return _result(stdout=datetime.now().astimezone().isoformat(timespec="seconds") + "\n")

    sleep = re.fullmatch(r"sleep\s+(\d+(?:\.\d+)?)", command, re.IGNORECASE)
    if sleep:
        duration = float(sleep.group(1))
        if duration > MAX_TIMEOUT_SECONDS:
            return _result(
                stderr=f"sleep is limited to {MAX_TIMEOUT_SECONDS} seconds",
                returncode=2,
            )
        if duration > timeout:
            time.sleep(timeout)
            return _result(stderr="timeout", returncode=-1)
        time.sleep(duration)
        return _result()

    return _result(
        stderr="Unsupported command. Allowed: echo, pwd, Get-Location, Get-Date, sleep.",
        returncode=2,
    )


TOOL = {
    "name": "terminal_run",
    "description": (
        "Runs a limited allowlist of safe local utilities (echo, pwd, Get-Location, "
        "Get-Date, sleep). Does not execute arbitrary shell commands."
    ),
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "command": {"type": "STRING"},
            "cwd": {"type": "STRING"},
            "timeout": {"type": "INTEGER", "default": 30},
        },
        "required": ["command"],
    },
    "risk_class": "write",
    "handler": terminal_run,
}
