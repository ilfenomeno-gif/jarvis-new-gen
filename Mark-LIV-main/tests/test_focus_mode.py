from types import SimpleNamespace

import ui


class _Panel:
    def __init__(self):
        self.visible = True

    def setVisible(self, value):
        self.visible = value


def test_focus_mode_hides_and_restores_both_side_panels():
    win = SimpleNamespace(_left_panel=_Panel(), _right_panel=_Panel(), _focus_mode=False)

    ui.MainWindow.set_focus_mode(win, True)
    assert win._focus_mode
    assert not win._left_panel.visible and not win._right_panel.visible

    ui.MainWindow.set_focus_mode(win, False)
    assert not win._focus_mode
    assert win._left_panel.visible and win._right_panel.visible
