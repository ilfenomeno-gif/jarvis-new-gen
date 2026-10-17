# viewer3d

Globo olografico (Three.js) mostrato nello stack centrale di `ui.py`. `viewer.bundle.js` è generato da `src/viewer.js` e committato, così l'app non richiede Node né rete a runtime. Three.js è MIT (vedi `LICENSES.md`).

Rigenerare il bundle (richiede Node), da una cartella temporanea:

```
npm i three@0.186.1 esbuild
set NODE_PATH=<cartella temporanea>\node_modules
npx esbuild <percorso>/src/viewer.js --bundle --minify --format=iife --outfile=<percorso>/viewer.bundle.js
```

API JS esposta come `window.jarvisViewer`: `flyTo(lat, lon)`, `addMarker(lat, lon, label)`, `clearMarkers()`, `spin(on)`, `setMaterialStyle('hologram'|'blueprint'|'realistic')`, `setPartInfo({parte: descrizione})` (tooltip al passaggio del mouse), `getState()`.


HDRI `hdr/studio.hdr`: Poly Haven `studio_small_03` 1k, licenza CC0 (usato da `realistic` per riflessi PBR).
