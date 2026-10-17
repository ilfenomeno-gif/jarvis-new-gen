import * as vscode from "vscode";
import { randomBytes } from "node:crypto";
import WebSocket from "ws";
import {
  buildChatRequest,
  isChatHistory,
  MAX_RECONNECT_ATTEMPTS,
  parseServerMessage,
  reconnectDelay,
  shouldReconnect,
} from "./protocol";

const VIEW_ID = "jarvis.sidebar";
const PING_INTERVAL_MS = 20_000;

class JarvisViewProvider implements vscode.WebviewViewProvider, vscode.Disposable {
  private view: vscode.WebviewView | undefined;
  private socket: WebSocket | undefined;
  private reconnectTimer: NodeJS.Timeout | undefined;
  private pingTimer: NodeJS.Timeout | undefined;
  private reconnectAttempts = 0;
  private disposed = false;
  private authenticated = false;
  private readonly pendingChats = new Map<string, string>();

  constructor(private readonly context: vscode.ExtensionContext) {}

  resolveWebviewView(view: vscode.WebviewView): void {
    this.view = view;
    this.disposed = false;
    this.reconnectAttempts = 0;
    view.webview.options = {
      enableScripts: true,
      localResourceRoots: [
        vscode.Uri.joinPath(this.context.extensionUri, "media"),
        vscode.Uri.joinPath(this.context.extensionUri, "src", "webview"),
      ],
    };
    view.webview.html = this.getHtml(view.webview);
    view.webview.onDidReceiveMessage((message: unknown) => {
      this.handleWebviewMessage(message);
    });
    view.onDidDispose(() => this.disconnect());
    this.connect();
  }

  dispose(): void {
    this.disposed = true;
    this.disconnect();
  }

  private disconnect(): void {
    this.authenticated = false;
    if (this.reconnectTimer) {
      clearTimeout(this.reconnectTimer);
      this.reconnectTimer = undefined;
    }
    if (this.pingTimer) {
      clearInterval(this.pingTimer);
      this.pingTimer = undefined;
    }
    this.socket?.removeAllListeners();
    this.socket?.close();
    this.socket = undefined;
    this.view = undefined;
  }

  private getHtml(webview: vscode.Webview): string {
    const htmlUri = vscode.Uri.joinPath(
      this.context.extensionUri,
      "src",
      "webview",
      "index.html",
    );
    const styleUri = webview.asWebviewUri(
      vscode.Uri.joinPath(this.context.extensionUri, "media", "style.css"),
    );
    const scriptUri = webview.asWebviewUri(
      vscode.Uri.joinPath(
        this.context.extensionUri,
        "src",
        "webview",
        "main.js",
      ),
    );
    const chatStateUri = webview.asWebviewUri(
      vscode.Uri.joinPath(
        this.context.extensionUri,
        "src",
        "webview",
        "chat-state.js",
      ),
    );
    const nonce = getNonce();
    const csp = [
      "default-src 'none'",
      `style-src ${webview.cspSource}`,
      `script-src 'nonce-${nonce}'`,
    ].join("; ");
    const fs = require("node:fs") as typeof import("node:fs");
    return fs
      .readFileSync(htmlUri.fsPath, "utf8")
      .replace("{{CSP}}", csp)
      .replace("{{STYLE_URI}}", styleUri.toString())
      .replace("{{CHAT_STATE_URI}}", chatStateUri.toString())
      .replace("{{SCRIPT_URI}}", scriptUri.toString())
      .replace("{{NONCE}}", nonce)
      .replace("<script src=", `<script nonce="${nonce}" src=`);
  }

  private handleWebviewMessage(raw: unknown): void {
    if (
      typeof raw !== "object" ||
      raw === null ||
      !("type" in raw) ||
      raw.type !== "chat" ||
      !("id" in raw) ||
      typeof raw.id !== "string"
    ) {
      return;
    }
    if (
      !("text" in raw) ||
      typeof raw.text !== "string" ||
      !("history" in raw) ||
      !isChatHistory(raw.history)
    ) {
      this.rejectChat(raw.id, "Richiesta chat o cronologia non valida.");
      return;
    }
    let request;
    try {
      request = buildChatRequest(raw.id, raw.text, raw.history);
    } catch (error) {
      this.rejectChat(
        raw.id,
        error instanceof Error ? error.message : "Richiesta chat non valida.",
      );
      return;
    }
    if (
      !this.authenticated ||
      this.socket?.readyState !== WebSocket.OPEN
    ) {
      this.rejectChat(raw.id, "JARVIS è offline o non autenticato.");
      return;
    }
    if (this.pendingChats.size > 0) {
      this.rejectChat(raw.id, "Attendi la risposta alla richiesta in corso.");
      return;
    }
    this.pendingChats.set(raw.id, request.text);
    try {
      this.socket.send(JSON.stringify(request));
    } catch (error) {
      this.pendingChats.delete(raw.id);
      this.rejectChat(
        raw.id,
        error instanceof Error ? error.message : "Invio a JARVIS non riuscito.",
      );
    }
  }

