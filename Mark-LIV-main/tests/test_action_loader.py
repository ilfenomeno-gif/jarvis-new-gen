"""Tests for the built-in action registry."""

from __future__ import annotations

import sys
import json
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.action_loader import discover_actions


def _write_action(directory: Path, filename: str, name: str, result: str) -> None:
    (directory / filename).write_text(
        "def run(parameters, player=None, speak=None):\n"
        f"    return {result!r} + ':' + str(parameters['value']) + ':' + str(player)\n"
        "\n"
        "TOOL = {\n"
        f"    'name': {name!r},\n"
        "    'description': 'Test action',\n"
        "    'parameters': {'type': 'OBJECT', 'properties': {}},\n"
        "    'handler': run,\n"
        "}\n",
        encoding="utf-8",
    )


def test_discovery_registers_actions_and_rejects_reserved_or_duplicate_names(
    tmp_path, monkeypatch
):
    actions_dir = tmp_path / "actions"
    actions_dir.mkdir()
    _write_action(actions_dir, "a_reserved.py", "protected", "reserved")
    _write_action(actions_dir, "b_first.py", "sample_action", "first")
    _write_action(actions_dir, "c_duplicate.py", "sample_action", "duplicate")
    messages: list[str] = []
    for module_name in (
        "actions.a_reserved",
        "actions.b_first",
        "actions.c_duplicate",
    ):
        monkeypatch.delitem(sys.modules, module_name, raising=False)

    registry = discover_actions(
        actions_dir,
        reserved_names={"protected"},
        logger=messages.append,
    )

    assert registry.names() == {"sample_action"}
    assert [item["name"] for item in registry.get_tool_declarations()] == [
        "sample_action"
    ]
    assert registry.run(
        "sample_action",
        {"value": 7},
        ctx={"player": "ui", "speak": "speech"},
    ) == "first:7:ui"
    assert any("collides with a reserved core tool" in message for message in messages)
    assert any("already used by action" in message for message in messages)


def test_destructive_actions_require_confirmation(tmp_path, monkeypatch):
    actions_dir = tmp_path / "actions"
    actions_dir.mkdir()
    (actions_dir / "wipe.py").write_text(
        "def run(parameters):\n    return 'wiped'\n\n"
        "TOOL = {'name': 'wipe', 'description': 'x', 'risk_class': 'destructive',\n"
        "        'parameters': {'type': 'OBJECT', 'properties': {}}, 'handler': run}\n",
        encoding="utf-8",
    )
    (actions_dir / "bad.py").write_text(
        "TOOL = {'name': 'bad', 'description': 'x', 'risk_class': 'nope',\n"
        "        'handler': lambda parameters: ''}\n",
        encoding="utf-8",
    )
    for module_name in ("actions.wipe", "actions.bad"):
        monkeypatch.delitem(sys.modules, module_name, raising=False)

    registry = discover_actions(actions_dir, logger=lambda _m: None)

    assert registry.names() == {"wipe"}
    assert registry.risk_class("wipe") == "destructive"
    declared = registry.get_tool_declarations()[0]["parameters"]["properties"]
    assert "confirmed" in declared
    assert "confirmation" in registry.run("wipe", {})
    assert registry.run("wipe", {"confirmed": True}) == "wiped"


def test_bundled_actions_are_discovered():
    registry = discover_actions(
        Path(__file__).resolve().parents[1] / "actions", logger=lambda _m: None
    )

    assert {"weather_report", "send_message", "reminder", "report_problem"} <= registry.names()
    assert registry.risk_class("weather_report") == "read"


