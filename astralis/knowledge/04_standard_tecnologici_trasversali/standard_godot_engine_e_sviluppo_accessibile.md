# Standard Godot Engine, Sviluppo Accessibile & Pattern di Runtime (v3.3.0)
# Autore: Luca (Sviluppatore Senior Non Vedente con Screen Reader NVDA) & Antigravity
# Target AI: Antigravity (Senior AI Pair Programmer & Software Engineer)
# Ambito: Globale / Master Hub ASTRALIS
# Origine: Consolidamento Architetturale World-tour (V5.5.1)

Questo documento definisce i criteri tecnici e metodologici obbligatori per lo sviluppo di progetti e videogiochi in **Godot Engine 4.x** con accessibilità totale per screen reader **NVDA** (**Zero Mouse**), test deterministici headless e igiene dei componenti visivi.

---

## 🎮 1. RUNTIME & PILASTRI DI ACCESSIBILITÀ ASSOLUTA

1. **Driver Nativo AccessKit (Windows UI Automation)**:
   - Avviare il runtime con supporto accessibilità attivo (`--accessibility-driver accesskit`, flag `--accessibility always`).
   - L'albero dei controlli derivati da `Control` espone nativamente ruoli e proprietà semantiche ad AccessKit per la lettura diretta di NVDA tramite l'API di Windows UIA.
2. **Interazione 100% da Tastiera (Zero Mouse)**:
   - Ogni interfaccia, pulsante, cursore o modale deve essere fruibile esclusivamente da tastiera (Frecce, Tab/Shift-Tab, Invio, Spazio, Esc e Numpad esteso).
3. **Volumi di Sicurezza Anti-Mascheramento & Ducking**:
   - I volumi di musica ed effetti ambientali devono essere congelati a un valore massimo compreso rigorosamente tra **`0.70f` e `0.75f`** (mai 1.0f pieno).
   - All'emissione di sintesi vocale da parte di NVDA o del sistema TTS di gioco, applicare un ducking automatico immediato attenuando il volume di gioco al **40%** (`ratio = 0.40`), ripristinandolo al termine dell'annuncio vocale.

---

## 🛑 2. PATTERN "ZERO FOCUS DROP" PER CONTROLLI INATTIVI

1. **Il Principio di Conservazione del Focus**:
   - In Godot Engine, impostare la proprietà nativa `disabled = true` su un `Button` o controllo rimuove l'elemento dal ciclo di tabulazione e dalla navigazione con tasti freccia.
   - Per un utente non vedente, la scomparsa invisibile di un'opzione (es. "Carica Partita" in assenza di salvataggi) crea forte disorientamento: fa credere che la funzione non esista o sia stata eliminata per errore.
2. **Canone Operativo**:
   - Mantenere il controllo sempre focalizzabile (`focus_mode = Control.FOCUS_ALL`).
   - Arricchire dinamicamente la descrizione accessibile del nodo tramite il gestore di accessibilità (es. *"Carica Partita, Pulsante. Nessun salvataggio trovato su disco"*).
   - Se azionato, il pulsante non crasha e vocalizza con immediatezza un feedback informativo discreto.

---

## 🔄 3. PATTERN ERGONOMICO "SAFE LOOP" (FOCUS CHAINING CICLICO CONTINUO)

1. **Eliminazione dei Vicoli Ciechi**:
   - Arrestare il cursore di focus al raggiungimento del primo o dell'ultimo controllo di un elenco costringe l'utente da tastiera a percorrere tutta la lista a ritroso.
2. **Configurazione Circolare**:
   - In ogni menu principale, barra comandi o elenco di opzioni, collegare a cerchio le proprietà `focus_neighbor`:
     - Dal **primo controllo**, freccia Su (o Sinistra) punta deterministicamente all'**ultimo controllo**;
     - Dall'**ultimo controllo**, freccia Giù (o Destra) torna deterministicamente al **primo controllo**.
   - Questa configurazione garantisce mobilità fluida, intuitiva e simmetrica per sessioni prolungate senza mouse.

