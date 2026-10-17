# Strategie di Testing, Isolamento Bug e Debug Sistemico (v3.0.0)
# Autore: Luca (Sviluppatore Senior Non Vedente con Screen Reader NVDA)
# Target AI: Antigravity (Senior AI Pair Programmer & Software Engineer)
# Ambito: Globale / Universale

Questo documento stabilisce le linee guida per la creazione di test automatici, la simulazione preventiva degli scenari, il troubleshooting sistemico delle anomalie e la sicurezza post-bonifica.

---

## 🧪 1. STRATEGIA DI TESTING AUTOMATICO

1. **Piramide dei Test**:
   - *Test Unitari (Base)*: Numerosi, veloci, isolati con mock su Domain e Use Cases.
   - *Test di Integrazione (Centro)*: Verificano il corretto funzionamento tra moduli interni (es. serializzazione, controller e servizi).
   - *Test End-to-End / Pre-Flight (Vertice)*: Testano l'avvio completo e i flussi critici.

2. **Convenzioni di Naming, Partizionamento per Dominio e Guardia Anti-Monolite**:
   - Pattern Arrange-Act-Assert (AAA) ben distinto in ogni funzione di test, con funzioni di test atomiche (un singolo scenario o contratto per funzione).
   - Nomi dei file di test espliciti per dominio e categoria: `test_<dominio>_<categoria>.py`, `<Dominio><Categoria>Tests.cpp` o `<Componente>Test.cs`.
   - *Partizionamento Obbligatorio per Categoria e Sottosistema*: ogni file di test copre un singolo ambito funzionale coeso; fixture, mock e helper condivisi vanno isolati in moduli di supporto dedicati (`test_common_fixtures.*` / `conftest.py`). È vietato creare o alimentare file "contenitore generico" che mescolano sottosistemi eterogenei.
   - *Divieto di Accodamento Inerziale e Soglia di Guardia*: è vietato accodare per inerzia nuove suite di milestone successive allo stesso file esistente; quando un file di test supera la soglia di guardia (~800–1.000 righe), ogni nuova suite o sotto-ambito deve essere allocata in una nuova partizione dedicata (`test_<dominio>_<sottoambito>.*`).
   - *Clausola Zero-Churn per Monoliti Storici*: i file di test monolitici preesistenti già stabili restano congelati (non si smontano speculativamente per evitare regressioni o attrito sul build system, ma è vietato accodarvi nuove suite).

3. **Esecuzione Veloce e Determinismo**:
   - I test devono essere riproducibili e non dipendere da risorse di rete esterne non controllate (usare fixture e mock).

---

## 🐞 2. PROTOCOLLO DI DEBUG SISTEMICO IN 4 PASSI

1. **Isolamento e Riproduzione Minima**:
   - Creare un test minimale o un comando riproducibile che isoli l'anomalia senza interferenze di contorno.
2. **Ispezione Forense dei Log e Dati**:
   - Tracciare input, stato interno e output al momento dell'errore.
3. **Correzione Chirurgica alla Causa Radice**:
   - Risolvere la causa profonda, non solo il sintomo visibile.
4. **Test di Regressione Permanente**:
   - Aggiungere il test di riproduzione alla suite di test automatici affinché il bug non si ripresenti mai più.

---

## 🛡️ 3. RESILIENZA AI LOCK TRANSITORI CLOUD (ONEDRIVE/DROPBOX ANTI-SNAPSHOT PATTERN)

1. **La Causa del Lock**:
   - Sui percorsi sincronizzati in tempo reale con cloud storage (OneDrive, Google Drive, Dropbox), i file di output generati rapidamente durante la compilazione o la compressione possono essere temporaneamente agganciati dal processo di sincronizzazione, sollevando eccezioni `AccessDeniedException`, `Cannot snapshot ... not a regular file` o file lock in PowerShell/Gradle/Python.
2. **Standard di Prevenzione**:
   - **Flag Anti-Daemon**: Nelle build Gradle/Java, specificare sempre `--no-daemon` per evitare processi in background persistenti su percorsi sincronizzati.
   - **Staging Temporaneo su `$env:TEMP`**: Tutti gli script di compressione o packaging ZIP devono creare l'archivio in una directory temporanea locale isolata e poi spostarlo atomicamente a destinazione.
   - **Pulizia Selettiva Cache**: In caso di errore `Cannot snapshot` o lock di directory di build, eseguire un `clean` selettivo della cartella `build/` o `__pycache__/` senza toccare l'albero dei sorgenti.

---

## 🧪 4. LA MATRICE DI SIMULAZIONE A 3 LIVELLI (STRESS-TEST LOGICO PREVENTIVO)

1. **Scopo Metodologico**:
   - Integrare la validazione formale sui 7 Assi con uno stress-test concettuale dinamico prima di scrivere codice, prevenendo bug di logica, race condition e regressioni posturali.

2. **I 3 Livelli di Simulazione**:
   - **Livello 1: Scenari Comuni (Happy Path / Uso Quotidiano — 80-90% dei casi)**:
     * Verifica del comportamento nominale in condizioni standard (es. avanzamento dritto, apertura finestre nominali).
   - **Livello 2: Scenari Meno Comuni (Alternative Paths & Casi Concorrenti)**:
     * Verifica di combinazioni lecite ma secondarie: filtri composti, cambi rapidi di direzione, input multipli o retromarcia su baratro.
   - **Livello 3: Casi Limite & Condizioni Estreme (Corner Cases, Null & Boundary Values)**:
     * Stress-test su valori zero, quantità unitarie ($T=1$), collezioni vuote ($N=0$), stringhe non tradotte, buffer overflow o timeout.

