# Standard di Tassonomia Documentale e Auto-Deduzione ASTRALIS
# Autore: Luca (Sviluppatore Senior Non Vedente con Screen Reader NVDA)
# Target AI: Antigravity, GPT/Codex e Collaboratori AI autorizzati
# Ambito: Governance locale della macchina
# Framework: ASTRALIS v3.0.5
# Master Hub: <astralis-hub>

Questa scheda è la fonte normativa unica per la tassonomia comune dei documenti operativi ASTRALIS. Definisce tipi, intenti, metadati, regole di auto-classificazione, ruoli, gating e collegamenti. I template e le schede verticali possono specializzare questi contratti senza ridefinirli o duplicarli.

---

## 🎯 1. Scopo e Ambito

### 1.1 Scopo

Lo standard rende ogni documento operativo riconoscibile, collegabile e verificabile da Luca, Antigravity, GPT/Codex e altri collaboratori autorizzati.

Ogni documento conforme deve permettere di determinare, senza interpretazioni arbitrarie:

- che tipo di documento è;
- quale risultato operativo persegue;
- quale ambito copre;
- quale stato ha il documento;
- quale stato ha il lavoro descritto;
- chi partecipa e con quale ruolo;
- quale gate operativo è vigente;
- quali fonti, evidenze e documenti sono collegati;
- quando è stato aggiornato l'ultima volta.

### 1.2 Ambito locale blindato

Questo standard governa esclusivamente l'ecosistema locale ASTRALIS della macchina di Luca e i progetti locali che lo ereditano tramite un puntatore esplicito.

- Se un documento appartiene al Master Hub locale, allora può applicare direttamente questo standard.
- Se un documento appartiene a un progetto locale, allora applica questo standard tramite il proprio router o modulo normativo.
- Se un artefatto è destinato a un repository pubblico o distribuibile, allora non eredita automaticamente percorsi, profili, ruoli personali o regole private contenuti in questa scheda.
- Se si propone un'esportazione verso un repository pubblico, allora serve una valutazione separata e un'autorizzazione esplicita di Luca.

Il repository pubblico o distribuibile `astralis-framework` è fuori dall'ambito di questa adozione locale. La presente scheda non autorizza modifiche, esportazioni o pull request verso tale repository.

### 1.3 Rete flessibile a cinque nodi

La rete documentale operativa comprende cinque tipi comunicanti:

1. `IDEA-RFC`;
2. `STRATEGIA`;
3. `PIANO-TECNICO`;
4. `REPORT`;
5. `VOCE-RRU`.

Il percorso ordinario può procedere da Idea/RFC a Strategia, Piano Tecnico, Report e Voce RRU, ma non costituisce una pipeline obbligatoria.

- Se un nodo non produce valore informativo o operativo, allora non deve essere creato.
- Se un bug nasce durante il runtime, allora può essere aperta direttamente una `VOCE-RRU`.
- Se una correzione è circoscritta e la causa è già verificata, allora la `VOCE-RRU` può generare direttamente un `PIANO-TECNICO` correttivo.
- Se un'Idea/RFC viene respinta, allora può essere annullata o archiviata senza generare una Strategia.
- Se un Report non rileva anomalie, allora non deve generare una Voce RRU.
- Se una Strategia non conduce a un intervento, allora non deve generare un Piano Tecnico.

### 1.4 Documenti infrastrutturali esclusi dalla tassonomia operativa

I router `GEMINI.md`, `AGENTS.md` e analoghi, le schede `knowledge/` e `knowledge/`, i template e gli indici sono infrastruttura normativa. Non devono essere forzati dentro uno dei cinque tipi operativi, salvo che svolgano esplicitamente anche la funzione di Idea/RFC, Strategia, Piano, Report o Voce RRU.

Questa esclusione evita categorie artificiali e permette alla presente scheda di definire la tassonomia senza dover classificare sé stessa come documento operativo.

### 1.5 Assenza di migrazione retroattiva

- Se un documento storico è chiuso o archiviato, allora rimane immutato.
- Se un documento attivo viene aggiornato soltanto per una correzione ortografica o un collegamento, allora non è obbligatoria la conversione della testata.
- Se un documento attivo viene riaperto per una modifica sostanziale, allora adotta la nuova testata nella misura necessaria al lavoro corrente.
- Se viene creato un nuovo documento operativo dopo l'entrata in vigore dello standard, allora deve adottare la Testata Universale Compatta.
- Se occorre allineare template, router o documenti normativi esistenti, allora tale allineamento costituisce una fase separata e richiede il proprio ambito e la propria autorizzazione.

---

## 🧭 2. Vocabolario Controllato

### 2.1 Regole generali del vocabolario

- I valori tassonomici devono essere scritti in maiuscolo come definiti in questa scheda.
- Ogni documento deve avere un solo `Tipo Documento` primario.
- Ogni documento deve avere un solo `Intento Operativo` primario.
- Se sono presenti scopi secondari, allora devono essere spiegati nell'Obiettivo senza creare combinazioni arbitrarie nel campo tassonomico.
- I sinonimi possono essere usati nel testo descrittivo, ma non sostituiscono i valori controllati nella testata.
- `NON DETERMINATO` è un valore temporaneo di fallback e non costituisce un sesto tipo documentale.

### 2.2 I cinque tipi documentali

#### `IDEA-RFC`

Documento precursore che formula un problema, un'opportunità o una proposta e richiede una decisione preliminare. Può confrontare ipotesi iniziali, ma non contiene ancora le invarianti convalidate proprie della Strategia né i passi esecutivi propri del Piano.

#### `STRATEGIA`

Documento di Fase 0 che definisce il modello mentale, analizza ipotesi concorrenti, svolge la dialettica avversariale e congela invarianti concettuali. Le invarianti convalidate saranno trasformate nei Named Contracts del Piano Tecnico.

#### `PIANO-TECNICO`

Documento prescrittivo di Sotto-Fase 1A che traduce requisiti e invarianti in Named Contracts D0..DN e S1..SN, file o componenti coinvolti, verifiche, criteri di accettazione e passi esecutivi. La sua approvazione non autorizza automaticamente l'esecuzione.

#### `REPORT`

Documento descrittivo ed empirico che registra attività, decisioni, risultati, evidenze, verifiche, telemetria, passaggi di consegne o chiusure. Il Report può riferirsi a qualsiasi Intento Operativo e non implica necessariamente che il lavoro sia completato o convalidato.

#### `VOCE-RRU`