---

## 🚀 4. PATTERN RUNTIME "DEFERRED SCENE TRANSITION"

1. **Causa Radice del Conflitto "Parent Node Busy"**:
   - Invocare sincronicamente `get_tree().change_scene_to_file(...)` o `change_scene_to_packed(...)` all'interno di una callback di segnale (es. `_on_button_pressed`) o durante l'elaborazione interna di notifiche GUI provoca l'errore:
     `ERROR: Parent node is busy adding/removing children, remove_child() can't be called at this time.`
   - La radice della scena corrente non può essere rimossa mentre l'albero sta iterando sui figli per propagare eventi.
2. **Canone Operativo Tassativo**:
   - Tutte le transizioni globali di scena devono essere obbligatoriamente invocate tramite il meccanismo asincrono differito:
     ```gdscript
     get_tree().change_scene_to_file.call_deferred("res://percorso/scena.tscn")
     ```
   - La sostituzione della scena viene così posposta alla fine del frame corrente, a notifiche completate, garantendo stabilità assoluta.

---

## 🧪 5. IMPORTAZIONE DETERMINISTICA ASSET IN TEST HEADLESS

1. **Gestione dei Metadati `.import` e `.ctex`**:
   - Quando nuovi file grafici (PNG, JPEG) o font TTF vengono posizionati nel repository o generati da script di build, Godot necessita della compilazione dei relativi file descrittori `.import` e binari `.ctex` in `.godot/imported/`.
   - Se i test headless vengono eseguiti prima dell'importazione, l'engine fallisce con `ERROR: No loader found for resource`.
2. **Comando Standard di Pre-Flight**:
   - Eseguire il bootstrap dell'editor headless con chiusura immediata prima di lanciare le suite di test:
     ```powershell
     Godot_console.exe --headless --editor --quit --path .
     ```
   - Questo comando genera i file di importazione, aggiorna la cache delle classi globali e termina con exit code 0.

---

## 🎨 6. IGIENE DEGLI ASSET GRAFICI (CLEAN ALPHA VS FAKE CHECKERBOARD)

1. **Prevenzione della Falsa Trasparenza Rasterizzata**:
   - Quando si importano asset grafici ritagliati da mockup, fogli di sprite o schermate di editor, verificare preventivamente che la griglia a scacchi bianco/grigia (checkerboard) usata per rappresentare la trasparenza non sia stata salvata come pixel RGB opachi.
   - Prima del rilascio nel repository, scansionare l'alpha channel: i pixel esterni ai contorni del disegno devono avere valore di trasparenza `Alpha = 0`, evitando bordi rettangolari grigi antiestetici sopra gli sfondi del gioco.

---

## 📐 7. PATTERN GAMEPLAY 2.5D: CONCENTRIC INSTANCE NORMALIZATION

1. **La Fragilità delle Istanze Modificate (`[editable path="..."]`)**:
   - In Godot, quando una scena di arredo o prop viene istanziata in un ambiente 2.5D/top-down e resa modificabile nell'editor visivo, muovere nodi interni (`Sprite2D`, `CollisionShape2D`, `TriggerArea`) causa il disallineamento progressivo della gerarchia rispetto alla posizione globale del nodo radice.
   - Poligoni di collisione duplicati o traslati arbitrariamente generano barriere invisibili o buchi di collisione spuri.
2. **Canone di Normalizzazione Concentrica**:
   - La radice del prop (`InteractiveProp` o `Node2D`) deve trovarsi alle esatte coordinate mondiali del punto di ancoraggio dell'oggetto.
   - Tutti i nodi figli devono mantenere coordinate concentriche locali `(0, 0)` o piccoli offset controllati unicamente lungo l'asse Y per allineare la sagoma alla base d'appoggio.
   - Preferire forme geometriche primitive regolari (`RectangleShape2D`, `CircleShape2D`) a poligoni manuali irregolari per la base solida.

---

