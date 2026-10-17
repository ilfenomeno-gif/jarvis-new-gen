const assert = require("node:assert/strict");
const test = require("node:test");
const {
  MAX_HISTORY_TURNS,
  MAX_RECONNECT_ATTEMPTS,
  buildChatRequest,
  completeChatHistory,
  isChatHistory,
  parseServerMessage,
  parseToolPrompt,
  reconnectDelay,
  shouldReconnect,
} = require("../dist/protocol.js");
const chatState = require("../src/webview/chat-state.js");

test("validates the prompt accepted by the language model tool", () => {
  assert.equal(parseToolPrompt({ prompt: "  ciao " }), "ciao");
  assert.throws(() => parseToolPrompt({}), /prompt/);
  assert.throws(() => parseToolPrompt({ prompt: "  " }), /prompt/);
  assert.throws(() => parseToolPrompt({ prompt: "x".repeat(4001) }), /4000/);
  assert.throws(() => parseToolPrompt(null), /prompt/);
});

test("parses status and reply protocol messages", () => {
  assert.deepEqual(
    parseServerMessage('{"type":"status","state":"ready","detail":"authenticated"}'),
    { type: "status", state: "ready", detail: "authenticated" },
  );
  assert.deepEqual(
    parseServerMessage('{"type":"reply","id":"c1","text":"hello"}'),
    { type: "reply", id: "c1", text: "hello" },
  );
});

test("rejects malformed and unsupported server messages", () => {
  assert.equal(parseServerMessage("{broken"), undefined);
  assert.equal(parseServerMessage('{"type":"status","state":"unknown","detail":"x"}'), undefined);
  assert.equal(parseServerMessage('{"type":"chat","text":"x"}'), undefined);
});

test("uses capped exponential reconnect delays", () => {
  assert.deepEqual(
    [1, 2, 3, 4, 5, 6].map(reconnectDelay),
    [1000, 2000, 4000, 8000, 16000, 30000],
  );
  assert.throws(() => reconnectDelay(0), RangeError);
  assert.equal(MAX_RECONNECT_ATTEMPTS, 3);
  assert.deepEqual([0, 1, 2, 3].map(shouldReconnect), [true, true, true, false]);
});

test("builds chat messages with id, prompt and previous turns", () => {
  const history = [
    { role: "user", parts: [{ text: "My name is Marco" }] },
    { role: "model", parts: [{ text: "Nice to meet you, Marco" }] },
  ];

  assert.deepEqual(buildChatRequest("id-1", "Who am I?", history), {
    type: "chat",
    id: "id-1",
    text: "Who am I?",
    history,
  });
});

test("appends a successful exchange in user/model order", () => {
  const history = [{ role: "user", parts: [{ text: "Earlier" }] }];

  assert.deepEqual(completeChatHistory(history, "Question", "Answer"), [
    ...history,
    { role: "user", parts: [{ text: "Question" }] },
    { role: "model", parts: [{ text: "Answer" }] },
  ]);
  assert.equal(history.length, 1);
});

test("trims outgoing and retained history to the latest 20 turns", () => {
  const history = Array.from({ length: MAX_HISTORY_TURNS + 4 }, (_, index) => ({
    role: index % 2 === 0 ? "user" : "model",
    parts: [{ text: `Turn ${index}` }],
  }));

  assert.equal(buildChatRequest("id", "next", history).history.length, 20);
  const completed = completeChatHistory(history, "next", "answer");
  assert.equal(completed.length, 20);
  assert.equal(completed[0].parts[0].text, "Turn 6");
  assert.equal(completed.at(-1).parts[0].text, "answer");
});

test("rejects malformed chat history and empty chat fields", () => {
  assert.equal(isChatHistory([{ role: "system", parts: [{ text: "bad" }] }]), false);
  assert.throws(() => buildChatRequest("", "prompt", []), /id must not be empty/);
  assert.throws(() => buildChatRequest("id", " ", []), /prompt must not be empty/);
  assert.throws(() => buildChatRequest("id", "prompt", [{}]), /valid user\/model turns/);
});

test("reports empty response errors without adding a history turn", () => {
  assert.throws(
    () => completeChatHistory([], "prompt", " "),
    /response must not be empty/,
  );
});

test("WebView chat state constructs messages and appends only completed exchanges", () => {
  const prompt = "Come mi chiamo?";
  const initialHistory = [
    { role: "user", parts: [{ text: "Mi chiamo Marco" }] },
    { role: "model", parts: [{ text: "Piacere, Marco" }] },
  ];
  const request = chatState.buildChatRequest("uuid-1", prompt, initialHistory);

  assert.deepEqual(request, {
    type: "chat",
    id: "uuid-1",
    text: prompt,
    history: initialHistory,
  });
  assert.deepEqual(
    chatState.completeChatHistory(initialHistory, prompt, "Marco"),
    [
      ...initialHistory,
      { role: "user", parts: [{ text: prompt }] },
      { role: "model", parts: [{ text: "Marco" }] },
    ],
  );
});

test("WebView chat state trims history and rejects invalid input or response", () => {
  const history = Array.from({ length: 24 }, (_, index) => ({
    role: index % 2 === 0 ? "user" : "model",
    parts: [{ text: `Turn ${index}` }],
  }));
  assert.equal(
    chatState.buildChatRequest("uuid-2", "next", history).history.length,
    chatState.MAX_HISTORY_TURNS,
  );
  assert.equal(
    chatState.completeChatHistory(history, "next", "answer").length,
    chatState.MAX_HISTORY_TURNS,
  );
  assert.throws(
    () => chatState.buildChatRequest("uuid", "next", [{ role: "system" }]),
    /valid user\/model turns/,
  );
  assert.throws(
    () => chatState.completeChatHistory([], "next", ""),
    /response must not be empty/,
  );
});
