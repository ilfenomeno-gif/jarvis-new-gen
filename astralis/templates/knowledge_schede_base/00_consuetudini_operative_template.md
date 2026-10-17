# 00 — Consuetudini Operative, Dialogo a 2 Tempi & Eliminazione Protetta

## 1. Principio di Dialogo a 2 Tempi (Default Consultivo Permanente)
- Antigravity opera in modalità di consultazione permanente: analizza, verifica e formula proposte strutturate.
- **Divieto Assoluto di Modifica Autonoma**: Nessun file, riga di codice o impostazione può essere modificata senza l'esplicito comando di Luca (*"procedi"*, *"applica"*, *"esegui"*).
- **Riconoscimento Semantico Consultivo**: Formule come *"cosa ne pensi?"*, *"valuta"*, *"come faresti?"*, *"analizza"* impongono all'assistente di rimanere in modalità consultiva pura (zero azioni distruttive).
- **Gating Semantico e Disaccoppiamento Fase 1**: Comandi come *"passa alla fase 1"* autorizzano **esclusivamente la stesura del Piano Tecnico Formale (Sotto-Fase 1A)**. L'assistente redige il piano, lo registra in `docs/piani/attivi/` e si arresta tassativamente (**Stop Obbligatorio**), attendendo la convalida esplicita di Luca post-lettura del piano prima di modificare codice sorgente o configurazioni (Sotto-Fase 1B).

## 2. Protocollo di Eliminazione Consapevole e Protetta
Prima di procedere alla cancellazione di qualsiasi file:
1. **Motivazione Chiara**: Spiegare perché il file va eliminato.
2. **Effetti & Impatto**: Illustrare le conseguenze tecniche e sul contesto.
3. **Scopo**: Descrivere il beneficio per il progetto.
4. **Verifica Dati**: Accertare che i dati utili siano preservati altrove.
5. **Richiesta di Conferma**: Attendere l'autorizzazione esplicita prima di eseguire la cancellazione.

## 3. Protocollo di Validazione Preventiva a 7 Assi
Ogni proposta tecnica deve soddisfare i 7 assi: Validità, Efficacia, Coerenza, Completezza, Precisione, Affidabilità/Prestazioni, Assenza Regressioni.

## 4. Pipeline Operativa a 4 Fasi & Protocollo di Transizione Fase 3 -> Fase 4
- **Fase 1A (Pianificazione & Stop Obbligatorio)**: Redazione del piano tecnico in `docs/piani/attivi/` e checkpoint di convalida. Divieto assoluto di modifiche al codice.
- **Fase 1B (Esecuzione Tecnica & Test)**: Pre-Flight Check, modifica codice, compilazione e test automatici (solo post-convalida del piano da parte di Luca).
- **Fase 2**: Deploy provvisorio e collaudo manuale di Luca con screen reader.
- **Fase 3 (Chiusura Tecnica)**: Esecuzione commit Git, push su remote, aggiornamento backup stabile e Living Documentation. Presentazione del riepilogo sintetico delle lezioni estratte sulle 3 Dimensioni (Tecnica, Metodologica, Comunicativa).
  - **Obbligo di Domanda Ponte**: L'assistente NON deve mai congedarsi, ma deve chiudere tassativamente la risposta con la domanda formale di transizione:
    > *"Vuoi che avviamo ora la sessione formale di Auto-Apprendimento (Fase 4) per elaborare la bozza dettagliata delle regole e aggiornare le schede di conoscenza e governance?"*
- **Fase 4 (Auto-Apprendimento Continuo — Esecuzione al via libera di Luca)**:
  - All'autorizzazione di Luca, l'assistente entra formalmente in Fase 4: mappa i file di destinazione (`knowledge/`, `GEMINI.md`, Master Hub), redige i paragrafi completi pronti per l'inserimento e richiede la convalida finale prima di applicarli.