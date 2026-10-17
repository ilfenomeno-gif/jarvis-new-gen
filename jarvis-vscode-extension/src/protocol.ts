export const MAX_TOOL_PROMPT_CHARS = 4000;
export const TOOL_TIMEOUT_MS = 60_000;

export type ServerMessage =
  | { type: "auth_ok" }
  | { type: "pong" }
  | { type: "status"; state: "ready" | "busy" | "error"; detail: string }
  | { type: "reply"; id: string | number; text: string };

export type ChatTurn = {
  role: "user" | "model";
  parts: Array<{ text: string }>;
};

export function parseToolPrompt(input: unknown): string {
  const prompt =
    typeof input === "object" && input !== null && "prompt" in input
      ? (input as { prompt: unknown }).prompt
      : undefined;
  if (typeof prompt !== "string" || !prompt.trim()) {
    throw new Error("Il tool richiede un campo 'prompt' non vuoto.");
  }
  if (prompt.length > MAX_TOOL_PROMPT_CHARS) {
    throw new Error(`Il prompt supera ${MAX_TOOL_PROMPT_CHARS} caratteri.`);
  }
  return prompt.trim();
}

export const MAX_HISTORY_TURNS = 20;
export const MAX_RECONNECT_ATTEMPTS = 3;

export function shouldReconnect(attempts: number): boolean {
  return Number.isInteger(attempts) && attempts >= 0 && attempts < MAX_RECONNECT_ATTEMPTS;
}

export function isChatHistory(value: unknown): value is ChatTurn[] {
  return (
    Array.isArray(value) &&
    value.every(
      (turn) =>
        typeof turn === "object" &&
        turn !== null &&
        "role" in turn &&
        (turn.role === "user" || turn.role === "model") &&
        "parts" in turn &&
        Array.isArray(turn.parts) &&
        turn.parts.length > 0 &&
        turn.parts.every(
          (part: unknown) =>
            typeof part === "object" &&
            part !== null &&
            "text" in part &&
            typeof part.text === "string",
        ),
    )
  );
}

export function buildChatRequest(
  id: string,
  text: string,
  history: unknown,
): {
  type: "chat";
  id: string;
  text: string;
  history: ChatTurn[];
} {
  if (!id.trim()) {
    throw new Error("Chat request id must not be empty.");
  }
  if (!text.trim()) {
    throw new Error("Chat prompt must not be empty.");
  }
  if (!isChatHistory(history)) {
    throw new Error("Chat history must contain valid user/model turns.");
  }
  return {
    type: "chat",
    id,
    text,
    history: history.slice(-MAX_HISTORY_TURNS),
  };
}

export function completeChatHistory(
  history: ChatTurn[],
  prompt: string,
  answer: string,
): ChatTurn[] {
  if (!prompt.trim()) {
    throw new Error("Chat prompt must not be empty.");
  }
  if (!answer.trim()) {
    throw new Error("Chat response must not be empty.");
  }
  const completedTurns: ChatTurn[] = [
    { role: "user", parts: [{ text: prompt }] },
    { role: "model", parts: [{ text: answer }] },
  ];
  return [
    ...history,
    ...completedTurns,
  ].slice(-MAX_HISTORY_TURNS);
}

export function parseServerMessage(raw: unknown): ServerMessage | undefined {
  if (typeof raw !== "string") {
    return undefined;
  }

  let value: unknown;
  try {
    value = JSON.parse(raw);
  } catch {
    return undefined;
  }
  if (typeof value !== "object" || value === null || !("type" in value)) {
    return undefined;
  }

  const message = value as Record<string, unknown>;
  switch (message.type) {
    case "auth_ok":
    case "pong":
      return { type: message.type };
    case "status":
      if (
        (message.state === "ready" ||
          message.state === "busy" ||
          message.state === "error") &&
        typeof message.detail === "string"
      ) {
        return {
          type: "status",
          state: message.state,
          detail: message.detail,
        };
      }
      return undefined;
    case "reply":
      if (
        (typeof message.id === "string" || typeof message.id === "number") &&
        typeof message.text === "string"
      ) {
        return {
          type: "reply",
          id: message.id,
          text: message.text,
        };
      }
      return undefined;
    default:
      return undefined;
  }
}

export function reconnectDelay(attempt: number): number {
  if (!Number.isInteger(attempt) || attempt < 1) {
    throw new RangeError("attempt must be a positive integer");
  }
  return Math.min(1000 * 2 ** (attempt - 1), 30_000);
}
