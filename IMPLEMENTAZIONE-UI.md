# Piano di implementazione: UI versatile e agentica

Checklist di riferimento per il lavoro sulla UI. **Dopo ogni step**: rileggere questo file, spuntare le caselle, annotare il comando eseguito e l'esito nel log in fondo. Il piano generale resta in `IMPLEMENTAZIONE.md`.

Regole: la UI è PyQt6 nativo (`ui.py`); il core resta Python. La UI non legge né scrive dati utente: i tool UI sono `risk_class: read`. Uno step è *chiuso* solo con una prova eseguita (test + prova su finestra reale offscreen); se manca la prova a schermo o con Gemini reale è `parziale: <motivo>`.

## Stato di partenza (verificato, commit `764f13b`, CI verde)

- [x] Focus mode (`Ctrl+Shift+F`, `MainWindow.set_focus_mode`).
- [x] Tool `ui_layout` (`focus_on/off/toggle`) via segnale Qt thread-safe.

## Step

- [x] **U1 — Registro pannelli, `toggle_panel`, workspace** (2026-10-17): `core/ui_panels.py` (`PanelState`, preset `full/focus/coding/recon`), `MainWindow.apply_workspace/set_panel_visible/_render_panels`, segnali Qt thread-safe, `ui_layout` esteso (`toggle_panel`, `workspace`, `status`). Provato: 385 test, incluso `test_real_window_renders_each_workspace` su `JarvisUI` reale offscreen (visibilità di tutti e 5 i pannelli per ogni preset). Parziale: non visto a schermo né chiamato da Gemini.
- [x] **U2 — `Viewer3D` (WebView con Three.js locale)** (2026-10-17): `assets/viewer3d/` (sorgente `src/viewer.js`, bundle esbuild 520 kB committato, Three.js MIT in `LICENSES.md`), pagina creata in modo pigro come pagina dello stack centrale (`MainWindow.show_viewer3d`). Provato: `test_real_page_loads_and_receives_commands` carica la pagina reale (offscreen, WebGL software) e rilegge lo stato JS. Parziale: non visto a schermo con GPU reale.
- [x] **U3 — Tool `viewer_3d`** (2026-10-17): `core/viewer3d.build_call` (allow-list di funzioni, range lat/lon, argomenti JSON mai interpolati nel testo dello script), `actions/viewer_3d.py` (`show/hide/fly_to/add_marker/clear_markers/spin`, `risk_class: read`), segnali Qt thread-safe. Provato: validazione (funzioni non ammesse, tipi, range) + stato JS riletto dopo `show`, `add_marker`, `fly_to` (marker "Roma", `flying=true`). Parziale: non chiamato da Gemini; il radar `HudCanvas` resta la vista predefinita (il globo è opt-in tramite `show`).
- [x] **U5 — Pannelli agganciabili (`QDockWidget`)** (2026-10-17): Activity Log, Controlli (SYS MONITOR) e Input (upload + comando + interrupt/mute) sono `HudDock` (spostabili, chiudibili con la X, staccabili in finestra flottante, anche a schede). Il viewer (radar/WebView/camera) resta il widget centrale, non agganciabile, e si espande quando i dock si chiudono. `ui_layout` ora ha `toggle_panel` (`activity_log|controls|input|header|content|footer`, alias `left`/`right`/`log`), `float_panel` (`floating` true/false/omesso = inverte) e `restore_layout`. Focus mode: nasconde i dock senza distruggerli e all'uscita ripristina esattamente lo stato precedente (dock chiusi restano chiusi, flottanti restano flottanti). Layout salvato in `config/ui_layout.json` (gitignorato; atomico; versione, `saveState` Qt in base64, geometria finestra, flag pannelli) all'uscita, ogni 5 s se cambia (copre kill del processo) e mai mentre la focus mode ha i dock nascosti; caricato all'avvio, con ripiego sul layout predefinito se il file manca/è corrotto/di altra versione. Menu tasto destro su header e titoli dock: mostra/nascondi dock e "Ripristina layout". Provato: 442 test, 14 nuovi/riscritti in `tests/test_ui_panels.py` su `JarvisUI` reale offscreen (spostamento tra aree, chiusura X, float, restore, focus, centro che si espande, riavvio simulato = seconda `JarvisUI` che rilegge il file, file corrotto). Parziale: trascinamento col mouse e tear-off a mano non provati (offscreen); non chiamato a voce da Gemini.

## Fuori scope per ora (non fare finché non c'è un asset/caso reale)

- `load_model`, `highlight_part`, `explode_model`: richiedono un modello `.glb` reale e un loader; senza asset sarebbero stub non provabili.
- `QWebChannel`: non necessario, i comandi vanno con `runJavaScript` e payload JSON; rivalutare se servono eventi da JS verso Python.
- Glassmorphism, hover reveal, sostituzione del radar `HudCanvas`.

## Log verifiche

| Data | Step | Comando / esito |
|------|------|-----------------|
| 2026-10-17 | Base | focus mode + `ui_layout`: 383 test, CI verde su `764f13b` |
| 2026-10-17 | U1 | pytest 385 passed; test_real_window_renders_each_workspace su JarvisUI offscreen ok |
| 2026-10-17 | U2, U3 | pytest 388 passed; test_viewer3d: pagina Three.js reale caricata offscreen, stato JS riletto (ready, flying, marker) |
| 2026-10-17 | U2 fix | CI 4882b3c: job jarvis rosso (WebGL2 blocklisted su runner, jarvisViewer non esposto). Viewer ora tollerante (getState.webgl); test passato con e senza WebGL (--disable-webgl) |
| 2026-10-17 | U2/U3 fix a schermo | Segnalato: tool 'Eseguito' ma radar 2D visibile. Ora fly_to/add_marker portano in primo piano il globo, workspace recon lo mostra, HTML con sfondo nero e testo 'Inizializzazione Ologramma...'. 389 test; verificato currentWidget e isVisible su finestra offscreen (grab WebEngine nero offscreen: non prova il rendering GPU) |
| 2026-10-17 | U4 voli live | Tool viewer_3d: load_live_flights (OpenSky anonimo, region europe/usa/world, max 400 punti, solo in volo) e clear_flights; HTTP nel thread del tool, JS via segnale Qt; punti gialli (THREE.Points). 392 test; prova reale: 400 voli Europa, getState().flights=400, webgl=true, globo in primo piano. Parziale: punti senza orientamento/rotta; OpenSky anonimo ha rate limit (errore esplicito); non chiamato a voce da Gemini |
