import asyncio

import pytest

from core.agent_loop import AgentLoop, resolve_max_steps


FOREGROUND = (123, "notepad.exe")


def _loop(
    tmp_path,
    plans,
    *,
    confirmed=True,
    max_steps=10,
    wait_results=None,
    kill_switch=lambda: False,
    foreground=lambda: FOREGROUND,
):
    executed = []
    prompts = []
    captures = []
    waits = iter(wait_results or [])
    plan_values = iter(plans)

    def capture():
        captures.append(True)
        return "frame", {"left": 0, "top": 0}

    def planner(goal, elements, history, step, frame, timeout):
        return next(plan_values)

    def execute(parameters):
        executed.append(parameters)
        return {"result": "action completed"}

    def wait_for_change(**_kwargs):
        return next(waits, {"changed": True})

    loop = AgentLoop(
        max_steps=max_steps,
        confirm_session=lambda prompt: prompts.append(prompt) or confirmed,
        planner=planner,
        capture=capture,
        ocr=lambda **_kwargs: [{"text": "Test"}],
        uia_tree=lambda: {"controls": []},
        execute_input=execute,
        wait_for_change=wait_for_change,
        foreground=foreground,
        hash_frame=lambda _frame: "0123456789abcdef",
        kill_switch=kill_switch,
        arm_kill_switch=lambda: None,
        log_dir=tmp_path / "logs",
    )
    return loop, executed, prompts, captures


def test_run_without_session_confirmation_is_cancelled(tmp_path):
    loop, executed, prompts, captures = _loop(
        tmp_path,
        [{"action": "done", "reason": "already complete"}],
        confirmed=False,
    )

    result = asyncio.run(loop.run("Complete the task"))

    assert result == {"result": "cancelled"}
    assert not executed
    assert not captures
    assert len(prompts) == 1
    assert "massimo di 10 azioni" in prompts[0]
    assert "Ctrl+Alt+Esc" in prompts[0]
    assert "Gemini cloud" in prompts[0]


def test_run_succeeds_when_gemini_returns_done_on_first_step(tmp_path):
    loop, executed, _prompts, captures = _loop(
        tmp_path,
        [{"action": "done", "reason": "The requested result is visible."}],
    )

    result = asyncio.run(loop.run("Inspect the current page"))

    assert result == {
        "result": "success",
        "steps": 0,
        "reason": "The requested result is visible.",
    }
    assert not executed
    assert captures == [True]
    assert len(list((tmp_path / "logs").glob("agent_loop_*.log"))) == 1


def test_run_executes_three_actions_then_succeeds(tmp_path):
    plans = [
        {"action": "type", "target": "focused field", "value": "one"},
        {"action": "hotkey", "target": "focused field", "value": "ctrl+a"},
        {"action": "scroll", "target": None, "value": "down"},
        {"action": "done", "reason": "Finished."},
    ]
    loop, executed, _prompts, _captures = _loop(
        tmp_path,
        plans,
        wait_results=[{"changed": True}] * 3,
    )

    result = asyncio.run(loop.run("Fill and inspect the form"))

    assert result["result"] == "success"
    assert result["steps"] == 3
    assert [item["action"] for item in executed] == ["type", "hotkey", "scroll"]
    assert all(item["_expected_window"] == FOREGROUND[0] for item in executed)


def test_run_stops_after_consecutive_no_change_steps(tmp_path):
    plans = [
        {"action": "click", "target": {"x": 20, "y": 30}, "value": None},
        {"action": "click", "target": {"bbox": [10, 10, 20, 20]}, "value": None},
        {"action": "click", "target": "Save", "value": None},
    ]
    loop, executed, _prompts, _captures = _loop(
        tmp_path,
        plans,
        wait_results=[{"changed": False}] * 3,
    )

    result = asyncio.run(loop.run("Save the document"))

    assert result["result"] == "no_change"
    assert result["steps"] == 3
    assert len(executed) == 3
    assert executed[0]["action"] == "click"
    assert (executed[0]["x"], executed[0]["y"]) == (20, 30)
    assert (executed[1]["x"], executed[1]["y"]) == (20, 20)
    assert executed[2]["action"] == "click_text"


def test_run_stops_immediately_when_kill_switch_is_set(tmp_path):
    loop, executed, _prompts, captures = _loop(
        tmp_path,
        [{"action": "type", "target": "focused field", "value": "unsafe"}],
        kill_switch=lambda: True,
    )

    result = asyncio.run(loop.run("Type text"))

    assert result == {"result": "killed"}
    assert not executed
    assert not captures


def test_run_stops_when_foreground_process_is_not_allowlisted(tmp_path):
    def denied_foreground():
        raise PermissionError("Input blocked for powershell.exe")

    loop, executed, _prompts, captures = _loop(
        tmp_path,
        [{"action": "done"}],
        foreground=denied_foreground,
    )

    result = asyncio.run(loop.run("Inspect the terminal"))

    assert result["result"] == "failed"
    assert "powershell.exe" in result["reason"]
    assert not executed
    assert not captures


def test_run_honors_the_hard_maximum_step_limit(tmp_path):
    action = {"action": "type", "target": "focused field", "value": "x"}
    loop, executed, _prompts, _captures = _loop(
        tmp_path,
        [action] * 2,
        max_steps=2,
        wait_results=[{"changed": True}] * 2,
    )

    result = asyncio.run(loop.run("Keep typing"))

    assert result["result"] == "max_steps"
    assert result["steps"] == 2
    assert len(executed) == 2


def test_environment_max_steps_is_a_hard_cap(monkeypatch):
    monkeypatch.setenv("JARVIS_AGENT_MAX_STEPS", "3")

    assert resolve_max_steps() == 3
    assert resolve_max_steps(10) == 3
    assert resolve_max_steps(2) == 2
    with pytest.raises(ValueError, match="between 1 and"):
        monkeypatch.setenv("JARVIS_AGENT_MAX_STEPS", "0")
        resolve_max_steps()