Unità atomica del Registro Revisioni Universale. Traccia un'anomalia, un disallineamento, un rischio o un affinamento dalla rilevazione alla verifica e alla chiusura. Il Registro RRU è il contenitore; la singola voce è l'unità classificata.

### 2.3 I sei intenti operativi

#### `INNOVAZIONE`

Introduce o valuta una nuova possibilità, capacità, esperienza, architettura o direzione progettuale non ancora consolidata.

#### `IMPLEMENTAZIONE`

Persegue la realizzazione di una nuova capacità già sufficientemente definita. Si usa quando il risultato richiesto è l'aggiunta concreta di comportamento, configurazione o documentazione operativa.

#### `CORREZIONE`

Persegue il ripristino di un comportamento atteso, la rimozione di un difetto o la correzione di un'incoerenza verificata.

#### `REFACTORING`

Persegue una modifica strutturale, una bonifica o una migrazione controllata preservando le invarianti funzionali dichiarate, salvo variazioni esplicitamente autorizzate.

#### `DIAGNOSI-VERIFICA`

Persegue l'acquisizione di evidenze, l'isolamento di una causa, il confronto tra ipotesi o la verifica di un risultato, senza implicare automaticamente un intervento correttivo.

#### `COORDINAMENTO-CHIUSURA`

Persegue il passaggio di consegne, la sincronizzazione tra partecipanti, la registrazione di una decisione, l'archiviazione o la convalida finale.

### 2.4 Vocabolari ausiliari comuni

#### Esito Classificazione

- `CONFERMATA`: tipo e intento sono dichiarati o dedotti senza ambiguità e soddisfano i campi minimi.
- `PROPOSTA`: tipo e intento sono plausibili, ma attendono la conferma del responsabile decisionale.
- `DA CLASSIFICARE`: mancano evidenze obbligatorie oppure più classificazioni restano compatibili.

#### Stato Documento

- `BOZZA`: contenuto iniziale ancora incompleto.
- `IN REVISIONE`: contenuto completo quanto basta per essere valutato, ma non ancora approvato.
- `APPROVATO`: contenuto documentale convalidato da Luca per lo scopo dichiarato.
- `ANNULLATO`: documento ritirato prima di produrre l'esito previsto.
- `SUPERATO`: documento conservato come riferimento, ma sostituito da una fonte più recente indicata esplicitamente.
- `ARCHIVIATO`: documento collocato nell'archivio previsto dopo la conclusione del proprio ciclo.

#### Stato Lavoro

- `NON APPLICABILE`: il documento non governa né registra un'attività eseguibile.
- `NON AVVIATO`: attività prevista ma non iniziata.
- `IN ESECUZIONE`: attività autorizzata e materialmente in corso.
- `IN VERIFICA`: attività eseguita e sottoposta alle verifiche pertinenti.
- `COMPLETATO`: attività previste terminate; non equivale automaticamente a collaudo o chiusura.
- `SOSPESO`: attività temporaneamente fermata; la motivazione deve essere indicata nel primo blocco operativo.

#### Gate Operativo

- `CONSULTIVO`: sono autorizzate soltanto acquisizione, lettura, analisi e proposta.
- `IN ATTESA DI AUTORIZZAZIONE`: esiste una proposta o un piano pronto, ma l'esecuzione non è autorizzata.
- `ESECUZIONE AUTORIZZATA`: Luca ha impartito un comando esplicito riferito allo specifico oggetto e alla specifica fase.
- `ESECUZIONE CONCLUSA`: le sole attività autorizzate sono state materialmente eseguite; restano separate verifica e convalida.

#### Modalità Operativa

- `SINGOLA`: una sola AI svolge una consultazione o un incarico circoscritto per Luca, senza un secondo collaboratore attivo.
- `PAIR`: Luca e una AI collaborano direttamente allo stesso ciclo di lavoro.
- `TRIADE`: Luca, AI primaria e AI ausiliaria partecipano esplicitamente allo stesso ciclo decisionale.

### 2.5 Categorie tecniche per le Voci RRU

Ogni `VOCE-RRU` deve usare una categoria tecnica primaria:

- `ACCESSIBILITA-NVDA`;
- `LOGICA-DOMINIO`;
- `ARCHITETTURA`;
- `INTEGRAZIONE-RUNTIME`;
- `PRESTAZIONI`;
- `SICUREZZA-INTEGRITA`;
- `I18N-CONTENUTI`;
- `TOOLING-AMMINISTRAZIONE`;
- `DOCUMENTAZIONE-GOVERNANCE`.

Se nessuna categoria è adeguata, usare temporaneamente `DA CLASSIFICARE` e motivare la necessità di una nuova categoria. Non creare autonomamente sinonimi o categorie locali concorrenti.

### 2.6 Severità e rischio per le Voci RRU

- `P0-CRITICA`: perdita o corruzione di dati, rischio grave per sicurezza o accessibilità, blocco totale senza alternativa praticabile.
- `P1-ALTA`: funzione essenziale inutilizzabile o regressione grave con alternativa insufficiente.
- `P2-MEDIA`: malfunzionamento significativo ma circoscritto, con percorso alternativo praticabile.
- `P3-BASSA`: difetto minore, miglioramento o residuo senza impatto operativo rilevante.

Il rischio usa i valori `BASSO`, `MEDIO`, `ALTO` o `CRITICO` e considera probabilità, impatto e reversibilità. Severità del sintomo e rischio dell'intervento devono restare distinti.

---

## 📌 3. Specifica della Testata Universale Compatta

### 3.1 Posizione e navigazione NVDA

La testata deve trovarsi subito dopo il titolo principale sotto questa intestazione di livello 2:

```markdown
## 📌 Metadati del Documento
```

Terminata la testata, deve iniziare immediatamente il primo blocco operativo di livello 2, normalmente:

```markdown
## 🎯 Obiettivo
```

Per un'Idea/RFC può essere usato `## 💡 Problema o Opportunità`; per una Voce RRU può essere usato `## 🧪 Sintomo Rilevato`. Questa struttura permette a Luca di leggere i metadati linearmente oppure saltare al blocco operativo successivo con il comando per intestazioni di NVDA.

Le emoji nelle intestazioni sono preservate come ancore sonore e di orientamento. Non devono sostituire parole descrittive.

### 3.2 Blocco canonico

