(function () {
  const vscode = acquireVsCodeApi();
  const status = document.getElementById("status");
  const messages = document.getElementById("messages");
  const form = document.getElementById("composer");
  const input = document.getElementById("messageInput");
  const sendButton = document.getElementById("sendButton");
  const pending = new Map();
  const history = [];
  let connected = false;
  let requestInFlight = false;

  const { buildChatRequest, completeChatHistory } = window.JarvisChatState;

  function addMessage(kind, text) {
    const item = document.createElement("div");
    item.className = `message ${kind}`;
    item.textContent = text;
    messages.appendChild(item);
    return item;
  }

  function updateComposer() {
    input.disabled = !connected || requestInFlight;
    sendButton.disabled = !connected || requestInFlight;
    if (requestInFlight) {
      status.textContent = "JARVIS sta pensando…";
    }
  }

  function setError(detail) {
    status.textContent = detail;
    status.classList.add("error");
  }

  function markOffline(detail) {
    connected = false;
    status.classList.add("error");
    status.textContent =
      detail || "JARVIS non è raggiungibile. Verifica che il server sia avviato.";
    updateComposer();
  }

  function failPending(detail) {
    for (const [id, request] of pending) {
      request.messageElement.remove();
      input.value = request.text;
      pending.delete(id);
    }
    requestInFlight = false;
    if (detail) {
      setError(detail);
    }
    updateComposer();
  }

  window.addEventListener("message", (event) => {
    const message = event.data;
    if (!message || typeof message !== "object") {
      return;
    }
    if (message.type === "connection") {
      if (message.state === "ready") {
        connected = true;
        status.textContent = String(message.detail || "JARVIS pronto.");
        status.classList.remove("error");
      } else if (message.state === "error") {
        markOffline(String(message.detail || "Errore di connessione a JARVIS."));
        failPending();
      } else {
        connected = false;
        status.textContent = String(message.detail || "Connessione a JARVIS…");
      }
      updateComposer();
      return;
    }
    if (message.type === "chatReply" && typeof message.id === "string") {
      const request = pending.get(message.id);
      if (!request) {
        return;
      }
      pending.delete(message.id);
      try {
        history.splice(
          0,
          history.length,
          ...completeChatHistory(history, request.text, String(message.text || "")),
        );
        addMessage("jarvis", String(message.text));
      } catch (error) {
        request.messageElement.remove();
        input.value = request.text;
        setError(
          error instanceof Error ? error.message : "Risposta JARVIS non valida.",
        );
      }
      requestInFlight = false;
      updateComposer();
      return;
    }
    if (message.type === "chatError" && typeof message.id === "string") {
      const request = pending.get(message.id);
      if (request) {
        request.messageElement.remove();
        input.value = request.text;
        pending.delete(message.id);
      }
      requestInFlight = false;
      setError(String(message.detail || "La richiesta a JARVIS non è riuscita."));
      updateComposer();
      return;
    }
    if (message.type === "serverStatus") {
      const state = String(message.state || "");
      if (state === "busy" && requestInFlight) {
        status.textContent = "JARVIS sta pensando…";
      } else if (state === "error") {
        failPending(
          String(message.detail || "Errore durante la richiesta a JARVIS."),
        );
      } else {
        status.textContent = String(message.detail || "JARVIS pronto.");
        status.classList.remove("error");
      }
      updateComposer();
    }
  });

  input.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && (event.ctrlKey || event.metaKey)) {
      event.preventDefault();
      form.requestSubmit();
    }
  });

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const text = input.value.trim();
    if (!text || !connected || requestInFlight) {
      return;
    }
    const id =
      typeof crypto.randomUUID === "function"
        ? crypto.randomUUID()
        : `${Date.now()}-${Math.random().toString(16).slice(2)}`;
    const messageElement = addMessage("user", text);
    let request;
    try {
      request = buildChatRequest(id, text, history);
    } catch (error) {
      messageElement.remove();
      setError(error instanceof Error ? error.message : "Richiesta non valida.");
      return;
    }
    pending.set(id, { text, messageElement });
    requestInFlight = true;
    input.value = "";
    status.classList.remove("error");
    updateComposer();
    vscode.postMessage(request);
  });

  updateComposer();
})();
