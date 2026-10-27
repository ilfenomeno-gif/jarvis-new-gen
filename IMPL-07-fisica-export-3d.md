# IMPL-07 — Fisica Rapier e output della scena 3D

Collegato a [00-PROMPT-MASTER.md](./00-PROMPT-MASTER.md). Dipendenza:
IMPL-02. Rapier, export HTML e video sono sottostep separati e ciascuno ha un
proprio GO/NO-GO.

## 1. Analisi dell'ambito

Ispezionare `Mark-LIV-main/assets/viewer3d/`, sorgenti e bundle, licenze,
`viewer_3d`, IPC, modelli, test isolati e policy di caricamento. Cercare prove
attuali di Rapier, export self-contained e cattura video. Non dedurre che
funzioni dal solo fatto che Three.js è presente.

## 2. Diagnosi

La fisica richiede WASM, lifecycle, mapping tra mesh/collider e gestione di
collisioni/risorse. L'export HTML crea un artefatto portabile con dipendenze e
modello incorporati; video richiede frame capture e forse ffmpeg. Rischi:
dimensioni, licenze, XSS, memory exhaustion, percorsi arbitrari e crash del
renderer. Definire use case e limiti distinti prima della scelta tecnica.

## 3. Convalida di fattibilità

**GO** solo per sottostep con asset di test, licenze verificabili, limite
dimensione/tempo e target browser dichiarati. Per Rapier accettazione: gravità
e collisione deterministiche in scena di test e stop/dispose puliti. Per HTML:
singolo file offline senza rete e con risorse controllate. Per video: durata,
risoluzione, codec, cancellazione e output validato. **NO-GO** se serve
caricare script o file arbitrari senza sanitizzazione.

### Gate Rapier (decisione prima dell'implementazione)

**GO limitato al sottostep Rapier; HTML e video restano fuori ambito.**

- Target: la pagina locale QtWebEngine del viewer, senza richieste a rete;
  WebAssembly deve avviarsi anche su `file://`.
- Dipendenza: `@dimforge/rapier3d-compat` 0.19.3, metadata npm `Apache-2.0`;
  tarball 2,6 MB, WASM 1.569.588 byte e WASM incluso nel bundle locale.
- Asset: `cad/pc.glb` (45.864 byte) e `a-red-apple-ca3ead.glb` (842.548 byte);
  il viewer applica già un tetto di 40 MiB per modello.
- Collider semplificato: un cuboide basato sui bounds per il modello attivo e
  un piano fisso; un solo modello attivo per il contratto corrente.
- Limiti runtime: gravità -9,81 m/s², passo fisso 1/60 s, massimo 4 substep
  per frame, drop da +2 unità, impulso verticale fisso 4, niente input di
  vettori o geometrie arbitrari. Stop del body quando si esplode/rimuove un
  modello e `World.free()` alla chiusura pagina; errore esplicito senza WASM,
  nessun fallback che simuli fisica.
- Accettazione misurabile: gravità e contatto col piano per entrambi i GLB;
  stato a riposo entro 0,03 unità dal piano e velocità verticale sotto 0,1;
  impulso con velocità verticale positiva; conflitto con `explode_model`
  risolto e testato in entrambi gli ordini; body rimosso quando cambia scena;
  pagina offline funzionante; bundle finale sotto 5 MiB.
- Rollback: rimuovere i comandi/API fisica, la dipendenza Rapier e rigenerare
  il bundle Three.js senza Rapier. La branch parte da `origin/main` pulito;
  le modifiche locali preesistenti restano escluse e intatte.

## 4. Implementazione

Rapier 0.19.3 è una dipendenza locale fissata da `package-lock.json`; il WASM
è incorporato nel bundle. `apply_physics` accetta solo `drop` o `impulse`,
senza vettori o geometrie forniti dal chiamante. Il viewer crea un cuboide
basato sui bounds del modello e un piano fisso; se Rapier/WASM non è pronto,
il comando restituisce errore e non simula un fallback. L'esplosione rimuove
il body e ripristina la posa iniziale; applicare fisica a un modello esploso
lo riassembla prima.

