import * as vscode from "vscode";
import { randomBytes } from "node:crypto";
import WebSocket from "ws";
import {
  buildChatRequest,
  isChatHistory,
  MAX_RECONNECT_ATTEMPTS,
  parseServerMessage,
  parseToolPrompt,
  reconnectDelay,
  shouldReconnect,
  TOOL_TIMEOUT_MS,
} from "./protocol";

const VIEW_ID = "jarvis.sidebar";
const PING_INTERVAL_MS = 20_000;
const TOKEN_SECRET_KEY = "jarvis.wsToken";

class JarvisViewProvider implements vscode.WebviewViewProvider, vscode.Disposable {
  private view: vscode.WebviewView | undefined;
  private socket: WebSocket | undefined;
  private reconnectTimer: NodeJS.Timeout | undefined;
  private pingTimer: NodeJS.Timeout | undefined;
  private reconnectAttempts = 0;
  private connectionGeneration = 0;
  private disposed = false;
  private authenticated = false;
  private legacyTokenCleanupWarningShown = false;
  private readonly pendingChats = new Map<string, string>();
  private readonly askWaiters = new Map<
    string,
    { resolve: (text: string) => void; reject: (error: Error) => void }
  >();

  constructor(private readonly context: vscode.ExtensionContext) {}

  ask(prompt: string, cancellation?: vscode.CancellationToken): Promise<string> {
    if (!this.authenticated || this.socket?.readyState !== WebSocket.OPEN) {
      return Promise.reject(
        new Error("JARVIS è offline o non autenticato: apri il pannello JARVIS e imposta il token."),
      );
    }
    if (this.pendingChats.size > 0) {
      return Promise.reject(new Error("Attendi la risposta alla richiesta in corso."));
    }
    const socket = this.socket;
    const id = `lm-${randomBytes(6).toString("hex")}`;
    const request = buildChatRequest(id, prompt, []);
    return new Promise<string>((resolve, reject) => {
      const timer = setTimeout(
        () => this.settleAsk(id, new Error("JARVIS non ha risposto in tempo.")),
        TOOL_TIMEOUT_MS,
      );
      const subscription = cancellation?.onCancellationRequested(() =>
        this.settleAsk(id, new Error("Richiesta annullata.")),
      );
      const finish = () => {
        clearTimeout(timer);
        subscription?.dispose();
      };
      this.askWaiters.set(id, {
        resolve: (text) => {
          finish();
          resolve(text);
        },
        reject: (error) => {
          finish();
          reject(error);
        },
      });
      this.pendingChats.set(id, request.text);
      try {
        socket.send(JSON.stringify(request));
      } catch (error) {
        this.settleAsk(id, error instanceof Error ? error : new Error("Invio non riuscito."));
      }
    });
  }

  private settleAsk(id: string, error: Error): void {
    this.pendingChats.delete(id);
    const waiter = this.askWaiters.get(id);
    this.askWaiters.delete(id);
    waiter?.reject(error);
  }

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

  async setToken(token: string): Promise<void> {
    const normalizedToken = token.trim();
    if (!normalizedToken) {
      throw new Error("Il token di connessione non può essere vuoto.");
    }
    await this.context.secrets.store(TOKEN_SECRET_KEY, normalizedToken);
    this.reconnectAttempts = 0;
    this.resetSocket();
    this.failPendingChats("Token di connessione aggiornato.");
    this.connect();
  }

  private disconnect(): void {
    this.resetSocket();
    this.view = undefined;
  }

  private resetSocket(): void {
    this.connectionGeneration += 1;
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
    this.authenticated = false;
    for (const id of [...this.askWaiters.keys()]) {
      this.settleAsk(id, new Error("Connessione a JARVIS interrotta."));
    }
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
    void this.connectWithToken(++this.connectionGeneration);
  }

