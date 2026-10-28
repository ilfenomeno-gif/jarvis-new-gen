"""Launch Steam games by App ID after explicit user confirmation."""
from __future__ import annotations

import re
from typing import Any

from actions.app_launcher import launch_uri

_APP_ID_PATTERN = re.compile(r"[1-9][0-9]{0,9}\Z")


def launch_steam_game(
    parameters: dict[str, Any] | None = None, **_context: Any
) -> dict[str, Any]:
    values = parameters or {}
    app_id = str(values.get("app_id", "")).strip()
    if not _APP_ID_PATTERN.fullmatch(app_id):
        raise ValueError("app_id must be a positive numeric Steam App ID.")
    if values.get("confirmed") is not True:
        return {
            "result": "Ask the user for explicit confirmation",
            "app_id": app_id,
        }
    return {"result": launch_uri(f"steam://rungameid/{app_id}"), "app_id": app_id}


TOOL = {
    "name": "launch_steam_game",
    "description": (
        "Launch a Steam game by its numeric App ID. Every launch requires explicit "
        "user confirmation in a separate turn. Never use this tool to control a game "
        "after launch."
    ),
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "app_id": {
                "type": "STRING",
                "description": "Positive numeric Steam App ID.",
            },
        },
        "required": ["app_id"],
    },
    "risk_class": "write",
    "handler": launch_steam_game,
}
