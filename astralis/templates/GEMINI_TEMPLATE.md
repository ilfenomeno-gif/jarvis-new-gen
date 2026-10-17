# [NOME PROGETTO] — Hub di Contesto & Governance Locale (GEMINI.md — ASTRALIS v3.0.5)
# Autore: Luca (Sviluppatore Senior Non Vedente con Screen Reader NVDA)
# Target AI: Antigravity (Primario) & Codex/ChatGPT (Copilota Ausiliario)
# Eredita da:
#   1. %USERPROFILE%\.gemini\config\GEMINI.md (Genoma Globale — Livello 0)
#   2. <cartella-progetti>\GEMINI.md (Ponte Amministrativo — Livello 1)
# Master Hub: <astralis-hub>

Questo repository implementa il progetto **[NOME PROGETTO]** ed è sviluppato in pair programming con **Luca**, sviluppatore completamente non vedente su Windows 11 con screen reader **NVDA** (**ZERO MOUSE**).
Tutta l'interazione con l'ambiente, il codice, i log e i menu avviene tramite sintesi vocale (NVDA / SAPI), feedback acustici e comandi da tastiera completi.

Questo file costituisce l'**Hub Centrale di Contesto Locale** del progetto, vincolante sia per l'assistente AI primario (**Antigravity**) che per i copiloti ausiliari di peer programming (come **Codex / ChatGPT**). Tutti i dettagli specialistici risiedono nella cartella [`knowledge/`](../knowledge).

---

## 🌟 Le Regole Auree Inviolabili del Progetto

0. **Consuetudini Operative, Dialogo a 2 Tempi & Gating Semantico (Regola 0)**:
   - Default consultivo: analizza, verifica i log, consulta le schede di riferimento e **attendi sempre la conferma esplicita di Luca prima di modificare codice o file** (*"procedi"*, *"applica"*, *"esegui"*).
   - *Gating Semantico Fase 1*: Comandi come *"passa alla fase 1"* autorizzano **esclusivamente la stesura del Piano Tecnico Formale (Sotto-Fase 1A)** in `docs/piani/attivi/` e impongono lo **Stop Obbligatorio** prima di toccare codice o configurazioni (Sotto-Fase 1B).
   - *Validazione Preventiva*: Ogni proposta deve essere verificata sui **7 Assi di Qualità** (Validità, Efficacia, Coerenza, Completezza, Precisione, Prestazioni, Assenza di Regressioni) e stress-testata sulla **Matrice di Simulazione a 3 Livelli** (Happy Path, Concorrenza/Alternative, Corner Cases).
   - *Protocollo di Eliminazione Protetta*: Motivazione chiara, analisi d'impatto, verifica assenza perdita dati e attesa di autorizzazione esplicita prima di qualsiasi cancellazione.

1. **Accessibilità Vocale Assoluta & Volumi di Sicurezza**:
   - Nessuna funzione deve dipendere da mouse o elementi visivi (interazione 100% da tastiera).
   - Volumi audio posizionale o effetti sonori congelati a un massimo compreso tra `0.7f` e `0.8f` per non coprire mai la voce dello screen reader.

2. **Standard I18N & Convenzioni Formato**:
   - Nello sviluppo ci concentriamo su **Italiano** (documentazione, log, commenti) e **Inglese** (naming convenzionale e standard PR upstream);
   - Nei file `.json` di lingua, chiavi disposte in **rigoroso ordine alfabetico crescente**.

3. **Rete Documentale Flessibile (Pointer Hub DRY) in `docs/`**:
   - `docs/idee/`: Idee/RFC quando utili al mandato; cinque tipi documentali secondo la tassonomia v3;
   - `docs/strategie/attive/`: Strategie logico-cognitive in elaborazione o discussione (Fase 0);
   - `docs/strategie/archiviate/`: Strategie convalidate e convertite in piani tecnici;
   - `docs/piani/attivi/`: Piani tecnici in stesura (1A) o in attesa di collaudo (1B);
   - `docs/piani/completati/`: Piani tecnici collaudati con successo e archiviati;
   - `docs/report/`: Registro Revisioni attivo (`REGISTRO_REVISIONI.md`) e archivio storico (`ARCHIVIO_REVISIONI.md`);
   - `docs/report/archivio/`: Report di sessione e telemetria storici;
   - `docs/manuali/`: Guide all'uso e protocolli di collaudo.
   - **Disaccoppiamento `README.md`**: Il `README.md` di root è riservato alla documentazione funzionale del software per gli utenti finali e la community. L'Indice Ragionato delle regole risiede unicamente in questo `GEMINI.md`.

4. **Pipeline Operativa a 4 Fasi, Resilienza Build & Protocollo Telemetria Live**:
   - *Fase 1A (Piano Tecnico & Stop)*: Stesura piano in `docs/piani/attivi/` con validazione preventiva sui 7 Assi e 3 Livelli;
   - *Fase 1B (Esecuzione Tecnica & Test)*: Modifiche al codice, compilazione con flag anti-lock su Windows/Cloud (`--no-daemon --no-watch-fs` per build Gradle) e test automatici eseguiti solo POST-APPROVAZIONE;
   - *Fase 2 (Distribuzione autorizzata, Telemetria & Test Manuale)*: Distribuzione soltanto nelle istanze previste dal mandato, con verifica dell’artefatto prima del test di Luca. Durante il collaudo opera la **Telemetria Live** (Protocollo 4) con aggiornamento automatico proattivo del **Registro Revisioni**;
   - *Fase PRAPI (Protocollo 5)*: Ciclo rapido di revisione e affinamento post-collaudo in 4 passi;
   - *Fase 3 (Chiusura Tecnica)*: Commit Git (`feat:`, `fix:`, `docs:`), aggiornamento `CHANGELOG.md`, archiviazione del piano in `docs/piani/completati/`, aggiornamento backup e chiusura tassativa con la **Domanda Ponte Obbligatoria**:
     > *"Vuoi che avviamo ora la sessione formale di Auto-Apprendimento (Fase 4) per elaborare la bozza dettagliata delle regole e aggiornare le schede di conoscenza e governance?"*
   - *Fase 4 (Auto-Apprendimento Continuo a Doppio Binario)*:
     - **Binario A (Locale)**: Aggiornamento delle schede in `knowledge/` del progetto;
     - **Binario B (Globale)**: Aggiornamento dei moduli in `knowledge/` del Master Hub.

