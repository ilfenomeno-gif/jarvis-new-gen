# CHANGELOG — ASTRALIS MASTER GOVERNANCE & STARTER KIT
# Autore: Luca (Sviluppatore Senior Non Vedente con Screen Reader NVDA) & Antigravity
# Standard: Semantic Versioning (SemVer) & Formattazione Lineare per NVDA

Tutte le modifiche rilevanti, i rilasci e le evoluzioni del framework di governance universale **ASTRALIS** sono tracciate in questo documento.

## [Non rilasciato] — 2026-10-03

### Completamento del ciclo di sviluppo — Astralis 3.X

- Aggiunti ideazione, strategia logica e testing/collaudo: 23 prompt e 27 skill, cataloghi 1.2.0. Rafforzata la pianificazione tecnica con contratti e verifiche.
- Allineati Protocollo 1, sei cancelli del Protocollo 12 e template alla tassonomia corrente; conservati snapshot dei file sostituiti.
- Collegati mappa operativa, indici e ingressi AI. Convalida preventiva documentale e verifiche tecniche registrate nel report dedicato; collaudo sui diversi client ancora aperto. Baseline 3.0.21 invariata.

### Ciclo dei report e continuità delle sessioni — Astralis 3.X

- Analizzati in sola lettura Minecraft Access e Skyrim Access, distinguendo repository codice e documentazione in SkyrimAccessSetup; inventario con hash delle fonti consultabili.
- Integrate routine di lettura selettiva, scrittura interna al lavoro sostanziale autorizzato, evidenze, handoff e archiviazione; allineato il formato dei nuovi report alla tassonomia corrente, preservando archivi legacy.
- Aggiornata redazione-report e aggiunte lettura-report, continuita-sessione e chiusura-report: 24 skill, catalogo 1.1.0. Collegati due ingressi locali e sei template.
- Aggiunti template REPORT, richiamo di progetto, collaudo specifico e ispezione documentale in sola lettura. Nessun aggiornamento dei progetti analizzati, release o distribuzione globale.

### Catalogo skill — revisione 1.0.0, esclusivamente Astralis 3.X

- Adattate 14 skill storiche e aggiunte sette capacità dai prompt: 21 SKILL.md autonomi, sei categorie, metadati di selezione e raccordo ai 12 protocolli.
- Aggiunti provenienza con hash, indice derivato, standard, procedura nella knowledge e scenari di collaudo d’uso; aggiornati due ingressi locali e sei template.
- Rimosse dipendenze SPARK dal metodo generale, quantità e perfezionamenti obbligatori e deleghe automatiche. Distinte selezione implicita, mandato ed effetti.
- Nessuna installazione globale, distribuzione ai progetti, esportazione pubblica o modifica del Lab; versione framework invariata.

### Selezione contestuale dei prompt — esclusivamente Astralis 3.X

- Aggiunta la scheda di conoscenza e collegati indice, router locali del Master Hub e sei template AI v3.
- Arricchiti i 20 prompt con criteri di scelta, esclusioni, materiali, esempi e relazioni; metadati schema 2 e catalogo revisione 1.1.0, indipendenti dalla versione del framework.
- Aggiunto indice JSON derivato con generazione e controllo senza scritture; nessuna attivazione automatica degli incarichi.
- Nessuna modifica a Lab, componenti Astralis 4, router di altri progetti o profili globali; preparazione documentale alla futura migrazione soltanto.


### Catalogo prompt operativo — revisione 1.0.0

- Adattate 18 sorgenti storiche in 17 prompt e standardizzati i tre ingressi del Master Hub: 20 documenti canonici in sette categorie.
- Aggiunti indice ragionato, standard comune, template, metadati con identificativi stabili e rapporto di provenienza; preservati sorgenti e ingressi precedenti.
- Separati validazione, autorizzazione e applicazione; collaudo senza correzioni implicite; mantenuta la tassonomia probatoria Astralis.
- Preparato il raccordo futuro alle skill v4 senza modificare il Lab o i progetti collegati.
- Aggiornata l'esportazione ricorsiva del catalogo e dei suoi link; controlli in staging, nessuna pubblicazione o nuova release.

## 🚀 [v3.0.21] — 2026-09-26 (Popomundo Cadence Pacing, Zero-Cost Rejection & Synchronous Virtual Clock Decoupling)

### 🏛️ Architettura & Design Pattern (`clean_architecture_e_design_pattern.md` §31)
- **Pattern Anti-Grinding a Rendimenti Decrescenti con Zero-Cost Rejection (§31)**:
  - Risoluzione definitiva del rischio di spamming compulsivo nei loop di simulazione/crafting gestiti da tastiera accessibile.
  - Tetto fisiologico quotidiano a massimo 2 sessioni per cantiere/istanza;
  - Resa decrescente al 50% con penalità di fatica/stress maggiorata (+50%) sulla seconda sessione;
  - Intercettazione della 3a sessione con rifiuto immediato a costo zero (0 risorse consumate, 0 stress, 0 tempo perso) e notifica esplicita per screen reader.
- **Disaccoppiamento della Pausa Motore dall'Avanzamento del Tempo Virtuale (`advance_virtual_hours`)**:
  - Esecuzione di attività orarie diegetiche all'interno di interfacce modali a schermo intero durante la pausa dinamica (`is_paused`), con avanzamento deterministico sincrono dell'orologio circadiano senza sbloccare la fisica o il movimento dell'avatar.
- **Trasparenza dello Stato e Accessibilità Zero-Guessing**:
  - Incorporazione automatica dello stato di saturazione (`[Progresso: 45% (1/2)]` o `[Satura per oggi (2/2)]`) nel nome dell'entità e commutazione dinamica del pulsante operativo con aggiornamento AccessKit per NVDA.

## 🚀 [v3.0.20] — 2026-09-25 (Synchronous Node Disentanglement, Zero-Regression Scene Tree Seams & Screen Reader Cognitive Clearance)

### 🎮 Motore Godot 4 & Integrazione Accessibile (`standard_godot_engine_e_sviluppo_accessibile.md` §19)
- **Disincaglio Sincrono dei Nodi (`remove_child + queue_free`) per Ricostruzioni UI Dinamiche e Test Headless a 0 ms (§19)**:
  - Causa radice delle asserzioni fallite e dei nodi persistenti: `queue_free()` pospone la deallocazione a fine frame; nei test sincroni o selezioni rapide, `container.get_children()` include nodi obsoleti.
  - Canone Operativo: invocazione obbligatoria di `container.remove_child(child)` prima di `child.queue_free()`.
- **Seam Zero-Regressione nella Ristrutturazione di Scene Preesistenti**:
  - Nel passaggio di finestre complesse da schermata singola ad architettura a schede multiple (Tabs), preservare rigorosamente i percorsi storici dei nodi principali per non rompere le suite di test di integrazione legacy.

### 🎧 Accessibilità Screen Reader NVDA & Zero Mouse (`standard_nvda_e_tastiera.md` §12)
- **Pattern "Screen Reader Cognitive Clearance" (Isolamento a Tab e Filtro a Branche per Dati Estesi) (§12)**:
  - Superamento del limite degli elenchi monolitici ad alta densità informativa che sovraccaricano la memoria di lavoro dell'utente con screen reader.
  - Segmentazione a 2 livelli: macro-tab tematici mutualmente esclusivi (tasti `1`, `2`) + sotto-branche filtrate con scorciatoie mnemoradicali a tasto singolo (`G`, `S`, `A`, `P`, `T`, `B`).
  - Mantenimento di liste corte (3–7 elementi) con navigazione a tasti freccia Su/Giù e collegamento circolare (*Safe Loop*).
  - Tasto di panoramica continua vocale (`R`) per lettura d'insieme immediata della branca attiva.

## 🚀 [v3.0.19] — 2026-09-25 (Kinematic Decoupling & Audio Pre-Caching, High-Contrast Vector Menus & Timed Action Deferral)

### 🎧 Accessibilità Gameplay & Audio (`accessibilita_videogiochi_e_gameplay.md` §§22–23)
- **Principio del Disaccoppiamento Cinetico & Audio Pre-Caching a 0 ms negli Hotspot Fisici (§22)**:
  - Causa radice dell'hitch/micro-stop cinetico (50-150 ms) all'avvicinamento agli arredi/trigger: chiamate vocali ad alta priorità (`is_interrupt = true`) che congelano il thread principale con lock COM/UIA sincroni a `DisplayServer.tts_stop()`, e generazione procedurale di stream audio on-demand durante il frame di collisione.
  - Canone del Pre-caching a 0 ms: pre-caricamento obbligatorio di tutti gli stream/earcon in memoria RAM in fase di avvio (`_ready()`).
  - Canone dell'Accodamento Dolce: emissione di annunci vocali di prossimità con `is_interrupt = false`, garantendo velocità cinetica costante e fluida (210 px/s) e preservando la lettura lineare di NVDA.
- **Principio dei Menu Testuali Vettoriali ad Alto Contrasto (WCAG AAA vs Bitmap Rigide) (§23)**:
  - Eliminazione dei vincoli e delle limitazioni delle cornici bitmap statiche a pergamena che impongono font da 8 px per non sbordare.
  - Sostituzione con pannelli vettoriali geometrici (`StyleBoxFlat`) scuri (`#11121a`) con bordi ad alto contrasto (`#c49a45`), larghezza espansa ($\ge 480$ px), font titolo $\ge 16$ px, font opzioni $\ge 14$ px con padding confortevole e autowrap word-smart.
  - Piena interazione Zero Mouse (numeri `1`..`9`, Numpad `1`..`9`, frecce, invio, spazio, esc) e lettura immediata dello screen reader.

### 🏛️ Architettura Software & FSM (`clean_architecture_e_design_pattern.md` §30)
- **Pattern Deferred State Mutation su Azioni Temporizzate (Timed Action Deferral & Atomic Abort Immunity) (§30)**:
  - Divieto di mutazione immediata dello stato globale (orologio, turno, risorse) all'avvio di azioni con durata (`duration_seconds > 0.0`).
  - Instradamento obbligatorio attraverso il sottosistema esecutivo (`ActionSystem`), con vincolo FSM `GAMEPLAY_BUSY`, inibizione cinetica e barra di progresso;
  - Risoluzione differita scatenata unicamente al completamento naturale (`action_completed`).
  - Atomic Abort Immunity: annullamento atomico non distruttivo su `Esc` (`action_canceled`) che congela l'orologio ed esenta da qualsiasi spesa o penalità.

### 🎮 Motore Godot 4 & Integrazione Accessibile (`standard_godot_engine_e_sviluppo_accessibile.md` §18)
- **Implementazione Concreta Disaccoppiamento Cinetico, Pre-caching & Menu Vettoriali (§18)**:
  - Pattern GDScript 2.0 per `precache_all_cues()` in `AudioCueSystem._ready()`.
  - Configurazione `AccessibilityManager.announce(text, false)` in `Area2D` di prossimità.
  - Routing differito in `ApartmentHud` con connessione a `action_completed` e `action_canceled`.
  - Styling vettoriale per `InteractionMenu` tramite `StyleBoxFlat` ad alto contrasto.

## 🚀 [v3.0.18] — 2026-09-25 (FSM Busy, Modal Exit Parity, Safe Abort Pattern & Test Seams Dependency Injection)

### 🏛️ Architettura Software, FSM & Test Seams (`clean_architecture_e_design_pattern.md` §29)
- **Canone Modal Exit Parity & Sblocco Simmetrico (§29.1)**:
  - Causa radice dei softlock/freeze: finestre modali o menu di pausa che emettono segnali specializzati di uscita (es. `resume_requested` su "Riprendi") non intercettati dal coordinatore HUD, con conseguente chiusura grafica a fronte di lock cinetico e pausa rimasti attivi all'infinito.
  - Canone di parità: obbligo di censire e connettere tutti i segnali di congedo (`closed`, `resume_requested`, `cancelled`) a un handler unificato (`close_modal()`), garantendo lo sblocco incondizionato del flag `is_movement_locked` e la revoca della pausa temporale.
