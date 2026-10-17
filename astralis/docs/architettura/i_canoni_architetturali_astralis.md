# I 6 Canoni Architetturali di Meta-Governance (ASTRALIS v3.0.21)
# Autore: Luca (Senior Developer & Author) & Antigravity (AI Pair Programmer)

Tutte le regole, i protocolli e i manifest di ASTRALIS devono conformarsi rigorosamente ai **6 Canoni Architetturali**:

1. **Canone 1 — Hub & Spoke & Budgeting Token**:
   - I file di ingresso (`GEMINI.md`, `AGENTS.md`) rimangono router snelli ad alto segnale (<= 250 righe / ~2.000 token); le trattazioni estese risiedono nei moduli dedicati in `knowledge/`.
2. **Canone 2 — Disaccoppiamento Manifest vs Modulo**:
   - Nei router locali alloggiano solo parametri concreti di configurazione del progetto (3-6 righe); la teoria risiede nei moduli.
3. **Canone 3 — Rete Documentale Pointer DRY**:
   - Zero duplicazioni di testo; collegamenti Markdown incrociati navigabili obbligatori tra Strategie, Piani Tecnici, Report di Sessione e Registri Revisioni.
4. **Canone 4 — Gating Deterministico a Tre Stati**:
   - Notazione standard `[ ]` (Da fare), `[/]` (In corso), `[x]` (Completato e collaudato). Divieto assoluto di spunta preventiva prima del collaudo reale.
5. **Canone 5 — Accessibilità Cognitiva NVDA**:
   - Flusso rigorosamente lineare dall'alto in basso, logica condizionale "Se... Allora", divieto di tabelle ASCII 2D o grafici complessi. Novità sempre in cima.
6. **Canone 6 — Igiene dei File & Portabilità**:
   - Codifica UTF-8 senza BOM, rispetto delle terminazioni di riga native (LF per documenti, CRLF per PowerShell su Windows), percorsi dinamici universali.