3. **Formattazione Standard Lineare per NVDA**:
   - Ciascuna simulazione deve essere redatta con lo schema sequenziale:
     * *Stato Iniziale / Input*: [Parametri e contesto]
     * *Flusso Esecutivo ("Se... Allora")*: [Regola logica]
     * *Output Prodotto & Riscontro Vocale*: [Cosa vocalizza lo screen reader]
     * *Esito*: `[Conforme / Fallback Protetto]`

---

## 🛡️ 5. PROTOCOLLO DI NON-REGRESSIONE E ROLLBACK AUTOMATICO POST-BONIFICA (PROTOCOLLO 11)

1. **La Doppia Barriera di Verifica Post-Pulizia**:
   - Subito dopo l'applicazione di una bonifica di codice o asset approvata da Luca, l'assistente esegue tassativamente la sequenza di verifica:
     1. *Compilazione Pulita*: Esecuzione di `gradle build --no-daemon`, `dotnet build` o controllo di sintassi Python per intercettare errori di compilazione;
     2. *Suite Test Automatici*: Esecuzione dei test unitari e di integrazione (`pytest`, test di modulo) per verificare l'integrità dei flussi funzionali.
2. **Clausola di Rollback Automatico Istantaneo**:
   - *Se* la build fallisce o un solo test non passa -> *Allora* l'assistente **annulla immediatamente la modifica (Rollback automatico via Git o Quarantena)**, ripristina lo stato precedente e notifica a Luca l'esatto componente che ha causato la regressione.
   - *Se* i test hanno esito positivo al 100% -> *Allora* rilascia l'artefatto per il collaudo e registra l'intervento nel `CHANGELOG.md` sotto `⚙️ Modifiche & Refactoring`.
3. **Ispezione Dinamica Retroattiva**:
   - Qualsiasi elemento che dovesse fallire a runtime a causa di una chiamata implicita (Reflection o string lookup) viene registrato come `[RIFERIMENTO DINAMICO PERENNE]` e protetto in modo permanente da future campagne di bonifica.

---

## ⏱️ 6. DETERMINISMO TEMPORALE & INIEZIONE DI CLOCK VIRTUALE NEI TEST CON CONTRATTI TTL

1. **La Discrepanza Temporale Virtuale vs Reale**:
   - Quando si testano code con scadenze temporali (TTL, debounce, finestre di soppressione o scudi a tempo), l'uso implicito di `System.currentTimeMillis()` nei costruttori o nelle factory produce eventi con timestamp reale ($t \approx 1.7 \times 10^{12}$).
   - Se il test controlla il flusso del tempo simulando un clock virtuale (es. `now = 10000`), il calcolo della scadenza `isExpired` (`now - timestamp >= ttl`) produce numeri negativi enormi, rendendo i test temporali inaffidabili o fragili.
2. **Lo Standard di Iniezione dei Time Seams**:
   - **Contratti Sovraccaricati**: Ogni metodo che accetta entità temporizzate deve offrire un sovraccarico con parametro esplicito: `submit(item, timestamp)` o `flush(now)`.
   - **Fornitori di Tempo Sostituibili (Time Seams)**: Le classi che calcolano scadenze interne devono esporre fornitori di tempo iniettabili (es. `LongSupplier timeSupplier = System::currentTimeMillis;` con visibilità package-private per i test).
   - **Coerenza del Clock nei Test**: Nei test unitari, la creazione dell'oggetto, l'avanzamento del tempo e il controllo di scadenza devono attingere rigorosamente alla medesima sorgente temporale virtuale controllata (es. `AtomicLong simulatedTime = new AtomicLong(10000)`), garantendo test a 0 ms deterministici, privi di `Thread.sleep` e riproducibili al 100%.

---

## 🎯 7. LA TRIANGOLAZIONE EMPIRICA A TRE FONTI PER LA CONVALIDA FINALE (TEST + TELEMETRIA + PERSISTENZA)

1. **Il Limite del Test Singolo**:
   - I test unitari certificano la logica interna ma non la percezione d'uso; la telemetria dal vivo certifica ciò che viene inviato al canale sensoriale ma non garantisce che il motore applicativo abbia persistito lo stato; l'ispezione postuma dei dati non rivela la reattività o i tempi percepiti dall'utente.
2. **La Triangolazione a Tre Fonti**:
   - Nelle applicazioni interattive o accessibili per non vedenti, una feature o un refactor complesso si considerano convalidati in modo definitivo solo quando convergono tre fonti indipendenti:
     1. *Fonte 1 — Test Automatici Headless*: suite unitaria verde a 0 ms che valida contratti, contratti TTL, code e invarianti logiche;
     2. *Fonte 2 — Telemetria Live & Logging di Runtime*: tracciamento in tempo reale degli eventi vocalizzati, dello scudo interruttivo (`interrupt: true` vs `interrupt: false`) e dell'assenza di eccezioni o warning anomali;
     3. *Fonte 3 — Persistenza Dati su Disco*: riscontro forense sui file di stato, database o salvataggi (es. file di configurazione, statistiche, database locale), confermando che ogni operazione percepita e vocalizzata corrisponde a una mutazione deterministica registrata su disco.

---

## 🗺️ 8. DIAGNOSI FORENSE NEI GRAFI DI NAVIGAZIONE E PATHFINDING (A* / DIJKSTRA)