- **Blindatura FSM `GAMEPLAY_BUSY` & Disarmo Inerziale (Hardware Grounding) (§29.2)**:
  - Transizione formale allo stato `BUSY` per qualsiasi azione o routine asincrona con durata temporale.
  - Azzeramento immediato della velocità cinematica (`velocity = Vector2.ZERO`), cancellazione itinerari pendenti (auto-walk) e inibizione a monte in `_physics_process` e `_unhandled_input` di Frecce, Tastierino Numpad, click mouse e tasti rapidi modali.
- **Safe Abort Pattern da Tastiera (`Esc`) (§29.3)**:
  - Reversibilità universale: ogni operazione con durata deve prevedere l'annullamento atomico non distruttivo su tasto `Esc` (`cancel_action()`), ripristinando `GAMEPLAY_IDLE` senza consumo indebito di risorse né penalità e con notifica vocale immediata per NVDA (*"Azione interrotta."*).
- **Inviolabilità dei Test Seams & Priorità di Dependency Injection (§29.4)**:
  - Nei sottosistemi di dominio riutilizzabili, i getter interni di recupero dati (`get_player_data()`) devono dare priorità alle istanze locali iniettate dal costruttore prima di ripiegare sui singleton Autoload globali, proteggendo l'isolamento dei test seams headless a 0 ms.
- **Divieto Categorico di Salvataggio Persistente durante `BUSY` (§29.5)**:
  - Guardia esplicita `SaveManager.is_save_allowed()` per rifiutare categoricamente la serializzazione durante stati operativi transitori o azioni in corso, prevenendo la corruzione irreversibile del savegame.

### 🎮 Motore Godot 4 & Accessibilità Avatar (`standard_godot_engine_e_sviluppo_accessibile.md` §17)
- **Gestione Modali di Sistema, Resume Requested & Controllo Inerziale dell'Avatar (§17)**:
  - Sincronizzazione di `resume_requested` e `closed` in `ApartmentHud`.
  - Disarmo inerziale e cancellazione dell'auto-walk all'emissione di `action_started` e `modal_opened`.
  - Guardia reattiva `is_busy` sul controller dell'avatar (`player_alex.gd`) per sopprimere comandi di movimento e prevenire sovrapposizione di stati.

---

## 🚀 [v3.0.17] — 2026-09-25 (Raster Icon Lossless BBox Standard, 2.5D Peripheral HUD Baseline Alignment & Modal Theme Inheritance)

### 🎨 GUI, Grafica Pixel Art & Ergonomia HUD (`standard_godot_engine_e_sviluppo_accessibile.md` §§14–16)
- **Canone di Pre-trattamento Bounding Box Risorse Raster (Icon Crop Standard) (§14)**:
  - Causa radice delle icone sproporzionate/rimpicciolite a schermo: le immagini raster esportate con ampie cornici di tela trasparente vuota (padding) vengono ridotte involontariamente da Godot quando assegnate a pulsanti con `expand_icon = true`.
  - Canone di ritaglio al vivo (*lossless crop*): scansione preventiva del canale alpha e ritaglio dell'immagine esattamente sul bounding box opaco (`Alpha > 0`) prima del rilascio nel repository, garantendo rapporto 1:1, riempimento pieno del pulsante e perfetta armonia visiva con le altre icone dock.
- **Canone di Allineamento Periferico HUD per Ambienti 2.5D / Isometrici (§15)**:
  - Causa radice dell'invasività verticale: box di dialogo o pannelli periferici inferiori con altezze eccessive (> 150–200 px) occludono il pavimento calpestabile e gli arredi della scena di gioco.
  - Canone di allineamento alla baseline: i box periferici inferiori allineano la loro altezza massima alla linea di base dei dock principali adiacenti (es. 115–120 px), con tipografia compatta (font 9–10 px autowrappato) e ritratti proporzionati ($84 \times 84$ px), preservando clearance orizzontale generosa ($\ge 80$ px) e totale visibilità della scena.
- **Ereditarietà Tematica delle Finestre Modali di Sistema (§16)**:
  - Eliminazione della discontinuità estetica tra menu principale arcade e menu di pausa/sistema: obbligo di ereditare esplicitamente il file di tema condiviso (`res://.../menu_theme.tres`) e la tipografia di progetto (`PressStart2P.ttf`) su tutte le finestre modali di sistema (pausa `Esc`, impostazioni, statistiche), con palette colori coordinata (bordi neon ciano `#38bdf8`, accenti oro e sfondi scuri ad alto contrasto), garantendo conformità WCAG e accessibilità uniforme per NVDA.

---

## 🚀 [v3.0.16] — 2026-09-25 (Robust Auto-Walk Arrival Validation, Bistable Toggle Device Pattern & Domestic Action Specialization)

### 🎮 Accessibilità Gameplay & Navigazione 2.5D (`standard_godot_engine_e_sviluppo_accessibile.md` §§12–13)
- **Pattern Auto-Walk Robusto: Separazione Arrivo Effettivo vs Stallo da Ostacoli (§12)**:
  - Causa radice e prevenzione dell'apertura prematura dei menu: nei motori 2D/2.5D, lo scadere del timer di stallo ostacoli (`_stuck_timer > soglia`) non deve MAI essere equiparato a un arrivo a bersaglio.
  - Canone di validazione geometrica: la callback di completamento interazione o apertura dialogo viene eseguita unicamente se il personaggio è nel raggio effettivo di trigger (`dist <= target_radius` o `target_prop.is_player_in_range`). In caso di arresto per ostacolo o timeout, l'auto-walk viene interrotto, il menu NON viene aperto e viene emesso un avviso vocale NVDA per orientare il giocatore verso il movimento manuale.
  - Rilascio immediato dell'auto-walk al primo input direzionale manuale o alla pressione di Esc.
- **Pattern Stato Bistabile (Toggle On/Off) per Dispositivi Continui (§13.1)**:
  - Superamento del comportamento "usa e getta": i dispositivi o arredi con funzionamento continuo (stereo, giradischi, luci, elettrodomestici) devono adottare uno stato bistabile booleano (`is_active: bool` / `is_stereo_on: bool`) con commutazione On/Off, annunci NVDA simmetrici e aggiornamento del testo dell'Inspection Box che descrive come disattivare il dispositivo.
- **Coerenza Semantica delle Azioni Domestiche & Zero False Modali (§13.2)**:
  - Divieto di riutilizzare finestre modali esterne a pagamento (es. `relax_modal` da bar o parco pubblico con opzione "Prendi un caffè a 5€") per arredi domestici privati del loft.
  - Differenziazione contestuale ad accesso immediato e costo zero: divano (relax gratuito: recupero stress e morale), cucina (espresso del loft: recupero energia e zero spesa), giradischi (ascolto collezione vinili con chance di ispirazione artistica / scintilla creativa).

---

## 🚀 [v3.0.15] — 2026-09-24 (2.5D Collision Clearance, Concentric Instance Discipline, Stand-Point Auto-Walk & Dual-Channel Accessibility)

### 🎮 Accessibilità Gameplay, Interazione 2.5D & Simmetria Universale (`standard_godot_engine_e_sviluppo_accessibile.md` §§7–11)
- **Simmetria Universale & Dual-Channel Mouse/Keyboard (The Sims Foundation) (§10)**:
  - Architettura a doppio canale parallelo senza compromessi: cursore a manina (`CURSOR_POINTING_HAND`) e click sinistro con auto-walk per giocatori normovedenti (Holy Diver), con predisposizione per menu contestuali/tendina futuri.
  - Piena e totale conservazione dell'accessibilità da tastiera e navigazione ciclica parlante per screen reader NVDA (Luca / Zero Mouse) tramite tasto Tab/Shift-Tab, numeri diretti e Numpad.
- **Pattern Hitbox Clearance Anti-Deadlock (Area2D vs StaticBody2D) (§8)**:
  - Causa radice e soluzione del deadlock cinetico: l'area sensibile di trigger (`Area2D`) DEVE estendersi oltre la sagoma fisica solida (`StaticBody2D`) di almeno 25–35 px su tutti i lati calpestabili. Se la sagoma solida è pari o superiore al trigger, i piedi del personaggio collidono con l'ostacolo prima di toccare l'area sensibile, impedendo l'emissione del segnale `body_entered` e bloccando l'interazione.
- **Pattern Stand-Point Decoupled per Auto-Walk (§9)**:
  - Disaccoppiamento tra il centro geometrico del prop (spesso situato all'interno del collider solido) e la destinazione dell'auto-walk.
  - Introduzione del metodo `get_stand_position()` con `stand_offset` esportato per guidare la cinematica verso lo spazio libero calpestabile antistante l'arredo.
- **Concentric Instance Normalization (`[editable path="..."]` Discipline) (§7)**:
  - Disciplina delle scene istanziate in ambienti 2.5D: la radice del prop detiene le coordinate assolute del mondo, mentre tutti i figli (`Sprite2D`, `TriggerShape`, `SolidShape`) mantengono coordinate locali concentriche `(0, 0)` o piccoli offset controllati lungo l'asse Y per la base fisica. Sostituzione di poligoni frammentati con forme geometriche primitive regolari.
- **Igiene Ancoraggi & Offsets CanvasLayer (Anti-Fuori-Schermo) (§11)**:
  - Divieto di coordinate o offset assoluti negativi ereditati su nodi `Control` innestati in `CanvasLayer` (es. HUD renderizzato a Y = -2161). Obbligo di preset Full Rect `(0, 0, 0, 0)` con gestione elastica tramite container.

---

## 🚀 [v3.0.14] — 2026-09-24 (ModalRouter Pattern, Hierarchical Input Decoupling & Headless Dummy Audio Leak Prevention)

### 🏛️ Architettura Software & Modularizzazione UI (`clean_architecture_e_design_pattern.md` §28)
- **Pattern ModalRouter per la Scomposizione Modulare di Controller Monolitici (§28)**:
  - Superamento del debito tecnico nei controller di schermata complessi che aggregano una pluralità di finestre modali o sottomenu ausiliari (es. HUD con 10–20 finestre modali), prevenendo violazioni di SRP e sforamento della soglia del Cancello 6 (<= 250 righe).
  - Isolamento in un componente router specializzato (`ModalRouter extends RefCounted`) preposto a: 1) registro deterministico finestre; 2) mutua esclusione atomica (`hide_all_modals()`); 3) cablaggio automatico segnali ed eventi asincroni `EventBus`; 4) memorizzazione e ripristino del focus da tastiera sul controllo chiamante (`_restore_hud()`).
  - Forwarder trasparenti sulla vista principale: conservazione al 100% dei contratti pubblici verso test runner e suite preesistenti.
  - Risoluzione deterministica del tipo tramite `const RouterClass = preload("...")` per azzerare dipendenze dall'ordine alfabetico dei file nei test headless privi di editor cache.