```markdown
# [TIPO DOCUMENTO]: [Titolo descrittivo]

## 📌 Metadati del Documento

- **ID Documento**: [identificatore univoco nel proprio ambito]
- **Tipo Documento**: [IDEA-RFC | STRATEGIA | PIANO-TECNICO | REPORT | VOCE-RRU | NON DETERMINATO]
- **Esito Classificazione**: [CONFERMATA | PROPOSTA | DA CLASSIFICARE]
- **Intento Operativo**: [INNOVAZIONE | IMPLEMENTAZIONE | CORREZIONE | REFACTORING | DIAGNOSI-VERIFICA | COORDINAMENTO-CHIUSURA]
- **Ambito**: [MASTER-HUB-LOCALE | PROGETTO:<nome> | MODULO:<progetto>/<modulo> | MULTI-PROGETTO:<elenco>]
- **Stato Documento**: [BOZZA | IN REVISIONE | APPROVATO | ANNULLATO | SUPERATO | ARCHIVIATO]
- **Stato Lavoro**: [NON APPLICABILE | NON AVVIATO | IN ESECUZIONE | IN VERIFICA | COMPLETATO | SOSPESO]
- **Gate Operativo**: [CONSULTIVO | IN ATTESA DI AUTORIZZAZIONE | ESECUZIONE AUTORIZZATA | ESECUZIONE CONCLUSA]
- **Evidenza del Gate**: [NON APPLICABILE | riferimento sintetico al comando esplicito, data e oggetto autorizzato]
- **Partecipanti e Ruoli**:
  - **Responsabile Decisionale**: [Luca]
  - **Coordinatore Operativo**: [nome | NON ASSEGNATO]
  - **Esecutore Previsto**: [nome | NON ASSEGNATO | NON APPLICABILE]
  - **Revisori**: [elenco | NESSUNO]
  - **Collaudatore Finale**: [nome | NON APPLICABILE]
- **Modalità Operativa**: [SINGOLA | PAIR | TRIADE]
- **Documenti Correlati**:
  - [tipo di relazione]: [link o NON APPLICABILE]
- **Riferimenti Git**: [SHA verificabile | NON APPLICABILE]
- **Ultimo Aggiornamento**: [YYYY-MM-DD HH:mm Europe/Rome]

## 🎯 Obiettivo

[Primo contenuto operativo del documento.]
```

### 3.3 Istruzioni di compilazione dei campi comuni

#### ID Documento

- Usare l'identificatore già previsto dal progetto, se esiste.
- Se il progetto non dispone di uno schema, usare un prefisso riconoscibile e un numero progressivo, per esempio `RFC-001`, `STR-001`, `PT-001`, `RPT-001` o `REV-01.1`.
- Non rinumerare retroattivamente documenti o revisioni esistenti.
- Non riutilizzare un ID già assegnato nello stesso ambito.

#### Tipo Documento ed Esito Classificazione

- Se tipo e intento sono dichiarati esplicitamente e i campi minimi sono presenti, allora usare `CONFERMATA`.
- Se l'AI propone una classificazione coerente ma manca ancora la conferma richiesta dal flusso, allora usare `PROPOSTA`.
- Se mancano evidenze obbligatorie o più tipi restano compatibili, allora usare `Tipo Documento = NON DETERMINATO` ed `Esito Classificazione = DA CLASSIFICARE`.
- Non usare `DA CLASSIFICARE` come Tipo Documento.

#### Intento Operativo

- Compilare l'intento in base al risultato principale richiesto al documento, non alle parole più frequenti.
- Non concatenare più intenti nello stesso valore.
- Descrivere eventuali finalità secondarie nell'Obiettivo.

#### Ambito

- Usare `MASTER-HUB-LOCALE` per regole o attività limitate alla governance privata della macchina.
- Usare `PROGETTO:<nome>` per un intero progetto.
- Usare `MODULO:<progetto>/<modulo>` per un sottosistema definito.
- Usare `MULTI-PROGETTO:<elenco>` soltanto quando il documento governa davvero più progetti.
- Non inserire `...` o descrizioni generiche al posto dell'ambito concreto.

#### Stato Documento e Stato Lavoro

- Aggiornare i due campi separatamente.
- `Stato Documento = APPROVATO` certifica il contenuto per lo scopo dichiarato, ma non autorizza l'esecuzione.
- `Stato Lavoro = COMPLETATO` indica che le attività previste sono terminate, ma non certifica test, collaudo o chiusura.
- Se il documento non governa o registra attività eseguibili, usare `Stato Lavoro = NON APPLICABILE`.
- Se si usa `SOSPESO`, indicare causa, condizione di ripresa e responsabile della decisione.
- Se si usa `SUPERATO`, collegare il documento sostitutivo.
- Se si usa `ARCHIVIATO`, verificare che i collegamenti in ingresso puntino alla posizione definitiva.

#### Gate Operativo ed Evidenza del Gate

- Il Gate descrive l'autorizzazione vigente; non la crea.
- Se non esiste un comando esplicito riferito all'esecuzione, usare `CONSULTIVO` o `IN ATTESA DI AUTORIZZAZIONE`.
- Se Luca autorizza un'attività specifica, registrare sinteticamente data, oggetto e fase autorizzata.
- Non copiare conversazioni complete nel campo Evidenza del Gate.
- Un'autorizzazione documentale non si estende a codice, configurazioni, test, build, deploy, commit, push, cancellazioni o chiusura.

#### Partecipanti e Ruoli

- `Responsabile Decisionale` identifica chi approva direzione, passaggi di fase e chiusura.
- `Coordinatore Operativo` organizza l'attività autorizzata.
- `Esecutore Previsto` indica chi svolgerebbe o svolge l'attività, ma non gli concede alcuna autorizzazione.
- `Revisori` elenca soltanto chi partecipa realmente alla revisione.
- `Collaudatore Finale` è obbligatorio quando la validazione richiede esperienza utente, NVDA o verifica in-game.
- Non attribuire automaticamente ruoli in base al nome del modello o all'ambiente applicativo.

#### Modalità Operativa

- Usare `SINGOLA` per una consultazione o un incarico affidato a una sola AI senza un secondo collaboratore attivo.
- Usare `PAIR` quando Luca e una AI collaborano direttamente sullo stesso lavoro.
- Usare `TRIADE` quando Luca, AI primaria e AI ausiliaria partecipano esplicitamente allo stesso ciclo decisionale.
- La Modalità non modifica autorizzazioni o responsabilità.

#### Documenti Correlati e Riferimenti Git

