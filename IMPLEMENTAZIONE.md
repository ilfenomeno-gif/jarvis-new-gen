# Piano di implementazione: Tool, Skill, Connettori MCP

Checklist di riferimento. **Dopo ogni step**: rileggere questo file, spuntare le caselle, annotare il test eseguito nel log in fondo.

Principio guida: *i connettori (MCP) sono infrastruttura, le skill sono conoscenza procedurale.* Riusare i registry esistenti, niente riscritture, ogni step verificato con test reali.

## Stato attuale verificato

- `ActionRegistry` (`Mark-LIV-main/core/action_loader.py`) collegato a `main.py`; solo `vscode_agent.py` e `vscode_control.py` espongono `TOOL`.
- `PluginRegistry` (`core/plugin_loader.py`) con client MCP GEV; `ws_server.py` loopback autenticato.
- Estensione VS Code: token in `SecretStorage`.
- `main.py` ha ancora rami `elif name == ...` statici (vedi inventario in Fase 1).
- Aggiunti nelle fasi 1-6: registry con `risk_class`, `SecretStore`, audit, connettori, skill, router, trasporti MCP, server MCP, LM Tool, `VoiceTransport`.

## Fase 0: Fondamenta (completata, da committare)

- [x] Token estensione in `vscode.SecretStorage` + comando `JARVIS: Set Connection Token` + migrazione `jarvis.wsToken`
- [x] `discover_actions` collegato a `main.py` (dichiarazioni + dispatch + nomi riservati)
- [x] Test `tests/test_action_loader.py`
- [x] Job CI `vscode-extension`
- [x] Commit + push + CI remota verde (commit `5dee2ea`, job jarvis/gev/vscode-extension success)

## Fase 1: Normalizzare i tool (parziale: infrastruttura completa, migrazione graduale)

- [x] Inventario dei rami statici di `_execute_tool`. Già nel registry: `weather_report`, `send_message`, `reminder`, `vscode_*`. Restano statici (da migrare a gruppi): `open_app`, `browser_control`, `file_controller`, `youtube_video`, `computer_settings`, `desktop_control`, `code_helper`, `dev_agent`, `large_file_reader`, `proxy_launcher`, `computer_control`, `game_updater`, `flight_finder`, agenti. Restano core per scelta: `save_memory`, `recall_memory`, `undo`, `open_website`, `press_key`, `click_link`, `read_page`, `stop_reading`, `screen_process`, `close_camera`, `web_search`, `file_processor`, `system_status`, `manage_monitor`, `shutdown_jarvis` (dipendono dallo stato interno di `main.py`)
- [x] Migrati 3 tool (`weather_report`, `send_message`, `reminder`) con rimozione di dichiarazione, ramo e import da `main.py`
- [x] Migrati altri 5 tool (`file_controller`, `desktop_control`, `large_file_reader`, `proxy_launcher`, `flight_finder`), stesso schema. Restano statici, ancora da migrare: `open_app`, `browser_control`, `youtube_video`, `computer_settings`, `code_helper`, `dev_agent`, `computer_control`, `game_updater`, agenti (dichiarazioni lunghe, da fare a gruppi). `read_active_page` condivide il modulo con `browser_control`, che può esporre un solo `TOOL`
- [x] Campo `risk_class` (`read`, `write`, `destructive`) nel contratto `TOOL`, validato
- [x] Conferma per `destructive`: parametro `confirmed` aggiunto alla dichiarazione, esecuzione rifiutata senza `confirmed=true`
- [ ] Migrare i rami statici rimanenti elencati sopra (lavoro ripetibile, un gruppo per volta; ogni migrazione = `TOOL` nel modulo + rimozione ramo/dichiarazione)
- Accettazione: suite JARVIS verde (fatto).

## Fase 2: Sicurezza

