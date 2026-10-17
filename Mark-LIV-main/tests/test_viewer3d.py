import os
import sys
import time

import pytest

from actions import viewer_3d
from core.viewer3d import build_call


def test_build_call_validates_and_serialises():
    assert build_call("flyTo", [41.9, 12.5]) == ("flyTo", "[41.9, 12.5]")
    assert build_call("addMarker", ["10", 20, "x" * 100])[1].count("x") == 60
    assert build_call("clearMarkers", []) == ("clearMarkers", "[]")
    for bad in (
        ("flyTo", [91, 0]), ("flyTo", [0, 181]), ("flyTo", ["a", 0]),
        ("flyTo", [True, 0]), ("flyTo", [1]), ("spin", [1]),
        ("eval", []), ("document.write", ["x"]),
    ):
        with pytest.raises(ValueError):
            build_call(*bad)


class _Ui:
    def __init__(self):
        self.calls = []

    def viewer3d_show(self, visible):
        self.calls.append(("show", visible))

    def viewer3d_call(self, function, args):
        build_call(function, args)
        self.calls.append((function, args))


def test_tool_routes_modes_and_reports_invalid_input():
    ui = _Ui()
    assert "shown" in viewer_3d.viewer_3d({"mode": "show"}, player=ui)
    assert "turning" in viewer_3d.viewer_3d({"mode": "fly_to", "lat": 1, "lon": 2}, player=ui)
    assert "Invalid" in viewer_3d.viewer_3d({"mode": "fly_to", "lat": 99, "lon": 2}, player=ui)
    assert "Invalid" in viewer_3d.viewer_3d({"mode": "fly_to"}, player=ui)
    assert "Unknown mode" in viewer_3d.viewer_3d({"mode": "x"}, player=ui)
    assert "not available" in viewer_3d.viewer_3d({"mode": "show"}, player=None)
    assert ui.calls == [("show", True), ("flyTo", [1, 2])]
    assert viewer_3d.TOOL["risk_class"] == "read"


def test_real_page_loads_and_receives_commands():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    os.environ.setdefault("QTWEBENGINE_CHROMIUM_FLAGS", "--disable-gpu --use-gl=angle --use-angle=swiftshader")
    from PyQt6.QtWidgets import QApplication
    import ui as ui_module

    app = QApplication.instance() or QApplication(sys.argv)
    jarvis = ui_module.JarvisUI("")
    win = jarvis._win

    viewer_3d.viewer_3d({"mode": "show"}, player=jarvis)
    viewer_3d.viewer_3d({"mode": "add_marker", "lat": 41.9, "lon": 12.5, "label": "Roma"}, player=jarvis)
    viewer_3d.viewer_3d({"mode": "fly_to", "lat": 41.9, "lon": 12.5}, player=jarvis)

    result = {}
    deadline = time.time() + 40
    while time.time() < deadline and "state" not in result:
        app.processEvents()
        if win._viewer3d_loaded:
            win._viewer3d.page().runJavaScript(
                "window.jarvisViewer ? JSON.stringify(window.jarvisViewer.getState()) : null",
                lambda value: result.__setitem__("state", value),
            )
            t = time.time() + 1
            while time.time() < t and "state" not in result:
                app.processEvents()
            if result.get("state") is None:
                result.pop("state", None)
        time.sleep(0.05)

    assert win._viewer3d_loaded, "page failed to load"
    import json
    state = json.loads(result["state"])
    assert state["ready"] and state["flying"]
    assert state["markers"] == [{"lat": 41.9, "lon": 12.5, "label": "Roma"}]
