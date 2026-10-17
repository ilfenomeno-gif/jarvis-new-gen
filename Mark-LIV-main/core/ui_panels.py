"""Panel visibility state and layout presets for the HUD. No Qt imports."""
from __future__ import annotations

PANELS = ("header", "left", "right", "content", "footer")

WORKSPACES: dict[str, dict[str, bool]] = {
    "full":   {"header": True,  "left": True,  "right": True,  "content": True,  "footer": True},
    "focus":  {"header": True,  "left": False, "right": False, "content": True,  "footer": True},
    "coding": {"header": True,  "left": False, "right": True,  "content": True,  "footer": False},
    "recon":  {"header": False, "left": False, "right": False, "content": True,  "footer": False},
}


class PanelState:
    def __init__(self) -> None:
        self._visible = dict(WORKSPACES["full"])
        self.workspace = "full"

    def visible(self, panel: str) -> bool:
        return self._visible[self._check(panel)]

    def set_visible(self, panel: str, value: bool) -> None:
        self._visible[self._check(panel)] = bool(value)
        self.workspace = "custom"

    def apply_workspace(self, name: str) -> dict[str, bool]:
        key = str(name).strip().lower()
        if key not in WORKSPACES:
            raise ValueError(
                f"Unknown workspace '{name}'. Use one of: {', '.join(WORKSPACES)}."
            )
        self._visible = dict(WORKSPACES[key])
        self.workspace = key
        return dict(self._visible)

    def snapshot(self) -> dict[str, bool]:
        return dict(self._visible)

    @staticmethod
    def _check(panel: str) -> str:
        key = str(panel).strip().lower()
        if key not in PANELS:
            raise ValueError(
                f"Unknown panel '{panel}'. Use one of: {', '.join(PANELS)}."
            )
        return key