- [x] `SecretStore` (`core/secret_store.py`): DPAPI Windows, nessun fallback in chiaro, backend iniettabile
- [x] Migrare `config/api_keys.json` nel `SecretStore`: `core/api_keys.py` (SecretStore prima, file in chiaro come fallback), lettori collegati, comando `python -m core.registry_cli migrate-api-key [--remove-plain]`; test in `tests/test_api_keys.py`. Resta all'utente eseguire la migrazione sulla propria macchina. La schermata di setup ora scrive nel `SecretStore` (`save_gemini_key`). Se DPAPI non è disponibile ripiega sul file in chiaro, con WARNING nel log e `QMessageBox` di avviso (`MainWindow._warn_plaintext_key`, test in `tests/test_setup_key_ui.py` su `_on_setup_done` con `self` finto; il dialog reale non è stato visto a schermo: parziale). Ordine di `migrate` controllato il 2026-10-17: scrive nel `SecretStore`, rilegge e confronta, solo dopo azzera il chiaro (Step 1 chiuso). Prova grafica della schermata NON eseguita; migrazione sulla macchina dell'utente NON eseguita (Step 2 e 3 in attesa dell'utente), quindi l'installazione esistente ha ancora la chiave in chiaro
- [x] `ScopeManager` (`core/connectors.py`): scope dichiarati nel descrittore, concessi dall'utente, verificati a ogni chiamata
- [x] Whitelist `node`: il plugin GEV invoca solo il `node.exe` portatile atteso (controllo già in `gev_plugin.py`); la whitelist generale in `guardrails.py` resta perché `code_helper` esegue `.js`
- [x] Audit log JSONL (`core/audit_log.py`) con redazione di token/segreti negli argomenti
- [x] Revoca: cancella il token, azzera gli scope, porta le skill dipendenti a `review_required` (anche dopo riavvio)
- Accettazione: test su scope negati, segreti non in chiaro, audit (fatto).

## Fase 3: Catalogo connettori

- [x] Descrittore `ConnectorDescriptor` con validazione; catalogo in `connectors/catalog/*.json` (Google Workspace, GitHub, Spotify, Canva, Higgsfield)
- [x] Stato persistente ispezionabile (`config/connectors_state.json`, gitignored)
- [x] `ConnectorAuth` (`begin_oauth`, `complete`, `refresh`, `revoke`, `status`) + implementazione `SecretStoreAuth`
- [x] Trasporti (`core/mcp_transport.py`): HTTP streamable con handshake `initialize`, Bearer, risposta JSON o SSE, solo https (http su loopback); stdio riusando `McpStdioClient`
- [x] Namespace stabile `gmail.search`, mappato al nome nudo del server
- [ ] Flusso OAuth interattivo reale (browser + redirect + refresh) e verifica contro server veri: NON fatto. Verificato solo che l'endpoint GitHub `https://api.githubcopilot.com/mcp/` esiste e risponde 401 senza token, e che `HttpMcpInvoker` lo mappa a `McpTransportError` (2026-10-17). Serve un token dell'utente (`registry_cli connect github`) per verificare `search_repositories`/`create_issue`; nomi dei tool/scope del catalogo non verificati. Per Google, Canva, Spotify manca l'endpoint
- Accettazione: ciclo enable → authenticate → scope → revoke testato con connettore del catalogo (fatto).

## Fase 4: Skill dichiarative

- [x] `skills/<nome>/SKILL.md`, frontmatter `name`, `description`, `triggers`, `tool_refs`, `risk_class`, `status`
- [x] Progressive disclosure su tre livelli (metadati, corpo, riferimenti confinati nella cartella)
- [x] `tool_refs` risolti solo all'attivazione, connettore mancante segnalato
- [x] Gate: una skill `active` senza approvazione, o con permessi cambiati, diventa `review_required`; `approve` richiede un revisore; `diff` mostra i permessi aggiunti
- [x] Skill di esempio in sola lettura: `google-workspace-briefing`
- [x] Nessuna skill preesistente da migrare nel repository
- Accettazione: test su parsing, gate, riferimenti, revoca (fatto).

## Fase 5: Router e orchestrazione

- [x] `SkillRouter` a due assi (intento, poi skill) in `core/skill_router.py`
- [x] Esposizione al modello: tool `use_skill`, `connectors_status`, `connector_call` (auto-scoperti), tutti con audit
- [x] CLI di gestione `core/registry_cli.py` (`status`, `connect`, `grant`, `revoke`, `skill-diff`, `skill-approve`), token con prompt nascosto
- [x] `TaskRunner` e workflow engine: scelta di NON costruirli. `prepare` + audit coprono il caso; riconsiderare solo con workflow concreti
- Classificazione intento: euristica a parole chiave, non un modello

## Fase 6: Superfici

- [x] LM Tool `jarvis_ask` in VS Code (`vscode.lm.registerTool`) sopra il bridge WebSocket autenticato, con conferma, timeout e annullamento (richiede VS Code 1.101+, `engines`/`@types` aggiornati)
- [x] Azioni esposte come server MCP stdio: `python -m core.mcp_server` (solo `read` di default; `--allow-write` aggiunge `write`; `destructive` mai)
- [x] `VoiceTransport` astratto + `NullTransport` (`core/voice_transport.py`)
- [ ] Integrare `VoiceTransport` nella sessione Gemini Live di `main.py`: NON fatto, è solo l'interfaccia
- [ ] Pannelli grafici Connectors/Skills: NON fatti. La proiezione di stato esiste (`ConnectorRegistry.view()`, `SkillRegistry.view()`, tool `connectors_status`, `registry_cli status`)
- [ ] Prova manuale del LM Tool dentro VS Code: NON eseguita (verificati compilazione e test del protocollo)

## Comandi di verifica

- JARVIS: `Mark-LIV-main\.venv\Scripts\python.exe -m pytest Mark-LIV-main\tests` (il Python globale manca di `PyQt6.QtWebEngineCore`)
- Estensione: `cd jarvis-vscode-extension; npm test`
- Controlli: `git diff --check`, CI GitHub
- Verifica per fase: `Mark-LIV-main\.venv\Scripts\python.exe verifica.py [--fast] [--phase N]`. Controlla file, test e coerenza con questa checklist (conteggio caselle e percorsi citati). La CI esegue `--fast`.

## Log verifiche

| Data | Step | Esito |
|------|------|-------|
| 2026-10-17 | Fase 0 | JARVIS 347 passed; estensione 10 passed (locale); CI remota su `5dee2ea`: jarvis, gev, vscode-extension tutti success |
| 2026-10-17 | Fasi 1-6 | JARVIS 366 passed; estensione 11 passed + `npm ci --dry-run` ok; `py_compile main.py` ok; DPAPI roundtrip reale ok; trasporto HTTP provato contro un server locale di prova |
| 2026-10-17 | `verifica.py` | 40/40 controlli OK in locale (suite completa inclusa) |
| 2026-10-17 | Chiave Gemini nel SecretStore | JARVIS 372 passed; roundtrip DPAPI reale con `--remove-plain` su cartella temporanea ok || 2026-10-17 | Migrazione 5 tool in registry | JARVIS 372 passed; registry carica 13 azioni; esecuzione reale di large_file_reader e proxy_launcher via registry ok |
| 2026-10-17 | Setup UI nel SecretStore | JARVIS 375 passed; py_compile ui.py ok; schermata non provata graficamente |
| 2026-10-17 | Step 1 e 4 (migrate, avviso UI) | JARVIS 378 passed; ordine di migrate letto nel codice; test su _on_setup_done ok; dialog non visto a schermo (parziale) |
| 2026-10-17 | Dettatura offline: pre-flight | core.stt.whisper_available + rifiuto prima della registrazione in _set_dictation; requirements-optional.txt (faster-whisper, extra opzionale, modello da scaricare/cache). Test automatico ok; parziale: non provata con faster-whisper installato e trascrizione reale. Baseline avvio: 13 action, 21 plugin, 0 rifiutati |
| 2026-10-17 | Dettatura offline: installazione | pip install -r requirements-optional.txt nel venv (faster-whisper 1.2.1); modello base scaricato; WhisperSTT('base') carica e trascrive su silenzio senza errori. Parziale: non provata con voce reale dal microfono |
| 2026-10-17 | Dettatura offline: 'no text' | Motore provato: parlato sintetico (SAPI, 16 kHz) trascritto correttamente. L'errore reale dal microfono resta da diagnosticare: ora il messaggio riporta durata e picco, con secondo tentativo senza VAD se il picco >= 0.02. Parziale |
| 2026-10-17 | UI: focus mode (Ctrl+Shift+F) | MainWindow.set_focus_mode nasconde colonne sinistra/destra; test unitario + prova offscreen su MainWindow reale (visibilita' before/focus/after ok). Parziale: non vista a schermo; hover reveal, dock, tool UI per Jarvis, glassmorphism NON fatti (brainstorming UI, nessuna roadmap approvata) |
| 2026-10-17 | UI agentica: tool ui_layout | actions/ui_layout.py (risk_class read; focus_on/focus_off/focus_toggle) -> JarvisUI.set_focus_mode via segnale Qt thread-safe. 383 test; prova offscreen su JarvisUI reale: on -> pannelli nascosti, toggle -> visibili. Parziale: non chiamato da Gemini a voce/testo, non visto a schermo. Registry ora 14 azioni. Restano: toggle_panel singolo, dock, preset, hover reveal |
| 2026-10-17 | UI agentica (piano separato: IMPLEMENTAZIONE-UI.md) | U1 workspace/toggle_panel, U2 Viewer3D, U3 tool viewer_3d: 388 test, prove su finestra reale offscreen. Registry ora 15 azioni. Parziale: non visto a schermo, non chiamato da Gemini |
