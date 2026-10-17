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


def test_fly_to_and_recon_bring_viewer_to_front():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    from PyQt6.QtWidgets import QApplication
    import ui as ui_module

    app = QApplication.instance() or QApplication(sys.argv)
    jarvis = ui_module.JarvisUI("")
    win = jarvis._win
    assert win._hud_cam_stack.currentWidget() is win.hud

    viewer_3d.viewer_3d({"mode": "fly_to", "lat": 1, "lon": 2}, player=jarvis)
    app.processEvents()
    assert win._hud_cam_stack.currentWidget() is win._viewer3d

    win.show_viewer3d(False)
    assert win._hud_cam_stack.currentWidget() is win.hud
    jarvis.apply_workspace("recon")
    app.processEvents()
    assert win._hud_cam_stack.currentWidget() is win._viewer3d


def test_parse_states_and_fetch_with_fake_opener():
    import io, json
    from core import viewer3d as v

    payload = {"states": [
        ["a", "ITA123 ", "IT", 0, 0, 12.5, 41.9, 10000.0, False],
        ["b", "GND1", "IT", 0, 0, 12.0, 41.0, 0, True],
        ["c", "NOPOS", "IT", 0, 0, None, None, 0, False],
    ]}
    assert v.parse_states(payload) == [[41.9, 12.5, "ITA123", 10000.0]]
    assert len(v.parse_states({"states": [["x", "", "", 0, 0, 1, 2, 3, False]] * 1000})) == v.MAX_FLIGHTS

    class Resp(io.BytesIO):
        def __enter__(self): return self
        def __exit__(self, *a): return False

    seen = {}
    def opener(req, timeout):
        seen["url"] = req.full_url
        return Resp(json.dumps(payload).encode())
    assert v.fetch_flights("usa", opener=opener)[0][2] == "ITA123"
    assert "lamin=24.0" in seen["url"]
    with pytest.raises(ValueError):
        v.fetch_flights("mars", opener=opener)

    def boom(req, timeout):
        raise OSError("offline")
    with pytest.raises(RuntimeError):
        v.fetch_flights("europe", opener=boom)


def test_set_flights_validation():
    from core.viewer3d import build_call
    fn, args = build_call("setFlights", [[[1, 2, "X", 5]]])
    assert fn == "setFlights" and '"X"' in args
    with pytest.raises(ValueError):
        build_call("setFlights", [[[100, 2, "X"]]])
    with pytest.raises(ValueError):
        build_call("setFlights", [[[1, 2]]])
    assert build_call("clearFlights", []) == ("clearFlights", "[]")


def test_tool_load_live_flights_runs_off_ui(monkeypatch):
    calls = []
    class P:
        def viewer3d_call(self, f, a): calls.append((f, a))
        def viewer3d_show(self, v): pass
    monkeypatch.setattr(viewer_3d, "fetch_flights", lambda region: [[1.0, 2.0, "AB", 0]])
    out = viewer_3d.viewer_3d({"mode": "load_live_flights", "region": "usa"}, player=P())
    assert "1 live flights" in out and calls == [("setFlights", [[[1.0, 2.0, "AB", 0]]])]
    def fail(region): raise RuntimeError("OpenSky not reachable: x")
    monkeypatch.setattr(viewer_3d, "fetch_flights", fail)
    assert "not reachable" in viewer_3d.viewer_3d({"mode": "load_live_flights"}, player=P())