def test_group_a_actions_keep_their_model_schemas_and_dispatch(monkeypatch):
    from actions import app_launcher, open_app, youtube_video

    registry = discover_actions(
        Path(__file__).resolve().parents[1] / "actions", logger=lambda _m: None
    )
    declarations = {
        item["name"]: item for item in registry.get_tool_declarations()
    }

    assert declarations["open_app"] == {
        "name": "open_app",
        "description": (
            "Compatibility launcher for websites, media files, and existing Steam game handoffs. "
            "For Windows desktop applications, use app_launcher instead. For websites, use "
            "open_website. GeoGuessr and speech-recognition variants such as 'Gio Gasser', "
            "'Jao Gasser', or 'Geo Guesser' keep their Steam handoff. Only a full audio/video "
            "file path is accepted; do not pass executable paths or arbitrary commands."
        ),
        "parameters": {
            "type": "OBJECT",
            "properties": {
                "app_name": {
                    "type": "STRING",
                    "description": (
                        "A website, Steam game handoff, or audio/video path. For desktop "
                        "applications use app_launcher; executable paths are not accepted here."
                    ),
                },
                "confirmed": {
                    "type": "BOOLEAN",
                    "description": "Set true only after the user explicitly confirmed this action.",
                },
            },
            "required": ["app_name"],
        },
    }
    assert declarations["youtube_video"] == {
        "name": "youtube_video",
        "description": (
            "Controls YouTube. Use for: playing videos, summarizing a video's content, "
            "getting video info, or showing trending videos. For a specific request, "
            "always search and play the first relevant result; never open only youtube.com. "
            "If playback fails, return the targeted search URL."
        ),
        "parameters": {
            "type": "OBJECT",
            "properties": {
                "action": {
                    "type": "STRING",
                    "description": "play | summarize | get_info | trending (default: play)",
                },
                "query": {"type": "STRING", "description": "Search query for play action"},
                "save": {
                    "type": "BOOLEAN",
                    "description": "Save summary to Notepad (summarize only)",
                },
                "region": {
                    "type": "STRING",
                    "description": "Country code for trending e.g. TR, US",
                },
                "url": {"type": "STRING", "description": "Video URL for get_info action"},
            },
            "required": [],
        },
    }
    assert registry.risk_class("open_app") == "destructive"
    assert registry.risk_class("youtube_video") == "write"

    opened = []
    monkeypatch.setattr(
        app_launcher,
        "launch_app",
        lambda app, args=None, confirmed=False: opened.append((app, confirmed)) or "safe-opened",
    )
    logs = []
    assert registry.run(
        "open_app",
        {"app_name": "Chrome", "confirmed": True},
        ctx={"player": type("Player", (), {"write_log": logs.append})()},
    ) == "safe-opened"
    assert opened == [("chrome", True)]
    assert logs == ["[open_app] Chrome"]

    played = []
    monkeypatch.setitem(
        youtube_video._ACTION_MAP,
        "play",
        lambda parameters, player: played.append((parameters, player)) or "played",
    )
    player = type("Player", (), {"write_log": logs.append})()
    assert registry.run(
        "youtube_video",
        {"action": "play", "query": "jazz"},
        ctx={"player": player},
    ) == "played"
    assert played == [({"action": "play", "query": "jazz"}, player)]


def test_bundled_actions_no_longer_duplicate_core_declarations():
    import main

    registry = discover_actions(
        Path(__file__).resolve().parents[1] / "actions", logger=lambda _m: None
    )
    core_names = {item["name"] for item in main.TOOL_DECLARATIONS}

    assert {"open_app", "youtube_video"} <= registry.names()
    assert not {"open_app", "youtube_video"} & core_names


def test_group_b_actions_keep_their_model_schemas_and_dispatch(monkeypatch):
    from actions import browser_control, computer_settings

    registry = discover_actions(
        Path(__file__).resolve().parents[1] / "actions", logger=lambda _m: None
    )
    declarations = {
        item["name"]: item for item in registry.get_tool_declarations()
    }

    browser_schema = declarations["browser_control"]
    assert browser_schema["description"].startswith(
        "Controls the user's external web browser."
    )
    assert browser_schema["parameters"]["required"] == ["action"]
    assert list(browser_schema["parameters"]["properties"]) == [
        "action", "browser", "url", "query", "engine", "selector", "text",
        "description", "direction", "amount", "key", "path", "incognito",
        "clear_first",
    ]
    assert browser_schema["parameters"]["properties"]["action"]["description"] == (
        "go_to | search | click | type | scroll | fill_form | smart_click | "
        "smart_type | get_text | get_url | press | new_tab | close_tab | "
        "screenshot | back | forward | reload | switch | list_browsers | close | close_all"
    )

    settings_schema = declarations["computer_settings"]
    assert settings_schema["description"].startswith("Controls the computer:")
    assert settings_schema["parameters"]["required"] == []
    assert list(settings_schema["parameters"]["properties"]) == [
        "action", "description", "value",
    ]
    assert "restart | shutdown" in (
        settings_schema["parameters"]["properties"]["action"]["description"]
    )
    assert registry.risk_class("browser_control") == "write"
    assert registry.risk_class("computer_settings") == "write"

    sessions = []
    monkeypatch.setattr(
        browser_control._registry, "list_sessions",
        lambda: sessions.append("listed") or "Open browsers: none",
    )
    player_logs = []
    player = type("Player", (), {"write_log": player_logs.append})()
    assert registry.run(
        "browser_control", {"action": "list_browsers"}, ctx={"player": player}
    ) == "Open browsers: none"
    assert sessions == ["listed"]
    assert player_logs == ["[browser] Open browsers: none"]

    monkeypatch.setattr(computer_settings, "_PYAUTOGUI", True)
    monkeypatch.setattr(computer_settings, "volume_get", lambda: None)
    settings_calls = []
    monkeypatch.setitem(
        computer_settings.ACTION_MAP, "volume_up",
        lambda: settings_calls.append("volume_up"),
    )
    assert registry.run(
        "computer_settings", {"action": "volume_up"}, ctx={"player": player}
    ) == "Done: volume_up."
    assert settings_calls == ["volume_up"]


