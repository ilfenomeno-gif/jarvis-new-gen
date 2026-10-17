import os
import sys
import tempfile

# Tests that open the real window must never read or overwrite the user's saved HUD layout.
os.environ.setdefault("JARVIS_UI_LAYOUT", os.path.join(tempfile.mkdtemp(prefix="jarvis_layout_"), "ui_layout.json"))


import pytest


@pytest.fixture(autouse=True)
def _close_qt_windows():
    # Real-window tests leave WebEngine pages and paint timers alive; they pile up across a full run.
    yield
    qt = sys.modules.get("PyQt6.QtWidgets")
    app = qt.QApplication.instance() if qt else None
    if app is not None:
        app.closeAllWindows()
        app.processEvents()