Export HTML e video non sono stati implementati in questo sottostep.

## 5. Test e debug

Test unitari per mapping collider, gravità, collisioni, reset, asset mancante
e leak; real-page isolati con scena locale. HTML: parsing, offline, hash,
assenza di URL remoti e limite dimensione. Video: test sintetico breve,
interruzione, codec non disponibile e file finale apribile. No telemetria
fittizia; misurare FPS e memoria su hardware dichiarato.

## 6. Analisi dei risultati

| Sottostep/criterio | Prova/comando ed esito | Limite |
|---|---|---|
| Rapier: fisica e lifecycle | `npm ci`: 4 package installati, 0 vulnerabilità. Build esbuild: 2.942.506 byte (< 5 MiB). `python -m pytest -q tests\test_viewer3d.py -k "not test_real_page"`: 15 passed, 4 skipped, 12 deselected. Pagina QtWebEngine software-rendered: PC drop/impulse ed entrambi gli ordini con `explode_model`, cleanup; PC e mela entrambi a riposo entro 0,03 dal pavimento e velocità verticale sotto 0,1. `verifica.py --fast`: 38/38. | La suite isolata include un errore baseline non correlato: `test_real_page_model_events_restore_viewer_and_report_load_errors` importa `save_screenshot` non esportato da `core.viewer3d`; la suite completa in un processo non è certificata per il crash nativo Qt/WebEngine già osservato. Nessuna misura FPS/memoria su GPU hardware. |
| HTML: file autonomo offline | [da compilare] | |
| Video: output leggibile/cancellabile | [da compilare] | |
| Licenza e bundle Rapier | `@dimforge/rapier3d-compat` 0.19.3 Apache-2.0; notice e testo licenza inclusi. Bundle standalone locale: 2.942.506 byte. | Non è una misura di prestazioni runtime. |

## 7. Diagnosi post-test

QtWebEngine/Chromium con rendering software SwiftShader (`--disable-gpu
--use-gl=angle --use-angle=swiftshader`), pagina locale `file://`. Asset
verificati: `cad/pc.glb` 45.864 byte e mela `a-red-apple-ca3ead.glb`
842.548 byte. Il test mela usa `JARVIS_TEST_APPLE_GLB` per copiare l'asset
temporaneamente nella directory locale dei modelli e lo rimuove al termine.
Non è stata usata una GPU hardware; export HTML e video restano fuori ambito.

## 8. Convalida finale

| Meccanica | Esito | Evidenza |
|---|---|---|
| Rapier | VERIFICATO-TEST | Test unitari e real-page isolati su PC e mela; drop, impulso, riassemblaggio/esplosione in entrambi gli ordini e cleanup verificati. |
| Export HTML autonomo | PARZIALE | Nessuna prova attestata nell'audit |
| Video/MP4 | PARZIALE | Nessuna prova attestata nell'audit |

### Log dello step

| Data | Step | Comando/prova | Esito | Cosa NON è provato |
|---|---|---|---|---|
| 2026-10-27 | IMPL-07 Rapier | `npm ci`; esbuild; `python -m pytest -q tests\test_viewer3d.py -k "not test_real_page"`; `python -m pytest -q tests\test_viewer3d.py::test_real_page_physics_pc_and_explode_interactions`; `JARVIS_TEST_APPLE_GLB=<asset> python -m pytest -q tests\test_viewer3d.py::test_real_page_physics_apple_drop`; `python verifica.py --fast` | Rapier VERIFICATO-TEST; sottostep export e video non eseguiti. Verifier 38/38; test mirati e prove live passati; bundle 2.942.506 byte. | Runner isolato ha rilevato un test preesistente non correlato con `ImportError: save_screenshot` da `core.viewer3d`; suite completa in un solo processo non certificata per crash nativo Qt/WebEngine; GPU hardware e prestazioni non misurate. |