- Indicare la relazione: `deriva-da`, `genera`, `verifica`, `segnala`, `sostituisce`, `allegato-di` oppure `correlato-a`.
- Per file locali attivi usare URI assoluti `file:///` risolti sulla macchina corrente, con barre `/` e caratteri di percorso codificati quando necessario.
- Nei template usare segnaposto chiaramente riconoscibili; risolverli nel percorso assoluto soltanto quando viene creato il documento operativo.
- Per un commit usare uno SHA completo quando disponibile; usare uno SHA abbreviato soltanto se verificato come univoco nel repository.
- Un commit non deve essere rappresentato come URI `file:///`.

#### Ultimo Aggiornamento

- Usare data e ora locali nel formato `YYYY-MM-DD HH:mm Europe/Rome`.
- Non scrivere un offset fisso come `UTC+2`, perché varia con l'ora legale.
- Aggiornare il campo soltanto quando cambia il contenuto sostanziale o lo stato.

---

## 🧩 4. Estensioni per i Cinque Tipi Documentali

La Testata Universale Compatta contiene i metadati comuni. Ogni tipo aggiunge soltanto i campi necessari alla propria funzione. Un template verticale può aggiungere campi di dominio, ma non può ridefinire il significato dei campi comuni.

### 4.1 Estensione `IDEA-RFC`

Campi operativi obbligatori:

- **Problema o Opportunità**: descrivere il bisogno osservabile senza anticipare una soluzione obbligatoria.
- **Beneficio Atteso**: indicare per chi nasce il beneficio e come sarebbe riconoscibile.
- **Ipotesi Iniziali**: elencare opzioni plausibili, inclusa l'opzione di non intervenire quando pertinente.
- **Vincoli Noti**: dichiarare accessibilità, compatibilità, sicurezza, ambito e limiti già verificati.
- **Decisione Richiesta**: indicare se occorre approfondire, respingere, archiviare o convertire in Strategia.
- **Esito della Decisione**: usare `IN ATTESA`, `ACCOLTA`, `RESPINTA` o `RINVIATA`, accompagnato dalla motivazione.

Regole:

- Se sono già presenti invarianti convalidate e confronto sistematico tra ipotesi, allora valutare `STRATEGIA`.
- Se sono già presenti file, contratti e passi esecutivi, allora valutare `PIANO-TECNICO`.
- Un'Idea/RFC accolta non autorizza implementazione.

### 4.2 Estensione `STRATEGIA`

Campi operativi obbligatori:

- **Dilemma o Domanda Strategica**: definire la decisione concettuale da risolvere.
- **Modello Mentale**: descrivere il comportamento o il dominio dal punto di vista dell'utente e del sistema.
- **Ipotesi Concorrenti**: confrontare almeno le alternative materialmente plausibili.
- **Tesi Selezionata**: indicare l'approccio preferito e perché supera le alternative.
- **Invarianti Concettuali**: elencare ciò che non dovrà regredire.
- **Rischi e Condizioni Limite**: includere scenari ordinari, alternativi e casi limite.
- **Registro di Convergenza**: distinguere punti aperti, convergenza preliminare e invarianti convalidate.
- **Criterio di Conversione**: dichiarare quando la Strategia è pronta a generare un Piano Tecnico.

Regole:

- La Strategia definisce invarianti concettuali; non anticipa la formalizzazione esecutiva completa.
- I Named Contracts D0..DN e S1..SN appartengono al Piano Tecnico.
- Se la Strategia anticipa una corrispondenza con futuri contratti, marcarla come mappatura preliminare.
- La conversione in Piano richiede una decisione esplicita di Luca.

### 4.3 Estensione `PIANO-TECNICO`

Campi operativi obbligatori:

- **Origine del Requisito**: collegare Idea/RFC, Strategia, Voce RRU o richiesta diretta.
- **Scopo ed Esclusioni**: indicare con precisione cosa verrà e non verrà interessato.
- **Precondizioni**: dichiarare stato del progetto, dipendenze e verifiche necessarie prima dell'esecuzione.
- **Named Contracts D0..DN e S1..SN**: definire decisioni, precondizioni, postcondizioni, invarianti e responsabilità.
- **Componenti Coinvolti**: elencare file, moduli, dati o ambienti previsti, senza dichiararli modificati prima dell'esecuzione.
- **Passi Esecutivi**: ordinare le attività in unità verificabili e reversibili.
- **Verifiche**: associare a ogni contratto evidenze automatiche, statiche, telemetriche o utente pertinenti.
- **Matrice a Tre Livelli**: coprire percorso ordinario, alternative o concorrenza e casi limite.
- **Audit sui Sette Assi**: validità, efficacia, coerenza, completezza, precisione, prestazioni e assenza di regressioni.
- **Impatto Versione AVF**: proporre l'incremento oppure motivare `NON APPLICABILE`.
- **Punto di Stop**: indicare chiaramente il confine tra Sotto-Fase 1A e attività esecutive.

Regole:

- L'approvazione del Piano certifica il disegno, non autorizza automaticamente la Sotto-Fase 1B.
- Se Luca autorizza soltanto la redazione o modifica del Piano, allora il Gate resta limitato all'attività documentale.
- Non contrassegnare come modificato, testato o collaudato ciò che è soltanto pianificato.

### 4.4 Estensione `REPORT`

Per lettura selettiva, aggiornamenti automatici compresi nel mandato, radici separate, fonti esterne e chiusura applicare la [routine report e continuità v3](gestione_report_e_continuita_sessioni.md). La testata universale è il formato dei nuovi report; le testate a sette campi restano compatibili in lettura. Nessuna riscrittura degli archivi storici è implicita.

Campi operativi obbligatori:

- **Obiettivo del Report**: indicare quale attività, decisione o verifica documenta.
- **Periodo o Sessione**: indicare intervallo, data o evento coperto.
- **Attività Effettivamente Svolte**: registrare soltanto azioni verificate.
- **Evidenze**: collegare log, test, file, telemetria, riscontri utente o commit pertinenti.
- **Risultati**: separare fatti osservati, inferenze e questioni ancora aperte.
- **Esito delle Verifiche**: indicare `NON ESEGUITE`, `PARZIALI`, `SUPERATE`, `FALLITE` o `NON APPLICABILI`, specificando quali verifiche.
- **Decisioni e Passaggi di Consegne**: registrare decisione, responsabile e prossimo gate senza estendere l'autorizzazione.
- **Limiti dell'Evidenza**: dichiarare ciò che non è stato verificato.

Regole:

- Mantenere in alto lo stato corrente e, nei flussi di sessione, usare cronologia inversa.
- Un test automatico superato non certifica da solo un comportamento runtime o l'esperienza NVDA.
- Un riscontro verbale generico non sostituisce log o telemetria quando tali fonti sono richieste.
- La chiusura richiede evidenze proporzionate alla natura del lavoro e la convalida finale di Luca.
- Se il lavoro modifica comportamento runtime o accessibilità, allora il completamento tecnico non sostituisce il collaudo reale con NVDA e, quando pertinente, in-game.

### 4.5 Estensione `VOCE-RRU`

Campi operativi obbligatori:

- **ID Revisione**: usare l'identificatore previsto dal progetto.
- **Severità**: `P0-CRITICA`, `P1-ALTA`, `P2-MEDIA` o `P3-BASSA`.
- **Categoria Tecnica**: scegliere una categoria dal vocabolario controllato.
- **Rischio dell'Intervento**: `BASSO`, `MEDIO`, `ALTO` o `CRITICO`.
- **Data e Contesto di Rilevamento**: indicare quando e in quale scenario emerge il problema.
- **Sintomo Osservabile**: descrivere ciò che l'utente o il sistema manifesta.
- **Evidenza Disponibile**: collegare log, telemetria, persistenza o riproduzione.
- **Causa Radice**: usare `NON DETERMINATA` finché non è sostenuta da evidenze.
- **Azione Successiva**: indicare diagnosi, Strategia, Piano, verifica, rinvio o chiusura.
- **Documenti Correlati**: collegare almeno il Report quando esiste; altrimenti collegare la fonte attiva pertinente.
- **Esito di Verifica**: distinguere attività pianificata, implementata, verificata e collaudata.

Regole:

- La Voce RRU deve rimanere sintetica; i dettagli estesi risiedono nel Report o nell'allegato collegato.
- Non dichiarare una causa radice sulla base del solo sintomo.
- Non chiudere una Voce RRU prima delle verifiche richieste dalla sua natura.
- Dopo la chiusura, preservare ID e collegamenti quando la voce viene trasferita nell'archivio.

---

## 🤖 5. Regole di Auto-Classificazione e Auto-Deduzione Deterministica

### 5.1 Principio generale

L'auto-deduzione classifica evidenze esplicite; non inventa intenzioni, autorizzazioni o stati. L'AI deve distinguere il contenuto principale del documento da citazioni, allegati, collegamenti e storia pregressa.

### 5.2 Ordine di valutazione

Applicare nell'ordine:

1. Individuare l'oggetto principale richiesto dal documento.
2. Ignorare, ai fini della classificazione primaria, testi citati e contenuti riportati soltanto come evidenza.
3. Cercare una dichiarazione esplicita del tipo e verificarne la compatibilità con i campi minimi.
4. Se il tipo non è dichiarato, applicare le regole della sezione 5.3.
5. Determinare l'intento dal risultato principale richiesto applicando la sezione 5.4.
6. Verificare che tipo e intento non contraddicano scopo, stato e gate.
7. Se rimane una sola classificazione compatibile, usare `CONFERMATA` o `PROPOSTA` secondo il flusso.
8. Se mancano evidenze obbligatorie o rimangono almeno due classificazioni compatibili, usare il paracadute `DA CLASSIFICARE`.

### 5.3 Deduzione del Tipo Documento

- Se il contenuto formula un problema o un'opportunità iniziale e chiede se approfondire, allora classificare `IDEA-RFC`.
- Se confronta ipotesi, definisce un modello mentale e congela invarianti concettuali, allora classificare `STRATEGIA`.
- Se prescrive componenti, Named Contracts, passi esecutivi e verifiche future, allora classificare `PIANO-TECNICO`.
- Se registra attività già svolte, risultati, evidenze, telemetria, decisioni o passaggi di consegne, allora classificare `REPORT`.
- Se traccia atomicamente un'anomalia o un affinamento con severità, stato ed esito, allora classificare `VOCE-RRU`.

Regole di disambiguazione:

- Se un Report cita un Piano, allora il collegamento non trasforma il Report in Piano.
- Se una Voce RRU contiene una soluzione proposta, allora rimane Voce RRU finché la sua funzione primaria è tracciare l'anomalia.
- Se una Strategia elenca componenti possibili, allora rimane Strategia finché non prescrive contratti e passi esecutivi.
- Se un Piano contiene una sintesi della diagnosi, allora rimane Piano se il risultato principale è guidare l'esecuzione.
- Se un testo svolge due funzioni primarie inseparabili, allora usare `NON DETERMINATO` e proporre la separazione in due documenti collegati.

### 5.4 Deduzione dell'Intento Operativo

- Se il risultato principale è valutare una nuova possibilità ancora aperta, allora usare `INNOVAZIONE`.
- Se il risultato principale è creare una nuova capacità già definita, allora usare `IMPLEMENTAZIONE`.
- Se il risultato principale è ripristinare un comportamento atteso o rimuovere un difetto, allora usare `CORREZIONE`.
- Se il risultato principale è migliorare struttura, separazione o manutenibilità preservando il comportamento dichiarato, allora usare `REFACTORING`.
- Se il risultato principale è acquisire evidenze, isolare una causa o verificare un esito, allora usare `DIAGNOSI-VERIFICA`.
- Se il risultato principale è coordinare partecipanti, trasferire responsabilità, archiviare o convalidare, allora usare `COORDINAMENTO-CHIUSURA`.

Disambiguazioni:

- Se si analizza un difetto senza autorizzare o progettare la correzione, allora usare `DIAGNOSI-VERIFICA`.
- Se la causa è verificata e il documento persegue la soluzione, allora usare `CORREZIONE`.
- Se una nuova architettura abilita una capacità nuova, allora usare `IMPLEMENTAZIONE`; descrivere il refactoring come vincolo secondario.
- Se il comportamento deve restare invariato, allora usare `REFACTORING`.
- Se un Report documenta un'implementazione, allora può usare `IMPLEMENTAZIONE`; il tipo resta `REPORT`.

### 5.5 Paracadute `DA CLASSIFICARE`

Usare il paracadute se si verifica almeno una condizione:

- mancano i campi minimi necessari a distinguere il tipo;
- due o più tipi restano compatibili dopo le regole di disambiguazione;
- l'intento dichiarato contraddice il risultato richiesto;
- il testo unisce funzioni primarie che richiedono documenti separati;
- l'ambito non permette di determinare quale standard verticale applicare.

In tal caso compilare:

```markdown
- **Tipo Documento**: NON DETERMINATO
- **Esito Classificazione**: DA CLASSIFICARE
```

L'AI deve presentare a Luca l'ambiguità concreta e le alternative compatibili. Non deve scegliere sulla base di preferenze implicite.

