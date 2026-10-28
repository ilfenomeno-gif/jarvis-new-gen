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
    live._asst_name = "JARVIS"
    live._session_log = []
    live._select_tool_declarations = lambda: [{
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