1. **La Trappola del Budget vs Connettività Topologica**:
   - Quando un algoritmo di ricerca percorso (A*, Dijkstra o BFS) restituisce fallimento (`NO_PATH`), non cedere alla tentazione ingenua di incrementare i limiti computazionali (es. raddoppiare il budget dei nodi espansi da 2.500 a 5.000 o 10.000).
   - Un aumento del budget è utile **unicamente** se il fallimento si manifesta per esaurimento del budget (`SEARCH_BUDGET_EXHAUSTED`) e l'open-set contiene ancora nodi promettenti in espansione verso la meta attraverso varchi aperti complessi.
2. **La Discriminante dell'Open-Set a Pochi Nodi**:
   - *Se* la ricerca termina con `NO_PATH` avendo esplorato una quantità esigua di nodi (es. poche decine o centinaia) in una stanza o corridoio ristretto;
   - *Allora* la causa è matematicamente e tassativamente **un arco mancante o bloccato nel grafo topologico** tra due nodi contigui.
   - Indagare immediatamente le funzioni di transizione geometrica (`isPassable`, `isClearHeadroom`, `isStandable`, `isSolid`) e le collision box dei blocchi o elementi decorativi presenti sulla soglia critica (es. scale a pioli, cartelli, torce, stipiti o mezze altezze).
3. **Clearance Volumetrica Multi-Punto per Entità Verticali**:
   - Nei motori a griglia o voxel in cui le entità superano l'unità di blocco ($H > 1.0\text{ m}$), ogni verifica di percorribilità, transizione o rischio caduta non deve mai limitarsi al solo piano di appoggio ($Y$).
   - Verificare obbligatoriamente l'intero volume della hitbox: se la cella a quota testa/occhi ($Y+1 \dots Y+H$) è occlusa da solidi o soffitti bassi, il passaggio fisico è precluso e l'allarme inferiore deve essere scartato come non percorribile.

---

## 🛡️ 9. DISCIPLINA DI VISIBILITÀ DEI TEST SEAMS & GERARCHIA DI ACCESSO

1. **Il Principio di Non-Invasività dei Test sull'Incapsulamento**:
   - La necessità di eseguire test unitari headless non costituisce mai, di per sé, una giustificazione valida per aprire indiscriminatamente la visibilità (`public`) di componenti, classi o adapter interni di produzione.
   - È vietato introdurre la regola o la prassi secondo cui un adapter debba diventare pubblico con il solo fine di agevolare un test.

2. **Ordine di Preferenza Obbligatorio (I 5 Livelli di Accesso)**:
   Nell'ordine tassativo dal più restrittivo al meno restrittivo:
   - *Livello 1 (Entry Point Produttivo)*: Verificare e validare il comportamento attraverso l'entry point produttivo già esistente;
   - *Livello 2 (Collocazione Same-Package)*: Collocare la classe di test nello stesso package del componente di produzione quando è sufficiente l'accesso package-private;
   - *Livello 3 (Seam Package-Private Estratto)*: Estrarre una factory o un seam package-private condiviso dedicato;
   - *Livello 4 (Visibilità Protetta)*: Utilizzare una visibilità protetta (`protected`) soltanto quando coerente con l'architettura a oggetti;
   - *Livello 5 (Visibilità Pubblica come Contratto Produttivo)*: Rendere un componente o adapter `public` SOLO SE costituisce un vero contratto produttivo destinato anche a consumatori esterni al package.

3. **Governo delle Deroghe Locali**:
   - Le deroghe locali devono essere formalmente autorizzate e registrate nella documentazione di progetto; non costituiscono precedenti universali e non devono essere elevate a standard globale.

---

## 🔬 10. METODOLOGIA FORENSE AVANZATA: TASSONOMIA PROBATORIA, ISOLAMENTO CAUSALE & RISALITA A MONTE

Nelle fasi di diagnosi ostica, troubleshooting, calibrazione quantitativa e refactoring di sistemi complessi:

1. **La Tassonomia a 7 Stati Probatori (Superamento del Binomio PASS/FAIL)**:
   - È vietato appiattire l'esito di un collaudo o di un'analisi sul semplice binomio ingenuo `PASS` vs `FAIL`.
   - La valutazione adotta sette stati formali. I primi quattro possono descrivere un avanzamento di evidenza, `FAIL` e `PARTIAL` sono rami diagnostici, mentre il passaggio empirico è il gate conclusivo quando applicabile:
     1. `THEORETICAL PASS`: Validazione puramente analitica e concettuale nel Piano Tecnico (coerenza logica, assenza di contraddizioni teoriche);
     2. `PASS STATICO`: Conformità del codice sorgente verificata staticamente (diff pulito, bilanciamento parentesi/costrutti, assenza di warning o errori dei tipi);
     3. `PASS HEADLESS`: Suite automatica pertinente superata in ambiente headless isolato, con dipendenze controllate e tempi di esecuzione effettivi;
     4. `OBSERVED / INSTRUMENTED`: Telemetria passiva attiva che misura parametri e transizioni oggettive sul flusso reale; attesta che la via di comunicazione è aperta, ma non costituisce ancora una feature convalidata;
     5. `FAIL AL GATE D'INGRESSO`: Il componente o l'attuatore non è fallito nella sua logica, ma è stato respinto o invalidato a monte da una guardia d'ingresso non soddisfatta (es. contesto modale, stringa evento mancante, permesso assente);
     6. `PARTIAL-GAIN / PARTIAL-CADENCE`: Il flusso raggiunge l'attuatore e produce un effetto misurabile, ma ampiezza o frequenza restano insufficienti. Integrità della memoria, completezza logica e assenza di regressioni richiedono prove distinte e non sono implicate automaticamente;
     7. `FULL EMPIRICAL PASS`: Convalida completa sul campo con percezione reale, verifica dell'integrità dello stato persistito e riscontro positivo confermato dall'utente.