  private connect(): void {
    if (this.disposed) {
      return;
    }
    const token = this.getToken();
    if (!token) {
      this.postConnection(
        "error",
        "Token mancante: configura jarvis.wsToken o JARVIS_WS_TOKEN.",
      );
      return;
    }

    const configuredPort = vscode.workspace
      .getConfiguration("jarvis")
      .get<number>("wsPort", 8765);
    const port =
      Number.isInteger(configuredPort) &&
      configuredPort >= 1 &&
      configuredPort <= 65535
        ? configuredPort
        : 8765;
    const socket = new WebSocket(`ws://127.0.0.1:${port}`);
    this.socket = socket;
    this.authenticated = false;
    this.postConnection("connecting", `Connessione a JARVIS sulla porta ${port}…`);

    socket.on("open", () => {
      socket.send(JSON.stringify({ type: "auth", token }));
    });
    socket.on("message", (data: WebSocket.RawData) => {
      this.handleServerMessage(data.toString());
    });
    socket.on("error", (error: Error) => {
      this.postConnection("error", `WebSocket: ${error.message}`);
    });
    socket.on("close", (code: number) => {
      this.authenticated = false;
      if (this.pingTimer) {
        clearInterval(this.pingTimer);
        this.pingTimer = undefined;
      }
      if (code === 4001) {
        this.postConnection(
          "error",
          "Autenticazione rifiutata (codice 4001). Controlla jarvis.wsToken.",
        );
        this.failPendingChats("Autenticazione JARVIS rifiutata.");
        return;
      }
      this.failPendingChats("Connessione a JARVIS interrotta.");
      this.scheduleReconnect();
    });
  }

  private handleServerMessage(raw: string): void {
    const message = parseServerMessage(raw);
    if (!message) {
      this.postConnection("error", "Risposta non valida dal server JARVIS.");
      return;
    }
    if (message.type === "auth_ok") {
      this.authenticated = true;
      this.reconnectAttempts = 0;
      this.postConnection("ready", "Autenticato con JARVIS.");
      this.pingTimer = setInterval(() => {
        if (this.authenticated && this.socket?.readyState === WebSocket.OPEN) {
          this.socket.send(JSON.stringify({ type: "ping" }));
        }
      }, PING_INTERVAL_MS);
      return;
    }
    if (message.type === "pong") {
      this.postConnection("ready", "JARVIS connesso (pong).");
      return;
    }
    if (message.type === "status") {
      this.postToWebview({ ...message, type: "serverStatus" });
      if (message.state === "error") {
        this.failPendingChats(message.detail);
      }
      return;
    }
    if (message.type === "reply") {
      const id = String(message.id);
      if (!this.pendingChats.has(id)) {
        return;
      }
      this.pendingChats.delete(id);
      this.postToWebview({
        type: "chatReply",
        id,
        text: message.text,
      });
    }
  }

  private scheduleReconnect(): void {
    if (this.disposed) {
      return;
    }
    if (!shouldReconnect(this.reconnectAttempts)) {
      this.postConnection(
        "error",
        `Connessione a JARVIS interrotta. Raggiunto il limite di ${MAX_RECONNECT_ATTEMPTS} tentativi.`,
      );
      return;
    }
    this.reconnectAttempts += 1;
    const delay = reconnectDelay(this.reconnectAttempts);
    this.postConnection(
      "connecting",
      `Nuovo tentativo ${this.reconnectAttempts}/${MAX_RECONNECT_ATTEMPTS} tra ${delay / 1000}s…`,
    );
    this.reconnectTimer = setTimeout(() => {
      this.reconnectTimer = undefined;
      this.connect();
    }, delay);
  }

  private getToken(): string {
    const environmentToken = process.env.JARVIS_WS_TOKEN?.trim();
    if (environmentToken) {
      return environmentToken;
    }
    return (
      vscode.workspace.getConfiguration("jarvis").get<string>("wsToken", "").trim()
    );
  }

  private postConnection(state: string, detail: string): void {
    this.postToWebview({ type: "connection", state, detail });
  }

  private rejectChat(id: string, detail: string): void {
    this.postToWebview({ type: "chatError", id, detail });
  }

  private failPendingChats(detail: string): void {
    for (const id of this.pendingChats.keys()) {
      this.rejectChat(id, detail);
    }
    this.pendingChats.clear();
  }

  private postToWebview(message: Record<string, unknown>): void {
    void this.view?.webview.postMessage(message);
  }
}

export function activate(context: vscode.ExtensionContext): void {
  const provider = new JarvisViewProvider(context);
  context.subscriptions.push(
    vscode.window.registerWebviewViewProvider(VIEW_ID, provider),
    vscode.commands.registerCommand("jarvis.openPanel", () =>
      vscode.commands.executeCommand("workbench.view.extension.jarvis"),
    ),
    provider,
  );
}

export function deactivate(): void {}

function getNonce(): string {
  return randomBytes(16).toString("base64");
}