### 🎮 Accessibilità Gameplay, Input & Audio 3D (`sonificazione_e_volumi_sicurezza.md` §7, `clean_architecture_e_design_pattern.md` §28.3)
- **Disaccoppiamento Gerarchico dell'Input (Autoload vs Controller di Scena) (`clean_architecture_e_design_pattern.md` §28.3)**:
  - Segregazione rigorosa dei ruoli: gli Autoload globali intercettano esclusivamente comandi a basso livello e di orientamento universale (Numpad Navigation e silenziamento d'emergenza `silence()`).
  - Divieto di mappare tasti alfanumerici ordinari (`1`..`4`, `T`, `R`, `C`, `Space`) negli Autoload: tali comandi appartengono alla vista attiva, prevenendo fenomeni di mascheramento prematuro (*input shadowing*) o race condition.
- **Protezione dei Mixer Dummy nei Test Headless e Prevenzione Memory Leak (`sonificazione_e_volumi_sicurezza.md` §7.4)**:
  - Protezione della riproduzione `AudioStreamPlayer.play()` con guardia `if not is_headless`, evitando che il dummy server audio di Godot 4 accumuli istanze C++ orfane di `AudioStreamPlayback` non consumate.
  - Azzeramento `player.stream = null` alla chiusura e invocazione preventiva di `silence()` prima del quit dei test runner.

---

## 🚀 [v3.0.13] — 2026-09-24 (Centralized Orchestrator & Modular Subsystems Pattern, Anti-Ghost Queue & Tactical Vital Preemption)

### 🏛️ Architettura Software & Metodologie di Sviluppo (`clean_architecture_e_design_pattern.md` §27, `abitudini_sviluppo_luca.md` §1)
- **Pattern Architetturale Orchestratore Centralizzato & Sottosistemi Specializzati (Hub-and-Spoke Gerarchico) (§27)**:
  - Rifiuto dell'anarchia distribuita: divieto per i componenti periferici di prendere decisioni autonome sullo stato globale (code, canali, lock di input o volumi).
  - Strutturazione Hub-and-Spoke a due livelli: Orchestratore Centrale come Single Source of Truth, Arbiter & Policy Gateway; Sottosistemi Specializzati come spokes modulari ad alta coesione e singola responsabilità (SRP), completamente disaccoppiati tra loro.
  - I 7 Attributi Sistemici della Visione di Luca: Strutturata, Sistemica, Sinergica, Scalabile, Modulare & Indipendente, Inclusiva, Interconnessa.
  - I 4 Presidi Tecnici Consolidati:
    1. *Aliasing Canonico di Raccordo Centrale*: alias globali nell'header di raccordo (`common.h`) per eliminare l'attrito dei tipi;
    2. *Anti-Ghost Queue & Purge Atomico su Interrupt*: svuotamento atomico e contestuale della coda passiva subordinate (`ClearQueuedItems`) ad ogni interruzione di priorità;
    3. *Schermatura a Camera Anecoica*: scudo di stato globale nell'Orchestratore per scartare a monte i flussi a bassa priorità durante contesti operativi intensivi;
    4. *Triplice Presidio degli Allarmi Continui*: Soglia di innesco critica + Cooldown temporale minimo + Isteresi monotona di riarmo.
- **Canone della Gestione Centralizzata nelle Abitudini di Sviluppo di Luca (`abitudini_sviluppo_luca.md` §1.6)**:
  - Consolidamento permanente della preferenza architetturale per le gerarchie Hub-and-Spoke, vincolando l'assistente a modellare ogni nuova funzionalità partendo dall'Orchestratore e dai sottosistemi modulari prima di toccare codice.

### 🎮 Accessibilità Gameplay, Audio 3D & Gerarchia Vocale (`accessibilita_videogiochi_e_gameplay.md` §1.10)
- **Isolamento Stagno delle Interfacce di Gestione Risorse, Pattern Canonico di Scorrimento e Allarmi Vitali Tattici (§1.10)**:
  - Formalizzazione universale per tutti i videogiochi: camera anecoica durante la gestione risorse, scorrimento canonico a liste con titolo interruttivo e dettagli accodati, e preemption tattica assoluta per gli allarmi salvavita.

---

## 🚀 [v3.0.12] — 2026-09-24 (Graph Spread Invariant in Distributed Topologies & Multi-Year Endless Sandbox Lifecycle)

### 🧪 Strategie di Testing, Debug Sistemico & Architettura di Simulazione (`strategie_testing_e_debug.md` §22)
- **Invariante Topologico nei Grafi di Rete & Parametrizzazione Dinamica delle Asserzioni di Diffusione (§22)**:
  - Isolamento della causa radice nei test di propagazione/riverbero distribuito (fan, mercati, follower, viralità) che verificano il totale aggregato con costanti scalari cablate a mano su vecchie dimensioni del grafo.
  - Formalizzazione della regola aurea: divieto di asserzioni scalari rigide; adozione sistematica di formule attese parametrizzate sulla cardinalità dinamica del dominio (`expected_total = base + local + ((nodes.size() - 1) * per_node_delta)`).
  - Garanzia di totale immunità da regressioni fittizie durante le espansioni di scala topologiche (es. da 12 a 16 metropoli mondiali).

### 🏛️ Architettura Software & Game Design (`clean_architecture_e_design_pattern.md` §26)
- **Pattern Multi-Year State Loop & Deterministic Transition nei Sandbox Endless Mode (§26)**:
  - Architettura a transizione continua post-endgame senza fork dei modelli dati né reset asimmetrici.
  - Estensione deterministica del calendario temporale su contatore annuale (`current_year`), preservando la periodicità invariata di festival, premi e classifiche con serializzazione atomica retrocompatibile.
  - Pattern Mentor Passive Endowment per la gestione pulita e disaccoppiata delle rendite di sussistenza nel New Game+ integrate direttamente nell'audit economico notturno.

---

## 🚀 [v3.0.11] — 2026-09-24 (Domain Catalog Expansion Invariant & Calendar-Coupled Deterministic Test Seams)

### 🧪 Strategie di Testing, Debug Sistemico & Architettura di Simulazione (`strategie_testing_e_debug.md` §20 & §21)
- **Invariante di Espansione dei Cataloghi di Dominio & Regression Boundaries (§20)**:
  - Isolamento della causa radice nelle asserzioni di test che verificano il popolamento dei cataloghi di default con uguaglianze scalari rigide (`catalog.size() == N`).
  - Divieto di cablare costanti magiche locali nei test storici: centralizzazione su costanti di dominio (`Constants.DEFAULT_CATALOG_COUNT`) o adozione di invarianti di soglia minima (`>= MIN_COUNT`) con validazione puntuale degli ID chiave del set originale, garantendo retrocompatibilità ed espandibilità priva di falsi allarmi di regressione durante le milestone evolutive (es. Endgame, stadi, arene).
- **Test Seams Deterministici con Override di Stato su Sistemi Accoppiati al Calendario Procedurale (§21)**:
  - Superamento dell'intermittenza nei test headless (flaky tests) derivante da logiche procedurali accoppiate a funzioni hash del calendario (`CalendarData.day_number`).
  - Obbligo per ogni sottosistema procedurale di esporre test seams espliciti di override deterministico (`set_venue_status_override(id, day, status)` o mock provider), consentendo alle suite headless a 0 ms di forzare lo stato desiderato della risorsa prima della transazione senza alterare gli orologi di gioco né introdurre attese asincrone.
- **Consolidamento Milestone V5.0.0 (Endgame, Grandi Stadi & Legacy Mondiale)**:
  - Chiusura formale di tutte le 11 Sezioni della Roadmap Modulare e della Fase 9 (Endgame V5.0) in *World-tour*, con 26/26 suite headless convalidate con 0 errori a 0 ms e piena conformità ai canoni Zero Mouse per NVDA.

---

## 🚀 [v3.0.10] — 2026-09-24 (Preload Script Decoupling Pattern in UI Controllers & Solvency Guardrails Pattern)

### 🧪 Strategie di Testing, Debug Sistemico & Architettura UI (`strategie_testing_e_debug.md` §17 & §18)
- **Pattern di Preload Script Decoupling nei Controller UI e Consumer Runtime (§17)**:
  - Isolamento della causa radice nel type pinning statico nei controller di interfaccia grafica verso classi introdotte dinamicamente nella stessa sessione di sviluppo.
  - Adozione universale del pattern `const ScriptClass = preload(...)` e tipizzazione polimorfica di base (`RefCounted`, `Resource`) sui parametri ricevuti, garantendo totale disaccoppiamento dai tempi di rigenerazione della class cache e azzerando i blocchi di parsing durante i test headless continuativi.
- **Guardie di Solvibilità Reattiva sulle Transazioni Onerose di Distacco o Rescissione (§18)**:
  - Identificazione del rischio di transizioni illegali o debiti occulti non tracciati in azioni di rottura o rescissione contrattuale soggette a penale finanziaria.
  - Obbligo di guardia economica preventiva reattiva atomica (`if player.liquid_funds < severance_penalty: return failure`), subordinando la rottura del legame contrattuale o relazionale all'effettiva disponibilità e addebito della penale.

---

## 🚀 [v3.0.9] — 2026-09-23 (Headless Test Runner Watchdog Pattern, Windows Console Freeze Prevention & String Format Escaping)

### ⏱️ Standard Automazioni PowerShell & Resilienza Multi-Computer (`automazioni_powershell_e_resilienza.md` §8)
- **Watchdog Timeout Pattern su `.NET System.Diagnostics.Process`**:
  - Superamento del limite di `Start-Process -Wait` privo di timeout e causa di deadlock/freeze indefinito in presenza di stalli dell'engine o modalità QuickEdit della console Windows (`conhost.exe`).
  - Introduzione del pattern Watchdog non bloccante con timeout perentorio a 15 secondi, terminazione forzata via `$proc.Kill()` e contatore lineare di avanzamento (`[1/N]`) ottimizzato per NVDA.
  - Pulizia preventiva dei processi orfani in memoria all'avvio della suite (`Stop-Process -Force -ErrorAction SilentlyContinue`).

### 🧪 Igiene del Runtime GDScript & Diagnostica Headless
- **Escaping Simbolo Percentuale in Stringhe Formattate**:
  - Regola di escaping per il carattere percentuale letterale in GDScript 2.0 (`%%`), prevenendo l'errore bloccante `unsupported format character` e standardizzazione monetaria con la parola estesa `euro` per screen reader.
- **Canone di Esecuzione Test Headless da Scena `.tscn`**:
  - Divieto di invocazione diretta di script `.gd` senza scena per test che estendono `Node`: obbligo di esecuzione tramite scena `.tscn` per garantire l'inizializzazione corretta del `SceneTree` e degli Autoload di sistema.

---

## 🚀 [v3.0.8] — 2026-09-23 (Headless Signal Closure Container Pattern & UI Lifecycle Idempotency)

### 🧪 Strategie di Testing, Debug Sistemico & Architettura UI
- **Canone Closure Container per Ricevitori di Segnali Headless (`strategie_testing_e_debug.md` §12)**:
  - Isolamento della causa radice nel rebinding scalare per valore nelle chiusure anonime/lambda (GDScript 4, Python, Lua): una variabile locale allocata a `null` catturata dalla lambda subisce una riassegnazione interna che non altera la variabile esterna del test runner.
  - Adozione universale del pattern **Closure Container**: cattura rigorosa tramite collezioni mutabili per riferimento (`Array` o `Dict`), garantendo la persistenza e verificabilità deterministica dei payload dei segnali nei test seams a 0 ms.
- **Idempotenza delle Connessioni UI & Ciclo di Vita `_ready()` (`strategie_testing_e_debug.md` §12)**:
  - Analisi del ciclo di vita sincrono all'invocazione di `add_child(inst)` all'interno dell'hook di test: divieto di invocare manualmente `inst._ready()` per evitare ri-registrazioni duplicate.
  - Codifica dell'obbligo di protezione sistematica `if btn and not btn.pressed.is_connected(_handler)` nei controlli grafici per prevenire eccezioni di runtime e garantire la resilienza totale dell'interfaccia.

---

## 🚀 [v3.0.7] — 2026-09-21 (Smart App Control NotSigned Paradigm, DirectShow Startup Sync & Proxy Lifecycle Pinning)

### 🛡️ Standard Modding Nativo & Sicurezza Kernel Windows 11
- **Rettifica Fondamentale Smart App Control & Paradigma NotSigned (`standard_modding_e_runtime.md` §12)**:
  - Superata la precedente teoria sull'auto-firma locale: scoperto e dimostrato empiricamente che le firme Authenticode con certificati autofirmati generano `Status: UnknownError` (CA non fidata), che Windows 11 Smart App Control blocca attivamente a livello di kernel con codice Win32 `4551` (Event 3077/3118).
  - Codificato il paradigma canonico **`NotSigned`**: i binari proxy locali posizionati nelle cartelle di gioco (Steam/GOG) non devono essere firmati con certificati locali fittizi. Il binario non firmato viene caricato all'istante (`LoadLibraryW` codice 0) senza incorrere nel rifiuto per firma non valida.
- **Standard Sincronizzazione Avvio con Video DirectShow (`standard_modding_e_runtime.md` §13)**:
  - Risolto il problema del mascheramento temporale nei motori che riproducono intro video a schermo intero (`vid/intro.AVI`) prima della schermata di menu reale.
  - Implementazione del monitor asincrono e differenziale del log di sistema (lettura incrementale `startOffset` non bloccante), prompt vocale tempestivo per lo skip con Spazio, inoltro trasparente di `VK_SPACE` a Eversim (`CallWindowProcW`) e apertura del menu virtuale accessibile sincronizzata su `Accueil`.
- **Disciplina del Ciclo di Vita delle Proxy DLL e Pinning in Memoria**:
  - Divieto di invocare `FreeLibrary` nei test harness sincroni su proxy DLL con thread worker asincroni attivi, prevenendo crash irreversibili `0xC0000005` (Access Violation) per deallocazione anticipata delle pagine di codice.

---

## 🚀 [v3.0.6] — 2026-09-20 (Windows 11 Kernel Code Integrity, Pure x64 Forwarding & Transient Window Diagnostics)

### 🛡️ Standard Modding Nativo & Sicurezza Kernel Windows 11
- **Jolly Smart App Control (SAC) & Auto-Firma Authenticode (`standard_modding_e_runtime.md` §12)**:
  - Codificata la causa radice e la soluzione per i crash silenti a 0 ms causati da `WinError 4551` (`ERROR_HVCI_POLICY_VIOLATION` / Event ID 3077/3118 nel log `Microsoft-Windows-CodeIntegrity/Operational`).
  - Integrazione obbligatoria e deterministica del passaggio di firma Authenticode self-signed (`Set-AuthenticodeSignature` con hash SHA-256) nelle pipeline di build per consentire l'esecuzione trasparente su Windows 11 con SAC attivo senza abbassare le difese di sistema.
- **Pipeline Pure Export Forwarder x64 Zero-Stub (`standard_modding_e_runtime.md` §11)**:
  - Superamento del limite di `link.exe /DEF` diretto a 64-bit tramite pipeline a due stadi: pre-generazione di `.exp` e `.lib` con `lib.exe /DEF` e collegamento diretto in `link.exe`.
  - Eliminazione totale di funzioni stub C++ manuali per librerie intercettate (zero overhead, zero disallineamento ABI nei registri x64).
  - Disciplina di naming della libreria inoltrata con underscore (`_original`) per prevenire errori di parsing nel loader PE di Windows.

### 👁️ Metodologia Forense & Anti-Mascheramento Acustico
- **Diagnosi Forense dei Fallimenti Silenti a 0 ms (`strategie_testing_e_debug.md` §11)**:
  - Definizione del protocollo di diagnosi a tre canali per crash in cui il log applicativo non viene generato, isolando eventi del kernel prima di ipotizzare anomalie logiche C++.
- **Anti-Mascheramento da Finestre Transitorie Effimere (`strategie_testing_e_debug.md` §11)**:
  - Analisi della race condition tra finestre di bootstrap temporanee (splash screen, updater) e lo screen reader (NVDA/JAWS): la distruzione della finestra scatena `EVENT_SYSTEM_FOREGROUND`, azzerando il parlato in corso.
  - Standard di enumerazione finestre con filtraggio per titolo, verifica dell'area client minima e finestra di stabilizzazione del focus prima del battesimo vocale.

---

## 🚀 [v3.0.5] — 2026-09-19 (Evidence Taxonomy, Semantic Router Parity & Governance Validation)

### 🔬 Tassonomia Probatoria e Disciplina Causale
- Sostituita la precedente lettura lineare della maturità con una tassonomia a sette stati: avanzamento di evidenza, rami `FAIL`/`PARTIAL` e gate empirico conclusivo.
- Ridefinito il canone monovariabile come isolamento di una sola causa comportamentale, mantenendo ammesse telemetria passiva e guardie fail-closed.
- Resa condizionata la preferenza pre-dispatcher alla proprietà effettiva della pipeline, evitando di trasformare un pattern valido in un dogma cross-runtime.
- Precisato il ciclo di vita nativo: memoria grezza, vtable, oggetti o sottoggetti realmente costruiti, distruzione simmetrica e deallocazione.

### 🤝 Parità Semantica Multi-AI e Sicurezza dei Confini
- Limitata l'armonizzazione ai router personali realmente presenti o richiesti; nessuna creazione nominale per client assenti.
- Protetti i documenti upstream della community: la parità tra assistenti è ottenuta tramite puntatori alle stesse fonti canoniche, non tramite sovrascritture o copie testuali.
- Resi espliciti nei router Gemini e Codex i moduli canonici del Protocollo 7 e dell'orchestrazione multi-AI.
- Separata l'autorizzazione al push remoto dal commit e dalla Living Documentation.

### 🛡️ Coerenza, Versionamento e Controlli
- Allineati a v3.0.5 il trittico di root, il catalogo, il Genoma Globale, il profilo Codex e i template dei collaboratori.
- Introdotto `scripts/verifica_coerenza_governance.ps1` per controllare versione, budget router, UTF-8/CRLF e collegamenti relativi dei documenti indicati.
- Consolidate nel progetto Skyrim Access le correzioni probatorie e i puntatori agli allegati archiviati senza modificare codice, build o runtime.

## 🚀 [v3.0.4] — 2026-09-08 (Proactive Update Check, High-Energy Emergency Transients & Token-Saving Scripts)

### 🌟 Rilevamento Proattivo Aggiornamenti & Pattern Deferred Query
- **Pattern Deferred Query & Update Prompt (`templates/GEMINI_TEMPLATE.md` Regola 8, `ISTRUZIONI_DI_AVVIO.md` §5)**:
  - Introdotto il controllo proattivo e non invasivo degli aggiornamenti all'avvio della prima richiesta dell'utente in una chat;
  - Se il sistema è allineato all'ultima versione (o offline), l'esperienza d'uso è fluida e priva di notifiche superflue (zero rumore per NVDA);
  - Se è presente una nuova release ufficiale su GitHub, la richiesta formulata viene salvata e visualizzata chiaramente con un riepilogo semantico ("Obiettivo" e "Descrizione") offrendo il bivio trasparente (Aggiorna prima / Procedi subito con la richiesta originale).
- **Architettura Scripting ad Alto Risparmio Token (`scripts/verifica_aggiornamenti_remoti.ps1`)**:
  - Creazione dello script autonomo portabile delegato a tutte le operazioni di rete, confronto SemVer e fallback;
  - Caching locale temporaneo (12 ore) in `$env:TEMP` per eliminare latenze di rete e chiamate ridondanti nella stessa sessione;
  - Risparmio del 95% del consumo di token per l'assistente AI grazie al disaccoppiamento su script a 1 riga con emissione JSON compatto a 4 campi.
  - Canale a due livelli: interrogazione REST primaria delle GitHub Releases API (`releases/latest`) con fallback fail-safe su `git ls-remote --tags`.

### 🎧 Accessibilità Audio & Transienti Metallici Acuti Salvavita
- **Principio del Transiente Acuto Penetrativo (`knowledge/02_accessibilita_e_audio/sonificazione_e_volumi_sicurezza.md` §5)**:
  - Codificata la regola universale per i segnali sonori di allarme imminente e pre-freno salvavita: divieto di impiegare toni morbidi, sordi o a bassa frequenza che verrebbero coperti dal parlato simultaneo della sintesi vocale TTS / NVDA;
  - Obbligo di impiego di campioni sonori dotati di attacco istantaneo ad altissima energia e spettro acuto metallico (es. risonanza d'incudine su ferro);
  - Immunità del canale audio: obbligo di instradamento degli allarmi di sicurezza personale su bus dedicati al giocatore (`PLAYERS`, `UI`, `SYSTEM`), escludendo i bus audio dell'ambiente soggetti a filtri o attenuazioni dell'utente.

---

## 🚀 [v3.0.3] — 2026-09-07 (Evolutionary Integrity, Centralized FSM, Clean Sweep D0 & Visual Orientation Shield)

### 🌟 Integrità Evolutiva, Zero Residui & Refactoring Disciplinato
- **Principio di Integrità Evolutiva & Bonifica dei Residui (`clean_architecture_e_design_pattern.md` §16, `GEMINI_TEMPLATE.md` Regola Aurea 7)**:
  - Codificato il principio di architettura pulita contro il debito tecnico tossico: divieto categorico di lasciare coesistere codice o strutture obsolete, parziali, morte o concorrenti a seguito dell'introduzione di una nuova soluzione;
  - Obbligo di scansione globale esaustiva (`grep_search`) prima di dichiarare completato qualsiasi refactoring.
- **Pattern FSM Centralizzato vs Catena di Tick Frammentata (`clean_architecture_e_design_pattern.md` §14)**:
  - Superamento delle sequenze a frame/tick dispersi nei moduli di locomozione; adozione di macchine a stati deterministiche sul loop principale con condizioni geometriche misurabili e seam di test headless a 0 ms.
- **Pattern Delegazione Unificata per Azioni Condivise tra Modalità (`clean_architecture_e_design_pattern.md` §15)**:
  - Unificazione implementativa per azioni motorie condivise tra input manuale e guida autonoma, garantendo coerenza percettiva assoluta per lo screen reader ed eliminando biforcazioni di bug.
- **Contratto D0 Clean Sweep Obbligatorio (`catalogo_protocolli_operativi_astralis.md` Protocollo 11, `PIANO_TECNICO_TEMPLATE.md`)**:
  - Formalizzato il primo contratto denominato (`D0`) interamente dedicato alla bonifica sistematica dei residui nei piani tecnici di refactoring prima dell'innesto del nuovo sistema.

### 🎮 Accessibilità Gameplay & Preservazione della Bussola Mentale
- **Principio di Intangibilità della Bussola Mentale del Giocatore (`accessibilita_videogiochi_e_gameplay.md` §19)**:
  - Riconoscimento dell'orientamento della telecamera come perno fondamentale della mappa cognitiva dell'utente non vedente;
  - Interazione programmatica diretta per operazioni semplici; divieto di rotazioni forzate arbitrarie senza accordo preventivo per automatismi complessi.
- **Estensione Gestione Varchi con AutoClose a Soglia Geometrica (`accessibilita_videogiochi_e_gameplay.md` §5.3)**:
  - Definizione dell'invariante di chiusura automatica determinata dal superamento della distanza euclidea di sicurezza ($d \ge 0.90\text{ m}$) senza rotazione visuale.

---

## 🚀 [v3.0.2] — 2026-09-06 (Conditional Multi-AI Symmetry Guard & Level 0 Detection)

### 🌟 Orchestrazione Multi-AI Condizionale, Anti-Bloat & Probing Esecutivo
- **Istituzione della Guardia Condizionale di Simmetria Multi-AI (`orchestrazione_multi_ai_e_collaboratori.md`, Protocolli 8 e 9)**:
  - Codificato il principio di *Attivazione Selettiva (Anti-Bloat & Zero Inquinamento)*: la gestione e la sincronizzazione di configurazioni per assistenti AI ausiliari (GPT Codex, Claude, Copilot) scattano esclusivamente su *Auto-Discovery* (rilevamento fisico concreto di cartelle client come `.codex` o `.claude` nel sistema operativo o router ausiliari nel workspace) oppure su *Richiesta Esplicita dell'Utente*;
  - In assenza di client ausiliari o richieste, il sistema opera in *Modalità Singola AI (Lean Mode)* per preservare la massima pulizia del filesystem.
- **Implementazione Esecutiva nel Tooling (`scripts/aggiorna_ecosistema.ps1`)**:
  - Aggiunto nella Fase 3 il probing condizionale deterministico per `%USERPROFILE%\.codex` e `%USERPROFILE%\.claude`;
  - Se rilevati, lo script esegue automaticamente il backup preventivo (`AGENTS.md.bak`, `CLAUDE.md.bak`) e segnala chiaramente lo stato nella ricevuta di conformità per NVDA.

---

## 🚀 [v3.0.1] — 2026-09-06 (Universal Role Neutrality, Script Hub Discovery & Multi-AI Alignment)

### 🌟 Perfezionamento Distributivo, Neutralità dei Ruoli & Scripting Portabile
- **Allineamento a Cascata Ecosistema Locale e Template**:
  - Aggiornati `GEMINI_TEMPLATE.md` e `AGENTS_TEMPLATE.md` a v3.0.0/v3.0.1 con inclusione del Cancello 6 Token Budget, Rete Pointer DRY e flag di resilienza build (`--no-daemon --no-watch-fs`);
  - Aggiornati tutti i prompt di setup e inizializzazione nel Master Hub a v3.0.1;
  - Allineato il router `AGENTS.md` in `minecraft-access` garantendo la simmetria multi-AI (Antigravity + Codex/ChatGPT).
- **Implementazione Esecutiva dell'Algoritmo Dinamico di Discovery Hub**:
  - Aggiornato `scripts/esporta_starter_kit_zip.ps1` per consultare esplicitamente `$env:ASTRALIS_HUB`, preferenze locali e percorsi standard del Master Hub.
- **Risoluzione Anomalie & Bonifica Versioni**:
  - Risolti i residui di versione antecedenti e normalizzati i line endings in CRLF.

---

## 🚀 [v3.0.0] — 2026-09-06 (Universal Release, Convergenza Modulare & Triplo Context Switcher)

### 🌟 Novità di Sistema, Governance Universale & Architettura
- **Triplo Context Switcher Automatico a Marker (`knowledge/.../catalogo_protocolli_operativi_astralis.md` — Protocollo 7, `abitudini_sviluppo_luca.md`)**:
  - Distinzione deterministica a runtime tra i 3 ambiti di auto-apprendimento:
    * *Ambito C (Framework Distribuibile)*: modalità Framework Core Maintainer per lo sviluppo open source in `astralis-framework` con Dogfooding in `docs/developer/`;
    * *Ambito B (Master Hub Locale)*: gestione della governance globale della postazione di Luca con Isola Protetta;
    * *Ambito A (Progetto Verticale)*: sviluppo mirato su singoli repository con doppio binario.
- **Algoritmo Dinamico di Discovery del Master Hub (Zero Hardcoding)**:
  - Eliminazione di percorsi cablati rigidi per il Master Hub locale; cascata deterministica a 3 livelli: Configurazione Esplicita (`Master Hub: <path>` o `$env:ASTRALIS_HUB`) -> Scansione Marker Strutturali -> Fallback interattivo one-time in `user_preferences.md`.
- **Lancio Ufficiale e Sincronizzazione con `Nemex81/astralis-framework` (v3.0.0)**:
  - Pubblicato il framework universale open source su GitHub sotto Licenza Apache-2.0, con matrice di convergenza modulare per tutti i domini (Game Dev accessibile, Scrittura narrativa, Software engineering, Addon, Utility) e script di sincronizzazione `Export-AstralisPublic.ps1`.

---

## 🚀 [v2.8.0] — 2026-09-06 (Universal Multi-AI Orchestration, Suite Collaboratori & Guardia Ausiliaria On-Demand)

### 🌟 Novità di Sistema, Governance Universale & Architettura
- **Orchestrazione Multi-AI, Suite Collaboratori & Guardia Ausiliaria On-Demand (`knowledge/.../orchestrazione_multi_ai_e_collaboratori.md`, `templates/collaboratori_ai/`, Protocolli 8 e 9)**:
  - Formalizzato il **Polimorfismo dei Ruoli Multi-AI**: disaccoppiamento simmetrico tra *AI Primaria* (lead operativa, test, codice, 100% autonoma) e *AI Ausiliarie / Collaboratori* (peer reviewer, dialettica avversariale, brainstorming, in sola consultazione/lettura).
  - Implementata l'**Auto-Deduzione Deterministica dell'Ambiente**: l'assistente attivo riconosce il proprio runtime e si propone come Primaria per default con conferma a 1 riga per NVDA.
  - Creata la cartella `templates/collaboratori_ai/` con template dedicati per: OpenAI/GPT Codex (`AGENTS_GPT_TEMPLATE.md`), Anthropic Claude (`CLAUDE_TEMPLATE.md`), GitHub Copilot (`COPILOT_TEMPLATE.md`) e Custom AI Agnostico (`CUSTOM_AI_TEMPLATE.md`).
  - Istituita **La Guardia Ausiliaria Multi-AI On-Demand**: sentinella silenziosa che rileva collaboratori non configurati o disallineati sulla macchina (`.codex`, `.claude`) e propone l'armonizzazione automatica a 1 comando.
  - Aggiornati i profili globali e locali della postazione di sviluppo (`%USERPROFILE%\.codex\AGENTS.md` e `minecraft-access/AGENTS.md`).

---

## 🚀 [v2.7.3] — 2026-09-06 (ASTRALIS Canon Crafting & Disciplina Formale di Meta-Governance)

### 🌟 Novità di Sistema, Governance Universale & Architettura
- **Formalizzazione della Meta-Governance & Ingegneria delle Regole (ASTRALIS Canon Crafting) (`knowledge/.../ingegneria_delle_regole_e_meta_governance.md`, Protocolli 7, 8, 12 e Regola 7 Globale)**:
  - Codificati i **6 Canoni Architetturali Fondamentali** per creare e manutenere regole:
    1. *Hub & Spoke & Budgeting Token*: Router snello ad alto segnale ($\le 250$ righe / ~2.000 token per i file `GEMINI.md`); spiegazioni estese allocate nei moduli `knowledge/`.
    2. *Disaccoppiamento Manifest vs Modulo*: Nei router locali risiedono unicamente parametri concreti di configurazione (3-6 righe); la teoria architetturale appartiene ai moduli dedicati.
    3. *Rete Documentale Pointer DRY*: Zero duplicazioni testuali; link incrociati navigabili `file:///` obbligatori tra i 4 nodi.
    4. *Gating Deterministico a 3 Stati*: Notazione standard `[ ]`, `[/]`, `[x]` con divieto di spunta preventiva prima del collaudo reale.
    5. *Accessibilità Cognitiva NVDA*: Flusso 100% lineare, logica "Se... Allora", divieto di tabelle ASCII o grafici 2D, novità sempre in cima.
    6. *Igiene dei File*: Formato UTF-8 senza BOM, rispetto delle terminazioni di riga CRLF su Windows e percorsi dinamici universali.
  - Integrata la **Regola 7** nel Genoma Globale (`%USERPROFILE%\.gemini\config\GEMINI.md`) e la Regola 5 in `templates/GEMINI_TEMPLATE.md`.
  - Estesi i protocolli: Protocollo 7 (validazione preventiva sui 6 Canoni in Fase 4), Protocollo 8 (audit automatico del token budget e integrità file) e Protocollo 12 (Cancello 6: Custode Critico del Budget Token & Anti-Bloat Normativo).

---

## 🚀 [v2.7.2] — 2026-09-06 (Universal Proactive Cognitive Strategy — UPCS, Rete a 4 Nodi & Profilo di Resilienza Multi-Canale)

### 🌟 Novità di Sistema, Governance Universale & Architettura
- **Istituzione Ufficiale del Framework Strategico Logico-Cognitivo (UPCS) (`templates/STRATEGIA_COGNITIVA_TEMPLATE.md`, `catalogo_protocolli_operativi_astralis.md` — Protocollo 1)**:
  - Introdotto il quarto pilastro documentale dell'ecosistema ASTRALIS dedicato all'elaborazione concettuale proattiva di Fase 0 (*Il Perché e il Modello Mentale*), disaccoppiato sia dai Report (retrospettivi) sia dai Piani Tecnici (esecutivi).
  - Codificati i **7 Archetipi Strategici Formali**: Concettuale-Implementativa, Diagnostico-Correttiva, Refactoring Strutturale & Disaccoppiamento, Euristico-Cognitiva per Screen Reader & Audio 3D, Dialettica Avversariale & Convergenza Multi-AI (Inner Codex), Integrazione & Interoperabilità di Runtime, Bonifica/Migrazione/Deprecazione.
  - Creato il template istituzionale `STRATEGIA_COGNITIVA_TEMPLATE.md` a 5 sezioni con Registro di Convergenza e checklist a 3 stati di Fase 0 per NVDA, con gestione trasparente dello stato iniziale del Piano Tecnico Derivato (`[DA DEFINIRE IN SOTTO-FASE 1A]`).
- **Architettura a Rete a 4 Nodi Comunicanti (DRY & Pointer Hub)**:
  - Interconnessione simmetrica tra **Strategie (`docs/strategie/`)**, **Piani Tecnici (`docs/piani/`)**, **Report di Sessione (`docs/report/archivio/`)** e **Registri Revisioni (`REGISTRO_REVISIONI.md` / `ARCHIVIO_REVISIONI.md`)**.
  - Ogni documento include puntatori espliciti cliccabili `file:///` verso gli altri tre nodi della catena, garantendo navigabilità istantanea da tastiera per l'utente non vedente.
- **Profilo di Resilienza, Versionamento & Canali Cloud Multi-Scopo (`knowledge/.../automazioni_powershell_e_resilienza.md`, Protocolli 8 e 9)**:
  - Disaccoppiamento funzionale dei 4 canali di memorizzazione per scopo operativo:
    * *Canale 1 (VCS Codice / GitHub)*: tracciamento atomico sorgenti e documentazione;
    * *Canale 2 (Ponte Operativo Multi-Macchina)*: cartella cloud sincronizzata per dati runtime pesanti (saves, istanze, mondi di test) tra postazioni diverse (es. Desktop Salotto <-> Laptop MSI);
    * *Canale 3 (Cold Archive & Disaster Recovery)*: snapshot preventivi pre-fill, JAR compilati e memoria storica;
    * *Canale 4 (Backup Primario Resiliente)*: snapshot automatici zip per progetti No-Git.
  - Procedura di rilevamento adattivo in fase di bootstrap e aggiornamento con dialogo semplificato calibrato sul livello dell'utente.
- **Estensione dell'Archival Guard a Zero Residui (`catalogo_protocolli_operativi_astralis.md` — Protocollo 6)**:
  - All'atto della chiusura tecnica della revisione e collaudo positivo di Luca, la migrazione automatica sposta simultaneamente la Strategia da `docs/strategie/attive/` a `docs/strategie/archiviate/`, il Piano da `attivi/` a `completati/`, il Report in `archivio/` e la voce nel Registro Storico, aggiornando tutti i puntatori incrociati. Zero documenti orfani.

---

## 🚀 [v2.7.1] — 2026-09-05 (URCP In-Flight Ingestion, Pipeline Aggiornamento Ecosistema a 3 Fasi & Bootstrap Zero-Debito)

### 🌟 Novità di Sistema, Governance Universale & Architettura
- **Ingestione & Proposta di Normalizzazione Post-Analisi (URCP In-Flight) (`catalogo_protocolli_operativi_astralis.md` — Protocollo 4)**:
  - Esteso il Protocollo 4 (Telemetria, Diagnosi e Reporting): quando viene sottoposto ad Antigravity un report esterno non conforme (da ChatGPT/Codex, tester o dump grezzi), oltre alla valutazione tecnica e alle risposte di merito, l'assistente formula proattivamente la proposta di normalizzazione URCP a 7 campi.
  - Con il consenso esplicito dell'utente, il file viene subito convertito e reso fruibile con NVDA fin dall'avvio dei lavori, eliminando la permanenza di report disomogenei nel ciclo attivo.
- **Riforma del Ciclo di Aggiornamento Ecosistema a 3 Fasi (`catalogo_protocolli_operativi_astralis.md` — Protocollo 8)**:
  - Strutturata la procedura universale di upgrade macchine esistenti nella sequenza deterministica *Prima $\rightarrow$ Durante $\rightarrow$ Dopo*:
    1. *Fase 1: Pre-Flight Audit dello Stato Attuale (PRIMA)*: scansione preliminare del delta versioni, registri revisione legacy, report non conformi e anomalie di codifica (BOM);
    2. *Fase 2: Aggiornamento Master Hub & Release Starter Kit (DURANTE)*: fusione integrativa salvaguardando l'Isola Protetta Utente e generazione dello Starter Kit ZIP versionato;
    3. *Fase 3: Post-Flight Migration & Riconciliazione Progetti Attivi (DOPO)*: allineamento selettivo della knowledge locale, migrazione retrocompatibile del `REGISTRO_REVISIONI.md` al pointer hub DRY e bonifica URCP di tutti i report storici ed attivi.
- **Bootstrap Nativo Zero-Debito su Nuova Macchina (`catalogo_protocolli_operativi_astralis.md` — Protocollo 9)**:
  - Codificato il bootstrap diretto dall'ultimo Starter Kit ZIP versionato, garantendo che ogni nuova postazione o progetto nasca con architettura disaccoppiata, standard report e registri revisione nativamente conformi al 100%.
- **Guardia di Ingestione & Archiviazione Report (URCP Standard) (`catalogo_protocolli_operativi_astralis.md` — Protocollo 6 & RRU)**:
  - Istituito il controllo automatico a 4 passi all'atto dell'archiviazione: normalizzazione 7 campi, inversione cronologica, compattazione log e bonifica UTF-8 pulita (zero BOM).

---

## 🚀 [v2.7.0] — 2026-09-05 (Protocollo 12 Inner Codex, Report Pointer Hub a Cronologia Inversa & Sinergia RRU)


### 🌟 Novità di Sistema, Governance Universale & Architettura
- **Istituzione Ufficiale del Protocollo 12 — Dialettica Ingegneristica & Auto-Revisione Avversariale (L'Inner Codex Pattern) (`catalogo_protocolli_operativi_astralis.md`)**:
  - Elevata la governance da 11 a 12 Protocolli Operativi Ufficiali.
  - Codificata la capacità nativa e autonoma di Antigravity di agire come Senior Reviewer critico, intransigente e avversariale, strutturato sui **5 Cancelli Inviolabili (The 5 Inviolable Gates)**:
    1. *Cancello 1 — Rifiuto del Patching Euristico (Invariante Topologica vs Sintomo Numerico)*: divieto di mascherare problemi strutturali alterando budget, tick, delay o costanti arbitrarie.
    2. *Cancello 2 — Purezza dell'Intento Fisico nei Sistemi Ibridi (Hardware Grounding)*: ancoraggio obbligatorio del rilevamento di input umano ai probe hardware reali (GLFW / periferiche pure), escludendo stati logici simulati da automatismi concorrenti.
    3. *Cancello 3 — Integrità della Hitbox e Volumetria Continua*: analisi spaziale rigorosa su geometrie 3D continue ($0.6 \times 1.8\text{ m}$), clearance verticale occhi/testa e forme di collisione sottili.
    4. *Cancello 4 — Disciplina dei Contratti Denominati e Chiusi (Named Contract Pattern)*: scomposizione atomica delle modifiche complesse in contratti formali numerati (D0..DN, S1..SN) con precondizioni, postcondizioni e invarianti.
    5. *Cancello 5 — Determinismo Headless e Time-Seam a 0 ms*: obbligo di time-seam package-private per l'esecuzione istantanea di test unitari con clock virtuale senza `Thread.sleep`.
  - Integrato l'Audit Avversariale Preventivo a 5 voci nella Sotto-Fase 1A dei Piani Tecnici (`templates/PIANO_TECNICO_TEMPLATE.md`).
- **Standard del Report di Sessione & Telemetria ad Alto Segnale (`templates/REPORT_SESSIONE_TEMPLATE.md`, `catalogo_protocolli_operativi_astralis.md`)**:
  - Codificata l'intestazione standard a 7 campi (`Autore`, `Revisori`, `Data e Ora`, `Stato dell'Implementazione`, `Obiettivi`, `Piani & Strategie Correlate`, `Breve Descrizione`).
  - *Flusso Messaggi in Ordine Cronologico Inverso (Newest First)*: il messaggio più recente risiede sempre in cima alla sezione messaggi per l'atterraggio istantaneo con tasto rapido `H` in NVDA.
  - *Standard Atomico ad Alto Segnale (4 Campi)*: Contesto/Sintomo ($\le 2$ righe), Causa Radice Concettuale, Approccio Risolutivo & Pattern, Puntatori Espliciti (`file:///...`) a sorgenti, test, log e piani (divieto di file bloat, dump integrali di log e codice massivo).
  - *Archiviazione Automatica a Zero Residui*: migrazione automatica del report da `docs/report/` a `docs/report/archivio/` durante il Protocollo 6 (Chiusura Tecnica - Fase 3).
- **Sinergia a Puntatore Diretto RRU $\rightarrow$ Report (`templates/REGISTRO_REVISIONI_TEMPLATE.md`, `catalogo_protocolli_operativi_astralis.md`)**:
  - Applicazione rigorosa del principio DRY: le singole voci nel Registro Revisioni mantengono una sintesi estrema e puntano direttamente al Report di Sessione, eliminando la duplicazione degli elenchi di file.
  - Aggiornamento deterministico dei puntatori al path di archivio (`docs/report/archivio/`) al momento della migrazione in `ARCHIVIO_REVISIONI.md`, garantendo zero link rotti.
- **Ergonomia Cognitiva per Screen Reader (`stile_comunicazione_nvda.md`)**:
  - Codificata la Sezione 3 sui vantaggi ergonomici della cronologia inversa e dello standard a puntatori per sintesi vocale NVDA.
- **Pattern dei Contratti Denominati e Chiusi (`clean_architecture_e_design_pattern.md`)**:
  - Codificata la Sezione 12: formalizzazione modulare degli interventi complessi con contratti chiusi per blindare la non-regressione e guidare la scrittura di test unitari 1-a-1.
- **Principio di Purezza dell'Intento Fisico nei Sistemi Ibridi (`clean_architecture_e_design_pattern.md`)**:
  - Codificata la Sezione 13: isolamento assoluto tra le guardie reattive di sicurezza che pilotano stati di emergenza e i canali di intercettazione dell'intento volontario umano.
- **Aggiornamento Diagnostica di Ricerca Grafi (`strategie_testing_e_debug.md`)**:
  - Formalizzata la Sezione 8 sull'isolamento sistemico delle anomalie di pathfinding A*/Dijkstra tramite discriminante open-set vs budget di espansione.
- **Aggiornamento Sicurezza Sistemi di Assistenza Ibridi (`accessibilita_videogiochi_e_gameplay.md`)**:
  - Formalizzata la Sezione 16 sul disaccoppiamento tra automatismi di salvataggio posturale e takeover volontario umano.

---

## 🚀 [v2.6.3] — 2026-09-04 (Buffer di Rifinitura Pre-Release Universale, DirectInteractionShield & Triangolazione a Tre Fonti)

### 🌟 Novità di Sistema, Governance Universale & Architettura
- **Strategia Universale dei Buffer di Rifinitura (`catalogo_protocolli_operativi_astralis.md`)**:
  - Aggiornato il Protocollo 5 (PRAPI): codificato il principio universale agnostico per cui i ritocchi secondari e le rifiniture non bloccanti emersi durante la produzione non devono spezzare l'inerzia del lavoro primario, ma vengono accorpati in un buffer dedicato a conclusione del corpo dell'opera e prima della revisione/collaudo complessivo. Valido per software, scrittura creativa, audio e governance.
- **Principio del Rasoio Funzionale Anti-Sovraingegnerizzazione (`catalogo_protocolli_operativi_astralis.md`)**:
  - Integrato nel Protocollo 2 (Validazione): divieto assoluto di refactoring speculativi o nuove macchine a stati su comportamenti o moduli già convalidati empiricamente come funzionanti e risolti con screen reader NVDA.
- **Pattern "DirectInteractionShield" per Flussi Concorrenti (`clean_architecture_e_design_pattern.md`)**:
  - Integrato nella Sezione 4: token temporale vincolante attivato dalle azioni manuali esplicite dell'utente da tastiera, con emissione immediata a latenza zero (`interrupt: true`) e assorbimento silenzioso dei flussi passivi e di telemetria di fondo.
- **La Triangolazione Empirica a Tre Fonti (`strategie_testing_e_debug.md`)**:
  - Codificata la Sezione 7: standard metodologico di convalida definitiva basato sulla convergenza sincronizzata di Test Automatici Headless a 0 ms (logica), Telemetria Live di Runtime (percezione sensoriale vocale/audio) e Persistenza Dati su Disco (riscontro forense dello stato).

---

## 🚀 [v2.6.2] — 2026-09-04 (Sinergia Multi-AI Triangolo Virtuoso, Ownership Token, Doppio Guard GUI & Flag Gradle --no-watch-fs)

### 🌟 Novità di Sistema, Metodologia & Design Pattern
- **Il Metodo del Triangolo Virtuoso di Pair Programming Multi-AI (`abitudini_sviluppo_luca.md`)**:
  - Codificata la Sezione 16: cooperazione sinergica e non-competitiva tra Luca (Lead Architect & Product Owner sovrano), ChatGPT (Senior Reviewer & Architectural Analyst per second-opinions e confini formali) e Antigravity (Resident Pair Programmer & Esecutore Locale sul filesystem, build e telemetria live).
  - Obbligo metodologico di **Delimitazione Negativa ("Cosa NON Toccare")** e matrice delle **Invarianti Anti-Regressione** nei piani tecnici di Sotto-Fase 1A.
- **Pattern "Ownership Token vs State Probe" (`clean_architecture_e_design_pattern.md`)**:
  - Codificata la Sezione 9: netta separazione tra lo stato osservato dal probe e l'autorità formale di comando (`systemOverrideActive`). Gli automatismi possono revocare esclusivamente gli stati da essi stessi imposti, con divieto assoluto di alterare o resettare la volontà manuale dell'utente.
- **Driver & Probe Purity (`clean_architecture_e_design_pattern.md`)**:
  - Codificata la Sezione 10: i lettori hardware di basso livello devono rimanere puri (Single Responsibility), delegando filtri e regole di business ai layer superiori.
- **Lifecycle-Safe Initialization (`clean_architecture_e_design_pattern.md`)**:
  - Codificata la Sezione 11: prevenzione dei crash statici da singleton prematuri; inizializzazione dei campi con costanti sicure di fallback e binding dinamico differito al lifecycle dedicato.
- **Inviolabilità Input Manuale & Architettura a Doppio Guard nelle GUI (`standard_nvda_e_tastiera.md`)**:
  - Codificate le Sezioni 5 e 6: tutela dei modificatori fisici nei menu e pattern a doppio guard (a monte sui binding, a valle sui metodi fisici, con sincronizzazione atomica in `tick()`) per eliminare crash e ghost narrations.
- **Resilienza ai Lock Cloud OneDrive/Dropbox (`automazioni_powershell_e_resilienza.md`)**:
  - Aggiunto il Livello 4 alla Sezione 6: adozione obbligatoria del flag `--no-watch-fs` nei runner di build/test su Windows per azzerare gli errori di snapshot sui reparse points.

---

## 🚀 [v2.6.1] — 2026-09-04 (Pattern Silent Commit, Monotonic Suppression & Continuità Voxel Verticale)

### 🌟 Novità di Sistema, Accessibilità & Gameplay
- **Pattern "Silent Commit" per Feedback Concorrenti in Movimento (`accessibilita_videogiochi_e_gameplay.md`)**:
  - Codificata la Sezione 15: assorbimento atomico dello stato interno durante le finestre di soppressione temporanea per prevenire l'accumulo di differenziali di mutazione e l'annuncio posticipato di bersagli superati (Lag Mutation Alert).
  - Finestra di soppressione monotona crescente ($\max(T_{\text{active}}, T_{\text{now}} + \Delta T)$) per evitare accorciamenti accidentali da chiamate concorrenti.
  - Bypass assoluto a latenza zero ($0\text{ ms}$) per le interrogazioni manuali esplicite dell'utente.
- **Sonar Podometrico, Aggancio Micro-Voxel & Direct Dispatching (`accessibilita_videogiochi_e_gameplay.md`)**:
  - Consolidata la Sezione 14 sul sonar di marcia metro per metro lungo pareti uniformi e il campionamento micro-raymarch per lamine sottili.

---

## 🚀 [v2.6.0] — 2026-09-02 (Releases Hub, Component-Based Discovery & Starter Kit Immutabili Versionati)

### 🌟 Novità di Sistema, Distribuzione & Governance
- **Istituzione della Cartella `releases/` (Releases Hub)**:
  - Creata la cartella ufficiale `$hubRoot\releases\` nel Master Hub come sede esclusiva e centralizzata per tutti gli archivi ZIP distribuiti, eliminando l'inquinamento del Desktop.
- **Script di Esportazione Potenziato (`scripts/esporta_starter_kit_zip.ps1`)**:
  - *Component-Based Discovery*: Individuazione deterministica del Master Hub tramite i 5 marker strutturali (`knowledge/`, `prompts/`, `templates/`, `scripts/`, `CHANGELOG.md`) per garantire portabilità su qualsiasi macchina o configurazione utente (zero hardcoding).
  - *Packaging Duale & Versioning Automatico*: Generazione dell'archivio storico immutabile `ASTRALIS_Universal_Starter_Kit_v{VERSIONE}.zip` e del puntatore `ASTRALIS_Universal_Starter_Kit_latest.zip`.
  - *Supporto Release Personalizzate*: Parametri dinamici `-Version`, `-CustomTag` (es. "luca-edition"), `-DestinationDir` e `-IncludeLatest`.
  - *Esclusione Ricorsiva & Staging Atomico*: Esclusione di `releases/` e `*.zip` durante la compressione su `$env:TEMP` per azzerare i lock cloud e l'annidamento ricorsivo.
- **Tutor Contestuale & Keybinding Introspection (`accessibilita_videogiochi_e_gameplay.md`)**:
  - Codificata la Sezione 11 (Tutor Vocale & Risoluzione Dinamica Tasti a Runtime) e la Sezione 12 (Calibrazione Hitbox Voxel per Salto Automatico Pilota).
- **Auto-Focus Menu di Pausa `Esc` (`accessibilita_videogiochi_e_gameplay.md`)**:
  - Codificata la Sezione 13 (Iniezione Auto-Focus Proattivo su `PauseScreen` & Zero Pre-Focus con Frecce Immediate).

---

## 🚀 [v2.5.5] — 2026-09-02 (Reattività Container Specialistici, Auto-Focus Dinamico & Disciplina JVM Deterministica)

### 🌟 Novità di Sistema & Governance
- **Reattività Container Specialistici & Auto-Focus Dinamico (`accessibilita_videogiochi_e_gameplay.md`)**:
  - Codificata la Sezione 10 con il pattern per GUI condizionali ed asincrone: tracciamento differenziale di stato $\rightarrow$ vocalizzazione quantitativa immediata $\rightarrow$ Smart Focus Relocation sul gruppo sbloccato (`selectGroupByKey`) e notifiche vocali discrete di fine ciclo.
- **Disciplina Runtime Gradle Deterministica (`standard_modding_e_runtime.md`)**:
  - Codificata la Sezione 7 per l'ancoraggio esplicito di `org.gradle.java.home` in `gradle.properties` al fine di eliminare i conflitti JVM in ambienti multi-JDK.
- **Benchmark Pilota su `minecraft-access`**:
  - Implementata e collaudata `Rev MC-26.4` con avanzamento alla versione locale **`v26.2-1.16.1`**.

---

## 🚀 [v2.5.4] — 2026-09-02 (Disciplina AVF nei Fork: Baseline Inception & Progressione Sovrana)

### 🌟 Novità di Sistema & Governance
- **Disciplina AVF nei Progetti Fork (Baseline & Progressione Sovrana)**:
  - Codificata in `clean_architecture_e_design_pattern.md` (Sezione 6.3) la regola per cui i fork si ancorano alla versione upstream di partenza (`Baseline Inception`) e avanzano progressivamente la numerazione interna nel diario sovrano, mantenendo la totale compatibilità con l'upstream (`## [Unreleased]`).
- **Consolidamento Auto-Apprendimento Fase 4**:
  - Testato e validato l'allineamento integrativo multi-macchina (Protocollo Onboarding e Protocollo Aggiornamento).

---

## 🚀 [v2.5.3] — 2026-09-02 (Disciplina Dual-Track nei Fork & Isolamento PR Upstream)

### 🌟 Novità di Sistema & Governance
- **Disciplina Universale del Doppio Binario nei Fork (Dual-Track Changelog)**:
  - Codificata in `standard_modding_e_runtime.md` (Sezione 6) e `catalogo_protocolli_operativi_astralis.md` (Protocollo 6) la gestione disaccoppiata per i progetti fork:
    * *Binario Pubblico Upstream*: Sezione `## [Unreleased]` in inglese puro nel `CHANGELOG.md` di radice per PR senza conflitti di versione;
    * *Binario Sovrano Personale*: Diario in italiano in `knowledge/` con versionamento semantico AVF a 3+1 livelli per la sovranità totale del fork.
- **Regola di Isolamento Assoluto delle Pull Request Upstream**:
  - Divieto tassativo di includere file di governance ASTRALIS (`gemini.md`, `knowledge/`, `docs/`) nei branch destinati a PR verso l'upstream.
- **Applicazione Pilota su `minecraft-access`**:
  - Creato il `CHANGELOG.md` pubblico in inglese con la ricostruzione integrale di tutte le feature implementate da inizio agosto a oggi;
  - Aggiornata la scheda `knowledge/03_standard_sviluppo_fork_pr.md` e allineato `knowledge/13_diario_modifiche_e_contributi_fork.md`.

---

## 🚀 [v2.5.2] — 2026-09-02 (Pattern RRU Disaccoppiato: Registro Attivo vs Archivio Storico)

### 🌟 Novità di Sistema & Governance
- **Istituzione del Pattern RRU Disaccoppiato**:
  - Separazione netta tra `docs/report/REGISTRO_REVISIONI.md` (registro attivo snello per le sole voci aperte o in lavorazione) e `docs/report/ARCHIVIO_REVISIONI.md` (memoria storica perenne delle revisioni collaudate e chiuse).
  - Ciclo di vita automatizzato: migrazione automatica delle voci collaudate in Fase 3/4 per mantenere i file attivi compatti (< 100 righe) e istantanei da consultare con screen reader NVDA.
- **Aggiornamento Template & Moduli**:
  - Creato `templates/ARCHIVIO_REVISIONI_TEMPLATE.md` e aggiornato `templates/REGISTRO_REVISIONI_TEMPLATE.md`.
  - Aggiornati `catalogo_protocolli_operativi_astralis.md` (Sezione RRU) e `abitudini_sviluppo_luca.md` (Sezione 11).
- **Allineamento a Cascata del Progetto Benchmark `minecraft-access`**:
  - Creato `docs/report/ARCHIVIO_REVISIONI.md` storicizzando le 7 revisioni/anomalie completate del 1 settembre.
  - Creato `docs/report/REGISTRO_REVISIONI.md` snello con le 2 revisioni aperte (Rev MC-26.4 e Rev MC-26.7).
  - Creato `knowledge/01_diario_modifiche_e_contributi_fork.md` in italiano per la disciplina I18N del fork.
  - Aggiornato `gemini.md` locale agli 11 protocolli con Indice Ragionato a micro-sommari inline.

---

## 🚀 [v2.5.1] — 2026-09-02 (Consolidamento Fase 4: Rollback Bonifica & Quarantena Letteraria)

### 📚 Documentazione & Auto-Apprendimento
- **Consolidamento del Testing & Debug**:
  - Inserita la Sezione 5 in `strategie_testing_e_debug.md` definendo la doppia barriera di verifica post-pulizia, la clausola di rollback automatico istantaneo e l'ispezione dinamica retroattiva.
- **Consolidamento del Profilo di Scrittura Creativa**:
  - Inserita la Sezione 3 in `metodo_scrittura_creativa.md` sancendo la Regola Aurea di Zero Cancellazione e la Quarantena Letteraria in `archivio_bozze/` e `note_pregresse/`.

---

## 🚀 [v2.5.0] — 2026-09-02 (Architettura a 11 Protocolli, Protocollo Pulizia, Trittico Inviolabile & Version Coherence Guard)

### 🌟 Novità di Sistema & Governance
- **Formalizzazione dell'11° Protocollo Operativo Ufficiale**:
  - Inserito il **Protocollo 11 — Pulizia & Bonifica *(Code & Asset Grooming / Dead Code Purge)*** a Doppio Binario (Astratto Globale + Specializzazioni Concrete sui 5 Domini).
  - Implementata la **Strategia a 5 Barriere di Sicurezza**:
    * *Barriera 1*: Audit a Doppia Chiave (Statica + Dinamica per JSON/I18N/Reflection con protezione per default degli identificatori dinamici);
    * *Barriera 2*: Prospetto di Bonifica Lineare per NVDA (Dry-run ad alto segnale con ID e livello di rischio `BASSO`, `MEDIO`, `ALTO`);
    * *Barriera 3*: Gating Semantico & Scelta Granulare dell'Utente (Regola 0 / Zero decisioni autonome);
    * *Barriera 4*: Quarantena di Sicurezza Reversibile & Snapshot (Zero Data Loss, divieto assoluto di cancellazione per Scrittura Creativa con archiviazione in `archivio_bozze/`);
    * *Barriera 5*: Compilazione, Test di Non-Regressione & Rollback Automatico a 1-Click.
- **La Regola del Trittico Inviolabile di Rilascio di Root**:
  - Vincolo procedurale: allineamento atomico e contestuale di `CHANGELOG.md`, `README.md` e `ISTRUZIONI_DI_AVVIO.md` prima di qualsiasi rilascio o esportazione Starter Kit.
- **Version Coherence Guard in `scripts/aggiorna_ecosistema.ps1`**:
  - Controllo dinamico automatico che verifica matematicamente che l'intestazione di versione dei file del Trittico coincida all'unisono (`v2.5.0`).
- **Specializzazione Polimorfica di Bonifica sui 5 Domini**:
  - Codificate in `abitudini_sviluppo_luca.md` (Sezione 15) e `clean_architecture_e_design_pattern.md` (Sezione 7) le direttive specifiche per Gaming/Modding, Addon NVDA, Python, PowerShell e Scrittura Creativa.

---

## 🚀 [v2.4.4] — 2026-09-02 (Allineamento Istruzioni di Avvio & Casi Particolari)

### 📚 Documentazione & Starter Kit
- **Allineamento ISTRUZIONI_DI_AVVIO.md con i Casi Particolari**:
  - Inserita la Sezione *Gestione Automatica dei Casi Particolari* con istruzioni esplicite per screen reader NVDA su:
    * Ricostruzione Storica Retroattiva per progetti legacy privi di changelog (da `git log` / `docs/`);
    * Triage e proposta proattiva di inizializzazione per progetti *Candidati Onboarding*;
    * Disciplina deterministica di versionamento AVF (`V.A.R[.M]`) e tutela dei changelog storici.
  - Rimossi tutti i refusi e riferimenti residui a versioni precedenti.

---

## 🚀 [v2.4.3] — 2026-09-02 (Consolidamento Fase 4: Disciplina AVF in Abitudini Sviluppo)

### 📚 Documentazione & Auto-Apprendimento
- **Consolidamento del Profilo & Consuetudini**:
  - Inserita la Sezione 14 in `abitudini_sviluppo_luca.md` codificando l'applicazione di AVF nei 3 momenti della pipeline (Fase 1A stima, Fase 3 calcolo deterministico, Fase 4 incremento per lezioni apprese).

---

## 🚀 [v2.4.2] — 2026-09-02 (Disciplina di Versionamento Semantico Esteso a 3+1 Livelli AVF)

### 🌟 Novità di Sistema & Governance
- **Istituzione della Disciplina AVF (Astralis Versioning Framework)**:
  - Codifica della specifica deterministica a 4 cifre (`V.A.R[.M]`):
    * *1ª Cifra V (Versione / Major)*: Grandi salti architetturali, breaking changes o nuovi Volumi narrativi (`X.0.0[.0]`);
    * *2ª Cifra A (Aggiornamento / Minor / Feature)*: Nuove funzionalità, moduli o capitoli senza rottura (`X.Y.0[.0]`);
    * *3ª Cifra R (Revisione / Patch / PRAPI)*: Bugfix, rifiniture post-collaudo e consolidamento Fase 4 (`X.Y.Z[.0]`);
    * *4ª Cifra M (Micro-Fix / Hotfix / Doc — Facoltativa)*: Typo, rifiniture di documentazione o commenti (`X.Y.Z.W`);
  - Inserita la Sezione 6 in `clean_architecture_e_design_pattern.md` con l'albero decisionale matematico per la proposta in Fase 3;
  - Aggiornato il Protocollo 6 (Chiusura Tecnica) con il passaggio operativo di calcolo deterministico del numero di versione;
  - Aggiornato `templates/CHANGELOG_PROGETTO_TEMPLATE.md` con il formato `V.A.R[.M]` e `templates/PIANO_TECNICO_TEMPLATE.md` con il metadato di stima incremento versione.

---

## 🚀 [v2.4.1] — 2026-09-02 (Architettura dei 10 Protocolli, Polimorfismo di Governance, RRU & Telemetria Live)

### 🌟 Novità di Sistema & Governance
- **Formalizzazione della Matrice dei 10 Protocolli Operativi Ufficiali**:
  - Inserimento del **Protocollo 4 — Telemetria & Monitoraggio in Tempo Reale**: ispezione continua e denoising dei file di log (`latest.log`, `nvda.log`) in tempo reale durante i collaudi (Fase 2) con popolamento proattivo delle anomalie.
  - Estensione del **Protocollo 2 — Validazione**: integrazione obbligatoria della **Matrice di Simulazione Scenari a 3 Livelli** (Scenari Comuni / Happy Path, Scenari Meno Comuni / Concorrenza, Casi Limite / Corner Cases & Boundary Values) a valle dei 7 Assi di Qualità.
  - Universalizzazione del **Protocollo 5 — Revisione & Affinamento Post-Implementazione (PRAPI)**: ciclo rapido di refinement in 4 passi esteso a tutti i 5 domini applicativi.
  - Blindatura del **Protocollo 8 — Aggiornamento Ecosistema**: Smart Merge a 5 fasi, Isola Protetta Globale e Locale, scansione a cascata del workspace con triage progetti e **Audit di Conformità Post-Aggiornamento**.
  - Blindatura del **Protocollo 9 — Onboarding**: Bootstrap zero-config per macchine pulite in 3 domande con generazione automatica dell'albero documentale.
- **Polimorfismo di Governance & Specializzazione Gerarchica**:
  - Distinzione netta tra *Framework Astratto Globale* (Master Hub / Livello 0) che definisce le linee guida universali e *Specializzazione Concreta Locale* (Singolo Progetto / Livello 2) che definisce le regole operative specializzate nel proprio `GEMINI.md` e schede `knowledge/`.
- **Registro Revisioni Universale (RRU) Proattivo**:
  - Standardizzazione dell'artefatto vivo di revisione per tutti i progetti in `docs/report/REGISTRO_REVISIONI.md`;
  - Innesco automatico proattivo durante il collaudo (l'assistente registra i feedback senza richiesta esplicita) con comando di riallineamento di sicurezza;
  - Nuovo template ufficiale `templates/REGISTRO_REVISIONI_TEMPLATE.md`.
- **Tutela Integrale dell'Auto-Apprendimento a Doppio Binario**:
  - *Binario B (Globale)*: Quadruplo presidio su `knowledge/` (Isola Protetta Utente nel Genoma Livello 0, smart merge a sezioni nei moduli tematici, auto-indicizzazione di moduli custom globali nel Dispatcher e snapshot di sicurezza preventivo).
  - *Binario A (Locale)*: Preservazione al 100% di tutte le schede `knowledge/` locali create nelle sessioni di Auto-Apprendimento durante gli aggiornamenti di progetto.
- **Smart Index & Micro-Sommari nei `GEMINI.md`**:
  - Inserimento di micro-sommari inline di 6-8 parole nella Sezione 4 del `GEMINI.md` Globale e negli indici locali;
  - Disaccoppiamento confermato: il `README.md` pubblico di root resta dedicato esclusivamente alla documentazione del software.
- **Dogfooding nel Master Hub & Registro Meta-Revisioni**:
  - Creazione della struttura `docs/` (`docs/piani/attivi/`, `docs/piani/completati/`, `docs/report/`) nel Master Hub;
  - Istituzione del Registro Meta-Revisioni perenne in `docs/report/REGISTRO_REVISIONI_ASTRALIS.md` (censite Rev AST-2.1 fino ad AST-2.9).
- **Audit & Validazione di Conformità Post-Aggiornamento**:
  - Autoverifica sistematica a fine aggiornamento su assenza di contraddizioni, ridondanze riverberate tra livelli e link rotti, con emissione della Ricevuta di Conformità per NVDA.

---

## 🚀 [v2.3.1] — 2026-08-31 (Incoronazione ASTRALIS, 8 Protocolli Operativi & Smart Merge)

### 🌟 Novità di Sistema & Governance
- **Incoronazione Ufficiale del Framework ASTRALIS**:
  - Adozione del nome ufficiale **ASTRALIS** (*Adaptive Standards for Testing, Rules, Accessibility & Level Integration Systems*).
- **Codifica della Gerarchia degli 8 Protocolli Operativi Ufficiali**:
  - Nuova scheda specialistica `knowledge/03_architettura_e_metodologie/catalogo_protocolli_operativi_astralis.md`.
  - Definizione formale degli 8 Protocolli: *Protocollo Progettazione*, *Protocollo Validazione (7 Assi)*, *Protocollo Esecuzione*, *Protocollo Chiusura*, *Protocollo Apprendimento*, *Protocollo Aggiornamento*, *Protocollo Onboarding*, *Protocollo Sicurezza*.
  - **Regola del Riconoscimento Semantico Flessibile & Feedback di Aggancio**: L'assistente riconosce qualsiasi formulazione naturale equivalente e dichiara esplicitamente a inizio risposta il protocollo attivo.
- **Aggiornamento Integrativo & Smart Merge (Livello 0)**:
  - Rilevamento automatico e differenziale di regole, consuetudini e istruzioni custom create dall'utente in `~/.gemini/config/GEMINI.md` o in `knowledge/`.
  - Notifica esplicita di *"Aggiornamento Integrativo"* e fusione non-distruttiva a sezioni protette (`## 🧩 REGOLE & CONSUETUDINI PERSONALIZZATE DELL'UTENTE`).
- **Scansione & Retrofit Integrativo a Cascata dei Progetti (Livello 1 e 2)**:
  - Scansione ricorsiva di tutti i workspace/progetti aperti; allineamento delle meta-regole nei `GEMINI.md` e della conoscenza locale in `knowledge/` preservando tutte le specificità e consuetudini locali.
- **Gestione Standardizzata del Changelog di Progetto & Ricostruzione Storica**:
  - Nuovo template `templates/CHANGELOG_PROGETTO_TEMPLATE.md` in italiano per i progetti personali.
  - Distinzione netta tra Progetti Personali (`CHANGELOG.md` alla radice) e Fork Open-Source (`knowledge/01_diario_modifiche_e_contributi_fork.md` in italiano per non alterare il changelog upstream per le PR).
  - *Ricostruzione Retroattiva da Git*: Se il file manca, viene generato e popolato estraendo la cronologia reale dai commit (`git log`) e dai documenti di implementazione completati.
- **Aggiornamento Script & Governance Tools**:
  - `scripts/esporta_starter_kit_zip.ps1` aggiornato con il pacchetto ufficiale `ASTRALIS_Universal_Starter_Kit.zip`.
  - `scripts/aggiorna_ecosistema.ps1` potenziato con verifica protocolli, diagnostica regole custom e scansione progetti.
  - `scripts/bootstrap_progetto.ps1` aggiornato con il Passo 6 per la creazione automatica del `CHANGELOG.md`.

---

## 🚀 [v2.3.0] — 2026-08-30 (Upgrade In-Place & Protocollo Self-Healing)

### 🌟 Novità di Sistema & Governance
- **Master Prompt di Aggiornamento Ufficiale (`PROMPT_AGGIORNAMENTO_ECOSISTEMA_ESISTENTE.md`)**:
  - Procedura guidata in 5 fasi per eseguire l'aggiornamento in-place su macchine con versioni precedenti dell'ecosistema.
  - Fusione non-distruttiva del Genoma Globale (Livello 0) con preservazione del 100% dell'identità utente, accessibilità NVDA/tastiera e percorsi configurati.
- **Protocollo di Ripristino Automatico (Self-Healing)**:
  - Rilevamento e ripristino proattivo automatico nel caso in cui sulla macchina di destinazione manchino file essenziali come `CHANGELOG.md`, `README.md`, `ISTRUZIONI_DI_AVVIO.md`, template o moduli di `knowledge/`.
- **Nuove Istruzioni di Avvio a Bivio Rapido (`ISTRUZIONI_DI_AVVIO.md`)**:
  - Separazione lineare e chiara per screen reader tra *Opzione A: Prima Installazione da Zero* e *Opzione B: Aggiornamento In-Place*.
- **Script Ausiliario di Verifica & Backup (`scripts/aggiorna_ecosistema.ps1`)**:
  - Utility PowerShell per audit di integrità dei moduli, backup preventivo timestampato del file `GEMINI.md` globale e validazione dell'ambiente.

---

## 🚀 [v2.2.0] — 2026-08-30 (Le 4 Meta-Regole Operative Universali)

### 🌟 Standardizzazione & Governance Globale
- **La Regola del Deploy Proattivo in Fase 2 (Zero Attrito di Collaudo)**:
  - Obbligo per Antigravity di compilare e distribuire automaticamente l'artefatto nelle istanze attive prima di richiedere il test a Luca.
- **La Doppia Barriera di Backup (Fase 3)**:
  - Aggiornamento dei backup stabili su cloud/OneDrive esclusivamente **POST-CONVALIDA positiva** e collaudo confermato da Luca.
- **Protocollo di Resilienza ai Lock Transitori Cloud (OneDrive/Dropbox Anti-Snapshot Pattern)**:
  - Uso sistematico di flag `--no-daemon`, staging su `$env:TEMP` e pulizia selettiva della cartella `build/` in caso di lock da parte del cloud sync.
- **Standardizzazione del Genoma Globale (Livello 0)**:
  - Allineamento di `~/.gemini/config/GEMINI.md`, `abitudini_sviluppo_luca.md`, `strategie_testing_e_debug.md` e `GEMINI_TEMPLATE.md`.