2. **Il Canone della Singola Variabile Causale (Single-Cause Discipline)**:
   - In fase di debug, tuning o rettifica correttiva, è fatto divieto di mutare contemporaneamente due o più grandezze comportamentali indipendenti.
   - Ogni iterazione sperimentale o proposta di modifica deve variare **una e una sola causa da falsificare**:
     * *Se* si calibra un valore numerico/guadagno, *allora* non si toccano l'hook, l'ordine dei gestori o le strutture dati;
     * *Se* si modifica una guardia di ammissione, *allora* non si alterano i moltiplicatori o l'attuatore.
   - Telemetria passiva, logging a transizioni e guardie fail-closed possono accompagnare il test se non cambiano l'esito funzionale. L'isolamento riguarda la causa comportamentale, non gli strumenti necessari per osservarla in sicurezza.

3. **Il Principio di Risalita a Monte della Causa Radice (Upstream Flow vs Downstream Symptom-Patching)**:
   - Quando un componente a valle fallisce, viene rifiutato o non risponde, non creare protesi, wrapper o bypass artificiali a valle per forzarne l'esecuzione.
   - Risalire sistematicamente la catena di propagazione fino al punto che possiede davvero filtri, ordine, scale utente e controlli di stato. Se tale proprietà resta nel dispatcher, usare un innesto pre-dispatcher; se un'API documentata assegna esplicitamente la proprietà al gestore finale, l'ingresso diretto è ammesso purché motivato e verificato. Il pre-dispatch è una conseguenza della proprietà del flusso, non un obbligo universale.

   - Ricostruire ingresso, dispatcher, gestori ed esito; indicare evidenza, componente proprietario e invariante violata. Scegliere il cambiamento minimo che elimina stabilmente la causa e ripetere la riproduzione, includendo chiamanti, priorità, eventi e ciclo di vita interessati.
   - Un adattatore necessario a un confine reale è legittimo con contratto e responsabilità espliciti. Se il difetto è locale, correggerlo localmente senza migrazione architetturale; se la causa è ignota, raccogliere prove prima di prescrivere una ristrutturazione.

4. **Sovranità del Ciclo di Vita della Memoria (Le 5 Fasi di Lifespan a Basso Livello)**:
   - Nei linguaggi e runtime di sistema (C++, Rust, wrapper nativi), distinguere rigorosamente le 5 fasi del ciclo di vita per prevenire leak silenti di contatori di riferimenti o pool condivise:
     1. *Allocazione*: Acquisizione della memoria grezza tramite l'allocatore specifico dell'host (`malloc_runtime`);
     2. *Inizializzazione*: Distinguere il posizionamento della vtable dalla costruzione C++. Costruire con `std::construct_at` soltanto l'oggetto completo se il relativo costruttore è realmente disponibile e previsto; altrimenti costruire esclusivamente i sottoggetti non banali effettivamente gestiti;
     3. *Transito*: Utilizzo e passaggio dell'oggetto nel canale di elaborazione;
     4. *Distruzione Simmetrica*: Invocare `std::destroy_at` esclusivamente sugli oggetti o sottoggetti realmente costruiti, in ordine compatibile con l'inizializzazione, prima del rilascio;
     5. *Deallocazione*: Restituzione della memoria grezza all'allocatore dell'host (`free`).

---

## 👁️ 11. DIAGNOSI FORENSE DEI FALLIMENTI SILENTI DI AVVIO PROCESSO & GESTIONE DEL FOCUS NEI CICLI DI VITA ASINCRONI

1. **La Diagnosi a Tre Canali per Crash Silenti a 0 ms (Kernel Code Integrity)**:
   - *Sintomo*: L'applicazione host o il gioco si chiude istantaneamente all'avvio. La DLL o il modulo iniettato non crea il file di log locale (`debug.log`), né il registro eventi standard (`Application` / `System`) riporta errori.
   - *Flusso Forense Obbligatorio*:
     * Canale 1: Verifica dello stato dei servizi di sicurezza Windows (`Get-MpComputerStatus`, `SmartAppControlState`).
     * Canale 2: Interrogazione del registro di sicurezza del kernel specializzato `Microsoft-Windows-CodeIntegrity/Operational` tramite PowerShell:
       `Get-WinEvent -LogName "Microsoft-Windows-CodeIntegrity/Operational" -MaxEvents 20`
     * Canale 3: Risoluzione del codice errore di sistema (es. Event ID 3077/3118 con `WinError 4551` / `ERROR_HVCI_POLICY_VIOLATION`), identificando immediatamente blocchi kernel su binari non firmati prima di ipotizzare errori di codice C++.

