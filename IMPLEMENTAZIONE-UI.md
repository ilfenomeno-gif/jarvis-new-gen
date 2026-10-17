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

## Fuori scope per ora (non fare finché non c'è un asset/caso reale)

- `load_model`, `highlight_part`, `explode_model`: richiedono un modello `.glb` reale e un loader; senza asset sarebbero stub non provabili.
- Migrazione completa a `QDockWidget`: rischio alto sul layout esistente, il registro pannelli copre il bisogno (nascondere/mostrare, preset) senza riscrivere `MainWindow`. Rivalutare se serve staccare i pannelli su un secondo monitor.
- `QWebChannel`: non necessario, i comandi vanno con `runJavaScript` e payload JSON; rivalutare se servono eventi da JS verso Python.
- Glassmorphism, hover reveal, sostituzione del radar `HudCanvas`.

## Log verifiche

| Data | Step | Comando / esito |
|------|------|-----------------|
| 2026-10-17 | Base | focus mode + `ui_layout`: 383 test, CI verde su `764f13b` |
| 2026-10-17 | U1 | pytest 385 passed; test_real_window_renders_each_workspace su JarvisUI offscreen ok |
| 2026-10-17 | U2, U3 | pytest 388 passed; test_viewer3d: pagina Three.js reale caricata offscreen, stato JS riletto (ready, flying, marker) |
