"""Lets Jarvis change the HUD layout. UI only: no data is read or written."""

_MODES = ("focus_on", "focus_off", "focus_toggle")


def ui_layout(parameters: dict, player=None, **_ignored) -> str:
    mode = str((parameters or {}).get("mode", "")).strip().lower()
    if mode not in _MODES:
        return f"Unknown mode '{mode}'. Use one of: {', '.join(_MODES)}."
    if player is None or not hasattr(player, "set_focus_mode"):
        return "The interface is not available."
    active = {
        "focus_on": True,
        "focus_off": False,
        "focus_toggle": not player.focus_mode,
    }[mode]
    player.set_focus_mode(active)
    return "Focus mode on: side panels hidden." if active else "Focus mode off: side panels shown."


TOOL = {
    "name": "ui_layout",
    "description": (
        "Changes the HUD layout. focus_on hides the side panels so only the "
        "central display stays visible; focus_off restores them; focus_toggle "
        "switches."
    ),
    "risk_class": "read",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "mode": {
                "type": "STRING",
                "description": "focus_on, focus_off or focus_toggle",
            }
        },
        "required": ["mode"],
    },
    "handler": ui_layout,
}