## 🛡️ 8. PATTERN HITBOX CLEARANCE ANTI-DEADLOCK (AREA2D VS STATICBODY2D)

1. **La Causa Radice dell'Hitbox Deadlock**:
   - Negli oggetti interagibili dotati sia di ingombro fisico solido (`StaticBody2D`) sia di area sensibile di attivazione (`Area2D`), se l'area di trigger ha dimensioni pari o inferiori alla sagoma fisica solida, il personaggio impatta con il proprio collider contro l'ostacolo prima che la capsula tocchi l'area sensibile.
   - Il segnale `body_entered` non viene mai scatenato e l'interazione risulta permanentemente bloccata.
2. **Canone di Clearance Minima Salvavita**:
   - L'area di rilevamento (`TriggerShape` dell'`Area2D`) **deve estendersi all'esterno della sagoma solida (`SolidShape` dello `StaticBody2D`) di almeno 25–35 pixel** su tutti i lati calpestabili.
   - Questo margine garantisce che il personaggio intercetti deterministicamente il trigger prima o contemporaneamente all'arresto contro la barriera fisica solida, consentendo l'interazione immediata da tastiera, mouse o prossimità.

---

## 🚶 9. PATTERN STAND-POINT PER AUTO-WALK (PUNTO DI STAZIONAMENTO CALPESTABILE)

1. **Il Fallimento del Puntamento al Centro Fisico**:
   - Quando si implementa l'avvicinamento automatico (`auto-walk` verso un target), inviare il pathfinding o il vettore di marcia verso `prop.global_position` causa il blocco dell'entità: il centro del prop si trova all'interno della barriera fisica solida, provocando scivolamenti errati o mancato raggiungimento della destinazione (`navigation failure`).
2. **Canone Stand-Point Decoupled**:
   - Ogni elemento interagibile deve esportare un offset relativo di stazionamento (`@export var stand_offset: Vector2 = Vector2(0, 40)`).
   - Esporre un metodo pubblico `get_stand_position() -> Vector2` che calcola `global_position + stand_offset`.
   - L'auto-walk guida l'entità esattamente al punto di stazionamento antistante calpestabile, arrestando il movimento e attivando automaticamente l'ispezione o l'interazione all'arrivo.

---

## 🖱️ 10. SIMMETRIA UNIVERSALE & DUAL-CHANNEL MOUSE/KEYBOARD (THE SIMS PATTERN)

1. **Coesistenza Armonica Senza Conflitti (Zero Mouse per Luca, Full Mouse per Vedenti)**:
   - L'inclusività radicale prevede che il gioco offra la massima espressività per utenti con disabilità visiva (NVDA / Zero Mouse) e al contempo un'esperienza naturale, ergonomica e moderna per utenti normovedenti con mouse (stile *The Sims*).
2. **Canone Operativo Dual-Channel**:
   - **Canale Mouse**: L'`Area2D` di ogni prop intercetta `mouse_entered`, `mouse_exited` e `_input_event`. Al passaggio del cursore, l'icona commuta su manina interattiva (`Input.set_default_cursor_shape(Input.CURSOR_POINTING_HAND)`). Al click sinistro, viene emesso il segnale `prop_clicked`, che avvia l'auto-walk verso il punto di stazionamento e predispone l'apertura del menu contestuale o modale.
   - **Canale Tastiera & Screen Reader**: Il ciclo di navigazione (Tab/Shift-Tab, tasti numerici diretti, comandi Numpad) seleziona ciclicamente gli arredi, vocalizza stato e opzioni tramite NVDA/AccessKit ed esegue l'azione con Invio o scorciatoie dirette, senza che il canale mouse interferisca minimamente con il focus o con la sintesi.

---

## 🖥️ 11. IGIENE ANCORAGGI & OFFSETS CANVASLAYER (ANTI-FUORI-SCHERMO)

