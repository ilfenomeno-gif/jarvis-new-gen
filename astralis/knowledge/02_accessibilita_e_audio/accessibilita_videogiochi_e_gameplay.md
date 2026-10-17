# Accessibilità nei Videogiochi, Navigazione e Gameplay Accessibile
# Autore: Luca (Sviluppatore Senior Non Vedente con Screen Reader NVDA)
# Target AI: Antigravity (Senior AI Pair Programmer & Software Engineer)
# Ambito: Globale / Universale

Questo documento raccoglie gli standard di game design e le soluzioni tecniche per rendere qualsiasi videogioco o mondo virtuale accessibile e fruibile al 100% da non vedenti.

---

## 🧭 1. SISTEMI DI ORIENTAMENTO E NAVIGAZIONE SPAZIALE

1. **Bussola Vocale Dinamica**:
   - Un tasto dedicato (es. `Numpad 5` o comando rapido) deve vocalizzare istantaneamente l'orientamento cardinale del personaggio:
     - 8 direzioni cardinali: Nord, Nord-Est, Est, Sud-Est, Sud, Sud-Ovest, Ovest, Nord-Ovest.
     - Gradi esatti (0°-359°) su richiesta o per regolazioni fini.

2. **Feedback Sonoro di Movimento & Terreno (Guadagno Dedicato Giocatore)**:
   - I motori di gioco commerciali tendono ad attenuare drasticamente i passi del personaggio (spesso al 15% del volume) considerandoli rumore di fondo.
   - Nelle interfacce accessibili, implementare un canale di amplificazione indipendente (fino a 200%-300%) dedicato esclusivamente al giocatore locale per garantire ritmo di marcia e discriminazione del terreno (legno, pietra, terra, ghiaia, sabbia, lana).
   - Offrire sempre sia la regolazione statica da menu opzioni, sia comandi rapidi da tastiera con modificatori sicuri (es. `Alt + Page Up/Down`) privi di effetti collaterali sulla postura o sul movimento (Zero-Sneak).
   - Feedback acustico distinto per azioni corporee: accovacciarsi (crouch), scattare (sprint), saltare, atterrare e arrampicarsi.

3. **Sonar e Beep di Puntamento Obiettivi**:
   - Sistema di scansione con segnale acustico (ping) modulato in frequenza (pitch più alto = più vicino) e panning stereofonico verso il target, waypoint o porta più vicina.

4. **Navigazione Assistita (AutoWalk) e Disaccoppiamento Posturale (Simmetria Bi-Direzionale)**:
   - Nei motori 3D (Creation Engine, Unity, Unreal), isolare rigidamente il pathing di avanzamento (spostamento su NavMesh/Waypoints) dal controllo cervicale o puntamento dello sguardo (`LookAt`).
   - Evitare l'attivazione di vincoli permanenti di sguardo verso i target di arrivo: tali vincoli costringono il motore di animazione a mantenere la testa o il busto rivolti verso il vecchio bersaglio, inducendo camminate all'indietro ("moonwalk") o scivolamenti laterali ("strafe") nelle marce successive.
   - Implementare barriere sistematiche di rilascio sguardo (`ClearLookAt` o azzeramento del target di orientamento) su tutti i punti cardine dello stato: avvio marcia a piedi, avvio in sella, arresto anticipato (input utente, dialogo, menu), completamento arrivo e ricaricamento salvataggi.
   - Preservare la naturalezza della deambulazione frontale e l'allineamento credibile del modello 3D per gli spettatori normovedenti, mantenendo intatta la libertà di esplorazione per il non vedente.