  private async connectWithToken(generation: number): Promise<void> {
    let token: string;
    try {
      token = await this.getToken();
    } catch (error) {
      if (generation !== this.connectionGeneration) {
        return;
      }
      this.postConnection(
        "error",
        `Impossibile recuperare il token JARVIS: ${
          error instanceof Error ? error.message : "errore sconosciuto"
        }`,
      );
      return;
    }
    if (
      generation !== this.connectionGeneration ||
      this.disposed ||
      !this.view
    ) {
      return;
    }
    if (!token) {
      this.postConnection(
        "error",
        "Token mancante: esegui «JARVIS: Set Connection Token» o imposta JARVIS_WS_TOKEN.",
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
          "Autenticazione rifiutata (codice 4001). Verifica il token di connessione.",
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
      const waiter = this.askWaiters.get(id);
      if (waiter) {
        this.askWaiters.delete(id);
        waiter.resolve(message.text);
        return;
      }
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

  private async getToken(): Promise<string> {
    const configuration = vscode.workspace.getConfiguration("jarvis");
    const legacyToken = configuration.get<string>("wsToken", "").trim();
    let storedToken = await this.context.secrets.get(TOKEN_SECRET_KEY);
    if (legacyToken) {
      if (!storedToken) {
        await this.context.secrets.store(TOKEN_SECRET_KEY, legacyToken);
        storedToken = legacyToken;
      }
      try {
        await configuration.update(
          "wsToken",
          undefined,
          vscode.ConfigurationTarget.Global,
        );
      } catch (error) {
        if (!this.legacyTokenCleanupWarningShown) {
          this.legacyTokenCleanupWarningShown = true;
          await vscode.window.showWarningMessage(
            `Token migrato in SecretStorage, ma non è stato possibile rimuoverlo dalle impostazioni utente: ${
              error instanceof Error ? error.message : "errore sconosciuto"
            }`,
          );
        }
      }
    }
    const environmentToken = process.env.JARVIS_WS_TOKEN?.trim();
    if (environmentToken) {
      return environmentToken;
    }
    return storedToken?.trim() ?? "";
  }

  private postConnection(state: string, detail: string): void {
    this.postToWebview({ type: "connection", state, detail });
  }

  private rejectChat(id: string, detail: string): void {
    this.postToWebview({ type: "chatError", id, detail });
  }

  private failPendingChats(detail: string): void {
    for (const id of [...this.pendingChats.keys()]) {
      if (this.askWaiters.has(id)) {
        this.settleAsk(id, new Error(detail));
      } else {
        this.rejectChat(id, detail);
      }
    }
    this.pendingChats.clear();
  }

  private postToWebview(message: Record<string, unknown>): void {
    void this.view?.webview.postMessage(message);
  }
}

function registerLanguageModelTool(provider: JarvisViewProvider): vscode.Disposable[] {
  // vscode.lm is absent on older hosts; the extension must keep working there.
  const lm = (vscode as unknown as { lm?: typeof vscode.lm }).lm;
  if (!lm || typeof lm.registerTool !== "function") {
    return [];
  }
  return [
    lm.registerTool<{ prompt: string }>("jarvis_ask", {
      prepareInvocation(options) {
        return {
          invocationMessage: "Chiedo a JARVIS…",
          confirmationMessages: {
            title: "Inviare la richiesta a JARVIS?",
            message: new vscode.MarkdownString(
              `JARVIS può eseguire azioni sul computer. Richiesta:\n\n> ${String(
                options.input?.prompt ?? "",
              ).slice(0, 500)}`,
            ),
          },
        };
      },
      async invoke(options, token) {
        const answer = await provider.ask(parseToolPrompt(options.input), token);
        return new vscode.LanguageModelToolResult([
          new vscode.LanguageModelTextPart(answer),
        ]);
      },
    }),
  ];
}

export function activate(context: vscode.ExtensionContext): void {
  const provider = new JarvisViewProvider(context);
  context.subscriptions.push(
    vscode.window.registerWebviewViewProvider(VIEW_ID, provider),
    vscode.commands.registerCommand("jarvis.openPanel", () =>
      vscode.commands.executeCommand("workbench.view.extension.jarvis"),
    ),
    ...registerLanguageModelTool(provider),
    vscode.commands.registerCommand("jarvis.setConnectionToken", async () => {
      const token = await vscode.window.showInputBox({
        password: true,
        ignoreFocusOut: true,
        prompt: "Inserisci il token condiviso con il server JARVIS locale.",
      });
      if (token === undefined) {
        return;
      }
      try {
        await provider.setToken(token);
        await vscode.window.showInformationMessage(
          "Token JARVIS salvato in SecretStorage.",
        );
      } catch (error) {
        await vscode.window.showErrorMessage(
          `Impossibile salvare il token JARVIS: ${
            error instanceof Error ? error.message : "errore sconosciuto"
          }`,
        );
      }
    }),
    provider,
  );
}

export function deactivate(): void {}

function getNonce(): string {
  return randomBytes(16).toString("base64");
}