1. **La Trappola degli Offset Assoluti Ereditati**:
   - Quando istanze UI complesse (HUD, modali, router) vengono collocate all'interno di un `CanvasLayer` in scene di gameplay 2D, è frequente che nodi `Control` ereditino coordinate assolute o offset negativi estremi derivanti da precedenti composizioni (es. `offset_top = -2161`, `offset_bottom = -1049`).
   - Sebbene i nodi siano formalmente "visibili" (`visible = true`), essi vengono renderizzati a migliaia di pixel al di fuori del viewport visivo, rendendo l'HUD completamente invisibile a schermo per i vedenti, pur continuando a rispondere ai test o a NVDA.
2. **Canone Full Rect a Zero**:
   - Ogni interfaccia radice innestata in un `CanvasLayer` deve essere configurata tassativamente con preset Full Rect e azzeramento assoluto degli offset:
     - `anchors_preset = 15` (PRESET_FULL_RECT)
     - `offset_left = 0`, `offset_top = 0`, `offset_right = 0`, `offset_bottom = 0`
   - Eventuali margini interni vanno gestiti esclusivamente tramite contenitori con layout elastico (`MarginContainer`, `PanelContainer`, layout box) con padding controllato.

---

## 🛑 12. PATTERN AUTO-WALK ROBUSTO: SEPARAZIONE ARRIVO EFFETTIVO VS STALLO DA OSTACOLI

1. **La Causa Radice dell'Apertura Prematura**:
   - Nei sistemi di cammino assistito (`auto-walk`), se lo scadere del timer di mancato avanzamento o stallo ostacoli (`_stuck_timer > soglia`) viene trattato indistintamente come un "arrivo completato", la funzione di callback associata (apertura menu contestuale, attivazione modale) viene eseguita anche quando il personaggio è rimasto bloccato contro una parete o un arredo a grande distanza dall'obiettivo.
2. **Canone di Validazione Geometrica dell'Arrivo**:
   - La callback di interazione al termine dell'auto-walk deve essere invocata **esclusivamente se il personaggio si trova nel raggio effettivo di trigger** dell'oggetto (`dist <= target_radius` o `target_prop.is_player_in_range`).
   - Se l'arresto è causato da timeout di stallo o collisione prima del raggiungimento del raggio:
     - Arrestare il movimento e ripristinare lo stato di `idle`;
     - **Non invocare mai** la callback di apertura menu/dialogo;
     - Emettere un feedback audio discreto e vocalizzare con NVDA l'avviso di orientamento: *"Percorso bloccato. Avvicinati manualmente con i tasti di movimento."*;
   - Rilasciare istantaneamente l'auto-walk al primo input direzionale manuale o alla pressione di Esc.

---

## 📻 13. PATTERN STATO BISTABILE (TOGGLE ON/OFF) & CONTESTUALITÀ DOMESTICA

1. **Gestione a Levetta per Dispositivi Continui**:
   - Gli arredi dotati di funzionamento continuo (impianti stereo, giradischi, luci, televisori) non devono essere trattati come consumabili a senso unico (solo accensione).
   - Implementare sempre una variabile di stato bistabile (`is_active: bool` / `is_stereo_on: bool`) che commuta tra On e Off:
     - All'attivazione: avvia l'effetto/musica, assegna i bonus/malus del caso e aggiorna il testo di ispezione descrivendo come disattivarlo;
     - Alla disattivazione: arresta il suono/effetto e ripristina la descrizione di riposo/silenzio.
2. **Coerenza Semantica delle Azioni Domestiche (Zero False Modali)**:
   - Evitare rigorosamente di riutilizzare finestre modali generiche di consumo esterno (es. `relax_modal` con opzioni a pagamento da bar o parco) per arredi domestici privati (divano, cucina del loft).
   - Gli arredi domestici devono erogare azioni immediate, gratuite e coerenti con l'ambientazione narrativa (es. l'espresso casalingo in cucina o il relax gratuito sul divano), arricchendo l'Inspection Box con feedback acustici e vocali specifici.

---