5. **Virate Discrete a Tempo Reale vs Snap Teletrasportato (Tutela dell'Audio 3D e della Bussola Mentale)**:
   - Nei giochi accessibili, l'esecuzione di virate rapide (90° ortogonali o 180° di inversione rotta) non deve mai avvenire tramite il teletrasporto istantaneo dell'angolo in un singolo frame logico.
   - Il salto secco disorienta gravemente il giocatore non vedente, frammenta il panning acustico 3D e annulla la percezione della rotazione nello spazio.
   - Le virate discrete devono essere implementate come interpolazioni progressive a tempo reale (clamp angolare per unità di tempo), consentendo al contempo la deambulazione sinergica con i tasti di marcia per compiere traiettorie curvilinee fluide e naturali.

6. **Navigazione Assistita su Cavalcature: Disaccoppiamento Tattico/Cinematico e Watchdog di Movimento Effettivo (Anti-Surplace)**:
   - *Disaccoppiamento Strutturale*: La navigazione autonoma per veicoli o cavalcature richiede la netta separazione tra il livello tattico (oracolo di percorso, sequenza nodi NavMesh/waypoint a memoria preallocata $O(1)$) e il livello cinematico (controllo di frame, sterzo fluido, velocità e frenata anticircling su soglia di tolleranza d'arrivo).
   - *Filtri di Clearance e Viabilità*: Gli algoritmi di pathing per cavalcature di grandi dimensioni devono escludere passaggi angusti, pendenze orografiche impraticabili e applicare sonde laterali a ventaglio per dare priorità alle strade battute o maestre.
   - *Watchdog di Movimento Effettivo su Coordinate Nette*: Monitorare costantemente la variazione euclidea delle coordinate reali nel mondo di gioco. Se l'entità impatta contro un ostacolo e rimane ferma per un tempo superiore a una soglia prestabilita (es. $2.0$s) pur avendo la marcia attiva, il sistema deve eseguire un arresto fail-closed immediato, troncare all'istante l'animazione e il loop sonoro di movimento (eliminando l'ingannevole "galoppo da fermo") ed emettere una notifica vocale immediata tramite screen reader.

7. **Resilienza all'Inerzia Fisica dei Runtime nei Controllori di Guida a Ciclo Chiuso (Inertial Filtering & State-Change Resets)**:
   - *L'Isteresi Meccanica dei Runtime Fisici*: Entità dotate di massa o ingombro elevato (cavalcature, veicoli terrestri, imbarcazioni) presentano nei motori fisici (Havok, PhysX, Chaos) un ritardo naturale di circa $200$–$400$ ms nell'applicare i momenti torcenti e completare l'inversione fisica del moto angolare durante brusche sterzate o curve a gomito.
   - *La Fallacia del Watchdog Istantaneo*: Un watchdog cinematico che sorveglia la divergenza angolare (heading error persistente contromano) rischia di scambiare il transitorio inerziale per uno stallo o una deviazione anomala se non è sincronizzato con la cinematica.
   - *I Due Presidi Inviolabili di Resilienza Inerziale*:
     1. *Reset Deterministico su Transizioni di Stato*: Qualsiasi evento cinematico legittimo (avanzamento a nuovo waypoint su rotta curvilinea, cambio di segno del target di sterzata, ingresso in zona morta di tolleranza, riarmo dell'attuatore) deve azzerare immediatamente il contatore di persistenza contromano (`divergence_frames = 0`);
     2. *Taratura Dinamica della Soglia di Persistenza*: La soglia temporale di tolleranza all'errore prima del blocco di sicurezza deve superare deterministicamente il tempo fisico massimo di inversione della rotazione (es. $\sim 400$ ms / $25$ frame a 60 Hz).
   - *Normalizzazione del Raggio di Cattura Terminale*: La tolleranza di arrivo non deve mai essere inferiore alla somma del raggio di ingombro geometrico (bounding radius) dell'entità e dello spazio di frenata alla velocità di crociera, prevenendo l'overshooting terminale e le conseguenti orbite di circling parassite.

8. **Canale Vocale Gerarchico e Coalescenza Bidirezionale Movimento/Raycast**:
   - *Gerarchia a Priorità Semantica*: L'emissione vocale non deve mai sovrapporsi in modo caotico. I messaggi devono essere incanalati attraverso una gerarchia rigida di priorità semantiche (es. Critico/Emergenza > UI Modale > Raycast Diretto/Interazione Mirino > Notifica di Evento > Bussola/Navigazione Continua > Ambiente), con logiche esplicite di troncamento (`Interrupt`), accodamento ordinato (`Queue`) o scarto silenzioso (`DropIfBusy`).
   - *Finestra di Tolleranza del Mirino (Grace Period)*: Il puntamento del mirino su elementi interattivi (porte, oggetti, attivatori, personaggi) deve garantire una finestra di persistenza temporale (es. $500$–$600$ ms) che impedisca a flussi informativi ad alta frequenza (come la lettura continua della direzione di marcia o della bussola) di troncare o soffocare l'annuncio dell'interazione fisica rilevata.
   - *Coalescenza Semantica Bidirezionale all'Arresto del Movimento*:
     1. *Buffer di Smorzamento Movimento (Motion Dampening Buffer)*: All'arresto del movimento cinematico o al completamento di una traiettoria guidata, l'oracolo di navigazione deve inserire una finestra temporale minima (es. $100$ ms) prima di dichiarare l'evento di arrivo, consentendo al motore fisico e al raycast visivo di completare l'aggiornamento geometrico e rilevare la presenza di ostacoli o varchi di destinazione;
     2. *Fusione Retroattiva (Look-Back Coalescence)*: Se nei millisecondi immediatamente precedenti (es. fino a $500$ ms prima dell'arresto) il mirino ha già rilevato e annunciato l'elemento bersaglio terminale (porta d'accesso, contenitore, NPC), l'evento di arrivo non deve emettere una notifica duplicata o isolata, bensì coalescere semanticamente componendo una singola frase fluida ed esaustiva (es. *"Arrivato a destinazione: [Nome Bersaglio]"*);
     3. *Fusione Proattiva (Look-Ahead Fallback)*: Se al momento dell'arresto l'annuncio del mirino non è ancora avvenuto, l'annuncio di arrivo riserva una breve finestra di attesa (es. $200$–$250$ ms): se il raycast rileva il bersaglio in tale intervallo, la sintesi fonde proattivamente l'informazione in un'unica stringa integrata, azzerando inversioni temporali percettive e frammentazione del parlato.

9. **Telemetria Vocale Dinamica in Navigazione Assistita (Densità Metrica Adattiva, Preemption di Partenza & Concisione Situazionale)**:
   - *Prevenzione del Vuoto Sensoriale Informativo*: Durante la locomozione autonoma a lungo raggio in mondi virtuali complessi, il silenzio vocale prolungato ingenera nell'utente non vedente disorientamento e incertezza operativa;
   - *Annuncio Atomico di Locomozione & Preemption del Comando Primario*: All'attivazione del tragitto assistito verso un target da comando utente (tastiera/gamepad), l'annuncio deve essere emesso come unico blocco indivisibile (*"In cammino verso [Nome Bersaglio], [Rotta Cardinale], [Distanza] metri"*). Per scongiurare drop acustici silenti causati da descrizioni prolungate di strumenti di scansione/consultazione attiva, l'avvio della locomozione deve avere priorità paritetica o superiore con politica `InterruptLowerOrEqual`, preceduta dall'azzeramento del grace period del mirino (`ResetCrosshairHold`), cancellando all'istante qualsiasi voce residua e confermando l'aggancio in modo immediato e certo;
   - *Canone di Densità Metrica e Isteresi Unidirezionale*:
     - La distanza residua deve essere comunicata a soglie decrescenti dense (es. step di 50 metri per distanze > 200m, step di 25 metri tra 50m e 200m, e gradini di arrivo a 25m e 10m);
     - *Isteresi Monotona Discendente*: L'indice di soglia scende soltanto; eventuali allontanamenti temporanei (aggiramento ostacoli, tornanti orografici) non devono mai riarmare verso l'alto le soglie già superate, azzerando le ripetizioni parassite;
   - *Concisione Situazionale della Rotta (Tratte Lunghe vs Avvicinamento Finale)*:
     - Nei cambi di direzione durante la marcia, differenziare la telemetria in base alla scala residua: su tratte lunghe ($\ge 50$m o macro-spostamenti) emettere l'annuncio combinato *"Rotta + Distanza Residua"* (es. *"Nord-Ovest, 150 metri"*) per consentire al non vedente di tracciare le curve del percorso; su tratte brevi ($< 50$m) e in avvicinamento terminale emettere la sola rotta concisa (*"Nord-Est"*), preservando il canale libero per i passi, i segnali sonori 3D e l'interazione del mirino;
   - *Coalescenza Atomica Rotta-Distanza*: Quando una virata coincide temporalmente con il varco di una soglia metrica decrescente (entro una finestra di $\sim 180$–$250\text{ ms}$), gli eventi coalescono in un'unica emissione integrata, dimezzando il parlato dello screen reader ed eliminando frammentazioni cognitive;
   - *Subordinazione Tattica in Marcia*: Durante la corsa a rotta stabilita, la telemetria continua deve operare a priorità subordinata e politica `DropIfBusy`, lasciando campo immediato e assoluto alle interazioni fisiche del mirino, notifiche di stato e allarmi vitali.

10. **Schermatura Modale Universale a Camera Anecoica, Pattern Canonico di Scorrimento, Allarmi Vitali Tattici e Tutela della Riservatezza**:
   - *Isolamento a Camera Anecoica delle Interfacce Sincrone*: Durante l'apertura di qualsiasi interfaccia sincrona o modale (inventari, loot, commercio, alberi di progressione/abilità, diari di missione, opzioni di dialogo con NPC, mappe a marcatori, minigiochi, menu di sistema o pannelli di configurazione), istituire uno scudo a monte che scarta istantaneamente tutti i flussi sonori/vocali continui a bassa priorità (passi ambientali, bussola cardinale a 45°, notifiche asincrone di eventi o mirino). Nessun rumore parassita deve disturbare la consultazione, la lettura narrativa o il conteggio di risorse. Alla chiusura dell'interfaccia, i canali sensoriali di esplorazione 3D devono ripristinarsi in modo deterministico e immediato;
   - *Pattern Canonico Titolo/Dettagli & Svuotamento Atomico della Coda (Anti-Ghost Queue)*: Nelle liste o negli alberi scorsi tramite tasti freccia, il titolo o nome dell'elemento selezionato deve avere politica di interruzione immediata (`Interrupt`), mentre le statistiche, descrizioni estese, obiettivi secondari e valori devono essere accodati con politica differita (`Queue`). Per prevenire il fenomeno delle "code fantasma" (accumulo in ritardo di descrizioni di elementi già superati durante una navigazione veloce), ogni nuova interruzione deve svuotare istantaneamente e atomicamente l'intera coda passiva;
   - *Tutela della Riservatezza e Mascheramento Credenziali (Zero-Leak Logging)*: Nelle schermate di autenticazione o nei campi di input utente per screen reader (es. login di rete, sincronizzazione cloud, token API), l'eco vocale per l'utente non vedente deve essere rigidamente disaccoppiato dalla telemetria di debug. Ogni canale di parlato deve supportare un flag di riservatezza (`isPrivate = true`) che inibisce la persistenza del testo nei log su disco o nei report diagnostici, mascherando i campi password con suoni discreti o conteggio caratteri, azzerando alla radice rischi di fughe di credenziali;
   - *Preemption Tattica Assoluta per Allarmi Vitali (Health Alert, Inabilitazione Fisica)*: Gli eventi di sopravvivenza critica (salute sotto la soglia di emergenza $\le 25\%$, paralisi, stordimento, individuazione furtiva) devono possedere priorità assoluta di emergenza, interrompendo qualsiasi parlato in corso — inclusa la voce delle interfacce grafiche/menu aperti. Devono essere protetti da un cooldown temporale (es. 3.000 ms) e da un'isteresi di riarmo (es. risalita $> 30\%$) per scongiurare spam e saturazione del canale acustico.

11. **Keyboard Preemption su Puntamento Passivo (Reset Grace Period) e Classificazione Semantica Notifiche HUD**:
    - *La Preemption dell'Input Intenzionale su Raycast Passivo*: Nei mondi virtuali in cui coesistono il puntamento passivo della telecamera (raycast continuo su oggetti inquadrati casualmente durante il movimento) e l'interrogazione attiva dell'ambiente (scanner da tastiera per categorie, lock bersagli, bussola istantanea), l'input esplicito da tastiera esprime intenzione cognitiva diretta dell'utente. Esso deve azzerare istantaneamente e atomicamente qualsiasi finestra di rispetto o grace period armata dal mirino passivo prima di emettere l'annuncio (`ResetCrosshairHold`), garantendo che il feedback vocale sia immediato al tocco e immune da micro-movimenti della telecamera o raycast concorrenti;
    - *Classificazione Semantica delle Notifiche di Gameplay (Transitorie vs Cumulative)*:
      1. *Notifiche Transitorie di Stato*: Cambi di postura, tutorial, scoperte geografiche, interrogazioni di parametri vitali devono adottare la politica di interruzione immediata (`InterruptLowerOrEqual`), affinché l'utente apprenda tempestivamente l'ultimo stato valido;
      2. *Notifiche Cumulative e Informative*: Aggiornamenti di quest/obiettivi, ricarica abilità, risorse equipaggiate, eventi di attivazione leve/porte/meccanismi devono adottare la politica di accodamento ordinato (`QueueIfBusy`) in un buffer bounded FIFO, garantendo che nessun dettaglio informativo o sonoro di rilievo vada perduto;
      3. *Schermatura a Monte nei Menu*: Tutte le notifiche di gameplay devono essere soggette a sbarramento silente a monte a costo zero durante la consultazione delle interfacce sincrone o dei menu modali.

12. **Simmetria Posturale Silenziosa nella Navigazione Assistita, Proximity Halt Watchdog & Neutralizzazione Hardware Input**:
    - *Neutralizzazione Hardware a Monte (Early Event Consumption)*: Quando un comando di accessibilità adotta scorciatoie composite con modificatori (es. `Alt + [Tasto]`, `Ctrl + [Tasto]`), l'elaborazione deve intercettare e consumare fisicamente l'evento nel chain di input del sistema a monte della vtable o del dispatcher vanilla del motore. Se l'evento non viene consumato alla radice (es. `NeutralizeEvent`), il tasto base si propaga ai componenti sottostanti scatenando finestre o azioni parassite indesiderate (es. menu Attendi/Riposa);
    - *Watchdog di Prossimità d'Arresto su Ostacoli a Collisione Bassa (Proximity Halt Watchdog)*: Nei sistemi di navigazione su NavMesh verso target con geometrie complesse o collisioni fisiche irregolari (arredi bassi, bauli, ceppi da taglio), l'ingombro geometrico può impedire al personaggio di raggiungere la distanza teorica di stop ($D \le D_{stop}$). Se il personaggio si trova all'interno di una sfera di prossimità estesa ($D \le D_{stop} + \Delta$) e la velocità residua è nulla o stazionaria per un tempo minimo di sicurezza ($\ge 1.0$s), l'arresto deve essere dichiarato con successo in modo deterministico via watchdog, azzerando gli stalli a 2 metri;
    - *Simmetria Posturale Silenziosa (Partenza vs Arrivo)*:
      1. *Livellamento Silenzioso alla Partenza*: Quando la marcia assistita viene avviata e la rotta calcolata con successo, il sistema deve verificare l'inclinazione verticale (pitch) dello sguardo. Se il personaggio guarda a terra o in alto ($|pitch| > 3^\circ$), lo sguardo deve essere livellato all'orizzonte ($0.0^\circ$) istantaneamente e in modo completamente silenzioso (zero TTS). Nessun feedback vocale ("Sguardo livellato") deve essere emesso, per non sporcare il canale vocale e consentire la limpida pronuncia dell'annuncio di partenza, assicurando al contempo un raggio mirino orizzontale ottimale;
      2. *Orientamento Mirino all'Arrivo*: Al completamento della marcia, il pitch e lo yaw della telecamera devono puntare automaticamente il centro 3D dell'oggetto bersaglio con finestra di coalescenza vocale estesa (es. $400$ms), consentendo al non vedente l'interazione immediata da tastiera (`E`/`G`) senza dover muovere manualmente la visuale.

---

## 🤖 2. SCANSIONE SCENARIO & INTEGRAZIONE VISIONE/IA

1. **Scansione dello Scenario su Richiesta**:
   - Funzionalità per catturare l'inquadratura attuale ed elaborare tramite IA/riconoscimento visivo l'elenco ordinato degli oggetti, nemici, ostacoli e punti di interesse presenti nel campo visivo.
2. **Modalità Esplorazione a Griglia / Blocchi**:
   - Per giochi strategici o RPG, supporto alla navigazione a celle logiche con sintesi vocale che descrive il contenuto della cella selezionata e le adiacenze.

---

## 🎯 3. SEMANTICA NATURALE DEI VETTORI SPAZIALI PER SCREEN READER

1. **Formule Vettoriali Lineari Dirette**:
   - Nella vocalizzazione delle posizioni relative (target, POI, nemici, NPC, waypoint), evitare tassativamente frammentazioni telegrafiche o calchi letterali dall'inglese (es. *"5 lontano dai blocchi"*).
   - Utilizzare formule vettoriali naturali relative all'orientamento del giocatore:
     - Formato: `"[Nome Bersaglio]: X [unità] avanti/indietro, Y in alto/basso, Z a sinistra/destra"`.
2. **Priorità Cognitiva e Sintesi**:
   - Collocare prima l'asse di avanzamento (avanti/indietro), poi il dislivello (in alto/in basso) e infine l'azimut laterale (a sinistra/a destra) per consentire al giocatore di orientarsi immediatamente senza dover ricalcolare la traiettoria a mente.

---

## 🎧 4. PROPAGAZIONE ACUSTICA REALISTICA & OCCLUSIONE MATERIALE (VOXEL/MESH)

1. **Il Paradosso della Vicinanza Sonora**:
   - Nei motori di gioco 3D privi di occlusione fisica, i suoni esterni attraversano pareti piene senza smorzamento, generando nel giocatore non vedente la falsa percezione che il mob/bersaglio sia nella stessa stanza a portata di mano.
2. **Gradiente Acustico Multi-Livello per Densità di Materiale**:
   - Calcolare l'assorbimento acustico lungo il raggio 3D (raycast tra occhi del giocatore e sorgente sonoro):
     - **Divisori Leggeri / Porosi** (porte, botole, lastre, vetri): attenuazione leggera ($-10\%$).
     - **Materiali Lavorati Standard** (legno, scale, casse, terra): attenuazione media ($-18\%$).
     - **Materiali Massicci / Fibrosi** (tronchi massicci, ceppi): attenuazione marcata ($-28\%$).
     - **Muratura Minerale** (pietra, mattoni, metalli standard): attenuazione forte ($-38\%$).
     - **Roccia Ultra-Densa / Metalli Pesanti** (ossidiana, deepslate, bedrock): attenuazione quasi totale ($-50\%$).
3. **Floor Minimo di Rilevabilità Acustica (1% / 0.01f)**:
   - Il volume finale attenuato non deve mai scendere al di sotto della soglia minima garantita dell'**$1\%$ (`0.01f`)**, per assicurare che il target rimanga sempre rilevabile a livello subliminale o con cuffie ad alta dinamica senza creare 'buchi' informativi.
4. **Sinergia Audio-Vocale**:
   - In presenza di occlusione significativa ($\ge 20\%$), abbinare all'attenuazione sonora un qualificatore vocale discreto (es. *" (oltre parete)"* o *" (dietro ostacolo)"*).

---

## 🌊⚔️ 5. PREVENZIONE FALSI ALLARMI IN AMBIENTI FLUIDI & THREAT SENTINEL PER LA SOPRAVVIVENZA

1. **Il Paradosso dei Fluidi nei Rilevatori di Cadute e Burroni (Fluid Safety Guard)**:
   - Nei motori di gioco 3D e voxel (es. Minecraft, Skyrim, Unreal/Unity), i blocchi fluidi (acqua, corsi d'acqua, fiumi, mare) hanno volume di collisione solida nullo (`collision shape` vuoto).
   - Un algoritmo di prevenzione cadute non consapevole dei fluidi attraversa l'intera colonna d'acqua fino al fondale roccioso, interpretando il volume d'acqua come un burrone mortale. Questo genera loop continui di allarmi vocali a raffica che saturano e ammutoliscono lo screen reader, lasciando il giocatore cieco di fronte ai pericoli reali.
   - **Regola Universale di Fluid Safety**:
     - Monitorare tutti gli stati fluidi dell'entità giocatore (`isInWater`, `isEyeInFluid`, nuoto a pelo d'acqua, galleggiamento) per sospendere all'istante gli allarmi di caduta.
     - Nei calcoli di dislivello, la presenza di uno stato fluido (`FluidState` non vuoto) lungo la traiettoria o sul fondo deve essere sempre valutata come **atterraggio morbido sicuro (`drop = 0`)**.
2. **Threat Sentinel (Allarme Minacce Ravvicinate Prioritario)**:
   - Durante le fasi notturne, dungeon o ambienti ostili, i nemici aggressivi (`Enemy` / mob ostili) che entrano nel raggio critico di ingaggio (entro 6 metri/blocchi) devono innescare un canale di allerta dedicato:
     - **Segnale Acustico 3D Percussivo**: Avviso sonoro posizionale immediato per stimolare il riflesso rapido.
     - **Vocalizzazione Prioritaria Interruttiva**: Annuncio telegrafico del tipo di minaccia e della coordinata vettoriale relativa (*"Attenzione: [Nemico] X metri avanti/indietro, Y in alto/basso, Z a sinistra/destra"*).
3. **Navigazione Guidata a Step con Gestione Porte e Varchi (AutoOpen & AutoClose)**:
   - Nei percorsi calcolati da un autopilota o guida passo-passo:
     - In presenza di una porta, botola o cancello chiuso lungo il tragitto, il movimento automatico deve arrestarsi a distanza di sicurezza (1.5-2 metri), orientare la visuale UNA SOLA volta verso il varco e invitare esplicitamente il giocatore all'interazione (*"Porta chiusa davanti a te. Premi [Tasto Interazione] per aprire"*).
     - Non appena il varco viene aperto, il sistema conferma l'azione (*"Porta aperta. Procedi verso [Target]"*) e riprende automaticamente la marcia.
   - **AutoClose a Soglia Geometrica (Zero Rotazione)**:
     - Quando il giocatore attraversa completamente il varco superando la soglia geometrica di sicurezza ($d_{\text{centro blocco}} \ge 0.90\text{ m}$), il sistema invia programmaticamente il comando di chiusura (`useItemOn` / interazione diretta) senza ruotare la visuale del giocatore (Principio di Intangibilità della Bussola Mentale — Sezione 19).
     - Esclusione rigorosa di porte o botole di metallo/ferro azionabili solo da meccanismi esterni.

---

## 🔍 6. SONDE VIRTUALI DI CAMMINO (PATH LOOK-AHEAD PROBES) & MODELLO A 3 LIVELLI DI VERBOSITÀ

1. **Il Ruolo della Sonda Virtuale di Cammino**:
   - Nei giochi 3D/Voxel, consentire al giocatore di esplorare in anticipo le direttrici cardinali e relative (Avanti nello sguardo, Dietro alle spalle, Nord, Sud, Ovest, Est, Diagonali) per conoscere calpestabilità, dislivelli, terreno e ostacoli prima di muoversi.
2. **La Triade dei Livelli di Verbosità**:
   - **`SUMMARY_ONLY` (Sintesi Istantanea a 1 Tocco)**: Informa solo se il cammino è libero o qual è il primo ostacolo di blocco (es. *"Nord: bloccato a 6 metri da Muro di pietra su Blocco d'erba"*).
   - **`COMPACT` (Operatività Quotidiana — Default)**: Comunica la lunghezza del primo tratto sicuro, il materiale del suolo calpestabile, le risorse/creature incontrate nel tratto e il primo ostacolo.
   - **`DETAILED` (Mappatura Spaziale Continua a Pieno Raggio)**: Non si arresta al primo ostacolo; prosegue fino alla fine del raggio impostato per descrivere l'intera sezione spaziale (tratti liberi, ostacoli attraversati, cambi di quota/gradini $\Delta Y$ e tutte le risorse/mob presenti).
3. **Campionamento Combinato di Entità e Blocchi Pianta Non-Solidi**:
   - Gli ortaggi, le colture e le piante commestibili hanno collisione vuota per consentire il passaggio fisico del giocatore: non devono essere ignorati come semplice aria vuota ma campionati a quota piedi e segnalati come risorse raccoglibili.
4. **Isolamento dei Modificatori & Prevenzione Conflitti con Mod Esterne**:
   - Evitare lettere alfabetiche contese da utility/motori grafici (es. shader, menu esterni); preferire le frecce direzionali o griglie numeriche isolate con modificatori composti espliciti (`Ctrl + Alt`).

---

## 🛡️ 7. SICUREZZA ANTICADUTA A DUE ZONE & FEEDBACK DI CONTATTO A BARRIERA ATTIVA (EDGE BUMP)

1. **Il Principio di Non-Degradazione della Marcia (Due Zone di Sicurezza)**:
   - Nei motori 3D/Voxel, i sistemi di assistenza fisica alla postura (es. auto-accovacciamento / auto-sneak anticaduta) non devono mai essere attivati alla stessa distanza della pre-allerta informativa.
   - **Zona 1 (Informativa / Pre-Allerta)**: A 2-4 metri dal baratro, avvisare con segnali sonori 3D e voce, e interrompere l'eventuale sprint per evitare slanci incontrollati. La camminata standard dell'utente rimane libera e a piena velocità.
   - **Zona 2 (Fisica / Bordo Immediato)**: Sul blocco confinante con il vuoto ($\le 0.85\text{ metri}$), attivare l'accovacciamento forzato per bloccare fisicamente il passo fatale tramite la fisica del motore di gioco.
2. **Disimpegno Istantaneo e Non-Interferenza Posturale**:
   - Se l'utente orienta i comandi in direzione opposta (retromarcia) o verso terreno solido, la postura di sicurezza deve essere rilasciata all'istante senza attrito né tempi di attesa.
3. **Feedback di Contatto a Barriera Attiva (Debounced Contact Bump)**:
   - Quando una barriera invisibile o un automatismo blocca il movimento dell'utente, l'insistenza sui comandi di marcia verso l'ostacolo non deve risultare muta (che darebbe la falsa impressione di tasti non funzionanti).
   - Emettere un riscontro sonoro 3D percussivo e un avviso vocale dedicato (*"Sul ciglio del dislivello, avanzamento protetto"*) con un debouncing temporale calibrato (es. $1.5\text{ secondi}$).
4. **Validazione Continua delle Strutture di Discesa Verticale**:
   - Riconoscere le vie di discesa sicure (scale a pioli, liane, corde, colonne d'acqua, atterraggi morbidi) scansionando la colonna verticale verso il basso per non bloccare mai le discese intenzionali.
5. **Chiusura della Fuga Verticale nei Sistemi di Protezione Ciglio (Anti-Jump Bypass)**:
   - Nei motori di gioco 3D (come Minecraft, Unreal, Unity), i vincoli di attrito orizzontale o raycast sul bordo agiscono quasi sempre solo quando l'entità è a contatto con la superficie calpestabile (`onGround == true`).
   - Se il giocatore preme il tasto di salto mentre è trattenuto sul ciglio, l'impulso verticale stacca il personaggio dal suolo e l'inerzia aerea supera la barriera facendolo precipitare.
   - **Regola Universale**: Quando un sistema di assistenza anticaduta o barriera fisica è attivo sul ciglio, **neutralizzare l'impulso fisico di salto alla radice** (intercettando il metodo di generazione della spinta verticale), mantenendo l'entità incollata a terra finché non si disimpegna o disattiva intenzionalmente la protezione.

---

## 🎯 8. UNIFICAZIONE ATOMICA DI PUNTAMENTO & ORIENTAMENTO (PATTERN TOKEN COMPOSITION & ORDERING ENUM)

1. **La Race Condition nei Sottosistemi di Puntamento e Telecamera**:
   - Nei giochi 3D/Voxel, i moduli di raycast continuo del mirino (cosa c'è sotto il reticolo) e i controller di rotazione della visuale (in che direzione guardo) operano spesso su loop indipendenti.
   - Se ciascun modulo invoca autonomamente la sintesi vocale con interruzione immediata (`interrupt: true`), la rotazione genera un troncamento vocale continuo e caotico (la voce legge l'angolo e viene tagliata dal blocco, o viceversa).

2. **Il Pattern Token Composition & Ordering Enum**:
   - Invece di moltiplicare all'infinito le costanti Enum per ogni combinazione possibile, suddividere il feedback in **token atomici indipendenti**:
     - Bersaglio/Entità (toggle booleano).
     - Distanza metrica (toggle booleano con gestione singolare/plurale).
     - Punto cardinale orizzontale (toggle booleano).
     - Gradi bussola $0^\circ..359^\circ$ (toggle booleano).
     - Inclinazione verticale/Pitch (toggle booleano per percepire la quota).
   - Governare la sequenza con un **Enum di Ordinamento Strutturale** (`TARGET_FIRST`, `ORIENTATION_FIRST`, `TARGET_CARDINAL_INLINE`).

3. **Debouncing & Sincronizzazione di Stato**:
   - Quando la telecamera ruota, il manager campiona istantaneamente sia la nuova direzione sia il bersaglio attuale, emette un'unica frase atomica e imposta una finestra di soppressione/sincronizzazione (80-100ms) sul loop continuo, azzerando il rumore e garantendo la massima fluidità con lo screen reader.

---

## 🎛️ 9. FEEDBACK ATOMICO SU CAMBI CONTESTO GUI, STATISTICHE DINAMICHE & BOUNDARY GATING

1. **Il Principio di Prevenzione delle "Silent Actions"**:
   - In un'interfaccia grafica (GUI), il cambio di categoria, scheda, pagina o filtro produce una trasformazione visiva immediata ma è completamente muto per lo screen reader a meno che non sia esplicitamente sonificato e vocalizzato.
   - Un'azione di cambio scheda che aggiorna solo gli elementi a schermo senza annunciare il nuovo stato lascia il giocatore non vedente disorientato e privo di feedback di conferma.

2. **La Triade di Feedback Coordinato per i Cambi di Stato**:
   - **Audio Cue Istantaneo**: Click sonoro dedicato per confermare fisicamente l'avvenuto azionamento del comando.
   - **Vocalizzazione Atomica del Nuovo Contesto**: Annuncio esplicito del nuovo stato (es. *"Categoria: [Nome]"*, *"Pagina [X] di [Y]"*).
   - **Auto-Posizionamento del Focus (Smart Focus Relocation)**: Spostamento automatico del cursore/focus logico sul primo elemento interattivo utile del nuovo contesto con lettura del suo contenuto, evitando che il puntatore rimanga fermo su coordinate o elementi appartenenti al contesto precedente.

3. **Il Pattern della Narrazione a 3 Livelli Atomici per GUI e Griglie Filtrabili**:
   - Nelle interfacce complesse (ricettari, elenchi di fabbricazione, inventari filtrabili):
     - *Livello 1 — Contesto & Stato*: Enunciazione del contesto corrente (Categoria, Pagina o Filtro applicato).
     - *Livello 2 — Statistiche Aggregate di Pagina*: Sintesi quantitativa immediata con concordanza grammaticale singolare/plurale:
       - Miste: `"[T] elementi: [R] disponibili, [N] non disponibili"` (es. *"15 ricette: 1 realizzabile, 14 non realizzabili"*).
       - Tutte disponibili: `"[T] elementi disponibili"` (o *"1 elemento disponibile"*).
       - Nessuna disponibile: `"[T] elementi non disponibili"` (o *"1 elemento non disponibile"*).
     - *Livello 3 — Dettaglio Elemento Puntato*: Lettura istantanea dell'elemento su cui è stato automaticamente riposizionato il cursore.

4. **Gestione Semantica dei Limiti di Paginazione (Boundary Gating)**:
   - Quando un utente tenta di avanzare oltre l'ultima pagina o retrocedere prima della prima pagina:
     - **Zero Azioni a Vuoto**: Non inviare eventi click di scorrimento ridondanti o non ammessi.
     - **Feedback Semantico Specifico**: Distinguere esplicitamente tra *"Prima pagina"*, *"Ultima pagina"* e *"Unica pagina"*.
     - **Riaffermazione del Focus**: Riaffermare il posizionamento del cursore sul primo elemento utile della pagina corrente con lettura immediata.

5. **Navigazione Universale a Frecce Direzionali (Dual-Binding Ergonomico)**:
   - In tutte le schermate a lista o a matrice di celle, offrire il doppio canale di input: tasti alfanumerici dedicati per la mano destra + le 4 Frecce Direzionali per la navigazione a una mano.
   - Mantenere il disaccoppiamento rigoroso con i campi di testo: se la casella di ricerca è a fuoco, le frecce pilotano il testo; quando defocalizzata (es. con `Invio`), tornano a pilotare le celle.

---

## ⚡ 10. REATTIVITÀ CONTAINER SPECIALISTICI & AUTO-FOCUS DINAMICO SU EVENTI DI TRASFORMAZIONE

1. **La Sfida dei Container a Trasformazione Asincrona o Condizionale**:
   - Nelle schermate specialistiche (banchi di taglio/tagliapietre, telai per stendardi, fornaci, alambicchi, banchi di ricerca), gli elementi interattivi o le opzioni di scelta non esistono finché il giocatore non inserisce i reagenti/ingredienti necessari, oppure compaiono solo al termine di una barra di caricamento (cottura o distillazione).
   - Senza listener dedicati, il giocatore non vedente non sa quando o quante opzioni sono disponibili, ed è costretto a navigare manualmente alla cieca tra gruppi vuoti.

2. **Il Pattern Tracciamento Differenziale & Auto-Focus (`selectGroupByKey`)**:
   - **Rilevamento del Delta di Stato**: Campionare lo stato del contenitore ad ogni tick o evento GUI (es. $N > 0 \land N_{\text{prev}} == 0$);
   - **Vocalizzazione Quantitativa Immediata**: Annunciare subito le opzioni sbloccate (es. *"%d forme disponibili per il taglio"*, *"%d motivi disponibili per lo stendardo"*);
   - **Smart Focus Relocation sul Gruppo Attivo**: Rigenerare l'albero dei gruppi di navigazione e posizionare automaticamente il focus logico e il puntatore sul primo elemento sbloccato (`recipes` o `output`), consentendo la selezione immediata da tastiera o 4 frecce senza passaggi intermedi a vuoto.

3. **Notifiche Discrete di Fine Ciclo (Discrete Cycle Finish Notices)**:
   - Per lavorazioni asincrone continue (es. fornaci, alambicchi, code di fabbricazione), monitorare il timer di avanzamento e notificare discretamente il completamento (*"Cottura completata"*, *"Distillazione completata"*) con priorità non bloccante (`interrupt: false`), preservando la leggibilità delle altre informazioni in corso senza creare sovrapposizioni sgradevoli.

---

## 🧠 11. TUTOR CONTESTUALE (CONTEXTUAL MENTOR) & KEYBINDING INTROSPECTION A RUNTIME

1. **Il Ruolo del Tutor Vocale Non Invasivo**:
   - Nei giochi complessi o sandbox, i giocatori non vedenti possono trovarsi temporaneamente disorientati (fermi da tempo, bloccati contro un ostacolo, al buio, affamati). Un sistema di tutoraggio contestuale discreto analizza periodicamente lo snapshot del giocatore ed eroga suggerimenti proattivi dotati di cooldown e rintocco acustico delicato.

2. **Contestualizzazione Spaziale Dinamica dell'Impatto**:
   - Non utilizzare frasi statiche ("Hai un ostacolo di fronte"): analizzare i vettori di input attivi al momento della collisione (assi WASD / joystick) per determinare la direzione effettiva di impatto (*"a sinistra"*, *"a destra"*, *"davanti"*, *"dietro"*).

3. **Pattern Keybinding Introspection (Risoluzione Dinamica dei Tasti)**:
   - **Zero Hardcoding di Tasti nei Testi**: I testi dei suggerimenti non devono mai contenere nomi fissi di tasti (es. *"Premi Spazio"* o *"Premi Alt+V"*), poiché il giocatore potrebbe aver riconfigurato i comandi nel menu Opzioni.
   - **Introspezione a Runtime**: Il motore di mentoring estrae dinamicamente la mappatura reale associata all'azione interrogando il mapper di input del gioco (es. Kuma API, KeyMapping vanilla, GLFW) e formattando modificatori (`Alt`, `Ctrl`, `Shift`) e nome del tasto in una stringa leggibile.
   - **Formato Strutturato & I18N Pulito**: Passare sempre i tasti risolti come argomenti formattabili al resolver di lingua (es. `I18n.get("rule_key", dir, jumpKey, inspectKey)`), evitando doppie valutazioni non sincronizzate che potrebbero generare artefatti di formato (*"Format error:"*).

---

## 🏃 12. GEOMETRIA DELLE HITBOX & CALIBRAZIONE SALTO NEI SISTEMI DI AUTONAVIGAZIONE VOXEL

1. **Il Paradosso della Distanza Minima di Collisione**:
   - Nei motori di gioco basati su griglia voxel (es. Minecraft), i blocchi hanno coordinate di centro a $(X+0.5, Z+0.5)$.
   - Quando l'entità del giocatore approccia un gradino solido di altezza $+1$, la collisione fisica della hitbox (es. raggio $0.3\text{ m}$) contro la parete (distante $0.5\text{ m}$ dal centro) arresta il movimento a una distanza orizzontale euclidea di contatto:
     $$d_{\text{collision}} = 0.5 + 0.3 = 0.80\text{ metri (fino a 1.0 m per approcci angolari)}$$
2. **Regola di Calibrazione del Salto nel Pilota Automatico**:
   - Non imporre mai soglie di distanza inferiori alla distanza fisica di collisione (es. $d < 0.65\text{ m}$), poiché richiederebbero una compenetrazione fisica impossibile all'interno del blocco solido.
   - Impostare una finestra di approccio naturale ($d \le 1.25\text{ m}$) abbinata all'ascolto della collisione fisica orizzontale (`horizontalCollision`), con impulso di salto sostenuto (almeno $200\text{ ms}$ / 4 tick) per superare il gradino senza arresti né micro-salti falliti.

---

## 🕹️ 13. AUTO-FOCUS PROATTIVO SUI MENU DI PAUSA (`Esc`) & ZERO PRE-FOCUS

1. **Il Problema dell'Elemento Non Focalizzato**:
   - Nei motori di gioco grafici, quando il giocatore preme il tasto di pausa/uscita (`Esc`), la finestra modale si apre ma spesso nessun widget possiede il focus della tastiera se il puntatore del mouse era dislocato in un'area neutra.
   - Questo costringe l'utente non vedente a premere un tasto di pre-focus (es. `Tab`) prima che le frecce direzionali possano scorrere le opzioni.
2. **Il Pattern di Iniezione Auto-Focus Proattivo (`ensureInitialFocus`)**:
   - All'apertura di una schermata di menu o di pausa:
     1. Spostare il cursore del mouse in una posizione neutrale (es. coordinate di sicurezza $10, 10$);
     2. Assegnare immediatamente il focus logico al primo elemento interattivo valido (`AbstractWidget` attivo e visibile);
     3. Emettere l'evento di accessibilità per lo screen reader e sbloccare all'istante la navigazione con le frecce direzionali (Zero Mouse & Zero Pre-Focus).

---

## 👣 14. SONAR DI CADENZA PODOMETRICA, AGGANCIO MICRO-VOXEL & DISPACCIAMENTO DIRETTO

1. **Il Principio del Sonar Podometrico di Parete**:
   - Quando un giocatore non vedente si muove lungo una superficie o parete uniforme (es. corridoi di legno, mura di pietra), non sopprimere l'annuncio dei blocchi attraversati anche se appartengono allo stesso materiale.
   - La ripetizione ritmica metro per metro funge da **sonar di velocità e cadenza spaziale essenziale**, confermando che il personaggio è in moto e permettendo di stimare le distanze percorse a orecchio.

2. **Aggancio Volumetrico a Micro-Passo per Lamine Sottili (Micro-Raymarch)**:
   - Nei motori 3D a griglia o voxel, gli elementi sottili (porte, vetri, grate, ringhiere, staccionate) occupano uno spessore trascurabile ($< 20\text{ cm}$) rispetto al volume del blocco.
   - Un raycast a passo troppo rado ($> 0.20\text{ m}$) o con partenza distante oltrepassa la lamina, rendendola invisibile nei passi rapidi e provocando salti di coordinate negative (`Math.floor`).
   - **Regola Micro-Raymarch**: Campionare lungo la linea di vista a partire da $d = 0.05\text{ m}$ con passo fisso di $0.10\text{ m}$ per intercettare infallibilmente qualsiasi elemento sottile a contatto.

3. **Pattern Direct Dispatching per Sensori Ambientali & Audio-Voice Synchronization**:
   - È vietato depositare allarmi ostacoli in registri passivi "in sospeso" in attesa che altri moduli grafici o di puntamento li consumino.
   - All'attivazione dell'allarme di prossimità o collisione, il sensore deve **invocare direttamente il Coordinator di Presentazione**, garantendo sincronia assoluta e istantanea tra il segnale audio 3D nelle cuffie e la voce sintetizzata dello screen reader.

---

## 🔇 15. PATTERN "SILENT COMMIT" PER LA SOPPRESSIONE DI FEEDBACK CONCORRENTI IN MOVIMENTO

1. **Il Problema dell'Annuncio Posticipato Fuori Tempo (Lag Mutation Alert)**:
   - Quando un sottosistema primario ad alta priorità (es. sensore ostacoli, allarme burroni o minacce) sopprime temporaneamente un sottosistema secondario a monitoraggio continuo (es. mirino o sensore del blocco/suolo puntato), il semplice blocco della chiamata vocale (early return o mute condizionale) genera un accumulo di divergenza tra lo stato registrato e la realtà fisica.
   - Durante il cammino rapido, l'ambiente circostante muta continuamente; se la voce viene soppressa per una breve finestra (es. 100 ms) senza aggiornare le variabili di stato interne, al primo tick utile dopo la scadenza del timer il modulo secondario confronta lo stato congelato prima del blocco con la nuova posizione, rilevando un finto cambio di contesto. Questo provoca la vocalizzazione in ritardo di bersagli o distanze superate proprio quando il personaggio si è già fermato.
2. **Il Principio del "Silent Commit"**:
   - Durante una finestra di soppressione attiva in movimento, il sottosistema secondario non deve limitarsi a tacere: deve **eseguire il commit atomico dello stato** (`absorbStateIfSuppressed`), aggiornando internamente tutti i riferimenti di memoria (bersaglio puntato, distanza corrente, impronta semantica) prima di scartare l'uscita vocale.
   - Alla scadenza della soppressione, lo stato interno coincide perfettamente con la realtà fisica attuale: zero allarmi residui, zero annunci fantasma e voce pulita che interviene unicamente se avviene una reale nuova mutazione successiva.
3. **Finestra di Soppressione Monotona Crescente**:
   - Il prolungamento di una finestra di soppressione temporale deve essere monotonicamente non decrescente:
     $$T_{\text{suppressedUntil}} = \max(T_{\text{suppressedUntil}}, T_{\text{now}} + \Delta T)$$
     garantendo che chiamate concorrenti o ravvicinate da eventi sovrapposti mantengano viva la protezione senza mai resettare o abbreviare la scadenza già attiva.
4. **Bypass Assoluto per Interrogazioni Manuali Intenzionali (Zero-Latency Direct Query)**:
   - Qualsiasi azione esplicita di interrogazione attivata intenzionalmente dal giocatore da tastiera o controller (es. orientamento, ispezione mirino a comando, query bussola) deve bypassare incondizionatamente qualsiasi soppressione automatica in corso, rispondendo a latenza zero ($0\text{ ms}$) con priorità assoluta.

---

## 🎮 16. PRINCIPIO DI PUREZZA DELL'INTENTO FISICO NEI SISTEMI DI ASSISTENZA IBRIDI (HUMAN-IN-THE-LOOP)

1. **Il Paradosso del Takeover Falso Positivo (Synthetic Override Hijack)**:
   - Nei videogiochi o mondi virtuali accessibili in cui convivono motori di guida autonoma o assistita (es. AutoWalk, pathfollowing vocale, autopilota) e sottosistemi di sicurezza reattiva attiva (es. frenata d'emergenza, auto-accovacciamento da ciglio/burrone, schivata ostacoli);
   - I sistemi di sicurezza scrivono frequentemente stati simulati o sintetici nei registri di input del motore di gioco (es. `setDown(true)` su comandi di movimento o tasti di camminata lenta);
   - Se la routine di **Human Takeover** (il controllo che restituisce il controllo all'utente non appena questi tocca i tasti) interroga lo stato logico o aggregato del motore di gioco (`isDown()`), l'intervento salvavita del bot viene scambiato per un'azione manuale dell'utente, provocando l'immediato e ingiustificato annullamento della navigazione automatica proprio nei punti più critici (es. cigli, pianerottoli stretti, curve a gomito).
2. **Regola Aurea della Purezza Hardware dell'Intento Umano**:
   - Qualsiasi logica deputata a determinare l'intento umano di interruzione o ripresa manuale (`isManualMovementKeyPressed`, `checkHumanTakeover`) deve interrogare **esclusivamente lo strato hardware fisico reale** (polling GLFW nativo, Win32 Raw Input, DirectInput o hook a basso livello), con totale immunità dagli stati sintetici iniettati dai sottosistemi software.
3. **Coesistenza Non Distruttiva di Pilota e Sicurezza**:
   - L'attivazione di una manovra protettiva automatica (es. sneak salvavita da ciglio) non deve interrompere l'autopilota, ma operare come un modulatore di velocità/postura trasparente: il pilota prosegue la rotta a velocità protetta e la navigazione si conclude felicemente a destinazione.

---

## 🔕 17. PRINCIPIO DI QUIETE SENSORIALE NEI MOTI AUTONOMI/GUIDATI (DENOISING CINESTETICO)

1. **Il Problema del Sovraccarico Sensoriale in Navigazione Autonoma (Sensory Chatter)**:
   - Quando un modulo di navigazione o pilota automatico governa lo spostamento e l'orientamento della telecamera lungo una traiettoria calcolata da un pathfinder, i sensori ambientali passivi (mirino/raycast sui blocchi attraversati, ostacoli ordinari superati con auto-jump o aggiramento, avvisi di ciglio o discesa sicura lungo scale o corridoi protetti) generano una raffica continua di parole.
   - Questo chiacchiericcio costante ("chatter") distrugge l'attenzione uditiva del giocatore non vedente, saturando la sintesi vocale e impedendo di percepire gli indizi sonori della rotta o le notifiche di stato della marcia.

2. **Soppressione Selettiva a Monte dei Sensori Ambientali Passivi**:
   - Il sistema deve offrire interruttori dedicati di configurazione (tutti attivi di default) che sopprimono a monte il flusso informativo passivo non appena il movimento autonomo è attivo (`isAutonomousMovementActive`).
   - La soppressione a monte deve aggiornare i puntatori di stato interni (pattern "Silent Commit") per evitare scatti o raffiche vocali di recupero non appena la marcia termina o si ferma.

3. **Le Tre Invarianti Inviolabili del Denoising**:
   1. **Sicurezza Fisica Fail-Safe Intoccabile**: I dispositivi di sicurezza fisica e di frenata (es. auto-sneak hardware, collision brake, arresto su ciglio) restano attivi ed operativi al 100% per proteggere il personaggio in qualsiasi istante.
   2. **Fast-Path Immediato per Minacce Letali (`CRITICAL`)**: Eventi di pericolo mortale immediato (fuoco, lava, vuoto, nemici a contatto) scavalcano qualsiasi silenziamento con priorità assoluta e interrompono all'istante la sintesi a latenza zero ($0\text{ ms}$).
   3. **Tutela Totale delle Interrogazioni Manuali Intenzionali (`DirectInteractionShield`)**: Qualsiasi comando impartito esplicitamente da tastiera dall'utente (es. query del mirino, centramento visuale orizzonte, bussola, scansione nemici) gode di un token di immunità temporale e risponde immediatamente, con assoluta trasparenza anche a marcia in corso.

---

## 🚪 18. PRINCIPIO DEL MAGNETISMO D'AZIONE & ALLINEAMENTO TRA VOLUME PERCETTIVO E RAYCAST FISICO (PERMISSIVE INTERACTION SNAP)

1. **Il Paradosso del Divario tra Volume Percettivo e Raycast Fisico**:
   - Nei videogiochi accessibili, audiogame 3D e mondi voxel/virtuali, i sistemi di assistenza vocale utilizzano scansioni volumetriche generose (es. micro-raymarch a passi densi o bounding box di cella intera $1 \times 2 \times 1\text{ m}$) per consentire allo screen reader di individuare elementi sottili o varchi (porte aperte, botole, cancelletti, leve, interruttori). Lo screen reader annuncia chiaramente: *"Porta aperta davanti a te"*.
   - Tuttavia, i motori fisici convenzionali (Minecraft, Unity, Unreal, Godot) risolvono l'azione del click di interazione tramite un raycast matematico rettilineo infinitesimale calcolato sulla collision box o mesh reale dell'oggetto.
   - Quando un elemento a battente (porta, cancelletto) è aperto, la sua massa fisica ruota adagiandosi allo stipite, riducendosi a una lamina millimetrica (es. soli 3 pixel / $18\text{ cm}$), lasciando oltre l'$80\%$ del volume del varco occupato da aria vuota.
   - *Se* il giocatore non vedente preme il tasto di interazione fidandosi dell'annuncio vocale, *allora* il raycast fisico nativo scivola attraverso l'aria vuota intercettando il muro posteriore o disperdendosi nel vuoto (`MISS`), rendendo l'interazione inefficace e costringendo a una frustrante ricerca millimetrica dello stipite al buio.

2. **La Regola del Permissive Action Snap (Magnetismo d'Azione)**:
   - Non è sufficiente che il mirino "veda" l'oggetto per vocalizzarlo: **l'azione di interazione primaria deve essere magneticamente agganciata e deviata sul target accessibile**.
   - *Se* l'utente scatena un input di interazione, *allora* il sistema verifica se il puntamento accessibile sta inquadrando un elemento aperto/interagibile entro la portata di reach e, in caso positivo, commuta atomisticamente l'hit result dell'azione fisica sull'elemento mirato.

3. **I 4 Cancelli Inviolabili di Sicurezza dell'Interazione Permissiva**:
   1. **Cancello 1 — Priorità Assoluta Entità**: Se il raycast fisico sta già intercettando un'entità primaria (mob, NPC, alleato, veicolo), il magnetismo sui blocchi viene tassativamente disattivato per consentire il dialogo, commercio o combattimento.
   2. **Cancello 2 — Trasparenza Puntamento Diretto**: Se il cursore dell'utente colpisce già fisicamente la hitbox/stipite reale dell'oggetto, non si applica alcuna deviazione artificiale, preservando il flusso nativo del motore di gioco.
   3. **Cancello 3 — Rigore di Portata (Zero-Cheat)**: Il raggio di calcolo del magnetismo deve coincidere incondizionatamente con la massima distanza fisica di interazione lecita del personaggio (`reachDistance`), impedendo azionamenti a distanza non autorizzata.
   4. **Cancello 4 — Esclusione Meccanismi non Manuali**: Gli elementi azionabili unicamente tramite energia esterna, redstone o chiavi (es. porte blindate o di ferro) devono essere rigorosamente esclusi dal magnetismo d'azione a mano libera.

---

## 🧭 19. PRINCIPIO DI INTANGIBILITÀ DELLA BUSSOLA MENTALE DEL GIOCATORE (PRESERVAZIONE DELL'ORIENTAMENTO VISIVO)

1. **Il Ruolo Vitale dell'Orientamento Visivo per il Non Vedente**:
   - Per un giocatore che interagisce tramite sintesi vocale e audio 3D posizionale, l'orientamento della telecamera (pitch, yaw, coordinate cardinali) costituisce l'unico asse di ancoraggio della propria **mappa mentale dello spazio circostante**.
   - Tutti i feedback vettoriali ("davanti", "alle spalle", "a sinistra", "a destra") e la percezione dei gradienti sonori stereofonici o surround dipendono istante per istante dalla stabilità e prevedibilità di questo vettore.
   - Variazioni forzate e impreviste della visuale non richieste esplicitamente dall'utente rischiano di produrre un grave disorientamento cognitivo, equivalente a ruotare improvvisamente la mappa nelle mani di chi naviga al buio.

2. **Regola per Operazioni Rapide e Semplici (Default Fortemente Consigliato)**:
   - Per azioni fisiche ordinarie e circoscritte nel mondo virtuale (es. chiusura di porte, cancelletti o botole alle spalle post-attraversamento, azionamento di interruttori/pulsanti, raccolta rapida di oggetti, toggles elementari), è **fortemente consigliato privilegiare l'interazione programmatica/logica diretta sul target**, mantenendo la telecamera e lo sguardo del personaggio perfettamente immobili.
   - Si evitano così fragili manovre cinetiche multi-tick (es. girare il personaggio di 180° per cliccare e poi tentare di riallinearlo in avanti), garantendo fluidità motoria e stabilità acustica assoluta.

3. **Regola per Automatismi Complessi, Manovre Composite o Casi Non Codificati (Gating con l'Autore)**:
   - Qualora una funzionalità avanzata richieda sequenze articolate (es. cinematica di navigazione su veicoli/velivoli, aggancio guidato a ormeggi/stazioni, inquadrature interattive di precisione, sequenze registiche) che necessitino dell'orientamento pilotato della telecamera:
     * **Divieto di Scelta Arbitraria Autonoma**: L'assistente AI non applica rotazioni forzate su propria supposizione o euristica;
     * **Consultazione Preventiva con l'Autore**: L'approccio cinetico deve essere preventivamente discusso e concordato con lo sviluppatore/autore dell'applicazione;
     * **Stipula del Contratto Operativo Contestuale**: L'intervento viene formalizzato nel Piano Tecnico definendo esplicitamente le tutele percettive necessarie (es. cue sonoro di pre-avviso rotazione, transizione morbida/interpolata vs snap, ripristino deterministico dell'azimut originario al termine della manovra, o attivazione di un beacon audio per consentire all'utente di ricalibrare la propria bussola mentale).

---

## 🛡️ 20. PRINCIPIO DI DISACCOPPIAMENTO DELLE SOGLIE ANTICADUTA & PERVIETÀ FISICA DEI CORRIDOI VERTICALI (ZONA 1 PERCEZIONE VS ZONA 2 INTERVENTO)

1. **Il Paradosso dell'Accoppiamento Monolitico nelle Barriere di Sicurezza**:
   - Nei videogiochi accessibili e nei mondi virtuali 3D (voxel o mesh), l'adozione di un'unica soglia per la segnalazione vocale di burrone e per il blocco fisico immediato del movimento (es. auto-accovacciamento o barriera invisibile) genera un attrito motorio inaccettabile.
   - Costringe lo sviluppatore a un compromesso forzato: o bloccare a terra il personaggio anche su dislivelli innocui privi di danno (incollando l'utente al terreno), oppure alzare la soglia perdendo la pre-allerta informativa su salti significativi.

2. **La Regola del Disaccoppiamento a Due Zone (Zona 1 Percezione vs Zona 2 Intervento)**:
   - **Zona 1 — Percezione Preventiva (`warningThreshold`)**:
     - Attiva tempestivamente la segnalazione vocale descrittiva e il cue acustico posizionale a distanza di sicurezza, uniti a un eventuale rallentamento cinetico della corsa (`autoSlowdown`), per consentire al giocatore non vedente di prepararsi cognitivamente all'ostacolo o al gradino.
     - Il controllo posturale e cinetico rimane libero al 100%: nessun ancoraggio forzato interviene.
   - **Zona 2 — Intervento Meccanico di Salvaguardia (`autoInterventionThreshold`)**:
     - Attiva la barriera fisica o l'auto-accovacciamento forzato (`autoSneak`) sul bordo solo e soltanto quando il dislivello supera la reale soglia di danno fisico o letalità del gioco (es. 4 blocchi in Minecraft vanilla, dove ha inizio il danno da caduta).
   - **La Finestra di Transizione Fluida ($[warningThreshold, autoInterventionThreshold)$)**:
     - Nella fascia intermedia (es. salto di 3 blocchi a danno zero), il giocatore riceve l'informazione vocale ma può camminare, scendere o saltare liberamente con il normale comando di avanzamento (`W`), azzerando l'incollamento artificiale al terreno.

3. **Il Principio di Pervietà Fisica Continua delle Colonne di Caduta & Discesa nei Fluidi**:
   - Quando il sistema valuta vie di discesa morbide o smorzate (es. pozze d'acqua, fieno, ragnatele, liane o scale a pioli), la scansione geometrica lungo la colonna verticale dal piano di deambulazione verso il basso deve verificare la reale pervietà del corridoio.
   - *Se* tra il piano dei piedi e la superficie smorzante si incontra un blocco o ostacolo solido dotato di sagoma di collisione impenetrabile (`!collisionShape.isEmpty()`), la ricerca deve arrestarsi immediatamente (`break;`).
   - È categoricamente vietato scansionare o accettare acque, caverne o fluidi sotterranei coperti da pavimentazioni, pietra o terra piena come vie di discesa, eliminando alla radice i falsi allarmi di "discesa sicura" su superfici compatte.

---

## 🛡️ 21. PRINCIPIO DI INTANGIBILITÀ DELLO STACK UI & ANTI-PATTERN DEL CURSORE MOUSE NELLE MOD ZERO-MOUSE

1. **Il Paradosso del Cursore Invisibile in Modalità Tastiera Pura (Zero Mouse)**:
   - Nei videogiochi commerciali (es. Skyrim, Creation Engine, Unity, Unreal), molti menu o dialoghi non mettono in pausa il motore di gioco (`isPaused == false`).
   - Un errore comune degli sviluppatori di mod di accessibilità è tentare di rilevare se un menu o dialogo è aperto interrogando le API del sistema operativo sul cursore del mouse (es. `GetCursorInfo()` su Windows).
   - *Se* l'utente interagisce al 100% da tastiera con screen reader (NVDA/JAWS), il cursore mouse hardware non viene mosso e rimane nascosto (`ci.flags == 0x0`). L'euristica basata sul cursore fallisce, credendo che il giocatore sia in movimento libero nel mondo 3D e continuando ad accumulare rotazioni della telecamera o suoni parassiti (es. `Wall.wav`) durante la navigazione nei dialoghi o nei menu.

2. **La Regola Universale dell'Interrogazione Diretta dello Stack Modale**:
   - È fatto divieto categorico di affidarsi allo stato visivo del cursore del mouse per inferire lo stato dei menu in contesti di accessibilità.
   - Il codice deve interrogare **esclusivamente e direttamente lo stack modale nativo dell'UI engine** (tutti i menu Scaleform/GUI censiti) tramite una fonte centralizzata atomica e fail-closed (`IsAnyMenuOpen()`), bloccando all'istante la telecamera e i listener di movimento non appena qualsiasi finestra modale o di dialogo è aperta.

---

## 🏃 22. PRINCIPIO DEL DISACCOPPIAMENTO CINETICO & AUDIO PRE-CACHING A 0 MS NEGLI HOTSPOT FISICI

1. **Il Paradosso del Micro-Stop da Trigger di Prossimità (Hitch Percettivo)**:
   - Nei videogiochi 2D, 2.5D isometrici o 3D con navigazione libera da tastiera, l'attraversamento di trigger di prossimità o hotspot interattivi (arredi, NPC, varchi, porte) rischia di generare un fastidioso micro-stop ("hitch" di 50-150 ms) che spezza la cadenza motoria del giocatore non vedente.
   - La causa radice risiede quasi invariabilmente in due fattori concorrenti sul thread principale di esecuzione:
     * *Lock Sincrono del Driver Vocale (TTS Stop Locking)*: Se l'annuncio dell'oggetto avvicinato viene inviato con flag di interruzione immediata (`is_interrupt = true`), il motore esegue una chiamata forzata a `tts_stop()`. Su sistemi operativi moderni (come Windows 11), questa chiamata effettua lock sincroni su interfacce COM/UIA, congelando il main thread dell'engine e facendo perdere all'interprete fisico (`_physics_process` o tick di movimento) i pacchetti di input da tastiera del frame corrente;
     * *Sintesi o Allocazione Audio Procedurale on-demand*: Se il cue sonoro di prossimità viene generato proceduralmente (calcolo di campioni trigonometrici o allocazione buffer in memoria) alla prima riproduzione anziché all'avvio, il sovraccarico di calcolo cade esattamente sul frame di contatto.

2. **La Regola Universale del Pre-Caching Audio a 0 ms**:
   - Qualsiasi campione sonoro, earcon sintetizzato o feedback posizionale deve essere pre-caricato o pre-sintetizzato in memoria RAM durante la fase di avvio/inizializzazione del modulo sonoro (`_ready()` o bootstrap del livello), eliminando qualsiasi allocazione o calcolo procedurale on-demand durante i cicli di collisione fisica.

3. **La Regola dell'Accodamento Dolce per Trigger di Prossimità (Non-Interrupting Proximity)**:
   - Gli annunci vocali scatenati passivamente dall'attraversamento di hotspot o trigger di prossimità devono essere accodati dolcemente senza interruzione forzata (`is_interrupt = false`);
   - Questo consente allo screen reader (NVDA/JAWS) di pronunciare il nome del punto d'interesse senza bloccare il thread di rendering o di fisica, preservando la velocità cinetica continua del personaggio (es. 210 px/s);
   - L'interruzione vocale forzata (`is_interrupt = true`) deve essere riservata unicamente ad allarmi critici salvavita o all'apertura volontaria di menu interattivi e dialoghi su esplicito comando del giocatore.

---

## 🎨 23. PRINCIPIO DEI MENU TESTUALI VETTORIALI AD ALTO CONTRASTO (WCAG AAA VS BITMAP RIGIDE)

1. **Il Limite delle Cornici Grafiche Bitmap Rigide nelle Interfacce Accessibili**:
   - L'impiego di texture bitmap disegnate a dimensione fissa (es. pergamene o riquadri grafici pixel art a 320 px) per ospitare menu di selezione a testo dinamico impone vincoli visivi e tipografici penalizzanti:
     * Costringe a utilizzare font microscopici (<= 8 px) per non far fuoriuscire il testo dai bordi grafici;
     * Riduce drasticamente il contrasto cromatico rispetto allo sfondo della pergamena, degradando la leggibilità per utenti ipovedenti, persone con disabilità visiva parziale o fruitori su display Full HD / 4K.

2. **La Soluzione del Contenitore Vettoriale Responsive ad Alto Contrasto**:
   - Per tutti i menu interattivi a scelte multiple o elenchi di azioni, le texture bitmap statiche devono essere sostituite da pannelli vettoriali geometrici (`StyleBoxFlat` o equivalenti);
   - Utilizzare palette sobrie ed eleganti: sfondo scuro profondo ad altissima opacità (`#11121a`), bordi sottili e netti ad alto contrasto (oro brillante `#c49a45` o neon ciano) e testo bianco/giallo vivo;
   - Dimensioni minime di sicurezza ergonomica: larghezza contenitore $\ge 480$ px, font titolo $\ge 16$ px, font opzioni $\ge 14$ px con padding interno confortevole ($\ge 12 \times 8$ px) e autowrap del testo con algoritmo word-smart per evitare qualsiasi troncamento.

3. **Simmetria di Interazione Universale (Dual-Track Tastiera/Voce)**:
   - Il menu deve garantire piena accessibilità da tastiera con selezione diretta rapida (tasti `1`..`9` e `Numpad 1`..`Numpad 9`), frecce verticali Su/Giù, Numpad 8/2, tasto Invio/Spazio per confermare ed `Esc` per chiudere;
   - All'apertura del menu, l'annuncio vocale lineare per NVDA deve vocalizzare istantaneamente il titolo del contesto e l'elenco delle opzioni disponibili, assicurando perfetta parità d'esperienza tra utente vedente (grafica nitida e grande) e utente non vedente (screen reader fluido e immediato).

---

## 🛡️ 24. SISTEMI DI PROTEZIONE PERIMETRALE FISICA (FRENI DI SICUREZZA CIGLIO), CLEARANCE A VENTAGLIO E COESISTENZA CON LA LOCOMOZIONE AUTONOMA

1. **Il Principio di Non-Interferenza dei Freni di Sicurezza con la Locomozione Autonoma**:
   - *Il Conflitto Sistemico*: Nei giochi con navigazione assistita (AutoWalk) e moduli fisici di protezione da cadute o baratri (Cliff Guard), i due sottosistemi entrano in conflitto se il freno perimetrale non è a conoscenza dello stato del pathfinder. Se l'AutoWalk affronta un dislivello ripido o una discesa marcata, il rilevatore di cadute scambia il sentiero per un burrone, inserisce il freno e azzera gli attuatori di marcia continua, provocando l'interruzione accidentale del viaggio;
   - *La Regola Inviolabile del Predicato Unificato*:
     - Non interrogare mai singole variabili isolate o specifiche di una sola modalità (es. solo marcia a piedi);
     - Centralizzare la sorveglianza in un predicato deterministico (`IsAnyAutonomousNavigationActive()`) che includa marcia a piedi, cavalcature, veicoli e virate discrete guidate;
     - Se qualsiasi forma di navigazione autonoma è attiva, il freno cadute deve essere bypassato al 100%, poiché il percorso tracciato sulla NavMesh garantisce per definizione geometrica la calpestabilità del terreno.

2. **La Regola della Clearance Orizzontale a Ventaglio Multi-Livello (Anti-Falsi Baratri)**:
   - *Il Limite del Raggio Singolo a Quota Fissa*: Una sonda orizzontale posta ad altezza fissa elevata sorvola nel vuoto argini bassi, dossi, greti fluviali o muretti di altezza inferiore al raggio. Mancando l'impatto (`!hit`), l'algoritmo classifica l'assenza di suolo solido come abisso aperto;
   - *La Soluzione a Ventaglio (Dual-Ray Fan Clearance)*:
     - Scansionare l'orizzonte ad almeno due quote complementari: quota bassa (altezza stinco/ginocchio) per argini, dossi e muretti bassi, e quota media (altezza torace/baricentro) per pareti rocciose ed edifici;
     - *Se* almeno uno dei raggi intercetta materia solida, *allora* l'assenza di impatto della sonda verticale viene classificata come ostacolo solido (`kSafeSolid`) e non come burrone; solo se entrambi i raggi mancano il bersaglio il vuoto viene trattato come baratro letale (`kCliffEdge`).

3. **Cinematica dei Quadrupedi/Veicoli & Preservazione dello Sterzo sull'Orlo**:
   - *Calibrazione Geometrica delle Sonde*: La distanza della sonda frontale deve considerare la distanza tra baricentro e muso/paraurti dell'entità, lasciando un margine di arresto ristretto (es. 30–35 unità) per evitare che il raggio si proietti nei fossati laterali durante curve stradali strette;
   - *Preservazione dello Sterzo Puro sul Ciglio*: La maschera di neutralizzazione deve agire selettivamente solo sulla spinta vettoriale che spinge verso il vuoto. I comandi di rotazione yaw sul posto (sterzo tastiera o asse orizzontale analogico) non devono mai essere neutralizzati dal freno cadute, consentendo all'utente di voltarsi e fuggire dal pericolo anche con il veicolo a filo dell'orlo.

4. **Denoising Vocale degli Allarmi Perimetrali (Anti-Flood NVDA)**:
   - Gli allarmi vocali di pericolo (*"Burrone di fronte"* / *"Burrone alle spalle"*) non devono essere emessi a ciclo continuo al solo arresto sul ciglio;
   - L'emissione vocale deve scattare unicamente su **insistenza attiva** del comando di movimento verso il baratro bloccato dal freno;
   - Applicare un debounce temporale rigido (minimo **2500 ms**) a livello di priorità elevata, mantenendo il canale acustico limpido e privo di spam.


