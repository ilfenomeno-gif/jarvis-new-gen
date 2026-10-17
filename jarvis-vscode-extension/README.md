# JARVIS VS Code Extension

This extension is a thin VS Code client for the local Python JARVIS service.
It hosts the chat in a WebView and connects to the backend over an authenticated
WebSocket on loopback (`127.0.0.1`, default port `8765`). It does not hold the
Gemini API key; Gemini requests are handled by the Python backend.

## Connect to JARVIS

1. Start the JARVIS desktop application and its local WebSocket service.
2. In VS Code, run **JARVIS: Set Connection Token** and enter the shared token
   from `Mark-LIV-main/config/api_keys.json` (`ws_token`).
3. Open **JARVIS: Open Panel**.

The extension stores the connection token in VS Code `SecretStorage`. Existing
`jarvis.wsToken` user settings are migrated to `SecretStorage` and removed from
the user settings when the extension connects. If VS Code cannot remove the
legacy value, the extension warns and still connects using the migrated secret.
For managed environments, `JARVIS_WS_TOKEN` in the Extension Host process
remains an environment-variable override.

The WebSocket port can be changed with `jarvis.wsPort`. The backend remains
bound to loopback and validates the shared token before accepting messages.

## Development and tests

```powershell
npm ci
npm test
```
