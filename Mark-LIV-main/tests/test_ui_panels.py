import os
import sys

import pytest

from actions import ui_layout
from core.ui_panels import PANELS, WORKSPACES, PanelState


def test_panel_state_presets_and_validation():
    state = PanelState()
    assert all(state.visible(p) for p in PANELS)
    state.apply_workspace("focus")
    assert not state.visible("left") and not state.visible("right")
    assert state.workspace == "focus"
    state.set_visible("footer", False)
    assert state.workspace == "custom" and not state.visible("footer")
    with pytest.raises(ValueError):
        state.apply_workspace("nope")
    with pytest.raises(ValueError):
        state.set_visible("nope", True)
    assert set(WORKSPACES["full"]) == set(PANELS)


class _Ui:
    def __init__(self):
        self.state = PanelState()

    @property
    def focus_mode(self):
        return self.state.workspace == "focus"

    def set_focus_mode(self, active):
        self.state.apply_workspace("focus" if active else "full")

    def apply_workspace(self, name):
        self.state.apply_workspace(name)

    def set_panel_visible(self, panel, visible):
        self.state.set_visible(panel, visible)

    def panel_status(self):
        return {"workspace": self.state.workspace, "panels": self.state.snapshot()}


def test_tool_panel_workspace_status():
    ui = _Ui()
    assert "hidden" in ui_layout.ui_layout({"mode": "toggle_panel", "panel": "left"}, player=ui)
    assert not ui.state.visible("left")
    assert "shown" in ui_layout.ui_layout({"mode": "toggle_panel", "panel": "left", "visible": True}, player=ui)
    assert "applied" in ui_layout.ui_layout({"mode": "workspace", "workspace": "coding"}, player=ui)
    assert not ui.state.visible("left") and ui.state.visible("right")
    assert '"coding"' in ui_layout.ui_layout({"mode": "status"}, player=ui)
    assert "Unknown workspace" in ui_layout.ui_layout({"mode": "workspace", "workspace": "x"}, player=ui)
    assert "Unknown panel" in ui_layout.ui_layout({"mode": "toggle_panel", "panel": "x"}, player=ui)


def test_real_window_renders_each_workspace():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    from PyQt6.QtWidgets import QApplication
    import ui as ui_module

    app = QApplication.instance() or QApplication(sys.argv)
    jarvis = ui_module.JarvisUI("")
    win = jarvis._win
    app.processEvents()
    names = {
        "header": win._header_panel, "left": win._left_panel,
        "right": win._right_panel, "content": win._content_panel,
        "footer": win._footer_panel,
    }
    for workspace, expected in WORKSPACES.items():
        ui_layout.ui_layout({"mode": "workspace", "workspace": workspace}, player=jarvis)
        app.processEvents()
        assert {n: w.isVisible() for n, w in names.items()} == expected, workspace
    ui_layout.ui_layout({"mode": "toggle_panel", "panel": "right", "visible": False}, player=jarvis)
    app.processEvents()
    assert not win._right_panel.isVisible()
    assert jarvis.panel_status()["workspace"] == "custom"
