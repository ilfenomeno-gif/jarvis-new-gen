# [NOME PROGETTO] — Direttive di Progetto per Codex / ChatGPT (ASTRALIS v3.0.5)
# Autore: Luca (Sviluppatore Senior Non Vedente con Screen Reader NVDA)
# Target AI: Codex / ChatGPT (Copilota Ausiliario e Peer Programmer - Opzionale)
# Framework: ASTRALIS v3.0.5
# Eredita da: %USERPROFILE%\.codex\AGENTS.md (Direttive Globali Macchina)
# Hub di Contesto Master: GEMINI.md
# Master Hub: <astralis-hub>

> [!NOTE]
> **Componente Opzionale**: Questo file è il router dedicato per chi utilizza un secondo assistente AI (ChatGPT / Codex) in modalità pair programming insieme ad Antigravity. Se utilizzi unicamente Antigravity, le direttive risiedono primariamente in `GEMINI.md`.

Questo repository implementa il progetto **[NOME PROGETTO]** in pair programming con **Luca**, sviluppatore completamente non vedente su Windows 11 con screen reader **NVDA** (**ZERO MOUSE**).
Tutta l'interazione con l'ambiente, il codice, i menu e gli strumenti di sviluppo avviene tramite sintesi vocale (NVDA / SAPI), feedback acustici e comandi da tastiera completi. Formattazione rigorosamente lineare ad elenchi (divieto assoluto di tabelle o grafici 2D).

---

## ⚡ 1. REGOLA DI INGAGGIO E CARICAMENTO PROGRESSIVO (ON-DEMAND)

Per garantire la massima velocità di risposta e preservare la finestra di contesto di Codex:
- **Richieste brevi, chiarimenti o domande veloci**: usa unicamente questo file `AGENTS.md` senza caricare la documentazione estesa.
- **Pianificazione, revisione approfondita o test**: consulta le Fonti di Verità (Sezione 2) caricando **esclusivamente le 1–3 schede in `knowledge/` pertinenti** al modulo da esaminare (tramite l'Indice Ragionato in `GEMINI.md`).
- **Divieto di sovraccarico**: non caricare mai in massa l'intera cartella `knowledge/`, i piani archiviati in `docs/piani/completati/` o le revisioni chiuse in `docs/report/ARCHIVIO_REVISIONI.md`.

---

## 🏛️ 2. FONTI DI VERITÀ E REGOLE DI PROGETTO (POINTER HUB DRY)

Quando il compito richiede pianificazione, diagnosi o analisi approfondite, consulta i seguenti nodi documentali:
- `GEMINI.md`: Hub centrale di contesto con i parametri di progetto e i protocolli operativi.
- `knowledge/`: Base di conoscenza modulare del progetto (architettura, flussi, convenzioni e registro bug).
- `docs/piani/attivi/`: Piani tecnici formali delle attività correnti (Sotto-Fase 1A/1B).
- `docs/report/REGISTRO_REVISIONI.md`: Registro aperto delle anomalie e revisioni emerse dai collaudi (RRU).

---

## 🛡️ 3. VINCOLI TECNICI INVIOLABILI

1. **Regola 0 (Default Consultivo Permanente & Gating Semantico)**:
   - Non effettuare MAI modifiche autonome al codice sorgente o ai file di configurazione senza il comando esplicito di Luca (*"procedi"*, *"applica"*, *"esegui"*).
   - Richieste come *"cosa ne pensi?"*, *"valuta"*, *"analizza"* richiedono risposte esclusivamente consultive.
   - Gating Fase 1: *"passa alla fase 1"* autorizza SOLO la stesura del piano tecnico (1A) con Stop Obbligatorio prima del codice (1B).
   - Validazione preventiva: proposta verificata sui **7 Assi di Qualità** e **3 Livelli di Simulazione**.
2. **Accessibilità Vocale & Zero Mouse**:
   - Nessuna interfaccia o funzionalità deve richiedere l'uso del mouse.
   - I volumi sonori ed effetti audio devono essere congelati a un massimo tra `0.7f` e `0.8f` per non coprire mai la sintesi vocale dello screen reader.
3. **Resilienza Build & Ambienti Cloud**:
   - Nei comandi di build Gradle su Windows/OneDrive, usare sempre i flag obbligatori `--no-daemon --no-watch-fs`.
4. **Protocollo 12 — Inner Codex Pattern (6 Cancelli Inviolabili)**:
   - Cancello 1: Rifiuto patching euristico;
   - Cancello 2: Hardware grounding da periferica;
   - Cancello 3: Hitbox & clearance continua;
   - Cancello 4: Named contracts atomici (D0..DN / S1..SN);
   - Cancello 5: Determinismo headless con clock controllato nei test temporali pertinenti;
   - Cancello 6: Token budget & anti-bloat normativo ($\le 250$ righe nei router).
5. **Organizzazione Documentale e Partizionamento Modulare**:
   - Tutta la documentazione tecnica vive all'interno del repository in `docs/` e `knowledge/`.
   - Il `README.md` di root è riservato alla presentazione funzionale del progetto agli utenti finali.
   - Nuovi sottosistemi e suite di test vanno partizionati per dominio e categoria (con fixture condivise separate), vietando l'accodamento inerziale a file monolitici ($\ge 800\text{–}1.000$ righe); i monoliti storici stabili e i file upstream nei fork restano protetti dalla Clausola Zero-Churn su fix locali.

## Routing operativo — Astralis 3.X
HUB è il Master Hub dinamico dichiarato in testata; risolvi la variabile nell’ambiente e verifica il percorso.
Le destinazioni seguenti sono relative a HUB; consulta soltanto quelle pertinenti al mandato.
- Conoscenze: `knowledge/README.md`.
- Prompt: `knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md`; `prompts/INDICE_SELEZIONE.json`.
- Skill: `knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_skill_astralis.md`; `skills/INDICE_SELEZIONE.json`.
- Report: `knowledge/03_architettura_e_metodologie/gestione_report_e_continuita_sessioni.md`.
- Ciclo di sviluppo: `knowledge/03_architettura_e_metodologie/ciclo_sviluppo_e_selezione_strumenti_astralis.md`.
Leggi il candidato prima dell’uso; non caricare entrambi gli indici per default né ripetere fonti già lette e ancora attuali.
Consigliare o selezionare non concede permessi; usa il mandato già dato. Mantieni report utili alla continuità, senza crearli per chiarimenti banali.
Fallback: indice assente/obsoleto → catalogo README e scheda sotto lo stesso HUB, se leggibili; non rigenerare o installare automaticamente.
HUB/procedura non accessibile → indica percorso ed errore reali, limita il risultato; non simulare letture né cercare nel Lab/v4.
