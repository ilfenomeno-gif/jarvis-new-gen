# Ingegneria delle Regole e Meta-Governance (ASTRALIS Canon Crafting)
# Autore: Luca (Sviluppatore Senior Non Vedente con Screen Reader NVDA)
# Target AI: Antigravity (Senior AI Pair Programmer & Software Engineer)
# Ambito: Globale / Universale
# Master Hub: <astralis-hub>

Questo documento definisce gli standard ingegneristici, architetturali e operativi per concepire, redigere, strutturare, validare e manutenere qualsiasi regola, routine o protocollo all'interno dell'ecosistema ASTRALIS.

---

## 🏛️ 1. I 6 CANONI FONDAMENTALI DELL'INGEGNERIA DELLE REGOLE

Ogni regola, direttiva o aggiornamento normativo deve conformarsi rigorosamente ai seguenti 6 Canoni Architetturali:

### Canone 1 — Hub & Spoke & Budgeting Token (Router Snello)
- **Scopo**: Proteggere la finestra di contesto di qualsiasi modello AI, prevenendo allucinazioni, decadimento dell'attenzione ed overhead di token.
- **Regola Dimensionale**: I file di ingresso master (`GEMINI.md`, `AGENTS.md`) fungono esclusivamente da **Router ad Alto Segnale** e non devono mai superare il limite di sicurezza di **250 righe** (circa 1.800 - 2.200 token).
- **Dislocazione della Conoscenza**: Tutto il dettaglio teorico, i flussi analitici, gli script, gli elenchi estesi e le casistiche applicative devono risiedere nelle schede tematiche della cartella `knowledge/` (locale di progetto) o `knowledge/` (Master Hub).

### Canone 2 — Disaccoppiamento Manifest vs Modulo
- **Separazione dei Ruoli**:
  - **Manifest di Progetto (`GEMINI.md` locale)**: Contiene unicamente i parametri concreti di configurazione (URL del repository Git, branch attivo, percorsi delle cartelle ponte o di backup, hostname specifici) in 3-6 righe lineari ad alto segnale.
  - **Modulo di Conoscenza (`knowledge/*.md`)**: Contiene la spiegazione architetturale, le motivazioni di design, i comandi CLI e le procedure operative complete.
- **Invariante**: Se una spiegazione concettuale si applica a più progetti, appartiene a `knowledge/`. Se si applica a un dominio specifico, appartiene a `knowledge/` di quel progetto. In nessun caso deve essere riversata per intero nel `GEMINI.md`.

