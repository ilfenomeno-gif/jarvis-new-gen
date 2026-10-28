from pathlib import Path

import pytest

from actions.terminal import MAX_OUTPUT_LENGTH, TRUNCATION_MARKER, _result, terminal_run


def test_terminal_run_is_discovered_as_a_write_action():
    from core.action_loader import discover_actions

    registry = discover_actions(
        Path(__file__).resolve().parents[1] / "actions",
        logger=lambda _message: None,
    )

    assert "terminal_run" in registry.names()
    assert registry.risk_class("terminal_run") == "write"
    declaration = next(
        item
        for item in registry.get_tool_declarations()
        if item["name"] == "terminal_run"
    )
    assert declaration["parameters"]["required"] == ["command"]


@pytest.mark.parametrize(
    ("command", "matched"),
    [
        ("rm -rf C:\\temp", "rm -rf"),
        (r"del /f /s C:\temp", "del /f /s"),
        ("format C:", "format"),
        ("shutdown /s /t 0", "shutdown"),
        (r"reg delete HKCU\Software\Example", "reg delete"),
        (
            "Remove-Item -Recurse -Force C:\\temp",
            "Remove-Item -Recurse -Force",
        ),
        (r"rd /s /q C:\temp", "rd /s /q"),
    ],
)
def test_terminal_run_requests_confirmation_for_every_denylist_pattern(
    command, matched
):
    result = terminal_run({"command": command})

    assert result == {
        "result": "Ask the user for explicit confirmation",
        "matched": matched,
    }


def test_terminal_run_echoes_safe_command():
    result = terminal_run({"command": "echo hello"})

    assert result == {"stdout": "hello\n", "stderr": "", "returncode": 0}


def test_terminal_run_does_not_execute_denylisted_command_after_confirmation():
    result = terminal_run({
        "command": r"del /f /s C:\temp",
        "confirmed": True,
    })

    assert result["returncode"] == 2
    assert "not supported" in result["stderr"]


def test_terminal_run_returns_timeout_for_long_sleep():
    result = terminal_run({"command": "sleep 5", "timeout": 1})

    assert result == {"stdout": "", "stderr": "timeout", "returncode": -1}


def test_terminal_run_truncates_long_output():
    result = terminal_run({"command": f"echo {'x' * 5000}"})

    assert len(result["stdout"]) == MAX_OUTPUT_LENGTH + len(TRUNCATION_MARKER)
    assert result["stdout"].endswith(TRUNCATION_MARKER)


def test_terminal_run_truncates_long_stderr():
    result = _result(stderr="x" * 5000)

    assert len(result["stderr"]) == MAX_OUTPUT_LENGTH + len(TRUNCATION_MARKER)
    assert result["stderr"].endswith(TRUNCATION_MARKER)


def test_terminal_run_refuses_unallowlisted_shell_command():
    result = terminal_run({"command": "python -c \"import os; print(os.listdir())\""})

    assert result["returncode"] == 2
    assert result["stdout"] == ""
    assert "Unsupported command" in result["stderr"]
