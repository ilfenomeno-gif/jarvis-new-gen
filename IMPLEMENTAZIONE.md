# Piano di implementazione: Tool, Skill, Connettori MCP

Checklist di riferimento. **Dopo ogni step**: rileggere questo file, spuntare le caselle, annotare il test eseguito nel log in fondo.

Principio guida: *i connettori (MCP) sono infrastruttura, le skill sono conoscenza procedurale.* Riusare i registry esistenti, niente riscritture, ogni step verificato con test reali.

## Stato attuale verificato

- `ActionRegistry` (`Mark-LIV-main/core/action_loader.py`) collegato a `main.py`; solo `vscode_agent.py` e `vscode_control.py` espongono `TOOL`.
- `PluginRegistry` (`core/plugin_loader.py`) con client MCP GEV; `ws_server.py` loopback autenticato.
- Estensione VS Code: token in `SecretStorage`.
- `main.py` ha ancora ~35 rami `elif name == ...` e `TOOL_DECLARATIONS` statici.
- Non esistono: skill dichiarative, catalogo connettori, SecretStore/ScopeManager Python, audit, LM Tools, `VoiceTransport`, MCP esposto dai plugin.

## Fase 0: Fondamenta (completata, da committare)

- [x] Token estensione in `vscode.SecretStorage` + comando `JARVIS: Set Connection Token` + migrazione `jarvis.wsToken`
- [x] `discover_actions` collegato a `main.py` (dichiarazioni + dispatch + nomi riservati)
- [x] Test `tests/test_action_loader.py`
- [x] Job CI `vscode-extension`
- [x] Commit + push + CI remota verde (commit `5dee2ea`, job jarvis/gev/vscode-extension success)

## Fase 1: Normalizzare i tool

- [ ] Inventario dei rami statici di `_execute_tool` con classificazione (azione / plugin / core)
- [ ] Migrare gradualmente i rami in `actions/*.py` con `TOOL` (un gruppo per volta, test a ogni gruppo)
- [ ] Campo `risk_class` (`read`, `write`, `destructive`) nel contratto `TOOL`
- [ ] Conferma utente per `destructive`
- [ ] Rimuovere `TOOL_DECLARATIONS` duplicate quando un tool è migrato
- Accettazione: suite JARVIS verde, nessun cambio di comportamento osservabile.

## Fase 2: Sicurezza (prima di qualsiasi UI)

- [ ] `SecretStore` Python (keyring/DPAPI) per token OAuth e API key; migrare `config/api_keys.json`
- [ ] `ScopeManager`: scope dichiarati nel descrittore, verificati prima di ogni chiamata
- [ ] Restringere whitelist `node`/`node.exe` del plugin GEV e verificare la fonte del runtime
- [ ] Audit log per ogni chiamata tool (skill di provenienza, scope, esito)
- [ ] Revoca: invalida i token e disabilita le skill dipendenti
- Accettazione: nessun segreto in chiaro nel repository o nei file di config; test su scope negati.

## Fase 3: Catalogo connettori (`MCPRegistry`)

- [ ] Schema descrittore: `id`, `name`, `type`, `transport`, `auth`, `status`, `scopes`, `tool_refs`
- [ ] Stato persistente ispezionabile (JSON/SQLite)
- [ ] Interfaccia `ConnectorAuth`: `begin_oauth()`, `refresh()`, `revoke()`, `status()`
- [ ] Avvio e discovery dei tool MCP con namespace stabile (`gmail.search`)
- [ ] Primi connettori esistenti: Google Workspace, GitHub, Spotify; poi Canva, Higgsfield (remoti OAuth)
- Accettazione: connettore finto di test passa enable → authenticate → scope → revoke.

## Fase 4: Skill dichiarative (`SkillRegistry`)

- [ ] Struttura `skills/<nome>/SKILL.md` + `reference.md` opzionale + `examples/`
- [ ] Formato `SKILL.md` con frontmatter `name`, `description` (+ `tool_refs`, `risk_class`)
- [ ] Progressive disclosure: precarico solo metadati; corpo al trigger; riferimenti su richiesta
- [ ] Risoluzione `tool_refs` solo all'attivazione; segnalare connettore non connesso
- [ ] Ciclo di vita (`draft`, `active`, `review_required`, `archived`) e gate su espansione di scope
- [ ] Prima skill di esempio in sola lettura (briefing)
- [ ] Migrare le skill esistenti al formato
- Accettazione: test su parsing, trigger, gate scope.

## Fase 5: Router e orchestrazione

- [ ] Router a due assi: intento, poi skill
- [ ] `TaskRunner` con checkpoint e audit
- [ ] Workflow engine solo se emergono workflow concreti (non anticipare)

## Fase 6: Superfici

- [ ] LM Tools in VS Code (`vscode.lm.registerTool`) sopra il bridge WebSocket
- [ ] Plugin esposti come server MCP
- [ ] `VoiceTransport` astratto
- [ ] Pannelli Connectors / Skills come proiezione dello stato del registry

## Comandi di verifica

- JARVIS: `Mark-LIV-main\.venv\Scripts\python.exe -m pytest Mark-LIV-main\tests` (il Python globale manca di `PyQt6.QtWebEngineCore`)
- Estensione: `cd jarvis-vscode-extension; npm test`
- Controlli: `git diff --check`, CI GitHub

## Log verifiche

| Data | Step | Esito |
|------|------|-------|
| 2026-10-17 | Fase 0 | JARVIS 347 passed; estensione 10 passed (locale); CI remota su `5dee2ea`: jarvis, gev, vscode-extension tutti success |