### Canone 3 — Rete Documentale Pointer DRY & Link `file:///`
- **Principio DRY (Don't Repeat Yourself)**: È fatto divieto assoluto di duplicare blocchi di testo o descrizioni tra documenti diversi. Ogni informazione ha un'unica Fonte di Verità (*Single Source of Truth*).
- **Rete Documentale Comunicante a 5 Nodi**: La catena operativa (`Idea/RFC` -> `Strategia` -> `Piano Tecnico` -> `Report` -> `Voce RRU`) rispetta i contratti definiti nello [Standard di Tassonomia Documentale](standard_tassonomia_documentale_e_auto_deduzione.md).
- **Collegamento Ipertestuale Obbligatorio**: Ogni riferimento a file, moduli o contratti deve utilizzare percorsi assoluti con protocollo `file:///` (es. `[Piano Tecnico](file:///c:/percorso/piano.md)`), permettendo a Luca e all'assistente di saltare istantaneamente alla fonte.

### Canone 4 — Gating Deterministico a 3 Stati
- **Tracciamento Atomico**: Qualsiasi avanzamento, piano o checklist adotta la notazione a 3 stati:
  - `[ ]` (Da Iniziare / Aperto);
  - `[/]` (In Corso / In Lavorazione / Parziale);
  - `[x]` (Completato, Verificato e Collaudato con Successo).
- **Divieto di Spunta Preventiva**: Nessuna casella può essere contrassegnata con `[x]` fino a quando non sono stati eseguiti i test formali previsti e, nel caso di collaudi in-game o utente, fino al feedback positivo esplicito di Luca.

### Canone 5 — Accessibilità Cognitiva NVDA & Zero Visual Bloat
- **Flusso Lineare Obbligatorio**: La struttura del testo deve essere fruibile in modo fluido tramite screen reader NVDA riga per riga da tastiera.
- **Divieti Visivi Assoluti**:
  - Divieto di tabelle ASCII con bordi complessi (`+---+---+`), frecce grafiche (`--->`), alberi disegnati a caratteri o layout a griglia bidimensionale.
  - Sostituire sempre con elenchi puntati nidificati o costrutti sequenziali ad alto contrasto cognitivo: `Se [Condizione] -> Allora [Azione]`.
- **Ordine Cronologico Inverso per i Log**: Nei registri delle revisioni, nei diari e negli archivi, le voci più recenti devono essere collocate in cima (dopo l'intestazione), così che Luca non debba scorrere decine di pagine per consultare le ultime novità.

### Canone 6 — Igiene dei File, Codifica & Portabilità Cross-Platform
- **Codifica & BOM**: Tutti i file di testo (`.md`, `.json`, `.py`, `.ps1`) devono essere salvati rigorosamente in formato UTF-8 senza BOM (*Byte Order Mark*).
- **Terminazioni di Riga (Line Endings)**:
  - Su ambiente Windows, preservare e utilizzare terminazioni CRLF (`\r\n`) per evitare diff fantasma sui repository Git e corruzioni nei tool locali.
- **Portabilità Assoluta (Zero Hardcoding)**: Divieto di inserire lettere di unità fisse o nomi utente rigidi. Usare esclusivamente variabili d'ambiente di sistema (`$env:OneDrive`, `$env:USERPROFILE`, `$env:APPDATA`, `%USERPROFILE%`, `%ONEDRIVE%`) o percorsi relativi ancorati allo script (`$PSScriptRoot`, `%~dp0`).

### Canone 7 — Il Commit di Sicurezza Pre-Bonifica (Canone D41 Guard)
- **Scopo**: Eliminare il rischio di regressione durante le fasi di pulizia del codice morto, rimozione elementi obsoleti (Dead Code Purge D41) o rifinitura post-collaudo.
- **Regola Operativa**:
  - *Se*: una complessa iterazione di codice ha superato con successo il collaudo funzionale in-game o utente e richiede una successiva operazione di bonifica di codice orfano/superato;
  - *Allora*: è obbligatorio eseguire un **commit Git di sicurezza dedicato** (punto di ripristino congelato a 1-click) PRIMA di toccare qualsiasi riga di codice per la bonifica.
- **Verifica di Assenza Regressioni**: La pulizia deve essere eseguita a piccoli lotti atomici, seguita immediatamente dall'esecuzione della suite completa di test prima di promuovere l'artefatto finale.

---

## 🔄 2. CICLO DI VITA DI UNA NUOVA REGOLA O PROTOCOLLO

Prima di proporre o codificare qualsiasi nuova regola, l'assistente AI deve seguire questa procedura in 4 passi:

1. **Passo 1 — Valutazione di Necessità & Non-Ridondanza (Fase 0)**:
   - Verificare se l'esigenza è già coperta dai 12 Protocolli o dalle schede esistenti.
   - Determinare se la regola è *Globale* (Master Hub) o *Locale* (singolo progetto).
2. **Passo 2 — Redazione nel Modulo Esteso (Knowledge)**:
   - Creare o aggiornare la scheda specialistica in `knowledge/` o `knowledge/` applicando i Canoni 5 (Linearità NVDA) e 6 (Igiene File).
3. **Passo 3 — Puntatore Sintetico nel Router (`GEMINI.md`)**:
   - Inserire nel file `GEMINI.md` pertinente una sintesi di massimo 2-4 righe con link cliccabile `file:///` al modulo esteso.
   - Verificare che il file non superi la soglia limite di 250 righe.
4. **Passo 4 — Audit di Conformità & Dialogo a 2 Tempi (Regola 0)**:
   - Presentare a Luca la proposta in formato compatto ad alto segnale.
   - Attendere il comando esplicito (*"procedi"*, *"applica"*) prima di effettuare qualsiasi scrittura su disco.

---

## 🛡️ 3. CHECKLIST PRE-COMMIT DI META-GOVERNANCE

Prima di archiviare una sessione o esportare un nuovo rilascio di ASTRALIS, verificare:
- [ ] È stata eseguita la rivalutazione esplicita dell'incremento di versione AVF (`V.A.R[.M]`) e convalidata con Luca prima di esportare lo Starter Kit?
- [ ] Il file `GEMINI.md` contiene meno di 250 righe totali?
- [ ] Tutti i link tra nodi documentali sono attivi e utilizzano il formato `file:///`?
- [ ] È stata evitata qualsiasi duplicazione di spiegazioni tra router e moduli?
- [ ] La formattazione è 100% lineare senza tabelle o diagrammi ASCII 2D?
- [ ] Il file è codificato in UTF-8 senza BOM e con interruzioni di riga corrette?