def test_group_b_actions_no_longer_duplicate_core_declarations():
    import main

    registry = discover_actions(
        Path(__file__).resolve().parents[1] / "actions", logger=lambda _m: None
    )
    core_names = {item["name"] for item in main.TOOL_DECLARATIONS}

    assert {"browser_control", "computer_settings"} <= registry.names()
    assert not {"browser_control", "computer_settings"} & core_names


def test_group_c_code_actions_keep_their_schemas_and_dispatch(monkeypatch):
    from actions import code_helper, dev_agent

    dispatched = []

    def handler(name):
        def run(parameters, player=None, speak=None):
            dispatched.append((name, parameters, player, speak))
            return f"{name} dispatched"

        return run

    monkeypatch.setitem(code_helper.TOOL, "handler", handler("code_helper"))
    monkeypatch.setitem(dev_agent.TOOL, "handler", handler("dev_agent"))
    registry = discover_actions(
        Path(__file__).resolve().parents[1] / "actions", logger=lambda _m: None
    )
    declarations = {
        item["name"]: item for item in registry.get_tool_declarations()
    }

    code_schema = declarations["code_helper"]
    assert code_schema["description"] == (
        "Writes, edits, explains, runs, or builds code files."
    )
    code_parameters = dict(code_schema["parameters"])
    code_properties = dict(code_parameters["properties"])
    confirmation = code_properties.pop("confirmed")
    code_parameters["properties"] = code_properties
    assert code_parameters == {
        "type": "OBJECT",
        "properties": {
            "action": {
                "type": "STRING",
                "description": "write | edit | explain | run | build | auto (default: auto)",
            },
            "description": {
                "type": "STRING",
                "description": "What the code should do or what change to make",
            },
            "language": {
                "type": "STRING",
                "description": "Programming language (default: python)",
            },
            "output_path": {"type": "STRING", "description": "Where to save the file"},
            "file_path": {
                "type": "STRING",
                "description": "Path to existing file for edit/explain/run/build",
            },
            "code": {"type": "STRING", "description": "Raw code string for explain"},
            "args": {"type": "STRING", "description": "CLI arguments for run/build"},
            "timeout": {
                "type": "INTEGER",
                "description": "Execution timeout in seconds (default: 30)",
            },
        },
        "required": ["action"],
    }
    assert confirmation == {
        "type": "BOOLEAN",
        "description": "Set true only after the user explicitly confirmed this action.",
    }

    dev_schema = declarations["dev_agent"]
    assert dev_schema["description"] == (
        "Builds complete multi-file projects from scratch: plans, writes files, "
        "installs deps, opens VSCode, runs and fixes errors."
    )
    dev_parameters = dict(dev_schema["parameters"])
    dev_properties = dict(dev_parameters["properties"])
    confirmation = dev_properties.pop("confirmed")
    dev_parameters["properties"] = dev_properties
    assert dev_parameters == {
        "type": "OBJECT",
        "properties": {
            "description": {"type": "STRING", "description": "What the project should do"},
            "language": {
                "type": "STRING",
                "description": "Programming language (default: python)",
            },
            "project_name": {
                "type": "STRING",
                "description": "Optional project folder name",
            },
            "timeout": {
                "type": "INTEGER",
                "description": "Run timeout in seconds (default: 30)",
            },
        },
        "required": ["description"],
    }
    assert confirmation == {
        "type": "BOOLEAN",
        "description": "Set true only after the user explicitly confirmed this action.",
    }
    assert registry.risk_class("code_helper") == "destructive"
    assert registry.risk_class("dev_agent") == "destructive"
    assert "confirmation" in registry.run("code_helper", {"action": "write"})
    assert "confirmation" in registry.run(
        "dev_agent", {"description": "test project"}
    )

    player = object()
    speak = object()
    for name, args in (
        ("code_helper", {"action": "explain", "confirmed": True}),
        ("dev_agent", {"description": "test project", "confirmed": True}),
    ):
        assert registry.run(
            name, args, ctx={"player": player, "speak": speak}
        ) == f"{name} dispatched"

    assert dispatched == [
        ("code_helper", {"action": "explain", "confirmed": True}, player, speak),
        ("dev_agent", {"description": "test project", "confirmed": True}, player, speak),
    ]


