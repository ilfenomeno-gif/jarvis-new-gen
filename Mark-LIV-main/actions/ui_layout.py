"""Lets Jarvis change the HUD layout. UI only: no data is read or written."""

import json

from core.ui_panels import PANELS, WORKSPACES

_MODES = ("focus_on", "focus_off", "focus_toggle", "toggle_panel", "workspace", "status")


def ui_layout(parameters: dict, player=None, **_ignored) -> str:
    params = parameters or {}
    mode = str(params.get("mode", "")).strip().lower()
    if mode not in _MODES:
        return f"Unknown mode '{mode}'. Use one of: {', '.join(_MODES)}."
    if player is None or not hasattr(player, "set_focus_mode"):
        return "The interface is not available."

    if mode in ("focus_on", "focus_off", "focus_toggle"):
        active = {
            "focus_on": True,
            "focus_off": False,
            "focus_toggle": not player.focus_mode,
        }[mode]
        player.set_focus_mode(active)
        return "Focus mode on: side panels hidden." if active else "Focus mode off: side panels shown."

    if mode == "status":
        return json.dumps(player.panel_status())

    if mode == "workspace":
        name = str(params.get("workspace", "")).strip().lower()
        if name not in WORKSPACES:
            return f"Unknown workspace '{name}'. Use one of: {', '.join(WORKSPACES)}."
        player.apply_workspace(name)
        return f"Workspace '{name}' applied."

    panel = str(params.get("panel", "")).strip().lower()
    if panel not in PANELS:
        return f"Unknown panel '{panel}'. Use one of: {', '.join(PANELS)}."
    visible = params.get("visible")
    if not isinstance(visible, bool):
        visible = not player.panel_status()["panels"][panel]
    player.set_panel_visible(panel, visible)
    return f"Panel '{panel}' {'shown' if visible else 'hidden'}."


TOOL = {
    "name": "ui_layout",
    "description": (
        "Changes the HUD layout. mode=focus_on/focus_off/focus_toggle hides or "
        "restores the side panels. mode=workspace with workspace=full|focus|"
        "coding|recon applies a preset. mode=toggle_panel with panel="
        "header|left|right|content|footer and optional visible=true|false shows "
        "or hides one panel. mode=status reports what is visible."
    ),
    "risk_class": "read",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "mode": {"type": "STRING", "description": ", ".join(_MODES)},
            "workspace": {"type": "STRING", "description": ", ".join(WORKSPACES)},
            "panel": {"type": "STRING", "description": ", ".join(PANELS)},
            "visible": {"type": "BOOLEAN", "description": "Omit to toggle."},
        },
        "required": ["mode"],
    },
    "handler": ui_layout,
}