### 5.6 Auto-deduzioni vietate

Non dedurre mai automaticamente:

- autorizzazione a modificare file o codice;
- autorizzazione a eseguire test, build, deploy, commit, push o cancellazioni;
- approvazione del documento;
- superamento delle verifiche;
- collaudo positivo;
- chiusura o archiviazione;
- causa radice non sostenuta da evidenze;
- ruolo operativo basato soltanto sull'ambiente o sul modello AI attivo.

---

## 🛡️ 6. Ruoli, Autorizzazioni, Gating Semantico e Regola 0

### 6.1 Regola 0 blindata

ASTRALIS opera con dialogo a due tempi:

1. acquisizione, analisi, proposta e revisione;
2. esecuzione limitata da un comando esplicito di Luca.

La testata registra il gate vigente, ma non può concederlo. Nessun ruolo, stato, tipo, intento, checklist o collegamento sostituisce l'autorizzazione esplicita.

### 6.2 Autorizzazione vincolata all'oggetto

- Se Luca autorizza la stesura di un documento, allora è autorizzata soltanto la scrittura di quel documento.
- Se Luca approva una Strategia, allora è autorizzata soltanto la transizione concordata verso la pianificazione, se esplicitamente richiesta.
- Se Luca dice “passa alla fase 1”, allora è autorizzata esclusivamente la Sotto-Fase 1A di pianificazione.
- Se Luca autorizza l'esecuzione di un Piano, allora l'autorizzazione copre soltanto scopo, file, comandi e fase dichiarati nel Piano approvato.
- Se la richiesta introduce un oggetto materialmente diverso, allora occorre un nuovo gate.
- Se l'autorizzazione è ambigua rispetto all'oggetto, allora il Gate resta `IN ATTESA DI AUTORIZZAZIONE` per la parte ambigua.

Le parole `procedi`, `applica` ed `esegui` devono essere interpretate nel contesto dell'oggetto immediatamente autorizzato. Non costituiscono autorizzazioni universali.

### 6.3 Disaccoppiamento dei ruoli

- Il Responsabile Decisionale approva direzione e passaggi di fase.
- Il Coordinatore Operativo organizza il lavoro autorizzato.
- L'Esecutore Previsto identifica un possibile esecutore e non riceve poteri dalla testata.
- Il Revisore valuta contenuto ed evidenze e non modifica automaticamente l'oggetto revisionato.
- Il Collaudatore Finale convalida l'esperienza reale quando richiesta.

Se una stessa persona o AI assume più ruoli, allora ogni ruolo deve essere dichiarato. L'accumulo dei ruoli non amplia il gate.

### 6.4 Transizioni del Gate Operativo

- Stato iniziale ordinario: `CONSULTIVO`.
- Se esiste un piano o una proposta pronta e serve un via libera: `IN ATTESA DI AUTORIZZAZIONE`.
- Dopo un comando esplicito e circoscritto di Luca: `ESECUZIONE AUTORIZZATA`.
- Dopo l'esecuzione delle sole attività autorizzate: `ESECUZIONE CONCLUSA`.

`ESECUZIONE CONCLUSA` non modifica automaticamente Stato Documento o Stato Lavoro. Le verifiche e la convalida seguono i propri criteri.

### 6.5 Gating della verifica e della chiusura

- Se il lavoro è documentale, allora verificare struttura, completezza, coerenza, link, codifica e accessibilità NVDA pertinenti.
- Se il lavoro riguarda codice, allora usare le verifiche tecniche previste dal progetto.
- Se il lavoro modifica un comportamento runtime, allora integrare test automatici con telemetria reale quando richiesta.
- Se il lavoro modifica l'esperienza accessibile, allora richiedere il collaudo di Luca con NVDA e, quando pertinente, in-game.
- Se le evidenze richieste non sono disponibili, allora dichiarare il limite e non segnare la chiusura come convalidata.
- La chiusura ufficiale richiede la decisione esplicita di Luca.

### 6.6 Eliminazione protetta

Se un'attività prevede cancellazione, sostituzione distruttiva o perdita potenziale di dati, allora il documento deve indicare motivazione, impatto, recuperabilità e target esatti. L'esecuzione richiede un'autorizzazione esplicita riferita alla cancellazione.

---

## 🔗 7. Collegamenti Pointer DRY e Sintesi Multi-AI nei Report

### 7.1 Fonte unica per ogni informazione

- La presente scheda è la fonte unica della tassonomia comune.
- Il documento operativo è la fonte dello stato e delle decisioni che gli appartengono.
- Il Report è la fonte della sintesi della sessione, delle evidenze utilizzate e dell'esito.
- L'allegato è la fonte del dettaglio esteso che il Report collega senza duplicare.
- La Voce RRU conserva la sintesi forense e punta al Report o alla fonte operativa pertinente.
- Il Piano conserva contratti e passi previsti; il Report registra ciò che è stato realmente eseguito.

### 7.2 Relazioni Pointer DRY

Usare una relazione esplicita per ogni collegamento:

- `deriva-da`: il documento nasce da una fonte precedente;
- `genera`: il documento produce un nodo successivo;
- `verifica`: il documento raccoglie evidenze su un altro nodo;
- `segnala`: la Voce RRU registra un'anomalia relativa alla fonte;
- `sostituisce`: il documento rende superata una versione precedente;
- `allegato`: il documento principale collega un file di dettaglio esteso;
- `allegato-di`: il file di dettaglio collega il proprio documento principale;
- `correlato-a`: esiste una relazione utile che non rientra nelle precedenti.

Evitare collegamenti generici senza spiegare la relazione.

### 7.3 Regole per i file locali

- Nei documenti operativi materializzati usare un URI assoluto nel formato `file:///C:/percorso/file.md`.
- Usare barre `/` nell'URI.
- Codificare gli spazi come `%20` quando necessario per la compatibilità del visualizzatore.
- Verificare che il collegamento punti al file effettivo, non a una scorciatoia `.lnk`.
- Se un documento viene spostato in archivio, aggiornare i collegamenti operativi che devono continuare a raggiungerlo.
- Nei template usare segnaposto e non nomi utente rigidi; risolvere il percorso al momento della creazione del documento.

### 7.4 Regole per Git e altre evidenze

- Riferire un commit tramite SHA verificato.
- Preferire lo SHA completo nei documenti di chiusura.
- Se si usa uno SHA abbreviato, verificarne l'univocità nel repository.
- Aggiungere un collegamento remoto soltanto se il repository e il commit sono accessibili nel perimetro autorizzato.
- Non usare `file:///` per rappresentare un commit.
- Per log voluminosi indicare file, intervallo temporale, pattern o righe pertinenti senza incollare dump integrali.

