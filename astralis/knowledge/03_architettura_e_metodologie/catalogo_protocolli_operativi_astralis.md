# Catalogo dei Protocolli Operativi Ufficiali ASTRALIS (v3.0.21)
# Autore: Luca (Sviluppatore Senior Non Vedente con Screen Reader NVDA) & Antigravity
# Target AI: Antigravity (Senior AI Pair Programmer & Software Engineer)
# Ambito: Globale / Master Hub ASTRALIS
# Origine: ASTRALIS (Adaptive Standards for Testing, Rules, Accessibility & Level Integration Systems)

Questo documento costituisce la specifica formale e vincolante dei **12 Protocolli Operativi Ufficiali di ASTRALIS**.
Ciascun protocollo definisce un flusso di lavoro atomico, i suoi requisiti di ingresso/uscita, le regole di accessibilità cognitiva e i presidi di non-regressione.

---

## 🧬 IL PRINCIPIO DI GOVERNANCE POLIMORFICA & SPECIALIZZAZIONE GERARCHICA

1. **Framework Astratto Globale (Master Hub & Livello 0)**:
   - Definisce le **Linee Guida Universali** e la metodologia trasversale (il *"Cosa"* di sistema: standard di validazione, pipeline a 4 fasi, disaccoppiamento dei log, gestione revisioni, 12 protocolli, Trittico di rilascio).
2. **Specializzazione Concreta Locale (Singolo Progetto & Livello 2)**:
   - Ogni progetto specializza i protocolli e le regole nel proprio file `GEMINI.md` e nelle schede `knowledge/` locali (il *"Come"* pratico: Mixin Java e Voxel per Minecraft, SKSE e Papyrus per Skyrim, wxPython e thread asincroni per Addon NVDA, pytest per Python, formattazione pura per Scrittura Creativa).
3. **Esecuzione Quotidiana ad Alto Segnale**:
   - Durante il lavoro quotidiano, Antigravity legge e applica le regole locali specializzate del progetto, minimizzando il consumo di token e garantendo precisione assoluta senza dover ricaricare la teoria generale.
4. **Ciclo di Auto-Apprendimento Continuo (Fase 4)**:
   - *Binario A (Locale)*: consolida le lezioni specifiche nelle schede `knowledge/` del progetto;
   - *Binario B (Globale)*: astrae i pattern trasversali arricchendo i moduli di `knowledge/` nel Master Hub.

---

## 🧠 IL PRINCIPIO DI RICONOSCIMENTO SEMANTICO FLESSIBILE & FEEDBACK DI AGGANCIO

1. **Flessibilità Semantica**:
   - Luca non è vincolato all'uso della parola "Protocollo". Qualsiasi formulazione naturale equivalente (es. *"studiamo la strategia"*, *"verifica sui 7 assi"*, *"passa in modalità telemetria"*, *"revisioniamo questo comportamento"*, *"chiudiamo il task"*, *"passiamo all'apprendimento"*, *"aggiorna il sistema di regole"*, *"configuriamo questa macchina"*, *"bonifichiamo il codice morto"*, *"fai l'auto-revisione avversariale"*) innesca all'istante il protocollo corrispondente.
2. **Dichiarazione Esplicita di Avvio**:
   - Quando Antigravity riconosce un'intenzione operativa, apre la risposta dichiarando esplicitamente il protocollo agganciato per dare conferma immediata a sintesi vocale (es. `🛡️ [ASTRALIS] Avvio del Protocollo Pulizia...`).

---

## 🏛️ SPECIFICA DEI 12 PROTOCOLLI OPERATIVI UFFICIALI

---

### 1. PROTOCOLLO PROGETTAZIONE *(Strategy, Contracts & Architecture — Fase 0 & Sotto-Fase 1A)*
- **Comandi Trigger**: *"Avvia Protocollo Progettazione"*, *"fase di progettazione"*, *"studiamo la strategia per [tema]"*, *"passa alla fase 1"*, *"pianifichiamo le modifiche"*, *"elabora la strategia cognitiva"*.
- **Scopo**: Definire il modello mentale, l'architettura logica, le invarianti e i contratti prima di toccare il codice sorgente o le configurazioni.
- **La Struttura a Rete a 5 Nodi Comunicanti (DRY & Pointer Hub)**:
  La rete flessibile comprende cinque tipi, secondo la tassonomia comune. Creare soltanto i nodi utili e compresi nel mandato; non è una pipeline obbligatoria. I puntatori mantengono la tracciabilità:
  * **Idea/RFC (`docs/idee/`)**: bisogno, benefici, ipotesi e decisione richiesta quando l’idea è ancora embrionale;
  * **Strategia Logico-Cognitiva (`docs/strategie/`)**: Modello mentale, tesi ingegneristica, dialettica avversariale e invarianti (Fase 0);
  * **Piano Tecnico (`docs/piani/`)**: Contratti formali D0..DN, classi target, checklist a 3 stati e test plan (Fase 1);
  * **Report di Sessione & Telemetria (`docs/report/`)**: Evidenza empirica, log live e collaudo pratico NVDA (Fase 2);
  * **Registro Revisioni RRU (`REGISTRO_REVISIONI.md` / `ARCHIVIO_REVISIONI.md`)**: Tracciabilità forense e memoria perenne (Fase 3).
