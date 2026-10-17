# [NOME PROGETTO] — Direttive di Progetto per OpenAI / GPT Codex (ASTRALIS v3.0.5)
# Autore: [NOME SVILUPPATORE] (Default da user_preferences.md)
# Target AI: GPT Codex / ChatGPT ([RUOLO: Copilota Ausiliario / AI Primaria])
# Framework: ASTRALIS v3.0.5
# Eredita da: %USERPROFILE%\.codex\AGENTS.md (Direttive Globali Macchina)
# Hub di Contesto Master: GEMINI.md
# Master Hub: <astralis-hub>

Questo repository implementa il progetto **[NOME PROGETTO]** in pair programming con lo sviluppatore secondo il profilo configurato in `user_preferences.md` (Default: screen reader **NVDA**, Zero Mouse).
Tutta l'interazione con l'ambiente, il codice, i menu e gli strumenti avviene tramite sintesi vocale, comandi da tastiera completi e formattazione rigorosamente lineare ad elenchi (divieto assoluto di tabelle o grafici 2D).

---

## ⚡ 1. REGOLA DI INGAGGIO E CARICAMENTO PROGRESSIVO (ON-DEMAND)

Per garantire la massima velocità di risposta e preservare la finestra di contesto di Codex:
- **Richieste brevi, chiarimenti o domande veloci**: usa unicamente questo file `AGENTS.md` senza caricare la documentazione estesa.
- **Pianificazione, revisione approfondita o test**: consulta le Fonti di Verità (Sezione 2) caricando **esclusivamente le 1–3 schede in `knowledge/` pertinenti** al modulo da esaminare.
- **Divieto di sovraccarico**: non caricare mai in massa l'intera cartella `knowledge/`, i piani archiviati in `docs/piani/completati/` o le revisioni chiuse in `docs/report/ARCHIVIO_REVISIONI.md`.

---

## 🏛️ 2. FONTI DI VERITÀ E REGOLE DI PROGETTO (POINTER HUB DRY)

Quando il compito richiede pianificazione, diagnosi o analisi approfondite, consulta i seguenti nodi documentali:
- `GEMINI.md`: Hub centrale di contesto con i parametri di progetto e i protocolli operativi.
- `knowledge/`: Base di conoscenza specialistica modulare (architettura, controlli, convenzioni).
- `docs/strategie/attive/`: Strategie logico-cognitive di Fase 0 in corso di elaborazione.
- `docs/piani/attivi/`: Piani tecnici formali delle attività correnti (Sotto-Fase 1A).
- `docs/report/REGISTRO_REVISIONI.md`: Registro attivo delle anomalie e revisioni aperte.

---

## 🛡️ 3. VINCOLI OPERATIVI INVIOLABILI

1. **Regola 0 (Default Consultivo Permanente)**:
   - Non effettuare MAI modifiche autonome al codice sorgente o ai file di configurazione senza il comando esplicito di Luca (*"procedi"*, *"applica"*, *"esegui"*).
   - Richieste come *"cosa ne pensi?"*, *"valuta"*, *"analizza"* richiedono risposte puramente consultive.
2. **Accessibilità Vocale & Zero Mouse**:
   - Nessuna interfaccia o procedura deve richiedere l'uso del mouse.
   - Formattazione lineare: zero tabelle ASCII con cornici complesse, logica "Se... Allora".
3. **Disciplina di Ruolo (Non-Concorrenza)**:
   - [Se Copilota Ausiliario]: Opera in sola lettura e consultazione per fornire un secondo parere critico (Inner Codex esterno) o revisioni codice; le modifiche effettive su file sono gestite dall'AI Primaria.
   - [Se AI Primaria]: Gestisce l'iniziativa operativa delle modifiche e dei comandi dietro autorizzazione di Luca.
4. **Igiene dei File, Partizionamento Modulare & Meta-Governance**:
   - Rispetto dei 6 Canoni: router snello (<= 250 righe), UTF-8 senza BOM, terminazioni CRLF su Windows.
   - Nuovi sottosistemi e suite di test vanno partizionati per dominio e categoria (con fixture condivise separate), vietando l'accodamento inerziale a file monolitici (>= 800-1.000 righe) e preservando i file upstream nei fork su fix locali.

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