## 🖼️ 14. CANONE DI PRE-TRATTAMENTO BOUNDING BOX RISORSE RASTER (ICON CROP STANDARD)

1. **La Fallacia del Canvas Padding Eccessivo nelle Icone Quadrate**:
   - Quando si importano asset grafici (es. icone per dock, inventario, barre azioni) generati da software di grafica o mockup esterni, è frequente che l'immagine contenga un'ampia cornice di tela trasparente vuota (padding) attorno al perimetro dell'emblema.
   - In Godot Engine, se tali texture vengono assegnate a pulsanti quadrati con `expand_icon = true`, l'engine calcola le proporzioni dell'icona sulla totalità del canvas raster (compresi i margini vuoti), comprimendo l'elemento visibile a una frazione minima delle sue dimensioni nominali.
2. **Canone di Ritaglio al Vivo Lossless (BBox Opaco)**:
   - Prima dell'integrazione o del rilascio definitivo nel repository, ogni risorsa raster destinata a pulsanti o slot UI deve essere scansionata ed elaborata con ritaglio al vivo (*lossless crop*) sui pixel opachi effettivi (`Alpha > 0`).
   - Questo garantisce che l'emblema occupi il 100% dell'area del pulsante con proporzioni simmetriche 1:1, armonizzandosi perfettamente alle altre icone della barra senza alterare l'architettura dei controlli.

---

## 📐 15. CANONE DI ALLINEAMENTO PERIFERICO HUD PER AMBIENTI 2.5D / ISOMETRICI

1. **La Causa Radice dell'Invasività Verticale dei Pannelli Periferici**:
   - Nelle interfacce di gioco 2.5D e isometriche, i pannelli periferici inferiori (es. box di dialogo, messaggi degli arredi, log di ispezione) tendono a espandersi verso l'alto se dimensionati arbitrariamente con font grandi o aree di ritratto sproporzionate.
   - Un'altezza eccessiva (es. > 150–200 px su viewport Full HD) crea una barriera opaca che invade l'area calpestabile del pavimento, occludendo arredi, porte o personaggi e danneggiando l'esperienza visiva dei collaboratori normovedenti.
2. **Canone di Allineamento alla Baseline del Dock**:
   - I box periferici inferiori devono allineare la propria altezza massima alla linea di base dei dock di comando adiacenti (es. 115–120 px).
   - Tipografia compatta autowrappata (font a 9–10 px su 2–3 righe) e ritratti proporzionati ($84 \times 84$ px anziché $120 \times 120$ px) consentono di comunicare la totalità delle informazioni e degli indicatori contestuali preservando una clearance orizzontale di sicurezza generosa ($\ge 80$ px) e lasciando libera l'intera visuale del mondo di gioco.

---

## 🎨 16. EREDITARIETÀ TEMATICA DELLE FINESTRE MODALI DI SISTEMA

1. **La Discontinuità Visiva dei Menu di Pausa / Sistema**:
   - È un anti-pattern comune creare o modificare le finestre modali di sistema (menu di pausa `Esc`, impostazioni audio/video, caricamento/salvataggio) come scene isolate senza assegnare il tema centrale dell'applicazione (`Theme`).
   - Di conseguenza, tali finestre ricadono sullo stile generico predefinito dell'engine (pulsanti grigi, font di fallback), spezzando l'immersione artistica (pixel art retrò arcade vs grigio piatto desktop).
2. **Canone di Propagazione del Tema Centrale**:
   - Ogni modale di sistema deve ereditare esplicitamente il file di tema condiviso (`res://.../menu_theme.tres`) sulla radice del pannello.
   - Tutti i titoli, bottoni e sotto-pannelli devono impiegare la tipografia di progetto (`PressStart2P.ttf` o font dedicato) con dimensioni proporzionate e palette colori coerente (bordi neon ciano, accenti oro e sfondi scuri ad alto contrasto), garantendo perfetta coerenza estetica e conformità WCAG.

---