5. **Disciplina di Meta-Governance & Ingegneria delle Regole (ASTRALIS Canon Crafting)**:
   - Divieto assoluto di inventare regole ad-hoc o appesantire questo file (limite di sicurezza: $\le 250$ righe / ~2.000 token).
   - Ogni integrazione segue i **6 Canoni**: Hub & Spoke, Manifest vs Modulo, Rete Documentale Pointer DRY con percorsi risolti e collegamenti relativi verificati, Gating Deterministico a 3 Stati (`[ ]`, `[/]`, `[x]`), Linearità NVDA e Igiene File (UTF-8 no BOM, CRLF).

6. **Protocollo 12 — Dialettica Ingegneristica & Auto-Revisione Avversariale (L'Inner Codex Pattern)**:
   - Autonomia critica basata sui **6 Cancelli Inviolabili**:
     * *Cancello 1 (Rifiuto Patching Euristico)*: Divieto di forzare ritardi o pesi artificiali;
     * *Cancello 2 (Hardware Grounding)*: Disaccoppiamento tra input diretto da periferica e guardie reattive;
     * *Cancello 3 (Hitbox & Clearance Continua)*: Controllo geometrico rigoroso delle collisioni e volumi di sicurezza;
     * *Cancello 4 (Named Contracts D0..DN / S1..SN)*: Scomposizione atomica delle modifiche complesse in contratti formali numerati;
     * *Cancello 5 (Determinismo Headless)*: Test seams e clock virtuale dove applicabili, senza promesse sulla durata reale dei test;
     * *Cancello 6 (Budget Token & Anti-Bloat Normativo)*: Rispetto rigoroso dei canoni di token budget ($\le 250$ righe nei file router, zero duplicazioni testuali).

7. **Principio di Integrità Evolutiva, Partizionamento Modulare & Bonifica dei Residui**:
   - Quando un'architettura, flusso, funzione o componente viene sostituito o evoluto da una nuova soluzione, è fatto divieto categorico di lasciare coesistere elementi del vecchio meccanismo (codice morto, campi orfani, logiche concorrenti, frammenti obsoleti o deleteri).
   - Ogni transizione include sistematicamente, come parte integrante dell'intervento, la bonifica completa e l'eliminazione verificata di tutti i residui del sistema superato prima di dichiarare conclusa l'opera, azzerando alla radice ambiguità cognitive e debiti tecnici silenti.
   - **Partizionamento per Dominio e Guardia Anti-Monolite**: nuovi sottosistemi, componenti e suite di test vanno partizionati per dominio e categoria (con fixture condivise separate), vietando l'accodamento inerziale a file monolitici ($\ge 800\text{–}1.000$ righe); i monoliti storici stabili e i file upstream nei fork restano protetti dalla Clausola Zero-Churn su fix locali.

8. **Rilevamento Proattivo Aggiornamenti (Pattern Deferred Query & Update Prompt)**:
   - All'avvio della prima interazione di una chat, l'assistente esegue silenziosamente lo script leggero `scripts/verifica_aggiornamenti_remoti.ps1`.
   - *Se non ci sono nuove versioni*: silenzio assoluto (zero rumore vocale per NVDA) e risposta immediata all'utente.
   - *Se è disponibile una nuova release di ASTRALIS*: memorizza temporaneamente la richiesta appena formulata dall'utente, visualizza una sintesi chiara ("Obiettivo" e "Descrizione") e propone la scelta trasparente: 1) procedere prima con l'aggiornamento di ASTRALIS; 2) procedere subito con la richiesta corrente rimandando l'aggiornamento.

---

## 🧭 Indice Ragionato della Base di Conoscenza Locale (`knowledge/`)

- [`00_architettura_e_struttura.md`](../knowledge/00_architettura_e_struttura.md): Panoramica architetturale, moduli e flussi di dati del progetto.
- [`01_accessibilita_e_controlli.md`](../knowledge/01_accessibilita_e_controlli.md): Mappatura tasti, gestione focus ed eventi di sintesi vocale.
- [`02_standard_sviluppo_e_convenzioni.md`](../knowledge/02_standard_sviluppo_e_convenzioni.md): Convenzioni di codice, gestione branch Git e internazionalizzazione.
- [`03_gestione_errori_e_diagnostica.md`](../knowledge/03_gestione_errori_e_diagnostica.md): Gestione eccezioni, log diagnostici e protocolli di debug.

---

## 🛡️ SEZIONE PERSONALIZZATA PROGETTO (REGOLE SPECIALISTICHE)

*Spazio riservato alle regole tecniche e consuetudini specifiche di questo repository.*

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