def test_group_c_actions_no_longer_duplicate_core_declarations():
    import main

    registry = discover_actions(
        Path(__file__).resolve().parents[1] / "actions", logger=lambda _m: None
    )
    core_names = {item["name"] for item in main.TOOL_DECLARATIONS}

    assert {"code_helper", "dev_agent"} <= registry.names()
    assert not {"code_helper", "dev_agent"} & core_names


def test_group_d_agent_actions_keep_their_schemas_and_dispatch(monkeypatch):
    from actions import research_agent, supervisor_agent

    registry = discover_actions(
        Path(__file__).resolve().parents[1] / "actions", logger=lambda _m: None
    )
    declarations = {
        item["name"]: item for item in registry.get_tool_declarations()
    }

    supervisor_schema = declarations["supervisor_agent"]
    assert supervisor_schema["description"] == (
        "Coordinates complex work by planning tasks and running independent "
        "research-agent tasks in parallel. Coding and test commands are returned "
        "as explicit handoffs and are not executed automatically."
    )
    assert supervisor_schema["parameters"] == {
        "type": "OBJECT",
        "properties": {
            "task": {
                "type": "STRING",
                "description": "Full description of the complex task to plan and execute.",
            },
        },
        "required": ["task"],
    }
    research_schema = declarations["research_agent"]
    assert research_schema["description"] == (
        "Research agent. Searches for technical documentation, API references, "
        "and code examples for a given topic."
    )
    assert research_schema["parameters"] == {
        "type": "OBJECT",
        "properties": {
            "topic": {
                "type": "STRING",
                "description": "The technical topic or API to research.",
            },
        },
        "required": ["topic"],
    }
    assert registry.risk_class("supervisor_agent") == "read"
    assert registry.risk_class("research_agent") == "read"

    calls = []
    monkeypatch.setattr(
        supervisor_agent._agent,
        "run_supervisor",
        lambda task: calls.append(("supervisor", task)) or {"plan_summary": "stub"},
    )
    monkeypatch.setattr(
        research_agent._agent,
        "run_research",
        lambda topic: calls.append(("research", topic)) or "research stub",
    )
    result = json.loads(registry.run(
        "supervisor_agent", {"task": "plan safely"}
    ))
    assert result["plan_summary"] == "stub"
    assert result["research_results"] == []
    assert result["handoff"] == {
        "coding": (
            "Not executed; code generation requires a separate user-directed "
            "coder_agent call and an approved destination."
        ),
        "testing": (
            "Not executed; commands require a separate user-directed "
            "debugger_agent call and explicit confirmation."
        ),
    }
    assert registry.run("research_agent", {"topic": "API docs"}) == "research stub"
    assert calls == [
        ("supervisor", "plan safely"),
        ("research", "API docs"),
    ]


def test_group_d_actions_no_longer_duplicate_core_declarations():
    import main

    registry = discover_actions(
        Path(__file__).resolve().parents[1] / "actions", logger=lambda _m: None
    )
    core_names = {item["name"] for item in main.TOOL_DECLARATIONS}

    assert {"supervisor_agent", "research_agent"} <= registry.names()
    assert not {"supervisor_agent", "research_agent"} & core_names