## 🛡️ 17. GESTIONE MODALI DI SISTEMA, RESUME REQUESTED & CONTROLLO INERZIALE DELL'AVATAR (GODOT 4)

1. **Il Segnale `resume_requested` e la Parità di Chiusura Modale**:
   - In Godot 4, i componenti modali complessi come i menu di sistema o le schermate di pausa implementano spesso un pulsante dedicato "Riprendi" (o tasto rapido `Esc`) che emette `signal resume_requested` anziché il convenzionale `signal closed`.
   - Se il coordinatore dell'HUD (`ApartmentHud` o `ModalRouter`) connette unicamente `closed` al gestore di disarmo, il menu scompare graficamente ma Alex rimane congelato con `player.is_movement_locked = true` e il motore temporale resta fermo in pausa perpetua.
   - *Canone*: Connettere categoricamente sia `resume_requested` che `closed` al metodo unificato `close_modal(modal)`, garantendo il ripristino simmetrico dello stato fisico del giocatore e la revoca di `GameManager.is_paused()`.

2. **Azzeramento Immediato di Inerzia e Auto-Walk all'Avvio di Azioni**:
   - All'emissione di segnali di avvio azione (`EventBus.action_started`) o apertura modale (`modal_opened`):
     * Impostare immediatamente `player.velocity = Vector2.ZERO`;
     * Disarmare l'auto-walk (`player.cancel_auto_walk()`);
     * Impostare `player.is_movement_locked = true`.
   - Questo azzera qualsiasi forza inerziale residua impedendo che l'avatar scivoli via o completi itinerari di camminata pendenti mentre è impegnato o mentre una finestra di dialogo è a schermo.

3. **Inibizione degli Input a Monte durante `GAMEPLAY_BUSY`**:
   - Nel controller dell'avatar (`player_alex.gd`):
     * Aggiungere la guardia reattiva `var is_busy: bool = GameManager != null and GameManager.current_state == Enums.GameState.GAMEPLAY_BUSY`;
     * In `_physics_process(delta)`: se `is_busy` o `is_movement_locked`, azzerare `velocity = Vector2.ZERO` e restituire anticipatamente `return`;
     * In `_unhandled_input(event)`: sopprimere l'elaborazione degli eventi fisici durante `is_busy`.
   - Nel controller di scena (`apartment.gd`):
     * Intercettare `KEY_ESCAPE` durante `GAMEPLAY_BUSY` per invocare `action_system.cancel_action()`, consentendo l'interruzione sicura da tastiera;
     * Sopprimere click del mouse (`_on_prop_clicked`) e richieste di interazione arredi (`_on_player_interaction_requested`) se lo stato è `GAMEPLAY_BUSY`.

---

## 🏃 18. DISACCOPPIAMENTO CINETICO AVATAR, PRE-CACHING AUDIO A 0 MS & TTS NON-INTERRUPTING (GODOT 4)

1. **Pre-Caching Audio Procedurale Deterministico in `_ready()`**:
   - Nei nodi dedicati al sound design o sintesi procedurale (`AudioCueSystem`), il calcolo dei campioni PCM mono 16-bit (tramite `AudioStreamWAV` e cicli trigonometrici in GDScript) non deve mai avvenire al primo `play()`:
     ```gdscript
     func _ready() -> void:
         precache_all_cues()

     func precache_all_cues() -> void:
         for cue_type in AudioCueType.values():
             if not _stream_cache.has(cue_type):
                 _stream_cache[cue_type] = _generate_pcm_stream(cue_type)
     ```
   - In questo modo tutti gli earcon sono istantaneamente disponibili in memoria RAM a 0 ms, eliminando hitch di frame drop durante i contatti fisici.

2. **Accodamento Dolce per Annunci di Prossimità (`is_interrupt = false`)**:
   - Negli script che gestiscono trigger di contatto (`Area2D` con segnale `body_entered`):
     ```gdscript
     func _on_player_entered_prop(prop: InteractiveProp) -> void:
         # Annuncio vocale in modalità append per evitare lock COM sincroni
         AccessibilityManager.announce("Sei vicino a: " + prop.display_name, false)
     ```
   - L'impostazione `is_interrupt = false` evita l'invocazione sincrona a `DisplayServer.tts_stop()`, preservando la continuità di calcolo di `_physics_process` ed eliminando qualsiasi micro-stop cinetico del personaggio.