### 7.5 Sintesi Multi-AI nei Report

Ogni contributo di Luca, Antigravity, GPT/Codex o altro collaboratore deve essere registrato in forma sintetica e attribuita.

Blocco consigliato:

```markdown
### 🕒 [YYYY-MM-DD HH:mm Europe/Rome] — [Autore] — [Oggetto]

- **Contesto**: [fatto o domanda in massimo due righe]
- **Conclusione**: [decisione, diagnosi o proposta ad alto segnale]
- **Stato**: [confermato | proposto | da verificare]
- **Puntatori**: [documenti, evidenze o allegati]
```

Regole:

- Inserire l'aggiornamento più recente in alto quando il Report adotta una cronologia di sessione.
- Separare fatti osservati, inferenze e proposte.
- Non incollare integralmente risposte AI lunghe nel Report.
- Non duplicare nel Report contratti già definiti nel Piano o invarianti già definite nella Strategia.
- Registrare nel Report la conclusione operativa e il collegamento alla fonte estesa.

### 7.6 Allegati ad hoc

Creare un allegato soltanto se il dettaglio è necessario per audit, passaggio di consegne o riproducibilità e renderebbe il Report difficile da consultare con NVDA.

Un allegato deve:

- avere un nome riconoscibile associato all'ID del Report, per esempio `ALLEGATO_<ID-REPORT>_<ARGOMENTO>.md`;
- dichiarare autore, data, scopo e Report principale;
- contenere soltanto il dettaglio esteso necessario;
- essere collegato dal Report con relazione `allegato` e collegare a sua volta il Report con relazione `allegato-di`;
- non introdurre decisioni o stati assenti dal Report principale.

Se il contenuto è breve, allora inserirlo direttamente nella sintesi e non creare un allegato.

### 7.7 Collegamento minimo per tipo

- `IDEA-RFC`: collegare fonti del problema e nodo generato, se esiste.
- `STRATEGIA`: collegare Idea/RFC di origine, Piano derivato e Report di verifica, quando esistono.
- `PIANO-TECNICO`: collegare origine, Strategia, Report di esecuzione e Voci RRU pertinenti.
- `REPORT`: collegare oggetto documentato, evidenze, allegati e Voci RRU generate.
- `VOCE-RRU`: collegare il Report correlato quando esiste; altrimenti collegare la fonte attiva più pertinente.

L'assenza legittima di un nodo deve essere espressa con `NON APPLICABILE`; non creare documenti vuoti per soddisfare il collegamento.

---

## ✅ 8. Compatibilità, Adozione Progressiva ed Esempi Rappresentativi

### 8.1 Regole di compatibilità

- Questo standard prevale per la tassonomia comune dei nuovi documenti operativi locali.
- I template esistenti restano validi finché non vengono aggiornati o finché non generano conflitti materiali con un nuovo documento.
- Se un template usa uno stato precedente, allora il nuovo documento deve mapparlo al vocabolario corrente senza riscrivere l'archivio storico.
- Le regole verticali di progetto restano valide per dominio, build, test, accessibilità e rilascio.
- Se una regola verticale contraddice tassonomia o gating comune, allora segnalare il conflitto a Luca e non dedurre autonomamente una deroga.
- La creazione di questa scheda non autorizza l'aggiornamento di router, template, registri, archivi o Genomi globali.

### 8.2 Adozione progressiva

L'adozione avviene in passi separati:

1. creare e convalidare questa fonte normativa;
2. aggiungere, con autorizzazione dedicata, puntatori sintetici alle sole fonti normative attive necessarie;
3. applicare la testata ai nuovi documenti operativi;
4. aggiornare i template progressivamente in attività dedicate;
5. convertire un documento esistente soltanto quando viene riaperto per modifiche sostanziali;
6. lasciare invariati archivi, report chiusi e piani completati.

### 8.3 Esempio `IDEA-RFC`

```markdown
# IDEA-RFC: Esplorazione di un riepilogo vocale contestuale

## 📌 Metadati del Documento

- **ID Documento**: RFC-001
- **Tipo Documento**: IDEA-RFC
- **Esito Classificazione**: CONFERMATA
- **Intento Operativo**: INNOVAZIONE
- **Ambito**: PROGETTO:minecraft-access
- **Stato Documento**: BOZZA
- **Stato Lavoro**: NON APPLICABILE
- **Gate Operativo**: CONSULTIVO
- **Evidenza del Gate**: NON APPLICABILE
- **Partecipanti e Ruoli**:
  - **Responsabile Decisionale**: Luca
  - **Coordinatore Operativo**: Antigravity
  - **Esecutore Previsto**: NON ASSEGNATO
  - **Revisori**: GPT/Codex
  - **Collaudatore Finale**: NON APPLICABILE
- **Modalità Operativa**: TRIADE
- **Documenti Correlati**:
  - **correlato-a**: [Fonte del requisito](file:///C:/PERCORSO-ASSOLUTO/FONTE.md)
- **Riferimenti Git**: NON APPLICABILE
- **Ultimo Aggiornamento**: 2026-09-12 09:00 Europe/Rome

## 💡 Problema o Opportunità

Valutare se un riepilogo vocale su richiesta possa ridurre il carico cognitivo senza introdurre chatter.
```

### 8.4 Esempio `STRATEGIA`

```markdown
# STRATEGIA: Gerarchia del riepilogo vocale contestuale

## 📌 Metadati del Documento

- **ID Documento**: STR-001
- **Tipo Documento**: STRATEGIA
- **Esito Classificazione**: CONFERMATA
- **Intento Operativo**: INNOVAZIONE
- **Ambito**: MODULO:minecraft-access/cognitive
- **Stato Documento**: IN REVISIONE
- **Stato Lavoro**: NON APPLICABILE
- **Gate Operativo**: CONSULTIVO
- **Evidenza del Gate**: NON APPLICABILE
- **Partecipanti e Ruoli**:
  - **Responsabile Decisionale**: Luca
  - **Coordinatore Operativo**: Antigravity
  - **Esecutore Previsto**: NON ASSEGNATO
  - **Revisori**: GPT/Codex
  - **Collaudatore Finale**: Luca
- **Modalità Operativa**: TRIADE
- **Documenti Correlati**:
  - **deriva-da**: [RFC-001](file:///C:/PERCORSO-ASSOLUTO/RFC-001.md)
- **Riferimenti Git**: NON APPLICABILE
- **Ultimo Aggiornamento**: 2026-09-12 09:15 Europe/Rome

## 🎯 Obiettivo

Definire il modello mentale e le invarianti vocali prima della pianificazione tecnica.
```