2. **L'Anti-Mascheramento Acustico da Finestre Effimere di Bootstrap (Splash & Updater Window Race)**:
   - Nelle applicazioni con scompattamento, launcher o caricamento asincrono, il processo genera frequentemente finestre preliminari transitorie (es. splash screen, finestre di controllo aggiornamenti o controlli licenza) che rimangono visibili per 1-2 secondi prima di distruggersi per cedere il passo alla vera finestra di rendering o interfaccia.
   - *La Trappola del Focus per lo Screen Reader*: Se il modulo di accessibilità o la mod intercetta e associa la prima finestra visibile del PID inviando un comando vocale (es. `Speak()`), la distruzione improvvisa di quella finestra effimera scatena nel sottosistema Win32 l'evento `EVENT_SYSTEM_FOREGROUND`.
   - Lo screen reader (NVDA, JAWS), ricevendo il cambio di focus forzato verso il desktop o la nuova finestra, cancella immediatamente il proprio buffer di sintesi vocale in corso per inseguire il nuovo focus, lasciando l'utente in un silenzio ingannevole nonostante il codice abbia eseguito la chiamata con successo (`return 0`).
   - *Canone Architetturale di Filtro e Stabilizzazione Finestra*:
     * *Filtro Semantico e Dimensionale*: Durante l'enumerazione finestre (`EnumWindows`), scartare tassativamente finestre con parole chiave transitorie nel titolo (es. "aggiornament", "update", "splash") e imporre un vincolo sulle dimensioni minime dell'area client (es. almeno 600x400 pixel) per escludere popup di servizio;
     * *Finestra di Stabilizzazione Post-Aggancio*: Dopo l'individuazione della finestra reale dell'engine, attendere un intervallo di assestamento (1.0 - 1.5 secondi) prima di emettere earcon sonori o vocalizzazioni, garantendo che Windows abbia completato il transito di focus e che la voce dello screen reader risuoni forte, chiara e ininterrotta.

---

## ⚡ 12. DETERMINISMO DI SEGNALE NEI TEST HEADLESS: CLOSURE CONTAINER PATTERN & LIFECYCLE GUARDS

1. **La Trappola della Cattura Scalare per Valore nelle Chiusure (Closure Rebinding)**:
   - *Problema*: Nei linguaggi con chiusure e funzioni anonime (GDScript 4, Python, Lua, delegate), quando si collega un evento o segnale a una lambda per intercettare il payload (es. `obj.signal.connect(func(val): result = val)` con `var result = null`), la chiusura cattura la variabile scalare o il riferimento nullo *per valore*, riassociando (`rebind`) esclusivamente la copia interna dello stack frame della closure. La variabile esterna nello scope della funzione di test rimane inalterata (`null`), provocando falsi negativi sistematici nei test seams.
   - *Canone Universale: Closure Container Pattern*:
     * Non assegnare mai direttamente a scalari o riferimenti nulli dentro la lambda di test.
     * Utilizzare categoricamente un contenitore allocato per riferimento (Array, Lista, Dizionario) presente nello scope del test:
       `var received: Array = []`
       `obj.signal.connect(func(arg): received.append(arg))`
     * Verificare deterministically la presenza dell'evento (`received.size() > 0`) e il payload contenuto (`received[0]`). L'oggetto mutabile conserva le modifiche nello scope esterno senza dipendere da semantiche di scoping per valore.

2. **La Doppia Invocazione di Lifecycle nei Nodi UI e Guardie `is_connected()`**:
   - *Problema*: Nei motori a grafo di nodi (Godot Engine, framework GUI ad albero), l'inserimento di un componente istanziato (`add_child(inst)`) all'interno dell'hook di bootstrap di un runner già attivo scatena immediatamente e in modo sincrono il ciclo di vita del figlio (`_ready()`). Se il test runner invoca poi manualmente una seconda volta `inst._ready()`, si scatenano doppie registrazioni di ascoltatori o eccezioni bloccanti del motore (`Signal already connected`).
   - *Canone Architetturale*:
     * Nei nodi dell'interfaccia, proteggere sempre le connessioni di callback con guardie di idempotenza:
       `if btn and not btn.pressed.is_connected(_handler): btn.pressed.connect(_handler)`
     * Nei test runner headless, affidarsi unicamente al ciclo di vita scatenato dall'inserimento nell'albero (`add_child()`), evitando invocazioni ridondanti dei metodi di bootstrap interni dell'engine.

---

## 🎯 13. PRE-FLIGHT MARGINING PATTERN PER ASSERZIONI SU RISORSE CLAMPED A SOGLIA ZERO

1. **La Trappola del Clamping Inferiore nelle Sequenze di Test Concatenate**:
   - *Problema*: Nei simulatori e nei videogiochi, molte risorse vitali o operative (stress, fatica, salute, punti danno, fondi di riserva) sono soggette a vincoli matematici di saturazione o clamping rigido (es. `stress = maxf(0.0, stress - delta)`).
   - Quando una suite di test testa in sequenza molteplici scenari o eventi (es. bivi decisionali a catena, scelte multiple, abilità di cura), uno scenario precedente può ridurre la risorsa portandola esattamente al limite di clamping (`0.0`).
   - Se il test dello scenario successivo tenta di verificare l'efficacia di un'ulteriore riduzione (es. `assert_true(risorsa < pre_risorsa)`), l'asserzione fallisce categoricamente: la risorsa, essendo già ancorata al minimo, non può decrescere ulteriormente, generando un falso negativo fuorviante.

2. **Canone di Marginatura Pre-Test (Pre-Flight Margining)**:
   - Prima di esercitare un'azione o un evento che deve produrre un delta negativo su una risorsa saturabile, il test runner deve obbligatoriamente iniettare un margine di tolleranza dinamico noto nello stato del modello (es. `player.stress = 30.0` prima dell'evento di defaticamento o cura).
   - Questo garantisce che la metrica si trovi sempre all'interno della propria regione dinamica non satura, consentendo una misurazione matematica esatta e deterministica del delta senza collisioni con i morsetti di clamping.