3. **Routing Differito di Azioni con Durata Temporale**:
   - Nei controller HUD (`ApartmentHud`):
     * Se un'azione selezionata ha `duration_seconds > 0.0`, instradarla a `_run_action_with_duration(action_data)`;
     * Memorizzare l'azione corrente in `_current_running_action`;
     * Connettere `EventBus.action_completed` per applicare l'effetto finale (es. `time_system.advance_to_next_period()`) solo al termine naturale del timer;
     * Connettere `EventBus.action_canceled` per azzerare `_current_running_action` senza mutare l'orologio né addebitare costi.

4. **Layout Vettoriale ad Alto Contrasto per Menu Interazione (`StyleBoxFlat`)**:
   - Sostituire le `TextureRect` a pergamena bitmap rigide con un `PanelContainer` stilizzato tramite `StyleBoxFlat`:
     * `bg_color = Color("#11121a")` (scuro profondo), `border_color = Color("#c49a45")` (oro/rame), `border_width = 2px`, `corner_radius = 4px`;
     * Impostare `custom_minimum_size.x = 480.0` per garantire sufficiente clearance;
     * Per i pulsanti delle opzioni: `autowrap_mode = TextServer.AUTOWRAP_WORD_SMART`, font size $\ge 14$ px e `content_margin` generoso;
     * Titolo a 16 px con colore ad alto contrasto (`#ffe066`), garantendo piena conformità WCAG AAA e leggibilità immediata sia su schermo che tramite sintesi vocale.

---

## 🧹 19. DISINCAGLIO SINCRONO DEI NODI (`remove_child + queue_free`) PER RICOSTRUZIONI UI DINAMICHE E TEST DETERMINISTICI (GODOT 4)

