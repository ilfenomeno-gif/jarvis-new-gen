import asyncio
from types import SimpleNamespace

from main import JarvisLive


class FakeUI:
    muted = False

    def __init__(self):
        self.logs = []
        self.states = []

    def set_state(self, state):
        self.states.append(state)

    def write_log(self, text):
        self.logs.append(text)


class FakeRouter:
    backend = "local"

    def __init__(self, responses):
        self.responses = iter(responses)
        self.calls = []

    def stream_chat(self, messages, tools=None):
        self.calls.append((messages.copy(), tools))
        return next(self.responses)

    def model_name(self):
        return "qwen2.5:7b"

    def switch(self, backend):
        self.backend = backend


def _live(router):
    live = JarvisLive.__new__(JarvisLive)
    live.ui = FakeUI()
    live._brain_router = router
    live._local_messages = [{"role": "system", "content": "test system prompt"}]
    live._local_chat_lock = asyncio.Lock()
    live._local_pending_confirmation = None
    live._asst_name = "JARVIS"
    live._session_log = []
    live._select_local_tool_declarations = lambda _text: [{
        "name": "open_app",
        "description": "Open an app",
        "parameters": {
            "type": "OBJECT",
            "properties": {"app_name": {"type": "STRING"}},
            "required": ["app_name"],
        },
    }]
    return live


def test_local_text_runs_model_tool_call_and_logs_final_response():
    router = FakeRouter([
        [
            {
                "type": "tool_call",
                "id": "call-1",
                "name": "open_app",
                "args": {"app_name": "Notepad"},
            },
            {"type": "done", "full_text": ""},
        ],
        [
            {"type": "content", "text": "Notepad aperto."},
            {"type": "done", "full_text": "Notepad aperto."},
        ],
    ])
    live = _live(router)
    executed = []

    async def execute_tool(call):
        executed.append((call.id, call.name, call.args))
        return SimpleNamespace(response={"result": "opened"})

    live._execute_tool = execute_tool
    asyncio.run(live._handle_local_text("Apri Notepad"))

    assert executed == [("call-1", "open_app", {"app_name": "Notepad"})]
    assert router.calls[0][1][0]["function"]["parameters"]["type"] == "object"
    assert live.ui.logs == ["JARVIS: Notepad aperto."]
    assert live._local_messages[-1] == {
        "role": "assistant",
        "content": "Notepad aperto.",
    }


def test_local_model_cannot_run_a_tool_not_selected_for_the_request():
    router = FakeRouter([[
        {
            "type": "tool_call",
            "id": "call-1",
            "name": "quick_notes",
            "args": {"text": "nota non richiesta"},
        },
        {"type": "done", "full_text": ""},
    ]])
    live = _live(router)
    live._select_local_tool_declarations = lambda _text: []
    executed = []

    async def execute_tool(call):
        executed.append(call.name)
        return SimpleNamespace(response={"result": "unexpected"})

    live._execute_tool = execute_tool
    asyncio.run(live._handle_local_text("Dimmi una curiosità"))

    assert router.calls[0][1] == []
    assert executed == []
    assert live.ui.logs == [
        "JARVIS: Non posso eseguire uno strumento non pertinente alla richiesta."
    ]


def test_local_state_changing_tool_is_not_repeated_in_one_request():
    router = FakeRouter([
        [
            {
                "type": "tool_call",
                "id": "call-1",
                "name": "quick_notes",
                "args": {"text": "prima nota"},
            },
            {"type": "done", "full_text": ""},
        ],
        [
            {
                "type": "tool_call",
                "id": "call-2",
                "name": "quick_notes",
                "args": {"text": "nota duplicata"},
            },
            {"type": "done", "full_text": ""},
        ],
    ])
    live = _live(router)
    live._select_local_tool_declarations = lambda _text: [{"name": "quick_notes"}]
    executed = []

    async def execute_tool(call):
        executed.append(call.args["text"])
        return SimpleNamespace(response={"result": "Nota salvata."})

    live._execute_tool = execute_tool
    asyncio.run(live._handle_local_text("Prendi nota"))

    assert executed == ["prima nota"]
    assert live.ui.logs == [
        "JARVIS: Ho interrotto un tentativo di ripetere la stessa azione."
    ]


def test_local_app_launch_requires_confirmation_from_a_separate_user_message():
    router = FakeRouter([[
        {
            "type": "tool_call",
            "id": "call-1",
            "name": "app_launcher",
            "args": {"name": "Notepad", "confirmed": True},
        },
        {"type": "done", "full_text": ""},
    ]])
    live = _live(router)
    live._select_local_tool_declarations = lambda _text: [{
        "name": "app_launcher",
        "risk_class": "destructive",
    }]
    executed = []

    async def execute_tool(call):
        executed.append((call.name, call.args.copy()))
        if call.args.get("confirmed") is True:
            return SimpleNamespace(response={"result": "Launch completed for Notepad."})
        return SimpleNamespace(response={
            "result": (
                "Action 'app_launcher' is destructive. Ask the user for explicit "
                "confirmation, then call it again with confirmed=true."
            )
        })

    live._execute_tool = execute_tool
    asyncio.run(live._handle_local_text("Apri il blocco note"))
    assert live._local_pending_confirmation == {
        "id": "call-1",
        "name": "app_launcher",
        "args": {"name": "Notepad"},
    }
    assert executed == [("app_launcher", {"name": "Notepad"})]

    asyncio.run(live._handle_local_text("Sì, confermo"))

    assert executed == [
        ("app_launcher", {"name": "Notepad"}),
        ("app_launcher", {"name": "Notepad", "confirmed": True}),
    ]
    assert live._local_pending_confirmation is None
    assert live.ui.logs[-1] == "JARVIS: Launch completed for Notepad."


def test_local_voice_transcript_is_routed_to_local_model():
    live = _live(FakeRouter([]))
    handled = []

    async def handle_local_text(text):
        handled.append(text)

    live._handle_local_text = handle_local_text

    async def run():
        assert live._route_voice_transcript("Dimmi una curiosità")
        await asyncio.sleep(0)

    asyncio.run(run())
    assert handled == ["Dimmi una curiosità"]


def test_switching_to_cloud_cancels_pending_local_confirmation():
    live = _live(FakeRouter([]))
    live._local_pending_confirmation = {
        "id": "call-1",
        "name": "app_launcher",
        "args": {"name": "Notepad"},
    }

    assert live._route_voice_transcript("Torna al cloud")
    assert live._brain_router.backend == "gemini"
    assert live._local_pending_confirmation is None