---

## 🔬 14. CUMULATIVITÀ DEI MODIFICATORI IN TRANSAZIONI MULTI-FATTORE E GUARDIE DI CALENDARIO PREVENTIVE

1. **La Cumulatività Additiva di Più Sottosistemi Concorrenti**:
   - *Problema*: Nei simulatori articolati, una singola azione o risoluzione di evento (es. un concerto, una battaglia campale, un turno di gestione) può coinvolgere contemporaneamente più logiche indipendenti che alterano la medesima variabile di stato (es. la tipologia di palco che rilassa la band con `-10` tensione, sommata alla vittoria su una rivale che distende ulteriormente con `-15` tensione).
   - Se il test è progettato verificando unicamente uno dei due effetti (aspettandosi un valore finale calcolato solo sul primo delta), oppure se la somma combinata supera la riserva disponibile saturando a `0.0` per clamping, il test fallisce generando un falso negativo.
   - *Canone Architetturale*:
     * Quando si testano transazioni che coinvolgono molteplici sottosistemi, il valore iniziale deve essere calibrato tenendo conto della *somma algebrica cumulativa di tutti i delta attesi* (`valore_iniziale >= delta_1 + delta_2 + margine`).
     * L'asserzione deve verificare deterministically l'effetto combinato di tutti i componenti intervenuti nella transazione.

2. **Sincronizzazione Temporale Preventiva nei Mock di Calendario**:
   - *Problema*: I metodi di dominio che governano eventi vincolati a date fisse del calendario (es. festival estivi, tornei stagionali, date di consegna album) implementano guardie reattive rigide del tipo `if event.day < current_day: return false / "event_already_passed"`.
   - Se in un test runner la data del mock del calendario viene lasciata al valore di un test precedente o avanzata oltre la data dell'evento (es. `calendar.day = 153` per un evento previsto al giorno `104`), la richiesta di iscrizione o prenotazione viene respinta a monte. I passi successivi del test falliscono a cascata sollevando eccezioni del tipo `key not found` o `invalid access on Nil`.
   - *Canone Architetturale*:
     * Prima di esercitare qualsiasi contratto di prenotazione o candidatura ad eventi di calendario, il test runner deve obbligatoriamente allineare lo stato del calendario a una data *strettamente antecedente o coincidente* (`calendar.day <= event.day`).
     * In questo modo le guardie temporali del dominio risultano soddisfatte in modo deterministico, consentendo al flusso del test di raggiungere ed esercitare i rami logici interni della transazione.

---

## 📡 15. DISACCOPPIAMENTO DI TIPO NEGLI EVENTBUS GLOBALI & DIPENDENZE CIRCOLARI AL BOOTSTRAP

1. **La Trappola del Type Pinning negli Autoload di Sistema**:
   - *Problema*: Nei linguaggi e runtime ad albero o con moduli globali (es. Autoload in Godot Engine, moduli singleton in framework a iniezione di dipendenze), i bus degli eventi globali vengono inizializzati ed esaminati dal compilatore prima o parallelamente alla scansione e indicizzazione delle classi del modello di dominio.
   - Se la firma di un segnale o evento dichiara esplicitamente un tipo forte derivato da un modello custom (`signal entita_creata(dati: CustomDataClass)`), si crea una dipendenza circolare di bootstrap: l'Autoload cerca di risolvere una classe che il registro dei tipi non ha ancora consolidato, scatenando errori di parse (`Could not find type in current scope`) e impedendo il boot dell'engine o l'avvio della suite headless.
   - *Canone Universale*:
     * Nelle interfacce di broadcast universali (EventBus, Messaggerie globali), tipizzare i payload dei segnali con tipi base polimorfici nativi del runtime (`RefCounted`, `Resource`, `Object`, `Dictionary`).
     * Conservare la tipizzazione forte, sicura ed esplicita all'interno dei sottosistemi e dei controller riceventi, delegando all'EventBus la sola funzione pura di canale di transito agnostico.

---

## 🔄 16. CANONE DI REFRESH PREVENTIVO DELLA CLASS CACHE PER SCRIPT INTRODOTTI IN MODALITÀ HEADLESS

1. **La Discrepanza tra Runtime Headless e Indicizzatore dell'Editor**:
   - *Problema*: Nei motori moderni (Godot Engine 4.x), la dichiarazione di nuove classi globali (`class_name NomeClasse`) viene registrata in un file di cache centralizzato (`.godot/global_script_class_cache.cfg`).
   - L'editor visivo rigenera tale cache istantaneamente all'atto del salvataggio su disco; al contrario, l'esecuzione di test headless da riga di comando (`--headless res://...`) presuppone che la cache sia già valida e non ne forza la scansione automatica. L'aggiunta di una nuova classe pura via script provoca quindi fallimenti immediati di tipo `Identifier not found` nei test.
   - *Canone Architetturale*:
     * Quando un flusso di automazione, agente AI o script di build introduce un nuovo file con dichiarazione `class_name`, è obbligatorio eseguire un comando di bootstrap preventivo rapido e non interattivo:
       `godot --headless --path . --editor --quit`
     * Questa invocazione comanda all'editor di avviare il motore in background, effettuare la scansione delle classi globali, sincronizzare il file di cache e terminare in pochi millisecondi con codice di uscita 0, garantendo il 100% di determinismo per tutte le successive suite headless.