def test_group_e_agent_actions_keep_their_schemas_and_dispatch(monkeypatch):
    from actions import coder_agent, debugger_agent

    registry = discover_actions(
        Path(__file__).resolve().parents[1] / "actions", logger=lambda _m: None
    )
    declarations = {
        item["name"]: item for item in registry.get_tool_declarations()
    }

    coder_schema = declarations["coder_agent"]
    assert coder_schema["description"] == (
        "Coder agent. Writes production-quality code to a local file based on a "
        "task description and optional research context."
    )
    assert coder_schema["parameters"] == {
        "type": "OBJECT",
        "properties": {
            "task": {"type": "STRING", "description": "What to code."},
            "context": {
                "type": "STRING",
                "description": "Optional research context or API documentation.",
            },
            "file_path": {
                "type": "STRING",
                "description": "Absolute path where to write the code file.",
            },
        },
        "required": ["task", "file_path"],
    }
    debugger_schema = declarations["debugger_agent"]
    assert debugger_schema["description"] == (
        "Debugger Agent. Runs a command (compile/test/execute), intercepts errors, "
        "and returns an AI-generated fix suggestion."
    )
    debugger_parameters = dict(debugger_schema["parameters"])
    debugger_properties = dict(debugger_parameters["properties"])
    confirmation = debugger_properties.pop("confirmed")
    debugger_parameters["properties"] = debugger_properties
    assert debugger_parameters == {
        "type": "OBJECT",
        "properties": {
            "command": {
                "type": "STRING",
                "description": "Shell command to run, e.g. 'python main.py'.",
            },
            "cwd": {"type": "STRING", "description": "Working directory for the command."},
        },
        "required": ["command"],
    }
    assert confirmation == {
        "type": "BOOLEAN",
        "description": "Set true only after the user explicitly confirmed this action.",
    }
    assert registry.risk_class("coder_agent") == "write"
    assert registry.risk_class("debugger_agent") == "destructive"
    assert "confirmation" in registry.run(
        "debugger_agent", {"command": "noop"}
    )

    calls = []
    monkeypatch.setattr(
        coder_agent._agent,
        "run_coder",
        lambda task, context, file_path: calls.append(
            ("coder", task, context, file_path)
        ) or "coder stub",
    )
    monkeypatch.setattr(
        debugger_agent._agent,
        "run_debugger",
        lambda command, cwd: calls.append(("debugger", command, cwd))
        or "debugger stub",
    )
    assert registry.run(
        "coder_agent",
        {"task": "write a file", "context": "docs", "file_path": "out.py"},
    ) == "coder stub"
    assert registry.run(
        "debugger_agent",
        {"command": "echo safe", "cwd": ".", "confirmed": True},
    ) == "debugger stub"
    assert calls == [
        ("coder", "write a file", "docs", "out.py"),
        ("debugger", "echo safe", "."),
    ]


def test_group_e_actions_no_longer_duplicate_core_declarations():
    import main

    registry = discover_actions(
        Path(__file__).resolve().parents[1] / "actions", logger=lambda _m: None
    )
    core_names = {item["name"] for item in main.TOOL_DECLARATIONS}

    assert {"coder_agent", "debugger_agent"} <= registry.names()
    assert not {"coder_agent", "debugger_agent"} & core_names


