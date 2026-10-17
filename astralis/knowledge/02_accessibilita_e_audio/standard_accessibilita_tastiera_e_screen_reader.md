# Standard Accessibilità NVDA, Interazione da Tastiera e Zero Mouse
# Autore: Luca (Sviluppatore Senior Non Vedente con Screen Reader NVDA)
# Target AI: Antigravity (Senior AI Pair Programmer & Software Engineer)
# Ambito: Globale / Universale

Questo documento stabilisce le regole e i requisiti tecnici inviolabili per garantire che qualsiasi software, interfaccia, applicazione o script sia al 100% utilizzabile da tastiera con screen reader NVDA.

> **Fonte di Verità Architetturale Upstream**: Repository Ufficiale NVDA Core ([https://github.com/nvaccess/nvda/](https://github.com/nvaccess/nvda/)) — punto di riferimento autorevole per l'architettura dei driver di accessibilità (UIA, IAccessible2, MSAA), librerie controller client (`nvdaControllerClient`), gestione delle code vocali/sintesi e sviluppo addon/plugin.

---

## ⌨️ 1. INTERAZIONE 100% DA TASTIERA (ZERO MOUSE)

1. **Focus Management & Navigazione a Schede (Tab Order)**:
   - Ogni elemento interattivo (pulsanti, campi testo, liste, menu a discesa) deve essere raggiungibile tramite `Tab` e `Shift+Tab`.
   - L'ordine di tabulazione deve seguire la sequenza logica di lettura (da sinistra a destra, dall'alto al basso).
   - Nessun controllo deve "intrappolare" il focus della tastiera (zero keyboard trap).

2. **Scorciatoie Rapide & Access Keys**:
   - Fornire tasti di scelta rapida con `Alt+[Lettera]` per tutti i comandi principali.
   - Supporto completo per il tastierino numerico (Numpad) per movimenti, mappe a griglia o navigazione a blocchi.

3. **Ruoli e Stati Accessibili (WCAG & Accessibility APIs)**:
   - Utilizzare correttamente ruoli e proprietà semantiche native (`wx.Button`, `wx.TextCtrl`, MSAA / IAccessible2 / UIA).
   - Notificare esplicitamente i cambi di stato (es. selezionato/deselezionato, espanso/compresso, caricamento completato) tramite eventi di sistema o API vocali.

---

## 🔊 2. COMUNICAZIONE DIRETTA CON NVDA

1. **Libreria `nvdaControllerClient`**:
   - Negli ambienti C/C++ o Python, per inviare notifiche vocali immediate o silenziose, utilizzare la DLL `nvdaControllerClient.dll`:
     - `nvdaController_speakText(const wchar_t* text)`: Pronuncia immediata della stringa.
     - `nvdaController_brailleMessage(const wchar_t* text)`: Invio su display Braille.
     - `nvdaController_cancelSpeech()`: Interruzione immediata della voce per evitare code di sintesi.

2. **Gestione dei Messaggi Multipli**:
   - Evitare l'inondazione di eventi vocali (speech spam). Se si verificano molti eventi consecutivi, raggrupparli o dare priorità all'evento più recente.

3. **Il Canone "Single-Voice-Authority & Purge-on-Close"**:
   - *Unica Autorità Vocale (Zero Chiamate Dirette Disperse)*: Nelle architetture assistive o mod per non vedenti con interfacce multiple o concorrenti, qualsiasi vocalizzazione deve essere intermediata da un unico orchestratore di priorità semantica. È fatto divieto di lasciare entry-point legacy o chiamate dirette non qualificate a `nvdaController_speakText`.
   - *Purge-on-Close Obbligatorio*: Ogni schermata complessa, dialogo narrativo o documento a lettura estesa (libri, registri, terminali, schede descrittive) deve possedere un trigger deterministico di chiusura che invochi lo svuotamento della coda vocale passiva e l'interruzione immediata della sintesi attiva (`nvdaController_cancelSpeech()`), azzerando alla radice l'effetto distorsivo delle "voci fantasma" fuori contesto.

---

## 🖐️ 3. ERGONOMIA A UNA MANO (MANO SINISTRA) PER COMANDI FREQUENTI IN-GAME

1. **Azionamento a Una Mano Senza Attrito**:
   - Per i comandi rapidi di diagnostica, navigazione e scansione che il giocatore deve poter attivare mentre si muove o esplora, la scorciatoia da tastiera estesa deve essere progettata per l'azionamento esclusivo con la **sola mano sinistra** (es. `Alt + B`, `Ctrl + G`).
   - La combinazione deve permettere al pollice di poggiare su `Alt` (o al mignolo su `Ctrl`) e all'indice di raggiungere il tasto bersaglio senza spostare l'avambraccio dalla posizione naturale di riposo della tastiera.

---

## 🎯 4. ONESTÀ PERCETTIVA DELLE GUI: ZERO OPZIONI ORFANE O DECORATIVE

1. **Equivalenza Percettiva dello Screen Reader**:
   - Per un utente vedente, un pulsante grigio o un'opzione cosmetica priva di funzionalità può essere percepita visivamente come un "placeholder" o un'anteprima futura.
   - Per un utente non vedente con screen reader NVDA, ogni controllo navigabile viene annunciato con pari dignità e autorevolezza (es. *"Abilita ducking audio: Casella di controllo attivata"*).

2. **Divieto Assoluto di Controlli Decorativi o Orfani**:
   - È tassativamente vietato esporre in schermate di configurazione o interfacce utente opzioni, cursori o toggle prima che il motore logico sottostante sia effettivamente pronto a interpretarne e applicarne il valore a runtime.
   - Qualsiasi parametro futuro deve rimanere nella documentazione di progettazione e comparire nell'interfaccia utente **esclusivamente insieme al codice reale** che ne traduce lo stato in effetti concreti e verificabili.

---

## 🛡️ 5. INVIOLABILITÀ DELL'INPUT MANUALE RISPETTO AGLI AUTOMATISMI

1. **Non-Ingerenza dell'Automazione sulla Volontà dell'Utente**:
   - Qualsiasi automatismo, guida assistita o guardiano di sicurezza non deve mai annullare, forzare il rilascio o sovrascrivere un'azione derivante da un tasto fisico tenuto intenzionalmente premuto dall'utente (es. tasti modificatori, `Shift`, tasti direzionali).
2. **Principio di Titolarità del Comando (Ownership Token)**:
   - Se un automatismo deve sospendere temporaneamente la propria azione (es. quando l'utente entra in un menu), deve verificare se lo stato attivo era stato imposto dal sistema o se corrisponde a una pressione fisica manuale dell'utente.
   - Il sistema ha l'autorità di revocare **esclusivamente i propri comandi sintetici** (governati da un token di override esplicito). Non deve mai intervenire sulla postura o sullo stato generato dalla mano dell'utente.

---

## 🚪 6. ARCHITETTURA A DOPPIO GUARD NELLE INTERFACCE GRAFICHE & ANTI-GHOST NARRATION

Nelle applicazioni e nei giochi in cui gli eventi da tastiera viaggiano in modo asincrono rispetto al ciclo di vita delle schermate (aperture, transizioni, chiusure rapide con `Esc`):

1. **Prevenzione di Ghost Narrations e Crash da NullPointer**:
   - Transizioni repentine possono far giungere comandi di navigazione a elementi GUI in fase di distruzione o già azzerati a `null`.
2. **Lo Standard del Doppio Guard**:
   - *Guard a Monte*: All'ingresso di ogni gestore di input o navigazione, verificare preventivamente l'effettiva corrispondenza tra la schermata registrata e l'istanza attiva nel client.
   - *Guard a Valle*: Nei metodi operativi di basso livello (spostamento cursore, selezione elementi), inserire controlli difensivi null-safe indipendenti.
3. **Sincronizzazione Atomica del Ciclo di Vita**:
   - Nel tick o loop di aggiornamento dell'interfaccia, resettare lo stato di navigazione non appena la schermata non è più attiva, **prima** di elaborare qualsiasi intervallo o debouncer temporale.

---

## ⌨️ 7. ESCLUSIVITÀ RIGOROSA DEI MODIFICATORI DI INPUT (KEYBOARD MODIFIER SHIELDING)

1. **Il Rischio di Collisione Multi-Layer su Tasti Fisici Condivisi**:
   - Nelle applicazioni accessibili o nei giochi in cui un medesimo tasto fisico primario (es. `W`, `F`, `Space`) viene riutilizzato su diversi livelli funzionali tramite modificatori (es. `Tasto` da solo, `Alt + Tasto`, `Ctrl + Alt + Tasto`, `Shift + Alt + Tasto`);
   - I framework di binding (es. Kuma, GLFW keycallback, librerie input) registrano spesso i modificatori come maschere di bit o array. Se un handler di livello inferiore (es. `Alt + W`) non verifica esplicitamente che `Ctrl` sia assente, la pressione della combinazione complessa (`Ctrl + Alt + W`) farà scattare contemporaneamente o per primo il comando semplice, impedendo l'attivazione del comando combinato o provocando azioni impreviste.

2. **La Regola delle Guardie Esclusive nel Callback**:
   - Ogni gestore di evento da tastiera (`handleInput`, `keyCallback`) deve implementare guardie esclusive categoriche sul set di modificatori fisici attivi:
     - Comando Layer Singolo (`Alt`): verificare `hasAltOnly()` (ovvero `Alt == true && Ctrl == false && Shift == false`);
     - Comando Layer Doppio (`Ctrl + Alt`): verificare `hasControlAndAlt()` (ovvero `Ctrl == true && Alt == true && Shift == false`);
     - Comando Layer Diretto (senza modificatori): verificare `hasNoModifiers()`.
   - Se la combinazione non soddisfa l'esclusività richiesta, il gestore deve ritornare immediatamente `false` per consentire ai gestori successivi della catena di intercettare l'evento.

3. **Disaccoppiamento Semantico tra Macro di Menu e Comandi Diretti di Gioco**:
   - Separare nettamente gli identificatori dei comandi globali di gameplay rispetto alle funzioni di scelta rapida delle interfacce/menu (es. non condividere mai la medesima chiave interna `mod:auto_walk` per l'azione del menu rapido e `mod:other.auto_walk` per il binding di movimento).
   - I file di configurazione utente (`config.json`, `options.txt`) devono assegnare ai comandi non configurati lo stato neutro `unknown` (non assegnato), evitando sovrapposizioni silenziose su tasti di default preesistenti.

---

## 🔢 8. CONVENZIONE TASTIERA PER LISTE ESTESE (> 9 ELEMENTI) ZERO MOUSE

1. **Il Limite dei 9 Tasti Numerici nelle GUI ad Accesso Istantaneo**:
   - Nelle interfacce vocali e a controllo rapido da tastiera (Zero Mouse), quando un elenco di elementi selezionabili cresce oltre le 9 opzioni (es. da 10 a 12 metropoli, circuiti di eventi, banchi suoni o slot di inventario), l'uso di combo-box visive o menu a tendina crea attrito cognitivo per lo screen reader e rallenta l'interazione.
2. **Lo Standard Sequenziale della Riga Superiore**:
   - Per mantenere la selezione istantanea a tasto singolo (Zero Mouse, Zero sub-dialoghi), la mappatura da tastiera QWERTY standard deve adottare la sequenza naturale della riga numerica superiore:
     - Tasti da `1` a `9`: Primi 9 elementi (indici 0..8);
     - Tasto `0`: 10° elemento (indice 9);
     - Tasto `-` (Meno): 11° elemento (indice 10);
     - Tasto `=` (Uguale): 12° elemento (indice 11).
3. **Vantaggi di Accessibilità & Coesistenza**:
   - Libera completamente i tasti alfabetici per i comandi di azione e contesto (es. `M` per Modalità, `B` per Bivio, `S` per Conferma, `Esc` per Uscita).
   - Elimina la necessità di ricorrere a campi di testo di ricerca o filtri secondari per elenchi compatti (10-12 elementi).
   - Fornisce un annuncio vocale lineare immediato per NVDA ad ogni pressione, con feedback acustico di selezione.

---

## ⌨️ 9. PATTERN CANONICO DI NAVIGAZIONE DA TASTIERINO NUMERICO (NUMPAD NAVIGATION PATTERN)

1. **Ergonomia ad una Mano (Mano Destra) su Tastiera Estesa**:
   - Nelle sessioni prolungate di lavoro o di gameplay, l'utente non vedente beneficia grandemente della possibilità di navigare e interrogare l'interfaccia con la sola mano destra posizionata stabilmente sul tastierino numerico (Numpad), lasciando la mano sinistra libera per comandi di sistema o sintesi vocale.
2. **Schema Canonico di Mapping**:
   - **Croce Direzionale Ortogonale**: `KP_8` (Su), `KP_2` (Giù), `KP_4` (Sinistra), `KP_6` (Destra) — replica trasparente delle azioni `ui_up`, `ui_down`, `ui_left`, `ui_right`;
   - **Azionamento & Attivazione**: `KP_ENTER` e `KP_0` (`ui_accept`);
   - **Interrogazione e Focus Audit**: `KP_5` — annuncio vocale immediato dello stato, del testo e della descrizione accessibile del controllo correntemente focalizzato senza alterarne lo stato;
   - **Salto Rapido a Blocchi / Sezioni**: `KP_7` (blocco logico precedente) e `KP_9` (blocco logico successivo);
   - **Silenziamento di Sicurezza (Panic Button)**: `KP_DECIMAL` (Punto / Canc del Numpad) — silenziamento immediato dell'emissione vocale e arresto istantaneo di ogni flusso sonoro;
   - **Parametri Runtime & Velocità**: `KP_ADD` (+) e `KP_SUBTRACT` (-) per modulare velocità, ritmo o stati di pausa.
3. **Guardia Campi di Digitazione (Zero Keyboard Trap)**:
   - Quando il controllo attivo è un campo di testo (`TextBox`, `LineEdit`, `TextEdit`), i tasti del Numpad devono disattivare l'intercettazione dei comandi di navigazione per digitare regolarmente i numeri, garantendo la totale assenza di conflitti tra input dati e mobilità.

---

## 🛑 10. PATTERN UNIVERSALE A11Y — "ZERO FOCUS DROP" (ANTI-DISORIENTAMENTO SCREEN READER)

1. **Il Problema dell'Invisibilità dei Controlli Disabilitati**:
   - In molti framework e motori di gioco (Godot, Qt, wxWidgets, HTML/DOM), impostare la proprietà nativa `disabled = true` rimuove l'elemento dal ciclo di tabulazione o dal percorso di navigazione da tastiera.
   - Per un utente vedente, un pulsante grigio è visibile e comunica un'informazione di stato (es. "funzionalità momentaneamente non disponibile").
   - Per un utente non vedente che naviga con screen reader NVDA tramite tastiera (**Zero Mouse**), il controllo scompare del tutto. Questo genera un forte **disorientamento cognitivo**: l'utente non sa se la funzione manchi dal programma, se sia stata spostata o se si tratti di un'anomalia di caricamento.
2. **La Regola di Zero Focus Drop**:
   - **Mantenimento della Focusabilità**: I controlli inattivi o temporaneamente non azionabili (es. "Carica Partita" in assenza di file salvati, "Incolla" con appunti vuoti, "Avanti" con form incompleto) devono rimanere focalizzabili da tastiera (`focus_mode = FOCUS_ALL`).
   - **Descrizione Semantica Esplicita**: Il nome o la descrizione accessibile del controllo deve comunicare vocalmente e con immediatezza la motivazione dell'inattività (es. *"Carica Partita, Pulsante. Nessun salvataggio trovato su disco"*).
   - **Feedback Non Distruttivo all'Azionamento**: Se l'utente preme `Invio` o `Spazio` sul controllo, il sistema non deve andare in crash né rimanere in un silenzio ambiguo: deve emettere un breve annuncio informativo o un cue acustico discreto che ribadisca il motivo per cui l'azione non produce effetti.

---

## 🔄 11. PATTERN ERGONOMICO ZERO MOUSE — "SAFE LOOP" (FOCUS CHAINING CICLICO CONTINUO)

1. **Il Limite dei Vicoli Ciechi nelle Liste e nei Menu**:
   - Nei menu verticali o orizzontali, arrestare il cursore al raggiungimento dell'ultimo elemento costringe l'utente da tastiera a percorrere l'intera lista all'indietro per tornare all'inizio, creando affaticamento operativo e rallentando il flusso.
2. **Lo Standard del Safe Loop**:
   - In ogni menu principale, barra degli strumenti o elenco sequenziale di comandi, il grafo di navigazione deve essere configurato ad anello chiuso continuo:
     - Dal **primo elemento**, premendo il tasto freccia verso l'alto (o a sinistra) si deve saltare deterministicamente all'**ultimo elemento** della lista;
     - Dall'**ultimo elemento**, premendo freccia verso il basso (o a destra) si deve tornare deterministicamente al **primo elemento**;
   - Questa regola azzera i vicoli ciechi, garantendo un'esperienza di navigazione fluida, simmetrica e priva di attriti per sessioni prolungate.

---

## 🧠 12. PATTERN "SCREEN READER COGNITIVE CLEARANCE" (ISOLAMENTO A TAB E FILTRO A BRANCHE PER DATI ESTESI)

1. **Il Limite degli Elenchi Monolitici ad Alta Densità**:
   - Quando un'interfaccia deve presentare un catalogo esteso di dati eterogenei o un albero evolutivo ad alta granularità (es. decine di competenze, abilità speciali, elenchi completi di tracce o inventari complessi), esporli in un'unica lista piatta a scorrimento sequenziale satura la memoria a breve termine dell'utente con screen reader (**NVDA**).
   - Scorrere dozzine di elementi premendo ripetutamente i tasti freccia genera forte affaticamento cognitivo ed espone al rischio di perdersi o non cogliere la struttura concettuale d'insieme.

2. **La Soluzione Architetturale a 2 Livelli**:
   - **Livello 1 — Segmentazione a Schede Tematiche (Tabs)**:
     - Separare i contesti ortogonali in schede mutualmente esclusive raggiungibili tramite commutazione numerica diretta (es. tasto `1` per Anagrafica/Vitali, tasto `2` per Albero delle Competenze).
     - Ogni tab azzera e ricrea il contesto sonoro e visivo, mantenendo a schermo solo le informazioni pertinenti.
   - **Livello 2 — Filtro Categoriale per Sotto-Branche con Liste Corte**:
     - All'interno della schermata densa, non mostrare tutti i dati contemporaneamente: suddividerli in macro-branche o categorie tematiche (es. Generi, Strumenti, Teoria, Palco, Studio, Business).
     - Consentire la selezione istantanea della branca attiva tramite tasti di scelta rapida mnemoradicali a pressione singola (es. `G`, `S`, `A`, `P`, `T`, `B`).
     - Limitare la lista visualizzata a un numero contenuto di voci (3–7 elementi al massimo), navigabili con frecce Su/Giù e collegamento circolare (*Safe Loop*).
   - **Funzione di Sintesi Panoramica Vocale (`R`)**:
     - Prevedere un tasto dedicato (es. `R`) che pronunci in un'unica stringa sintetica e fluida la panoramica complessiva della branca attiva (conteggio competenze sbloccate, livello medio e stato complessivo), senza costringere l'utente a focalizzare manualmente ogni singolo nodo.