---

## 🧩 17. PATTERN DI PRELOAD SCRIPT DECOUPLING NEI CONTROLLER UI E CONSUMER RUNTIME

1. **La Fragilità del Type Pinning Statico su Classi Introdotte Dinamicamente**:
   - *Problema*: Nei linguaggi con compilazione Just-In-Time o a caricamento dinamico (come GDScript 4), i controller dell'interfaccia utente o i consumer di modelli runtime che annotano parametri o variabili locali con classi custom (es. `var x: NuovaClasse` o `func ricevi(dati: NuovaClasse)`) rischiano di fallire in fase di parsing/compilazione se l'albero delle classi non è stato preventivamente indicizzato o se il controller viene analizzato dall'engine prima della registrazione del tipo globale.
   - *Canone Universale*:
     * Nei controller dell'interfaccia utente (`ui/`) e nei moduli consumatori di runtime, disaccoppiare i tipi statici importando esplicitamente la risorsa tramite costante:
       `const NuovaClasseScript = preload("res://data/models/nuova_classe.gd")`
     * Tipizzare i parametri di ricezione o le variabili con la classe base polimorfica nativa del runtime (`RefCounted`, `Resource`) oppure sfruttare il duck typing strutturato.
     * Questo approccio elimina qualsiasi dipendenza d'ordine tra la compilazione dei controlli visivi e l'indicizzazione dei dati, garantendo resilienza totale durante sessioni continuative di sviluppo headless.

---

## 💰 18. GUARDIE DI SOLVIBILITÀ REATTIVA SULLE TRANSAZIONI ONEROSE DI DISTACCO O RESCISSIONE

1. **La Trappola della Rescissione Incondizionata nei Sistemi Economici**:
   - *Problema*: Nei simulatori economici, di carriera o di gestione risorse, le azioni di rottura contrattuale, rescissione o licenziamento (es. penale di rescissione del manager, clausole rescissorie sportive, buyout di accordi) comportano spesso una penale finanziaria a carico del giocatore. Se il sistema esegue lo sgancio del record o la transizione di stato prima di verificare la capienza del saldo o senza bloccare la transazione in caso di fondi insufficienti, si generano exploit di debiti negativi o inconsistenza tra modello contrattuale e bilancio.
   - *Canone Universale*:
     * Ogni transazione di gioco soggetta a penali o costi di liquidazione deve implementare una guardia preventiva reattiva:
       `if player.liquid_funds < severance_penalty: return { "success": false, "reason": "Fondi insufficienti per saldare la penale..." }`
     * La rottura del vincolo relazionale o contrattuale deve essere atomicamente subordinata all'effettivo addebito finanziario, prevenendo transizioni di stato illegali e debiti occulti non tracciati.
---

## 🛡️ 19. PROTOCOLLO DI ISOLAMENTO DELLE PROPRIETÀ DI DOMINIO NEI MOCK DI TEST (FIELD INVARIANT GUARDS)

1. **La Trappola degli Alias e dei Mutatori Fittizi nei Test Runner Headless**:
   - *Problema*: Durante la stesura rapida di suite di test o fixture di simulazione, gli sviluppatori o gli agenti AI tendono a creare oggetti di prova o accedere alle entità di dominio presumendo l'esistenza di proprietà arbitrarie o scorciatoie (es. assegnare `song.streams` o `rival.name = "X"` quando il modello dichiara formalmente `total_streams` o `rival_name`).
   - Nei linguaggi dinamici o con duck typing permissivo, tale assegnazione può non sollevare eccezioni immediate ma creare campi orfani ignorati dalla logica di dominio reale; al contrario, nei linguaggi e runtime a tipizzazione forte (GDScript 2.0 statico, TypeScript strict, C++, Rust), l'accesso a un identificatore inesistente scatena errori fatali di parsing o interruzioni immediate del runner di test (`Invalid set index 'streams' on base 'SongData'`).

2. **Canone Architetturale per la Rigorosa Conformità dei Test**:
   - **Ispezione Deterministica del Modello di Verità**:
     * Prima di manipolare o asserire proprietà su istanze del dominio in una nuova suite di test, verificare la definizione esatta della classe dati (campi esportati `@export`, tipi statici, costruttori e metodi canonici).
   - **Costruzione via Metodi di Dominio o Setter Canonici**:
     * Evitare manipolazioni invasive ad-hoc con proprietà non documentate. Se un'entità espone metodi di business logic o factory (es. `rival.log_dissing()`, `chart.register_play()`), impiegare prioritariamente l'API ufficiale del dominio.
   - **Invariante di Parità Test-Runtime**:
     * Nessun test deve utilizzare contratti più deboli, alias o mock non conformi al modello dati persistito e utilizzato a runtime dal gioco reale. Se il test richiede un campo ausiliario, esso deve essere promosso formalmente nel modello dati o documentato come transitorio.


---

## 🏛️ 20. INVARIANTE DI ESPANSIONE DEI CATALOGHI DI DOMINIO & REGRESSION BOUNDARIES

