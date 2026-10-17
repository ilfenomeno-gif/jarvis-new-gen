(function (root, factory) {
  const chatState = factory();
  if (typeof module === "object" && module.exports) {
    module.exports = chatState;
  }
  root.JarvisChatState = chatState;
})(globalThis, function () {
  const MAX_HISTORY_TURNS = 20;

  function isHistory(history) {
    return (
      Array.isArray(history) &&
      history.every(
        (turn) =>
          turn &&
          typeof turn === "object" &&
          (turn.role === "user" || turn.role === "model") &&
          Array.isArray(turn.parts) &&
          turn.parts.length > 0 &&
          turn.parts.every(
            (part) =>
              part &&
              typeof part === "object" &&
              typeof part.text === "string",
          ),
      )
    );
  }

  function buildChatRequest(id, text, history) {
    if (typeof id !== "string" || !id.trim()) {
      throw new Error("Chat request id must not be empty.");
    }
    if (typeof text !== "string" || !text.trim()) {
      throw new Error("Chat prompt must not be empty.");
    }
    if (!isHistory(history)) {
      throw new Error("Chat history must contain valid user/model turns.");
    }
    return {
      type: "chat",
      id,
      text,
      history: history.slice(-MAX_HISTORY_TURNS),
    };
  }

  function completeChatHistory(history, prompt, answer) {
    if (!isHistory(history)) {
      throw new Error("Chat history must contain valid user/model turns.");
    }
    if (typeof prompt !== "string" || !prompt.trim()) {
      throw new Error("Chat prompt must not be empty.");
    }
    if (typeof answer !== "string" || !answer.trim()) {
      throw new Error("Chat response must not be empty.");
    }
    return [
      ...history,
      { role: "user", parts: [{ text: prompt }] },
      { role: "model", parts: [{ text: answer }] },
    ].slice(-MAX_HISTORY_TURNS);
  }

  return {
    MAX_HISTORY_TURNS,
    buildChatRequest,
    completeChatHistory,
  };
});