- **Passaggi Operativi**:
  1. *Fase 0: Elaborazione Strategica Logico-Cognitiva (I 7 Archetipi Strategici UPCS)*:
     - **Regola di Soglia**: Obbligatoria per compiti complessi, architetturali, anomalie sistemiche o dispute tra AI; facoltativa per hotfix o interventi banali (che procedono direttamente dalla 1A).
     - **I 7 Archetipi di Strategia Cognitiva**:
       * **Concettuale-Implementativa** *(Ideazione & Feature Design)*: esplora lo spazio delle soluzioni e traduce idee astratte in modelli funzionali;
       * **Diagnostico-Correttiva** *(Anomalie Ostiche & Root-Cause Discovery)*: analizza bug sistemici concorrenti e smentisce ipotesi false;
       * **Refactoring Strutturale & Disaccoppiamento** *(Architectural Restructuring)*: ridefinisce i confini tra layer eliminando God Objects;
       * **Euristico-Cognitiva per Screen Reader & Audio 3D** *(UX Audio & NVDA)*: progetta l'esperienza sensoriale, gerarchia vocale, anti-chatter e volumi di sicurezza (0.7f - 0.8f);
       * **Dialettica Avversariale & Convergenza Multi-AI** *(Inner Codex Pattern)*: confronto oggettivo tra AI sui 6 Cancelli Inviolabili;
       * **Integrazione & Interoperabilità di Runtime**: isolamento di framework esterni e prevenzione ClassCastException;
       * **Bonifica, Migrazione & Deprecazione** *(Zero-Debt Clean-up)*: eliminazione sicura con strategia a 5 barriere e rollback garantito.
     - **Collocazione**: La strategia nasce in `docs/strategie/attive/` con il template formale `STRATEGIA_COGNITIVA_TEMPLATE.md` a 5 sezioni con checklist di convergenza.
  2. *Transizione e Congelamento Invarianti*: Quando Luca convalida la Strategia (*"strategia approvata"*), lo stato passa a `[CONVERTITA IN PIANO TECNICO]` e le invarianti diventano i vincoli del piano.
  3. *Sotto-Fase 1A: Redazione Piano Tecnico Formale (I 7 Archetipi di Piano Tecnico)*:
     - Scelta deterministica dell'archetipo in base alla natura dell'intervento:
       * **Implementativo** *(Feature & New Modules)*: requisiti, contratti denominati D0..DN/S1..SN, architettura a layer e I18N;
       * **Correttivo** *(Bug Fix & PRAPI Mirato)*: evidenza empirica Luca, Root Cause Analysis (RCA) senza pezze euristiche (Cancello 1), test di riproduzione isolato e patch chirurgica;
       * **Refactoring** *(Architectural Grooming)*: mappa code smell, disaccoppiamento interfacce/DIP e garanzia di **invarianza assoluta del comportamento esterno**;
       * **Bonifica & Pulizia** *(Dead Code Purge)*: rimozione codice/chiavi/asset morti con la Strategia a 5 Barriere di Sicurezza (Protocollo 11);
       * **Migrazione & Aggiornamento Stack** *(Runtime Upgrade)*: avanzamento versione runtime/motore, breaking changes e compatibilità binaria (Protocollo 8);
       * **Convalida, Hardening & Suite Test** *(QA Engineering)*: test seams headless a 0 ms (Cancello 5), eliminazione `Thread.sleep` e matrici di stress-test;
       * **Esplorativo & Fattibilità** *(Spike & PoC)*: benchmark preventivi su incertezze geometriche/prestazionali e dossier decisionale per il piano implementativo.
     - Adozione della **Testata Universale Compatta** e dell’estensione PIANO-TECNICO della tassonomia: stato documento, stato lavoro e gate separati; contratti, impatto AVF e audit dei sei cancelli nel contenuto pertinente. I vecchi formati restano compatibili in lettura, senza conversione degli archivi;
     - **Partizionamento Modulare e Guardia Anti-Monolite**: il piano tecnico alloca nuovi sottosistemi e nuove suite di test in file partizionati per dominio e categoria (con fixture condivise separate), vietando l'accodamento inerziale a file monolitici ($\ge 800\text{–}1.000$ righe) e preservando la struttura dei file upstream nei fork su fix locali;
  4. *Sommario Operativo & Registro di Avanzamento (Checklist con Gating di Convalida)*:
     - In cima al piano, subito dopo l'intestazione, inserimento della checklist sequenziale delle tappe e sotto-fasi del piano;
     - **La Matrice a 3 Stati per NVDA**:
       * `- [ ] [DA AVVIARE]`: Attività pianificata ma non iniziata;
       * `- [/] [IMPLEMENTATO — IN ATTESA DI CONVALIDA]`: Spunta parziale. Il codice è scritto e compila con successo, ma **NON è ancora convalidato**;
       * `- [x] [CONVALIDATO CON SUCCESSO]`: Spunta definitiva concessa **esclusivamente POST-CONVALIDA formale** (approvazione di Luca per la 1A, test suite 100% verde per la 1B, collaudo empirico in-game di Luca per la Fase 2);
   5. *Stop Obbligatorio (Gating Semantico)*: Divieto assoluto di modifica autonoma prima del via libera esplicito di Luca;
   6. *Cancello di Proporzionalità & Anti-Overengineering Gate (La Scala dell'Intervento Minimo Efficace)*:
      - Prima di pianificare l'aggiunta di codice custom, hook a basso livello, macchine a stati complesse o modifiche all'infrastruttura, l'assistente DEVE esplorare e verificare la scala di precedenza:
        * *Livello 0 (Comportamento Nativo & Configurazione Esistente)*: Verificare se opzioni di configurazione (file INI, JSON, YAML) o comandi standard risolvono il requisito;
        * *Livello 1 (Workaround Procedurale da Tastiera)*: Verificare se una sequenza standard accessibile da tastiera soddisfa l'esigenza dell'utente;
        * *Livello 2 (Configurazione Esterna o Strumento d'Ambiente)*: Verificare se l'ecosistema di supporto gestisce il caso;
        * *Livello 3 (Codice Sorgente & Estensioni Core)*: Ammesso unicamente se i livelli 0, 1 e 2 sono impraticabili o insufficienti.
      - *Soglia di Escalation nei Re-Audit Iterativi*: Se durante la peer review o l'affinamento di un piano tecnico emergono requisiti di ciclo di vita sempre più complessi (FSM aggiuntive, latch concorrenti, intercettazioni asincrone, subclassing WndProc), l'assistente NON deve procedere per inerzia ad accumulare strati ingegneristici. DEVE fermarsi, sospendere la stesura e proporre a Luca di riesaminare le premesse o esplorare un'alternativa più semplice.


---

### 2. PROTOCOLLO VALIDAZIONE *(7 Assi di Qualità + Matrice di Simulazione a 3 Livelli)*
- **Comandi Trigger**: *"Avvia Protocollo Validazione"*, *"valida questo piano"*, *"fai l'analisi sui 7 assi"*, *"stress-test preventivo"*, *"procediamo con la validazione"*.
- **Scopo**: Certificare la solidità, completezza e assenza di regressioni di un piano tecnico prima dell'implementazione.
- **Passaggi Operativi**:
  1. *Verifica sui 7 Assi di Qualità*: Validità, Efficacia, Coerenza, Completezza, Precisione per NVDA, Affidabilità/Prestazioni, Assenza di Regressioni;
  2. *Matrice di Simulazione a 3 Livelli*:
     - *Livello 1: Scenari Comuni* (Happy Path / Uso Quotidiano — 80-90% dei casi);
     - *Livello 2: Scenari Meno Comuni* (Alternative Paths & Casi Concorrenti);
     - *Livello 3: Casi Limite & Condizioni Estreme* (Corner Cases, Null, Zero, Boundary Values);
  3. *Principio del Rasoio Funzionale (Verifica Empirica Pre-Refactor)*: Se l'esperienza reale in collaudo con NVDA dimostra che un problema storico o un comportamento critico è già risolto e perfettamente funzionante, è fatto divieto assoluto di pianificare refactoring speculativi, nuove factory o macchine a stati. Si congelano i componenti sani e si circoscrive l'intervento al solo requisito minimo efficace.
  4. *Formattazione Lineare per NVDA*: Presentazione ad elenchi sequenziali "Se... Allora" ed emissione del verdetto chiaro.

---


### 3. PROTOCOLLO ESECUZIONE *(Build, Code & Deploy Proattivo — Sotto-Fase 1B / Fase 2)*
- **Comandi Trigger**: *"Avvia Protocollo Esecuzione"*, *"procedi con l'implementazione"*, *"applica il piano"*, *"esegui le modifiche"*.
- **Scopo**: Tradurre il piano validato in codice compilato, testato e distribuito automaticamente nelle istanze attive.
- **Passaggi Operativi**:
  1. *Sotto-Fase 1B (Esecuzione Tecnica)*: Modifiche chirurgiche e mirate, preservando commenti e codice circostante;
  2. *Compilazione & Test Automatici*: Build pulita con flag anti-daemon (`--no-daemon`) ed esecuzione test;
  3. *Deploy Proattivo (Fase 2)*: Distribuzione immediata dell'artefatto compilato (`.jar`, `.nvda-addon`, `.exe`) nelle cartelle o istanze di test prima del collaudo;
  4. *Redazione Walkthrough*: Sintesi accessibile delle modifiche e rilascio pronto per il test con NVDA.

---

### 4. PROTOCOLLO TELEMETRIA & MONITORAGGIO IN TEMPO REALE *(Live Logging & Denoising)*
- **Comandi Trigger**: *"Passa in modalità telemetria"*, *"avvia protocollo telemetria"*, *"monitoriamo i log del collaudo"*, *"assistimi durante il test"*, *"apri la sessione di telemetria"*.
- **Scopo**: Affiancare Luca come co-pilota analitico in tempo reale durante i collaudi (Fase 2), ispezionando i log dal vivo ed estraendo solo il segnale utile senza inondare la sintesi vocale.
- **Passaggi Operativi**:
  1. *Aggancio Dinamico delle Sorgenti*: Individuazione automatica dei file di log attivi (`latest.log`, `nvda.log`, output di console, dump);
  2. *Denoising & Filtro ad Alto Segnale per NVDA*: Isolamento istantaneo di warning, eccezioni, stacktrace, eventi tastiera e race conditions;
  3. *Correlazione Causa-Effetto in Tempo Reale*: Riscontro immediato dell'azione eseguita da Luca rispetto all'evento registrato dal motore;
  4. *Popolamento Proattivo del Registro Revisioni*: Appena Luca segnala un'anomalia o un dubbio, l'assistente la registra automaticamente nel Registro Revisioni locale del progetto con notifica vocale di 1 riga (`🛡️ [ASTRALIS] Registrata Rev X.Y`);
  5. *Generazione & Gestione del Report di Sessione (Pointer Hub Pattern)*:
     - All'avvio del collaudo, generazione/aggiornamento del report pertinente nella radice documentale risolta, secondo la [routine report v3](gestione_report_e_continuita_sessioni.md). I nuovi report usano la Testata Universale Compatta della tassonomia; le testate URCP a sette campi restano leggibili nei documenti legacy senza conversione retroattiva obbligatoria;
     - *Aggiornamenti Significativi in Ordine Cronologico Inverso*: decisioni, evidenze, verifiche, blocchi e consegne vengono registrati dal più recente al più antico; non trascrivere ogni messaggio o comando. Mantenere riepilogo corrente e prossimo passo in alto;
     - *Standard Atomico ad Alto Segnale (4 Campi)*: Contesto/Sintomo ($\le 2$ righe), Causa Radice Concettuale, Approccio Risolutivo & Pattern, Puntatori Espliciti a sorgenti, test, log e piani (divieto assoluto di file bloat o dump integrali).
  6. *Ingestione & Proposta di Normalizzazione Post-Analisi (URCP In-Flight)*:
     - Quando Luca o un collaboratore introduce nel progetto un report o un documento diagnostico proveniente dall'esterno (es. ChatGPT, tester, log grezzi) per richiederne l'analisi:
       * *Fase Analitica*: Antigravity esamina a fondo il documento, svolge le verifiche tecniche necessarie e risponde nel merito alle domande di Luca;
       * *Integrazione Contestuale*: l'AI incaricata distingue affermazioni esterne ed evidenze locali, preservando la fonte. Quando la documentazione interna è compresa nel mandato, registra l'esito nel report pertinente senza chiedere un secondo consenso;
       * *Normalizzazione Circoscritta*: se richiesta o necessaria al lavoro autorizzato, adottare lo standard corrente in una copia o nell'aggiornamento attivo, preservando originali e dettagli. La sola analisi non autorizza riscrittura della fonte o conversione degli archivi.

---

### 5. PROTOCOLLO REVISIONE & AFFINAMENTO POST-IMPLEMENTAZIONE (PRAPI)
- **Comandi Trigger**: *"Avvia Protocollo Revisione"*, *"fase di revisione post-collaudo"*, *"revisioniamo questa specifica"*, *"affiniamo il comportamento in collaudo"*, *"applica le revisioni del registro"*.
- **Scopo**: Gestire in modo strutturato, snello e chirurgico il ciclo di feedback emerso durante il collaudo (Fase 2) senza dover ricominciare da capo un intero ciclo di progettazione ex-novo.
- **Passaggi Operativi**:
  1. *Acquisizione Voci dal Registro Revisioni & Collegamento Report*: Presa in carico delle voci `Rev X.Y` aperte durante la telemetria o il collaudo; ciascuna voce nel `REGISTRO_REVISIONI.md` punta direttamente al Report di Sessione attivo, che funge da Single Source of Truth per l'elenco dei file e dei log coinvolti;
  2. *Diagnosi & Formulazione Soluzione*: Isolamento della discrepanza tra intenzione ed esperienza reale e formulazione del fix chirurgico nel piano in `docs/piani/attivi/`;
  3. *Strategia dei Buffer di Rifinitura (Resequencing delle Revisioni)*: Nei piani di lavoro articolati in fasi sequenziali, le revisioni secondarie, i ritocchi di dettaglio e gli affinamenti non bloccanti emersi durante la produzione dei singoli blocchi non devono frammentare l'inerzia del lavoro primario: vengono formalmente accodati e differiti a valle del completamento del corpo centrale dell'opera, costituendo un buffer di rifinitura e armonizzazione dedicato che precede la revisione complessiva o il collaudo generale di rilascio;
  4. *Stop Obbligatorio & Gating di Convalida (Regola 0)*: Presentazione del piano di affinamento a Luca e attesa approvazione;
  5. *Implementazione Chirurgica, Build & Re-Deploy (Sotto-Fase 1B / Fase 2)*: Modifica sorgenti, compilazione, deploy immediato nelle istanze e rilascio per il nuovo test mirato.

---

### 6. PROTOCOLLO CHIUSURA *(Doppia Barriera Git/Cloud, Disciplina AVF & Trittico Inviolabile — Fase 3)*
- **Comandi Trigger**: *"Avvia Protocollo Chiusura"*, *"chiusura tecnica"*, *"metti in sicurezza e fai il commit"*, *"chiudi il task"*, *"collaudo superato, chiudiamo"*.
- **Scopo**: Consolidare e proteggere il lavoro terminato nel repository Git e nel cloud a test positivo confermato, calcolando deterministamente il numero di versione secondo la disciplina AVF (`V.A.R[.M]`).
- **Passaggi Operativi**:
  1. *Bivio Changelog (Progetti Autonomi vs Fork Upstream)*:
     - **Per Progetti Autonomi**: Calcolo deterministico della nuova versione AVF (`V.A.R[.M]`) e aggiornamento del `CHANGELOG.md` pubblico;
     - **Per Fork di Terze Parti (Dual-Track)**: Aggiornamento della sezione `## [Unreleased]` in inglese nel `CHANGELOG.md` pubblico (zero version forcing per PR upstream) e contestuale registrazione della versione sovrana AVF nel diario in italiano `knowledge/NN_diario_modifiche_e_contributi_fork.md`;
  2. *Allineamento Trittico di Root & Cancello Bloccante AVF Pre-Export (Master Hub)*:
     - Aggiornamento contestuale ed atomico di `CHANGELOG.md`, `README.md` e `ISTRUZIONI_DI_AVVIO.md`;
     - **Cancello Bloccante AVF Pre-Export**: Prima di generare o riesportare lo Starter Kit ZIP versionato (`ASTRALIS_Universal_Starter_Kit_vX.Y.Z.zip`), l'assistente DEVE fermarsi ed eseguire la rivalutazione formale dell'incremento di versione AVF (`V.A.R[.M]`), proponendo esplicitamente il numero di versione a Luca ed ottenendone la conferma prima del lancio dello script di export. È fatto divieto assoluto di riesportare archivi ZIP con versioni implicite o ereditate per inerzia;
  3. *Fase 3 (Chiusura Tecnica)*: Commit Git con Conventional Commits (`feat:`, `fix:`, `refactor:`, `docs:`, `chore:`);
  4. *Doppia Barriera di Backup*: Aggiornamento del backup stabile su OneDrive/Cloud **esclusivamente POST-CONVALIDA positiva dell'utente**;
  5. *Rilascio Atomico GitHub & Invalidazione Cache CDN (Per Repository Pubblici)*:
     - Nei repository distribuiti tramite GitHub Releases, se un tag o una release subisce consolidamenti post-audit prima della diffusione pubblica, è fatto divieto di affidarsi al solo force-push del tag Git (la CDN di GitHub mantiene in cache i vecchi archivi automatici `.zip` e `.tar.gz` del codice sorgente);
     - Eseguire sempre la procedura di rigenerazione atomica a due stadi:
       * 1. Cancellazione release: `gh release delete <tag> --yes` (invalida la cache CDN e pulisce il database release);
       * 2. Ricreazione release: `gh release create <tag> --title "..." --notes-file <path>` legata deterministicamente al commit consolidato;
  6. *Living Documentation, Migrazione RRU & Archiviazione Automatica a Zero Residui*:
     - Aggiornamento delle schede in `knowledge/`;
     - **Archiviazione del Piano Tecnico**: Spostamento del piano completato da `docs/piani/attivi/` a `docs/piani/completati/`;
     - **Archiviazione Piani Abbandonati/Non Implementati (Protocollo 6 Adattato)**: Se un piano tecnico viene abbandonato in Sotto-Fase 1A prima dell'implementazione per evitare sovraingegnerizzazione o per cambio di strategia, viene marcato con stato `[ABBANDONATO IN SOTTO-FASE 1A - NON IMPLEMENTATO]` e spostato nella cartella dedicata `docs/piani/archiviati/`. La cartella `docs/piani/completati/` rimane rigorosamente riservata agli interventi implementati e collaudati positivamente sul campo. Nessun incremento di versione AVF viene applicato;
     - **Archiviazione della Strategia Cognitiva**: Spostamento della strategia validata da `docs/strategie/attive/` a `docs/strategie/archiviate/` con stato `[ARCHIVIATA CON SUCCESSO]`;
     - **Migrazione RRU**: Trasferimento delle revisioni collaudate da `docs/report/REGISTRO_REVISIONI.md` ad `ARCHIVIO_REVISIONI.md`;
     - **Archiviazione Automatica del Report**: Spostamento automatico di `docs/report/REPORT_SESSIONE_[TASK].md` in `docs/report/archivio/REPORT_SESSIONE_[TASK].md`, aggiornando deterministicamente tutti i puntatori incrociati ai path di archivio (zero link rotti e zero documenti orfani);
  7. *Domanda Ponte Obbligatoria*: L'assistente **NON si congeda mai a vuoto**, ma chiude tassativamente con la domanda di transizione:
     > *"Vuoi che avviamo ora la sessione formale di Auto-Apprendimento (Fase 4) per elaborare la bozza dettagliata delle regole e aggiornare le schede di conoscenza e governance?"*
     - *Pre-auto-learning relevance check* – Analisi silenziosa della sessione corrente; se non emergono nuove conoscenze, il prompt di auto-apprendimento viene omesso e viene comunicato “Nessuna rilevanza o lezione appresa in questa sessione di lavoro – salto l’auto-apprendimento”. Altrimenti, il prompt è mostrato con una breve sintesi dei punti rilevanti.

---

### 7. PROTOCOLLO APPRENDIMENTO *(Auto-Apprendimento Continuo Contestuale & Discovery Dinamico — Fase 4)*
- **Comandi Trigger**: *"Avvia Protocollo Apprendimento"*, *"passiamo all'auto-apprendimento"*, *"avvia la fase 4"*, *"estraiamo le lezioni"*, *"aggiorna la governance"*.
- **Scopo**: Capitalizzare la conoscenza emersa dalla sessione, estraendo pattern riutilizzabili ed evitando la perdita di memoria dell'AI, con isolamento assoluto tra contesti di progetto, governance locale dell'utente e framework distribuibile pubblico.
- **Passaggi Operativi**:
  1. *Triplo Context Switcher Automatico a Marker Strutturali (Rilevamento Deterministico del Contesto)*:
     All'avvio della Fase 4, l'AI auto-rileva istantaneamente l'ambito in cui sta operando prima di proporre modifiche:
     - **Ambito C — Manutenzione Framework Distribuibile (Repository GitHub)**:
       * *Riconoscimento*: Presenza del remote Git `astralis-framework` o della cartella `docs/developer/specifiche/`.
       * *Azione*: Modalità *Framework Core Maintainer*. Dogfooding su `knowledge/` pubblica, `templates/`, `scripts/`, documentazione `docs/`, registrazione in `docs/developer/report/REGISTRO_META_REVISIONI_ASTRALIS.md` e `CHANGELOG.md` pubblico. Divieto assoluto di memorizzare dettagli personali o percorsi della macchina.
     - **Ambito B — Manutenzione Master Hub Locale (Livello Globale Postazione Utente)**:
       * *Riconoscimento*: Presenza dell'hub locale dell'utente (marker `user_preferences.md` personale, `knowledge/` o router ponte Livello 1) e assenza del repository Git distribuibile pubblico.
       * *Azione*: Modalità *Master Hub Manager*. Aggiorna le regole trasversali della postazione e preserva l'Isola Protetta Utente. Lo Starter Kit ZIP locale viene rigenerato soltanto dopo il gate AVF e la conferma esplicita della versione.
     - **Ambito A — Sviluppo su Progetto Utente Verticale (Singolo Workspace)**:
       * *Riconoscimento*: Presenza di un workspace di progetto (videogioco, scrittura narrativa, addon, utility, software) con router locale di Livello 2.
       * *Azione (Doppio Binario)*:
         - *Binario A (Locale)*: Creazione/aggiornamento schede `knowledge/` del progetto;
         - *Binario B (Globale Privato Utente)*: Proposta dell'invariante trasversale unicamente al Master Hub locale dell'utente (individuato dinamicamente). Divieto assoluto di toccare il repository pubblico.
  2. *Algoritmo Dinamico di Discovery del Master Hub (Zero Hardcoding)*:
     Per individuare il Master Hub locale su qualsiasi computer senza presupporre percorsi cablati:
     - *Livello 1 (Configurazione Esplicita)*: Lettura del percorso nel manifest di Livello 0 (`Master Hub: <percorso>`) o variabile d'ambiente `$env:ASTRALIS_HUB`.
     - *Livello 2 (Discovery a Marker)*: Scansione nelle radici note (`$env:OneDrive`, `$env:USERPROFILE`, parent `..`) alla ricerca di una cartella contenente contemporaneamente `catalogo_protocolli_operativi_astralis.md`, `knowledge/` o `knowledge/` e `CHANGELOG.md`.
     - *Livello 3 (Fallback Interattivo)*: Richiesta one-time all'utente (*"In quale percorso risiede il tuo Master Hub ASTRALIS?"*) e memorizzazione nel profilo locale `user_preferences.md` escluso da Git.
  3. *Estrazione della Conoscenza sul Modello a 4 Faccette (The 4-Facet Learning Matrix)*:
      L'auto-apprendimento supera la semplice tripartizione tematica ed estrae sistematicamente la conoscenza lungo 4 assi di astrazione:
      - **Faccetta 1 — Tecnico-Meccanica (La Conoscenza Concreta)**: Sintassi, API, vtable, hook, memory layout, distinzione tra memoria grezza, posizionamento vtable, sottoggetti costruiti, distruzione simmetrica e deallocazione, formati binari e flag di compilazione. Collocazione: `knowledge/09_registro_bug_e_soluzioni.md` e `knowledge/04_standard_tecnologici_trasversali/`.
      - **Faccetta 2 — Logico-Cognitiva & Pensiero da Programmatore (Il Metodo Ingegneristico)**: Euristiche decisionali, risalita al punto che possiede il flusso, disciplina della singola variabile causale e tassonomia probatoria a 7 stati (`THEORETICAL PASS`, `PASS STATICO`, `PASS HEADLESS`, `OBSERVED`, `FAIL AL GATE`, `PARTIAL-GAIN/CADENCE`, `FULL EMPIRICAL PASS`). `FAIL` e `PARTIAL` sono rami diagnostici, non gradini superiori. Collocazione: `knowledge/03_architettura_e_metodologie/strategie_testing_e_debug.md` e `clean_architecture_e_design_pattern.md`.
      - **Faccetta 3 — Astratta & Universale (L'Invariante Cross-Dominio)**: Principi di architettura validi per qualunque tecnologia o linguaggio presente o futuro (C++, Python, C#, Rust, Web, shell). Collocazione: Master Hub Globale (`knowledge/` nei moduli 01, 02, 03).
      - **Faccetta 4 — Verticale di Dominio & Regole di Progetto (Il Contesto Locale)**: Specificità del singolo repository (es. Skyrim SE 1.6.1170.0, Minecraft Fabric, Add-on NVDA wxPython, audiodescrizioni). Collocazione: `knowledge/` locale del progetto e manifest locali.
  4. *Modulo di Peer-AI Cross-Learning & Sinergia a Specchio (Collaborazioni Multi-AI)*:
      Quando la sessione vede la cooperazione di una o più AI (Google Gemini / Antigravity, OpenAI GPT / Codex, Anthropic Claude, GitHub Copilot, modelli locali Jolly):
      - **Assimilazione dei Punti di Forza del Peer**: Retrospettiva sui metodi, formalismi e strumenti d'indagine adottati dall'altra AI rivelatisi vincenti, integrandoli come forma mentis permanente del sistema;
      - **Isolamento delle Divergenze & Convergenza Scientifica**: Risoluzione delle divergenze tecniche formulando test falsificabili su una sola variabile causale; telemetria passiva e guardie di sicurezza restano ammesse. Il verdetto empirico di Luca costituisce il *Ground Truth* dell'esperienza d'uso;
      - **Guardia di Parità Semantica dei Router Attivi**: Verifica dei soli router personali realmente presenti e usati. Essi puntano alle stesse fonti canoniche mantenendo ruolo, sintassi e budget di 250 righe; non vengono creati router per client assenti né sovrascritti documenti upstream per ottenere una simmetria nominale.
  5. *Auto-Audit Preventivo & Diagnosi Mancata Osservanza*: Ricerca se la regola esisteva già; se esisteva, spiega la causa radice della mancata osservanza.
  6. *Le 4 Regole Auree Anti-Conflitto e Context Fencing*:
     - *Direzionalità a senso unico della privacy*: i dati personali non fluiscono mai verso l'upstream pubblico.
     - *Separazione impermeabile dei registri*: RRU del progetto vs Registro locale dell'Hub vs Meta-Registro pubblico.
     - *Validazione pre-scrittura sui 6 Canoni di Meta-Governance* (token budget, disaccoppiamento, puntatori DRY, linearità NVDA, igiene UTF-8/LF/CRLF).
     - *Domanda Ponte Contestualizzata*: La chiusura di Fase 3 formula la domanda esplicitando chiaramente l'ambito (Progetto, Hub Locale, o Framework Distribuibile).
  7. *Checkpoint di Auto-Apprendimento Inter-Fase nei Grandi Refactor Multi-Fase (Consolidamento Frattale On-Demand)*:
     - Nelle epiche complesse multi-fase, consolidamento immediato delle lezioni apprese tra una sotto-fase e la successiva, proteggendo l'esecuzione da imprevisti ripetuti.

---

### 8. PROTOCOLLO AGGIORNAMENTO *(Smart Merge, Isola Protetta & Migrazione Progetti Attivi — Modello a 3 Fasi)*
- **Comandi Trigger**: *"Avvia Protocollo Aggiornamento"*, *"aggiorna il sistema di regole"*, *"aggiorna ASTRALIS a questa versione"*, *"esegui l'upgrade dell'ecosistema"*.
- **Scopo**: Aggiornare in-place l'infrastruttura di governance su una macchina esistente, fondendo le nuove regole ufficiali con la totale salvaguardia delle personalizzazioni utente e riconciliando retrocompatibilmente tutti i progetti aperti.
- **Passaggi Operativi (La Pipeline a 3 Fasi: Prima -> Durante -> Dopo)**:
  1. *Fase 1: Pre-Flight Audit dello Stato Attuale (PRIMA dell'Aggiornamento)*:
     - Snapshot `.bak` timestampati di `<config-dir>\config\GEMINI.md` e `knowledge/`;
     - Scansione automatica dei client AI presenti sulla macchina (`.gemini`, `.codex`, `.claude`, `.copilot`) per censire l'ecosistema Multi-AI attivo;
     - Rilevamento regole/consuetudini custom introdotte dall'utente;
     - Scansione preventiva del delta versioni tra Master Hub e progetti locali attivi (identificazione di registri revisione legacy, report non conformi, BOM, discrepanze).
  2. *Fase 2: Aggiornamento Master Hub & Release Starter Kit (DURANTE)*:
     - Aggiornamento del Genoma Globale incapsulando le consuetudini personali nell'Isola Protetta Utente;
     - Aggiornamento contestuale delle direttive globali per le AI collaboratrici censite sulla macchina (es. `%USERPROFILE%\.codex\AGENTS.md`, `%USERPROFILE%\.claude\CLAUDE.md`) con Guardia Condizionale di Simmetria a Livello 0 (aggiornamento solo se rilevate o richieste, zero file orfani);
     - Fusione a sezioni dei moduli in `knowledge/` e template in `templates/`;
     - Rigenerazione dello Starter Kit ZIP versionato (`releases/ASTRALIS_Universal_Starter_Kit_vX.Y.Z.zip`).
  3. *Fase 3: Post-Flight Migration & Riconciliazione Progetti Attivi (DOPO l'Aggiornamento)*:
     - *Allineamento Knowledge Locale*: sincronizzazione selettiva delle schede `knowledge/` pertinenti nei progetti attivi;
     - *Audit del Profilo di Resilienza & Canali Cloud*: verifica sui progetti attivi della presenza della sezione Profilo di Resilienza; se assente, propone la rilevazione deterministica di VCS e dei percorsi ponte/archivio cloud;
     - *Migrazione Retrocompatibile RRU*: verifica e aggiornamento di `REGISTRO_REVISIONI.md` e `ARCHIVIO_REVISIONI.md` per abilitare il puntamento DRY ai report (`Report di Sessione & File Correlati`) senza alterare i dati storici;
     - *Verifica Report*: rilevare discrepanze di testata, cronologia, encoding e collegamenti senza riscrivere archivi chiusi. Applicare lo standard corrente ai nuovi report e alle riaperture sostanziali autorizzate, secondo la routine report v3;
     - *Audit di Conformità & Token Budget*: verifica del rispetto dei 6 Canoni di Meta-Governance; controllo che nessun `GEMINI.md` superi il budget limite di 250 righe, assenza di BOM e integrità di tutti i collegamenti; emissione della **Ricevuta di Conformità Post-Aggiornamento** per NVDA.

---

### 9. PROTOCOLLO ONBOARDING *(Bootstrap Zero-Config Nuova Macchina o Progetto)*
- **Comandi Trigger**: *"Avvia Protocollo Onboarding"*, *"configura l'ambiente di lavoro"*, *"inizializza nuovo progetto"*, *"setup nuova macchina"*.
- **Scopo**: Inizializzare un computer da zero o generare l'albero di un nuovo workspace in meno di un minuto con specializzazione automatica, garantendo zero debito pregresso e piena conformità nativa.
- **Passaggi Operativi**:
  1. *Per Nuova Macchina*:
     - Bootstrap pulito direttamente dall'ultimo Starter Kit ZIP versionato (`ASTRALIS_Universal_Starter_Kit_vX.Y.Z.zip`);
     - Auto-Riconoscimento AI Attiva & Ruolo Primario: L'assistente rileva l'ambiente in cui opera (Antigravity, Claude, Codex) e si imposta come AI Primaria per default;
     - Intervista guidata snella (Nome sviluppatore, Uso Screen Reader NVDA/Tastiera, Accessibilità perenne);
     - Opzione Collaboratori AI Ausiliari: Se richiesto esplicitamente o rilevato a sistema, genera i profili globali (`.codex/`, `.claude/`) attingendo a `templates/collaboratori_ai/` con Guardia Condizionale (zero file superflui);
     - Creazione dell'albero documentale `docs/` nel Master Hub;
     - Pre-flight check percorsi dinamici, cloud e hostname (`$env:COMPUTERNAME`).
  2. *Per Nuovo Progetto*:
     - Intervista su tecnologia, runtime e dominio (es. mod Java, addon Python, script, narrativa);
     - Rilevamento adattivo VCS & Canali Cloud (Git vs No-Git con linguaggio calibrato sull'utente e configurazione ponte caldo/archivio);
     - Generazione cartelle `docs/` (`strategie/attive`, `strategie/archiviate`, `piani/attivi`, `piani/completati`, `report/archivio`), `knowledge/` a due cifre (`00_` .. `NN_`), router locale `GEMINI.md` (o dell'AI primaria) specializzato con Indice Ragionato e Profilo di Resilienza a 4 canali, ed eventuale generazione dei router ausiliari (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`) attingendo da `templates/collaboratori_ai/`;
     - Inizializzazione di `REGISTRO_REVISIONI.md` con pointer hub e riferimento al template REPORT corrente; non creare report vuoti senza un incarico che richieda continuità;
     - Creazione del `README.md` pubblico di root pulito e dedicato alla documentazione funzionale del software.

---

### 🛡️ LA GUARDIA AUSILIARIA MULTI-AI ON-DEMAND *(Proactive Multi-AI Health Check)*
- **Scopo**: Garantire l'armonizzazione e l'integrità automatica dell'ecosistema Multi-AI anche quando un collaboratore viene introdotto senza passare formalmente dall'Onboarding o dall'Upgrade.
- **Regola di Attivazione Silenziosa**:
  - In qualsiasi sessione di lavoro, l'AI Primaria esegue un controllo non invasivo sulla radice del progetto:
    * *Se* rileva un file manifest di un collaboratore ausiliario (es. `./AGENTS.md`, `./CLAUDE.md`) ma manca la controparte globale sulla macchina (`%USERPROFILE%\.codex\AGENTS.md`, `%USERPROFILE%\.claude\CLAUDE.md`);
    * *Oppure se* il file del collaboratore risulta disallineato rispetto alla versione corrente di ASTRALIS;
    * *Allora* emette una notifica proattiva a 1 riga per NVDA:
      > *"🛡️ [ASTRALIS] Rilevato collaboratore AI ([Nome AI]) con configurazione incompleta o disallineata. Vuoi che generi il profilo globale e armonizzi le direttive con 1 comando?"*
  - Su conferma di Luca, genera atomicamente i profili mancanti attingendo da `templates/collaboratori_ai/`, garantendo simmetria e cooperazione sicura a zero attrito.

---

### 10. PROTOCOLLO SICUREZZA *(Eliminazione Protetta & Diagnosi Bug Ostici)*
- **Comandi Trigger**: *"Avvia Protocollo Sicurezza"*, *"procedura di eliminazione protetta"*, *"diagnosi bug ostico"*, *"root cause analysis"*.
- **Scopo**: Gestire cancellazioni strutturali o anomalie complesse senza alcun rischio di perdita dati.
- **Passaggi Operativi**:
  1. *Per le Eliminazioni di File (Regola Inviolabile)*:
     - Motivazione chiara dell'eliminazione;
     - Descrizione dettagliata dell'impatto sul contesto operativo;
     - Verifica dell'assenza di perdita dati (tutti i contenuti utili preservati altrove);
     - *Per le eliminazioni di repository, cloni o worktree storici basate su salvaguardie compresse o Git bundle*: **Obbligo del Dry-Run Restore Drill** (estrazione reale in staging temporaneo `%TEMP%`, verifica presenza sorgenti chiave, aggancio di eventuali sottomoduli ricorsivi ed applicabilità di patch non committate) per dimostrare l'autosufficienza operativa prima di proporre la cancellazione;
     - **Richiesta e attesa di autorizzazione esplicita a Luca prima di procedere**;
  2. *Per i Bug Ostici*:
     - Ricerca della causa radice (Root Cause Analysis, zero pezze provvisorie);
     - Test isolato di riproduzione;
     - Registrazione vivente nel registro bug/soluzioni o nel registro revisioni.

---

### 11. PROTOCOLLO PULIZIA & BONIFICA *(Code & Asset Grooming / Dead Code Purge)*
- **Comandi Trigger**: *"Avvia Protocollo Pulizia"*, *"bonifica del codice"*, *"scansiona codice morto"*, *"rimuovi funzioni inutilizzate"*, *"clean up del repository"*, *"pulizia asset obsoleti"*.
- **Scopo**: Identificare, catalogare ed eliminare chirurgicamente codice morto, import orfani, classi deprecate, asset multimediali non referenziati e debito tecnico, garantendo l'assenza totale di regressioni e la sicurezza dei dati tramite la **Strategia a 5 Barriere di Sicurezza**.
- **La Strategia a 5 Barriere di Sicurezza**:
  1. *Barriera 1: Audit a Doppia Chiave (Statica + Dinamica)*:
     - Ispezione statica (AST/Call Graph) + ispezione dinamica (ricerca di stringhe in JSON, file lingua I18N, reflection, manifest).
     - **Regola di Prudenza**: Qualsiasi elemento referenziato anche solo come stringa è marcato `[POTENZIALE RIFERIMENTO DINAMICO]` e **protetto per default**.
  2. *Barriera 2: Prospetto di Bonifica Lineare per NVDA (Dry-Run ad Alto Segnale)*:
     - Generazione del prospetto sequenziale numerato: `[ID]`, Percorso e riga, Elemento, Natura, Prova di non-uso, Livello di Rischio (`BASSO`, `MEDIO`, `ALTO`) e Azione Proposta (*Eliminazione* o *Quarantena*).
  3. *Barriera 3: Gating Semantico & Scelta Granulare dell'Utente (Regola 0)*:
     - Nessuna modifica autonoma. Luca può accettare tutto, escludere ID specifici o richiedere la modalità conservativa.
  4. *Barriera 4: Quarantena di Sicurezza Reversibile & Snapshot (Zero Data Loss)*:
     - Creazione di snapshot preventivo locale (`docs/quarantena_[timestamp]/` o branch temporaneo);
     - Nei progetti di Scrittura Creativa vige il **Divieto Assoluto di Cancellazione**: le bozze o note dismesse vengono spostate in `archivio_bozze/`.
  5. *Barriera 5: Compilazione, Test di Non-Regressione & Rollback Automatico a 1-Click*:
     - Esecuzione immediata di compilazione e test automatici;
     - In caso di fallimento, scatta il **Rollback Automatico Istantaneo** con notifica dell'elemento critico; a test superati, registrazione in `CHANGELOG.md` sotto `⚙️ Modifiche & Refactoring`.
  6. *Integrazione Obbligatoria nei Piani di Refactoring (Contratto D0 Clean Sweep)*:
     - Quando un piano tecnico di tipo *Refactoring* o *Implementativo* sostituisce un meccanismo preesistente con una nuova architettura, il primo contratto del piano (`D0`) deve essere formalmente dedicato alla bonifica integrale di TUTTI i residui del vecchio meccanismo (campi, metodi, getter/setter, reset nei metodi di ciclo di vita, blocchi logici concorrenti, import orfani).
     - La bonifica del codice vecchio precede l'innesto del nuovo sistema per impedire alla radice la convivenza transitoria di logiche concorrenti o comportamenti spuri.

---

### 12. PROTOCOLLO DIALETTICA INGEGNERISTICA & AUTO-REVISIONE AVVERSARIALE *(L'Inner Codex Pattern)*
- **Comandi Trigger**: *"Avvia Protocollo Dialettica Ingegneristica"*, *"fai l'auto-revisione avversariale"*, *"applica l'Inner Codex Pattern"*, *"audit di rigore ingegneristico"*, *"sfida questa soluzione"*, *"analizza come farebbe Codex"*.
- **Scopo**: Elevare strutturalmente la profondità ingegneristica, la solidità diagnostica e la disciplina architetturale di Antigravity, interiorizzando stabilmente il ruolo di Senior Reviewer critico, intransigente e avversariale (L'Inner Codex Pattern). Questo consente ad Antigravity di operare con il medesimo livello di rigore anche in sessioni di lavoro solitarie, senza dipendere dalla presenza di un secondo assistente AI (ChatGPT/Codex) per smascherare assunzioni deboli o soluzioni fragili.
- **Ambito dei cancelli**: applicare i vincoli pertinenti al dominio. La proprietà delle responsabilità segue il [metodo architetturale, sezione 27](clean_architecture_e_design_pattern.md); la causa va dimostrata con il [metodo diagnostico, sezione 10](strategie_testing_e_debug.md). Nessun orchestratore globale obbligatorio.
- **I 6 Cancelli Inviolabili (The 6 Inviolable Gates)**:
  1. *Cancello 1: Rifiuto del Patching Euristico (Invariante Topologica vs Sintomo Numerico)*:
     - È severamente vietato tentare di risolvere anomalie geometriche, di navigazione o logiche alterando parametri quantitativi arbitrari (aumento del budget di espansione, pesi dell'euristica A*, allungamento dei delay in tick, mosse di fuga fisse).
     - Un grafo che fallisce con pochi nodi espansi suggerisce una discontinuità: verificare archi, dati, guardie e configurazione prima di attribuire la causa. Modificare budget o pesi solo se una misura dimostra che sono causalmente responsabili.
  2. *Cancello 2: Purezza dell'Intento Fisico nei Sistemi Ibridi (Hardware Grounding)*:
     - Nelle architetture cooperative o ibride (dove coesistono navigazione autonoma/bot e guardie reattive di sicurezza), il rilevamento della volontà dell'utente umano non deve mai interrogare lo stato logico simulato da un automatismo concorrente (es. `keyShift.setDown(true)`).
     - *Se* si deve rilevare il comando o la presa di controllo dell'utente umano -> *Allora* si interroga la verità fisica dell'hardware (polling GLFW raw input o driver di periferica puro).
  3. *Cancello 3: Integrità della Hitbox e Volumetria Continua*:
     - Un'entità non è mai assimilabile a un punto matematico o a una casella $1 \times 1$. Possiede una bounding box 3D volumetrica reale ($0.6 \times 1.8\text{ m}$).
     - *Se* si valuta la percorribilità, la caduta o il dislivello -> *Allora* si verifica obbligatoriamente la clearance continua dell'intera sagoma (luce sopraelevata per occhi/testa e forme di collisione sottili di porte, scale a pioli o muretti).
  4. *Cancello 4: Disciplina dei Contratti Denominati e Chiusi (Named Contract Pattern)*:
     - Nessuna modifica complessa può essere descritta in prosa generica.
     - *Se* si progetta o si revisiona un comportamento articolato -> *Allora* la modifica deve essere suddivisa in contratti atomici, numerati e univoci (D0..DN per le decisioni di design, S1..SN per i moduli software), ciascuno con precondizioni formali, postcondizioni osservabili, budget di complessità e invarianti anti-regressione.
  5. *Cancello 5: Determinismo Headless e Tempo Controllato*:
     - Nessun test unitario deve dipendere dal wall-clock di sistema o dall'esecuzione di `Thread.sleep`.
     - *Se* un componente adotta logiche a tempo (finestre di soppressione, debouncing, TTL, timeout) -> *Allora* deve obbligatoriamente esporre punti di controllo del tempo appropriati allo stack (clock virtuale / fornitori di timestamp) per verificare creazione, avanzamento e scadenza senza attese arbitrarie; il tempo reale della suite resta misurabile.
   6. *Cancello 6: Custode Critico del Budget Token & Anti-Bloat Normativo (Meta-Governance Gate)*:
      - È fatto divieto assoluto di accogliere o proporre inserimenti di spiegazioni estese nei file di ingresso master (`GEMINI.md`).
      - *Se* una nuova regola, routine o spiegazione richiede più di 4 righe -> *Allora* l'assistente DEVE rifiutare l'innesto diretto nel router, incapsulare il contenuto in una scheda modulare dedicata (`knowledge/`) e inserire nel router unicamente un puntatore ipertestuale conforme ai 6 Canoni.
- **Integrazione Obbligatoria nella Sotto-Fase 1A**:
  - In ogni Piano Tecnico Formale, prima della presentazione a Luca, l’AI responsabile esegue un audit preventivo esplicito a 6 voci, motivando la conformità oppure NON APPLICABILE per un cancello di dominio non pertinente.

---

## 📋 IL REGISTRO REVISIONI UNIVERSALE (RRU) & IL PATTERN DISACCOPPIATO

1. **Scopo del Sistema di Revisioni**:
   - Memoria vivente di tutte le anomalie, discrepanze tra intenzione ed esperienza reale, calibrazioni metriche e rifiniture emerse durante il ciclo di vita del progetto.

2. **L'Architettura Disaccoppiata (Registro Attivo vs Archivio Storico)**:
   - Per impedire il sovraccarico cognitivo dello screen reader NVDA e preservare la velocità di scansione (< 100 righe per file), il sistema di revisione è strutturato in due componenti complementari:
     * **`docs/report/REGISTRO_REVISIONI.md` (Registro Attivo Snello)**:
       - Ospita *unicamente* le revisioni aperte (`[APERTA]`), in lavorazione (`[IN LAVORAZIONE]`) o in collaudo (`[IN TELEMETRIA]`).
       - È il file di lavoro quotidiano, rapido e compatto.
     * **`docs/report/ARCHIVIO_REVISIONI.md` (Archivio Storico delle Revisioni)**:
       - Raccoglie in modo ordinato e cronologico tutte le revisioni completate e collaudate con successo (`[COLLAUDATA CON SUCCESSO]`).
       - È la memoria forense perenne del progetto, consultabile on-demand.

3. **Ciclo di Vita Automatizzato delle Revisioni**:
   - *Fase A (Rilevamento / Fase 2)*: L'anomalia emersa in telemetria viene registrata in `docs/report/REGISTRO_REVISIONI.md` (`🛡️ [ASTRALIS] Registrata Rev X.Y`);
   - *Fase B (Affinamento / PRAPI Protocollo 5)*: La voce viene lavorata e marcata `[IN LAVORAZIONE]`;
   - *Fase C (Chiusura Tecnica / Fase 3 o Fase 4)*: A collaudo positivo confermato da Luca, la voce viene marcata `[COLLAUDATA CON SUCCESSO]` e **migrata automaticamente dal registro attivo a `docs/report/ARCHIVIO_REVISIONI.md`**, lasciando il registro attivo sempre pulito.

4. **Anatomia Standard di Ogni Voce**:
   ```markdown
   ### 🟡 Rev [ID] — [Titolo Sintetico]
   - **Stato**: `[APERTA / IN TELEMETRIA]` | `[IN LAVORAZIONE]` | `[COLLAUDATA CON SUCCESSO]`
   - **Problema Riscontrato (Esperienza Luca)**: [Sintomo e discrepanza]
   - **Evidenza Telemetrica / Log**: [Eventuale riga di log o eccezione]
   - **Causa Radice**: [Perché si è verificato il comportamento]
   - **Soluzione di Affinamento**: [Cosa faremo nel PRAPI]
   - **Report di Sessione & File Correlati**: [`REPORT_SESSIONE_[TASK].md`](./docs/report/REPORT_SESSIONE_[TASK].md)
   - **Esito Collaudo**: [In attesa / Superato con successo in data YYYY-MM-DD]
   ```

5. **Integrazione con il Report di Sessione (Pointer Hub & DRY Pattern)**:
   - *Separazione delle Competenze*: Il `REGISTRO_REVISIONI.md` mantiene solo lo stato di alto livello e il puntatore al Report di Sessione attivo (`docs/report/REPORT_SESSIONE_[TASK].md`).
   - *Single Source of Truth*: L'elenco dettagliato dei file sorgenti modificati, dei test seams, delle righe di log e delle motivazioni architetturali risiede unicamente nel Report di Sessione, azzerando la duplicazione delle informazioni.
   - *Migrazione dei Link in Fase 3*: Al momento della chiusura tecnica, quando la revisione viene trasferita in `ARCHIVIO_REVISIONI.md` e il report viene spostato in `docs/report/archivio/`, il link nella voce archiviata viene aggiornato automaticamente per puntare al percorso di archivio del report, garantendo la tracciabilità forense perenne senza link interrotti.

6. **Guardia di Ingestione & Archiviazione Report (Report Ingestion & Archival Guard — Standard URCP)**:
   - *Scopo*: Impedire l'accumulo di debito documentale o entropia nei report di sessione generati internamente, forniti da copiloti esterni (ChatGPT/Codex) o redatti come appunti rapidi sul campo.
   - *Regola di Attivazione*: In qualsiasi momento venga richiesto il salvataggio o l'archiviazione di un report in `docs/report/archivio/` (o all'atto della chiusura in Fase 3):
     * *Se il report attivo è conforme allo standard corrente o è un legacy leggibile*: archiviazione nel ciclo di chiusura convalidato, verificando i puntatori. I report storici già chiusi restano immutati;
     * *Se un report attivo necessita adattamento sostanziale compreso nel mandato*: l'AI incaricata applica la **Pipeline URCP a 4 Passi**, preservando originali ed evidenze:
       1. **Allineamento dei Metadati**: adottare la Testata Universale Compatta e l'estensione REPORT della tassonomia senza inventare autore, revisori, date, stato, gate o autorizzazioni. I sette campi storici sono compatibilità di lettura, non un vincolo alternativo per nuovi report;
       2. **Inversione Cronologica per NVDA**: Riorganizzazione dei flussi dialogici o delle sezioni progressive (esito finale e stato dell'arte in alto, sezioni storiche in basso per consentire la lettura immediata all'apertura);
       3. **Denoising & Puntatori Intelligenti (DRY Pattern)**: Compattazione di dump prolissi di log in estratti ad alto segnale con link al file sorgente (`latest.log`), con **preservazione inviolabile al 100%** di ogni formula matematica, coordinata voxel, evidenza empirica o disamina architetturale;
       4. **Bonifica Tecnica & Formati**: Rimozione automatica di BOM UTF-8 (`\ufeff`), formattazione corretta dei collegamenti Markdown e normalizzazione dei marcatori Markdown.

## Raccordo degli strumenti del ciclo di sviluppo — Astralis 3.X

Per scelta del metodo fra idea, strategia, piano, analisi, validazione, revisione e prove usare la [mappa di fase](ciclo_sviluppo_e_selezione_strumenti_astralis.md). La mappa non aggiunge protocolli o permessi e non impone di percorrere tutte le fasi.
