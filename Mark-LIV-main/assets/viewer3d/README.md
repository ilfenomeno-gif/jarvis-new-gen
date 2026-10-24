# viewer3d

Globo olografico (Three.js) mostrato nello stack centrale di `ui.py`. `viewer.bundle.js` è generato da `src/viewer.js` e committato, così l'app non richiede Node né rete a runtime. Three.js è MIT (vedi `LICENSES.md`).

Rigenerare il bundle (richiede Node), da una cartella temporanea:

```
npm i three@0.186.1 esbuild
set NODE_PATH=<cartella temporanea>\node_modules
npx esbuild <percorso>/src/viewer.js --bundle --minify --format=iife "--define:import.meta.url=\"file:///three/examples/jsm/loaders/\"" --outfile=<percorso>/viewer.bundle.js
```

API JS esposta come `window.jarvisViewer`: `flyTo(lat, lon)`, `addMarker(lat, lon, label)`, `clearMarkers()`, `spin(on)`, `setMaterialStyle('hologram'|'blueprint'|'realistic')`, `setPartInfo({parte: descrizione})` (tooltip al passaggio del mouse), `getState()`.

Gli stati visuali sono definiti in `config/hud_states.json` e le durate in `config/hud_transitions.json`; PyQt6 interpola core, anelli, glow, waveform e particelle, mentre il viewer anima core, anelli e particelle con gli stessi parametri. Dopo aver modificato i JSON, eseguire `python -m core.registry_cli reload_hud_states` dalla cartella `Mark-LIV-main`: l'istanza attiva rileva il segnale su file e ricarica senza riavvio.


HDRI `hdr/studio.hdr`: Poly Haven `studio_small_03` 1k, licenza CC0 (usato da `realistic` per riflessi PBR).

Decoder Draco (Apache-2.0) in draco/, copiati da 	hree/examples/jsm/libs/draco/gltf/; il decoder Meshopt è incluso nel bundle. Il viewer carica solo risorse locali sotto models/ (URL esterni bloccati).
