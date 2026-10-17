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


def test_model_file_validation(tmp_path):
    from core.viewer3d import model_file
    from tests.glb_helper import make_glb
    make_glb(tmp_path / "ok.glb")
    assert model_file("ok.glb", tmp_path).name == "ok.glb"
    for bad in ("../ok.glb", "sub/ok.glb", "ok.txt", "", "C:\\x.glb", "missing.glb", "..\\ok.glb"):
        with pytest.raises(ValueError):
            model_file(bad, tmp_path)
    big = tmp_path / "big.glb"
    big.write_bytes(b"x")
    import core.viewer3d as v
    old, v.MAX_MODEL_BYTES = v.MAX_MODEL_BYTES, 0
    try:
        with pytest.raises(ValueError):
            model_file("big.glb", tmp_path)
    finally:
        v.MAX_MODEL_BYTES = old
    assert build_call("loadModel", ["ok.glb"]) == ("loadModel", '["ok.glb"]')
    with pytest.raises(ValueError):
        build_call("loadModel", ["../x.glb"])


def _poll_state(app, win, until, timeout=40):
    import json
    deadline, state = time.time() + timeout, None
    while time.time() < deadline:
        box = {}
        if win._viewer3d_loaded:
            win._viewer3d.page().runJavaScript(
                "JSON.stringify(window.jarvisViewer.getState())",
                lambda v: box.__setitem__("s", v),
            )
            t = time.time() + 1
            while time.time() < t and "s" not in box:
                app.processEvents()
            if box.get("s"):
                state = json.loads(box["s"])
                if until(state):
                    return state
        app.processEvents()
        time.sleep(0.1)
    return state


def test_real_page_loads_glb_model():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    from PyQt6.QtWidgets import QApplication
    import ui as ui_module
    from core.viewer3d import MODELS_DIR
    from tests.glb_helper import make_glb

    MODELS_DIR.mkdir(exist_ok=True)
    path = MODELS_DIR / "pytest_model.glb"
    make_glb(path)
    try:
        app = QApplication.instance() or QApplication(sys.argv)
        jarvis = ui_module.JarvisUI("")
        win = jarvis._win
        out = viewer_3d.viewer_3d({"mode": "load_model", "model": "pytest_model.glb"}, player=jarvis)
        assert "loaded" in out
        state = _poll_state(app, win, lambda s: s["model"]["status"] in ("ready", "error"))
        assert state["model"]["status"] == "ready", state["model"]
        assert state["model"]["nodes"] == ["part_a", "part_b"]
        assert win._hud_cam_stack.currentWidget() is win._viewer3d

        viewer_3d.viewer_3d({"mode": "clear_model"}, player=jarvis)
        state = _poll_state(app, win, lambda s: s["model"]["status"] == "none")
        assert state["model"]["status"] == "none"
        assert "not found" in viewer_3d.viewer_3d({"mode": "load_model", "model": "nope.glb"}, player=jarvis) \
            or "Invalid" in viewer_3d.viewer_3d({"mode": "load_model", "model": "nope.glb"}, player=jarvis)
    finally:
        path.unlink(missing_ok=True)


def test_real_page_explode_and_highlight():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    from PyQt6.QtWidgets import QApplication
    import ui as ui_module
    from core.viewer3d import MODELS_DIR
    from tests.glb_helper import make_glb

    MODELS_DIR.mkdir(exist_ok=True)
    path = MODELS_DIR / "pytest_parts.glb"
    make_glb(path)
    try:
        app = QApplication.instance() or QApplication(sys.argv)
        jarvis = ui_module.JarvisUI("")
        win = jarvis._win
        viewer_3d.viewer_3d({"mode": "load_model", "model": "pytest_parts.glb"}, player=jarvis)
        state = _poll_state(app, win, lambda s: s["model"]["status"] == "ready")
        assert state["model"]["parts"] == 2 and state["model"]["moved"] == [0, 0]

        assert "exploded" in viewer_3d.viewer_3d({"mode": "explode_model", "on": True}, player=jarvis)
        state = _poll_state(app, win, lambda s: s["model"]["explode"] == 1)
        assert state["model"]["explode"] == 1 and all(d > 0.1 for d in state["model"]["moved"]), state["model"]

        viewer_3d.viewer_3d({"mode": "highlight_part", "part": "part_a"}, player=jarvis)
        state = _poll_state(app, win, lambda s: s["model"]["highlight"] == "part_a")
        assert state["model"]["highlight"] == "part_a" and state["model"]["glowing"] == 1
        viewer_3d.viewer_3d({"mode": "highlight_part", "part": ""}, player=jarvis)
        state = _poll_state(app, win, lambda s: s["model"]["highlight"] == "")
        assert state["model"]["glowing"] == 0

        viewer_3d.viewer_3d({"mode": "explode_model", "on": False}, player=jarvis)
        state = _poll_state(app, win, lambda s: s["model"]["explode"] == 0)
        assert all(d < 0.001 for d in state["model"]["moved"]), state["model"]
    finally:
        path.unlink(missing_ok=True)


def test_explode_highlight_validation():
    assert build_call("explodeModel", [True]) == ("explodeModel", "[true]")
    assert build_call("highlightPart", [" turbine "]) == ("highlightPart", '["turbine"]')
    with pytest.raises(ValueError):
        build_call("explodeModel", ["yes"])
    with pytest.raises(ValueError):
        build_call("highlightPart", [5])


def test_real_page_hologram_shader_and_toggle():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    from PyQt6.QtWidgets import QApplication
    import ui as ui_module
    from core.viewer3d import MODELS_DIR
    from tests.glb_helper import make_glb

    MODELS_DIR.mkdir(exist_ok=True)
    path = MODELS_DIR / "pytest_holo.glb"
    make_glb(path)
    try:
        app = QApplication.instance() or QApplication(sys.argv)
        jarvis = ui_module.JarvisUI("")
        win = jarvis._win
        viewer_3d.viewer_3d({"mode": "load_model", "model": "pytest_holo.glb"}, player=jarvis)
        state = _poll_state(app, win, lambda s: s["model"]["status"] == "ready")
        assert state["model"]["hologram"] is True
        if state["webgl"]:
            time.sleep(1.5)  # let several frames compile and draw the shader
            state = _poll_state(app, win, lambda s: True)
            assert state["model"]["shaderError"] == ""

        viewer_3d.viewer_3d({"mode": "highlight_part", "part": "part_b"}, player=jarvis)
        state = _poll_state(app, win, lambda s: s["model"]["glowing"] == 1)
        assert state["model"]["glowing"] == 1

        viewer_3d.viewer_3d({"mode": "set_hologram", "on": False}, player=jarvis)
        state = _poll_state(app, win, lambda s: s["model"]["hologram"] is False)
        assert state["model"]["hologram"] is False and state["model"]["glowing"] == 1
        viewer_3d.viewer_3d({"mode": "set_hologram", "on": True}, player=jarvis)
        state = _poll_state(app, win, lambda s: s["model"]["hologram"] is True)
        assert state["model"]["hologram"] is True and state["model"]["glowing"] == 1
        assert state["model"]["shaderError"] == ""
    finally:
        path.unlink(missing_ok=True)