1. **La Fragilità delle Asserzioni Scalari Rigide su Cataloghi Evolutivi**:
   - *Problema*: Nei simulatori e motori di gioco modulari che implementano cataloghi di entità espandibili (locali, stadi, città, abilità, tratti, oggetti di scena, veicoli), le suite di test storiche tendono a verificare il caricamento del catalogo di default mediante asserzioni di uguaglianza numerica fissa (`assert_eq(catalog.size(), N)`). Quando una fase successiva o una milestone di espansione (es. Endgame con mega-stadi e palasport) arricchisce legittimamente il catalogo di dominio, queste asserzioni storiche falliscono immediatamente, generando falsi positivi di regressione pur in presenza di totale retrocompatibilità funzionale.
   - *Canone Universale*:
     * **Divieto di Dimensionamento Scalare Rigido Cablato**: Non cablare mai numeri magici scalari hardcoded nelle asserzioni di test che verificano collezioni di dominio intrinsecamente espandibili per design evolutivo.
     * **Centralizzazione delle Costanti di Baseline**: Quando il conteggio esatto è richiesto per validare il bootstrap starter, riferirsi sempre a una costante centralizzata del dominio (`Constants.DEFAULT_VENUES_COUNT`) anziché a un valore numerico locale nel test.
     * **Invarianti di Soglia Minima e Verifica Puntuale degli ID Chiave**: Nelle suite storiche volte a prevenire regressioni, verificare prioritariamente un confine inferiore (`assert(catalog.size() >= MINIMUM_COUNT)`) e la presenza/integrità dei record storici fondamentali (`assert(catalog.has("id_chiave"))`), garantendo che l'introduzione di nuovi record non rompa la suite di sicurezza del progetto.

---

## ⏱️ 21. TEST SEAMS DETERMINISTICI CON OVERRIDE DI STATO SU SISTEMI ACCOPPIATI AL CALENDARIO PROCEDURALE

1. **L'Intermittenza nei Test Headless di Logiche Concorrenti Accoppiate al Tempo**:
   - *Problema*: Nei simulatori di vita e gestionali dove la disponibilità di risorse condivise, locali, slot orari o eventi concorrenti viene risolta tramite algoritmi procedurali accoppiati al calendario (es. funzioni hash `day_number % X` o disponibilità pseudo-randomica per simulare il mercato), le suite di test headless a 0 ms possono subire fallimenti intermittenti (flaky tests). Se una data virtuale non specificata o calcolata dinamicamente collide con una giornata di occupazione procedurale, la transazione viene rifiutata (es. `venue_occupied`), provocando il fallimento delle asserzioni dell'happy path.
   - *Canone Universale*:
     * **Esposizione di Test Seams Deterministici**: Ogni sottosistema che governa la disponibilità di risorse mediante algoritmi procedurali tempo-dipendenti deve esporre un metodo esplicito di override per il testing (es. `set_venue_status_override(id, day, status)` o un mock provider di disponibilità).
     * **Isolamento Deterministico nei Test Harness**: Prima di invocare metodi transazionali ad alto impatto (es. `resolve_concert()`), la suite di test deve forzare esplicitamente la disponibilità della risorsa sulla data target mediante il test seam dedicato, garantendo determinismo assoluto al 100% senza alterare artificiosamente l'orologio globale né introdurre attese asincrone o dipendenze temporali.


---

## 🌐 22. INVARIANTE TOPOLOGICO NEI GRAFI DI RETE & PARAMETRIZZAZIONE DINAMICA DELLE ASSERZIONI DI DIFFUSIONE (GRAPH SPREAD INVARIANT)

1. **La Fragilità delle Asserzioni di Diffusione su Topologie di Rete Evolutive**:
   - *Problema*: Nei simulatori e nei sistemi ad agenti con propagazione distribuita su grafi (città, mercati territoriali, nodi di rete, follower, entità concorrenti), gli algoritmi allocano comunemente una quota primaria al nodo focale dell'azione ($P$) e una quota marginale di riverbero a ciascuno degli altri nodi della topologia:
     $$\text{Spread Totale} = P + (N - 1) \times \Delta$$
     dove $N$ è la cardinalità corrente del grafo e $\Delta$ è l'incremento unitario per nodo.
   - Quando la scala del dominio viene espansa (ad esempio espansione da 12 a 16 metropoli mondiali), la somma cumulativa generata scala algebricamente con $N$. Se le suite di test storiche verificano il totale aggregato con un'asserzione scalare rigida cablata a mano sul vecchio set (es. `assert_eq(total, 196)` per $N = 12$), l'espansione fisiologica e backward-compatible del grafo scatena un falso allarme di regressione ($200 \neq 196$), pur in presenza di totale correttezza algoritmica.

2. **Canone Universale di Parametrizzazione Dinamica**:
   - **Divieto di Costanti Scalari Hardcoded su Somme di Rete**: Non calcolare mai a mano nei test runner il valore aggregato complessivo generato su un grafo ignorando la cardinalità dinamica del set di nodi.
   - **Formule Attese Funzionali alla Dimensione del Dominio**:
     Nelle asserzioni di test, parametrizzare sempre la quota aggregata sulla dimensione effettiva della collezione o dell'enumerazione di dominio:
     `var expected_total = initial_amount + local_part + ((nodes.size() - 1) * per_node_delta)`
     oppure verificare separatamente due invarianti ortogonali:
     1. *Invariante Locale*: il nodo focale riceve esattamente la quota primaria $P$;
     2. *Invariante di Riverbero*: ciascun nodo del complementare riceve esattamente $\Delta$.
   - **Preservazione della Scalabilità Architetturale**: L'adozione di formule parametriche garantisce che future espansioni della rete geografica o topologica non richiedano alcun refactoring delle suite di sicurezza e regression testing preesistenti.