1. **Il Limite del Solo `queue_free()` nelle Rigenerazioni Sincrone**:
   - In Godot 4, il metodo `queue_free()` non rimuove immediatamente il nodo dalla gerarchia, bensì ne accoda la distruzione alla conclusione del frame corrente.
   - Quando una routine UI svuota un contenitore (`VBoxContainer`, `HBoxContainer`, `GridContainer`) e vi aggiunge immediatamente nuovi elementi nel medesimo frame (o all'interno di test harness headless eseguiti a 0 ms senza tick del loop principale), una successiva chiamata a `container.get_child_count()` o `container.get_children()` includerà ancora i vecchi nodi in attesa di deallocazione, provocando duplicazioni visive, conteggi errati o fallimenti di asserzione.

2. **Canone Operativo Universale di Pulizia**:
   - Prima di distruggere i nodi figli, scollega sempre ciascun nodo dalla gerarchia visiva tramite `remove_child()`, per poi invocarne la deallocazione sicura con `queue_free()`:
     ```gdscript
     func clear_container_synchronously(container: Node) -> void:
         for child in container.get_children():
             container.remove_child(child)
             child.queue_free()
     ```
   - Questo pattern garantisce che il contenitore risulti vuoto con certezza atomica e a 0 ms sia nei test headless sincroni sia in produzione su macchine ad alto frame rate, evitando ogni residuo o effetto collaterale di memoria.

---

## 🔠 20. PATTERN ERGONOMIA UI ACCESSIBILE: AUTOWRAP WORD-SMART & MULTI-RIGA PROTETTIVO SUI PULSANTI

1. **Il Limite del Default `AUTOWRAP_OFF` nei Controlli Godot 4**:
   - In Godot 4, i nodi `Button` e `Label` hanno per impostazione predefinita `autowrap_mode = TextServer.AUTOWRAP_OFF`.
   - Quando un'interfaccia modale visualizza opzioni complesse con descrizioni, metriche, orari o messaggi di stato/errore (es. *"Fuori orario: disponibile solo dalle 10:00 alle 16:00"*), una stringa di 100+ caratteri si espande orizzontalmente forzando la dimensione minima del pulsante oltre i confini del contenitore padre, sbordando dallo schermo.

2. **Canone di Progettazione Multi-Riga Protettivo**:
   - **Autowrap Intelligente Obbligatorio**: Configurare sempre `btn.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART` e `btn.size_flags_horizontal = Control.SIZE_EXPAND_FILL`.
   - **Strutturazione Gerarchica delle Righe**: Suddividere le informazioni su righe dedicate anziché concatenarle in un unico testo:
     * *Riga 1*: Intestazione, scorciatoia rapida e valore principale;
     * *Riga 2*: Costi, consumi o dettagli secondari;
     * *Riga 3*: Eventuale motivo di indisponibilità o disabilitazione con icona di attenzione.
   - **Contenimento in ScrollContainer**: Incapsulare le opzioni generate dinamicamente in uno `ScrollContainer` verticale a scorrimento orizzontale disabilitato (`SCROLL_MODE_DISABLED`), garantendo che nessun elemento possa mai eccedere la sagoma del layout modale.

---

## 💾 21. PATTERN PERSISTENZA MULTI-SLOT, SCANSIONE METADATI ATOMICA & SCRITTURA SICURA (.TMP $\to$ .JSON) PER GODOT 4

1. **Il Limite del File Singolo Monolitico**:
   - Limitare la persistenza di un gioco o applicazione a un singolo file (es. `user://savegame.json`) costringe l'utente a sovrascrivere la partita corrente ad ogni nuovo avvio, impedisce la creazione di carriere o backup paralleli e costringe a caricare per intero l'intero stato di gioco solo per mostrare un riepilogo in UI.

2. **Canone di Architettura Persistenza Multi-Slot (Schema v2)**:
   - **Cartella Dedicata**: Utilizzare una directory specifica (es. `user://saves/`) garantita tramite `DirAccess.make_dir_recursive_absolute()`.
   - **Disaccoppiamento Meta vs Payload**:
     * Suddividere il documento JSON in due sezioni distinte:
       ```json
       {
         "schema_version": 2,
         "meta": { "slot_id": "...", "save_name": "...", "updated_at": "...", "player_name": "...", "day_number": 5 },
         "data": { "player": { ... }, "world": { ... } }
       }
       ```
     * La funzione di scansione per gli elenchi UI (`get_save_slots_list()`) legge ed estrae unicamente il blocco `meta`, operando a 0 ms senza allocare o deserializzare i pesanti dizionari del payload di gioco.
   - **Scrittura Atomica Protetta (.tmp $\to$ .json)**:
     * Non scrivere mai direttamente sul file di salvataggio finale. Scrivere su `path + ".tmp"`.
     * Solo dopo la chiusura con successo (`file.close()`), sostituire o rinominare il file temporaneo con `DirAccess.rename_absolute(tmp_path, target_path)`.
     * Questo meccanismo previene al 100% la corruzione o il troncamento del salvataggio in caso di crash improvviso, interruzione di alimentazione o chiusura forzata.
   - **Migrazione Legacy Trasparente**:
     * All'avvio, se si rileva un vecchio file a slot singolo (`user://savegame.json`), migrarlo automaticamente nella nuova cartella come slot legacy (`save_legacy.json`) mantenendo un mirror sincronizzato per garantire la retrocompatibilità con test suite preesistenti.
   - **Accessibilità UI di Caricamento e Salvataggio**:
     * I menu di gestione slot devono consentire l'inserimento di un nome personalizzato (`LineEdit` con focus e conferma `Invio`), l'elenco navigabile con annunci NVDA dei metadati salienti, la creazione libera di nuove partite su slot indipendenti e la conferma protetta di cancellazione con annullamento rapido tramite tasto `Esc`.