def test_group_f_desktop_actions_require_confirmation_and_dispatch(monkeypatch):
    from actions import computer_control, game_updater

    monkeypatch.setitem(
        computer_control.TOOL,
        "handler",
        lambda parameters, player=None: f"computer:{parameters['action']}",
    )
    monkeypatch.setitem(
        game_updater.TOOL,
        "handler",
        lambda parameters, player=None, speak=None: f"game:{parameters['action']}",
    )
    registry = discover_actions(
        Path(__file__).resolve().parents[1] / "actions", logger=lambda _m: None
    )
    declarations = {
        item["name"]: item for item in registry.get_tool_declarations()
    }

    computer_schema = declarations["computer_control"]
    assert computer_schema["description"] == (
        "Direct computer control: type, click, hotkeys, scroll, move mouse, "
        "screenshots, find elements on screen."
    )
    computer_parameters = dict(computer_schema["parameters"])
    computer_properties = dict(computer_parameters["properties"])
    confirmation = computer_properties.pop("confirmed")
    computer_parameters["properties"] = computer_properties
    assert computer_parameters == {
        "type": "OBJECT",
        "properties": {
            "action": {
                "type": "STRING",
                "description": (
                    "type | smart_type | click | double_click | right_click | hotkey | "
                    "press | scroll | move | copy | paste | screenshot | wait | clear_field | "
                    "focus_window | screen_find | screen_click | random_data | user_data"
                ),
            },
            "text": {"type": "STRING", "description": "Text to type or paste"},
            "x": {"type": "INTEGER", "description": "X coordinate"},
            "y": {"type": "INTEGER", "description": "Y coordinate"},
            "keys": {"type": "STRING", "description": "Key combination e.g. 'ctrl+c'"},
            "key": {"type": "STRING", "description": "Single key e.g. 'enter'"},
            "direction": {"type": "STRING", "description": "up | down | left | right"},
            "amount": {"type": "INTEGER", "description": "Scroll amount (default: 3)"},
            "seconds": {"type": "NUMBER", "description": "Seconds to wait"},
            "title": {"type": "STRING", "description": "Window title for focus_window"},
            "description": {
                "type": "STRING",
                "description": "Element description for screen_find/screen_click",
            },
            "type": {"type": "STRING", "description": "Data type for random_data"},
            "field": {
                "type": "STRING",
                "description": "Field for user_data: name|email|city",
            },
            "clear_first": {
                "type": "BOOLEAN",
                "description": "Clear field before typing (default: true)",
            },
            "path": {"type": "STRING", "description": "Save path for screenshot"},
        },
        "required": ["action"],
    }
    assert confirmation == {
        "type": "BOOLEAN",
        "description": "Set true only after the user explicitly confirmed this action.",
    }

    game_schema = declarations["game_updater"]
    assert game_schema["description"] == (
        "Use for Steam or Epic operations that manage games: opening, installing, "
        "downloading, updating, listing installed games, checking download status, "
        "or scheduling updates. Opening a named game should launch it through Steam "
        "when it is in the Steam catalog. "
        "This tool has priority over file search for every videogame request. "
        "NEVER use browser_control or web_search for Steam/Epic."
    )
    game_parameters = dict(game_schema["parameters"])
    game_properties = dict(game_parameters["properties"])
    confirmation = game_properties.pop("confirmed")
    game_parameters["properties"] = game_properties
    assert game_parameters == {
        "type": "OBJECT",
        "properties": {
            "action": {
                "type": "STRING",
                "description": (
                    "update | install | list | download_status | schedule | "
                    "cancel_schedule | schedule_status (default: update)"
                ),
            },
            "platform": {
                "type": "STRING",
                "description": "steam | epic | both (default: both)",
            },
            "game_name": {
                "type": "STRING",
                "description": "Game name (partial match supported)",
            },
            "app_id": {
                "type": "STRING",
                "description": "Steam AppID for install (optional)",
            },
            "hour": {
                "type": "INTEGER",
                "description": "Hour for scheduled update 0-23 (default: 3)",
            },
            "minute": {
                "type": "INTEGER",
                "description": "Minute for scheduled update 0-59 (default: 0)",
            },
            "shutdown_when_done": {
                "type": "BOOLEAN",
                "description": "Shut down PC when download finishes",
            },
        },
        "required": [],
    }
    assert confirmation == {
        "type": "BOOLEAN",
        "description": "Set true only after the user explicitly confirmed this action.",
    }

    assert registry.risk_class("computer_control") == "destructive"
    assert registry.risk_class("game_updater") == "destructive"
    assert "confirmation" in registry.run(
        "computer_control", {"action": "screenshot"}
    )
    assert "confirmation" in registry.run("game_updater", {"action": "list"})
    assert registry.run(
        "computer_control", {"action": "screenshot", "confirmed": True}
    ) == "computer:screenshot"
    assert registry.run(
        "game_updater", {"action": "list", "confirmed": True}
    ) == "game:list"


def test_group_f_actions_no_longer_duplicate_core_declarations():
    import main

    registry = discover_actions(
        Path(__file__).resolve().parents[1] / "actions", logger=lambda _m: None
    )
    core_names = {item["name"] for item in main.TOOL_DECLARATIONS}

    assert {"computer_control", "game_updater"} <= registry.names()
    assert not {"computer_control", "game_updater"} & core_names