### 8.5 Esempio `PIANO-TECNICO`

```markdown
# PIANO-TECNICO: Implementazione del riepilogo vocale contestuale

## 📌 Metadati del Documento

- **ID Documento**: PT-001
- **Tipo Documento**: PIANO-TECNICO
- **Esito Classificazione**: CONFERMATA
- **Intento Operativo**: IMPLEMENTAZIONE
- **Ambito**: MODULO:minecraft-access/cognitive
- **Stato Documento**: APPROVATO
- **Stato Lavoro**: NON AVVIATO
- **Gate Operativo**: IN ATTESA DI AUTORIZZAZIONE
- **Evidenza del Gate**: Approvazione della Sotto-Fase 1A; esecuzione 1B non autorizzata
- **Partecipanti e Ruoli**:
  - **Responsabile Decisionale**: Luca
  - **Coordinatore Operativo**: Antigravity
  - **Esecutore Previsto**: Antigravity
  - **Revisori**: GPT/Codex
  - **Collaudatore Finale**: Luca
- **Modalità Operativa**: TRIADE
- **Documenti Correlati**:
  - **deriva-da**: [STR-001](file:///C:/PERCORSO-ASSOLUTO/STR-001.md)
  - **genera**: NON APPLICABILE
- **Riferimenti Git**: NON APPLICABILE
- **Ultimo Aggiornamento**: 2026-09-12 09:30 Europe/Rome

## 🎯 Obiettivo

Tradurre le invarianti convalidate nei Named Contracts e nelle verifiche della Sotto-Fase 1A.
```

### 8.6 Esempio `REPORT`

```markdown
# REPORT: Verifica del riepilogo vocale contestuale

## 📌 Metadati del Documento

- **ID Documento**: RPT-001
- **Tipo Documento**: REPORT
- **Esito Classificazione**: CONFERMATA
- **Intento Operativo**: DIAGNOSI-VERIFICA
- **Ambito**: MODULO:minecraft-access/cognitive
- **Stato Documento**: IN REVISIONE
- **Stato Lavoro**: IN VERIFICA
- **Gate Operativo**: ESECUZIONE CONCLUSA
- **Evidenza del Gate**: Esecuzione del PT-001 autorizzata da Luca nella sessione del 2026-09-12
- **Partecipanti e Ruoli**:
  - **Responsabile Decisionale**: Luca
  - **Coordinatore Operativo**: Antigravity
  - **Esecutore Previsto**: Antigravity
  - **Revisori**: GPT/Codex
  - **Collaudatore Finale**: Luca
- **Modalità Operativa**: TRIADE
- **Documenti Correlati**:
  - **verifica**: [PT-001](file:///C:/PERCORSO-ASSOLUTO/PT-001.md)
  - **allegato**: [Telemetria sintetizzata](file:///C:/PERCORSO-ASSOLUTO/ALLEGATO_RPT-001_TELEMETRIA.md)
- **Riferimenti Git**: 0123456789abcdef0123456789abcdef01234567
- **Ultimo Aggiornamento**: 2026-09-12 10:00 Europe/Rome

## 🎯 Obiettivo

Registrare separatamente test automatici, telemetria e collaudo NVDA, dichiarando i limiti delle evidenze disponibili.
```

### 8.7 Esempio `VOCE-RRU`

```markdown
# VOCE-RRU: Ripetizione del riepilogo durante il movimento

## 📌 Metadati del Documento

- **ID Documento**: REV-MC-01.1
- **Tipo Documento**: VOCE-RRU
- **Esito Classificazione**: CONFERMATA
- **Intento Operativo**: CORREZIONE
- **Ambito**: MODULO:minecraft-access/cognitive
- **Stato Documento**: APPROVATO
- **Stato Lavoro**: NON AVVIATO
- **Gate Operativo**: CONSULTIVO
- **Evidenza del Gate**: NON APPLICABILE
- **Partecipanti e Ruoli**:
  - **Responsabile Decisionale**: Luca
  - **Coordinatore Operativo**: Antigravity
  - **Esecutore Previsto**: NON ASSEGNATO
  - **Revisori**: GPT/Codex
  - **Collaudatore Finale**: Luca
- **Modalità Operativa**: TRIADE
- **Documenti Correlati**:
  - **segnala**: [RPT-001](file:///C:/PERCORSO-ASSOLUTO/RPT-001.md)
- **Riferimenti Git**: NON APPLICABILE
- **Ultimo Aggiornamento**: 2026-09-12 10:15 Europe/Rome

## 🧪 Sintomo Rilevato

- **Severità**: P2-MEDIA
- **Categoria Tecnica**: ACCESSIBILITA-NVDA
- **Rischio dell'Intervento**: MEDIO
- **Sintomo Osservabile**: Il riepilogo viene ripetuto durante il movimento e aumenta il carico vocale.
- **Causa Radice**: NON DETERMINATA
- **Azione Successiva**: Acquisire telemetria e isolare la condizione di ripetizione prima di proporre una correzione.
```

### 8.8 Checklist di conformità della nuova scheda o del nuovo documento

- [ ] Il documento usa uno dei cinque tipi oppure dichiara correttamente `NON DETERMINATO`?
- [ ] L'Esito Classificazione è separato dal Tipo Documento?
- [ ] È presente un solo Intento Operativo primario?
- [ ] Stato Documento, Stato Lavoro e Gate Operativo sono distinti?
- [ ] L'Esecutore Previsto è separato dall'autorizzazione?
- [ ] L'Evidenza del Gate è concreta e limitata all'oggetto autorizzato?
- [ ] Le verifiche richieste sono proporzionate alla natura del lavoro?
- [ ] I collegamenti locali usano URI `file:///` verificabili e i commit usano SHA?
- [ ] Il Report conserva la sintesi e collega gli eventuali dettagli estesi senza duplicarli?
- [ ] La struttura è lineare, navigabile con NVDA e usa intestazioni descrittive con emoji?
- [ ] Gli archivi storici sono rimasti immutati?
- [ ] Nessuna classificazione o stato è stato interpretato come autorizzazione implicita?

---

Questa scheda definisce la tassonomia comune. La sua applicazione a router, template o documenti esistenti deve essere autorizzata e verificata in attività successive e circoscritte.
