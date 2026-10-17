# Implementazione — Ologrammi 3D generati da Jarvis

Piano per il flusso testo → modello 3D → ologramma nel viewer Three.js già esistente (vedi `IMPLEMENTAZIONE-UI.md`, U2-U4).
Regole: uno step si chiude solo con una prova reale documentata; ciò che non è provato resta `parziale`.
A fine di ogni step il file viene riletto e aggiornato prima di passare al successivo.

## Contenuto del brief (sintesi)
Flusso: comando vocale → tool `generate_3d_model` (API Tripo3D o altro provider) → download `.glb` in `assets/viewer3d/models/` → `viewer_3d load_model` con `GLTFLoader` → effetto olografico (trasparenza, scanline, bagliore). Didattica: `explode_model`, `highlight_part`. Skill dichiarativa `ologramma`.
Provider citati: Tripo3D (SDK Python, free 200 crediti/mese), Meshy, Luma, Rodin (commerciali); Hunyuan3D 2.0 e ApexForge (open source, richiedono GPU); `three.ws` (citata come API keyless, non verificata).

## Decisioni
- Provider iniziale: **Tripo3D**, via REST con la sola libreria standard (nessuna nuova dipendenza); la chiave sta nel `SecretStore`, mai in chiaro né in chat. Senza chiave il tool risponde con un messaggio chiaro, non fallisce.
- Il tool di generazione è `risk_class: write` (scarica e scrive file) e opera solo dentro `assets/viewer3d/models/`.
- `load_model` accetta solo file `.glb`/`.gltf` dentro la cartella modelli (niente percorsi arbitrari), con limite di dimensione.
- Non si usano API non verificate (`three.ws`, endpoint inventati): si aggiungono solo dopo averli letti nella documentazione ufficiale.

## Fasi
- [x] **G1 — `GLTFLoader` e `load_model`** (2026-10-17, ok): bundle con `GLTFLoader`; comando `loadModel`/`clearModel` validato (solo cartella modelli); il modello compare al centro. Criterio: un `.glb` reale viene caricato nella pagina reale e `getState()` riporta nodi/mesh.
- [x] **G2 — Didattica** (2026-10-17, ok): `explode_model(on)` e `highlight_part(name)` sui nodi del modello. Criterio: stato JS riletto (posizioni dei nodi cambiate, parte evidenziata) su un `.glb` con più nodi.
- [x] **G3 — Effetto olografico** (2026-10-17, ok): materiale con trasparenza, scanline e bagliore sul modello; interruttore `hologram`. Criterio: nessun errore di shader nella pagina reale (stato `hologram` letto indietro).
- [~] **G4 (parziale: test con client finto 7/7, suite 404 OK, `verifica.py --fast` 38/38; chiamata Tripo reale NON provata, manca la chiave; `set-tripo-key` aggiunto) — Tool `generate_3d_model`**: client Tripo3D (REST, thread del tool), download in `models/`, poi `load_model`. Criterio: test con trasporto finto (successo, errore, timeout, chiave assente) + lettura documentazione ufficiale dell'API. La prova con la rete reale richiede la chiave dell'utente: `parziale` finché non c'è.
- [x] **G5 (fatto: `skills/ologramma/SKILL.md` caricata dal registry, `review_required` finché l'utente non esegue `skill-approve ologramma`) — Skill `ologramma`**: `SKILL.md` nel formato delle skill esistenti, con quando/come usare generazione e controllo del modello. Criterio: la skill viene caricata dal registry senza rifiuti.
- [x] **G6 (in chiusura: commit, push, CI, riavvio) — Chiusura**: suite completa, `verifica.py --fast`, CI verde, riavvio di JARVIS, aggiornamento di `LICENSES.md` (GLTFLoader fa parte di Three.js, MIT).

## Fuori scope
- Meshy/Luma/Rodin, Hunyuan3D locale, scene procedurali OSM, HY-World 2.0: servono chiavi, GPU o analisi separata.
- Rigging/animazione dei modelli generati.

## Fase L — Generazione 3D locale (nessuna API a pagamento)
Brief: motore open source in locale sulla GPU. Fatti verificati dal README ufficiale: **TripoSR è solo image-to-3D** (nessun `text_2_3d.py`), ~6 GB di VRAM; quindi pipeline a due stadi **SD-Turbo (testo→immagine) → TripoSR (immagine→mesh)**, caricati in sequenza per stare in 8 GB. Hunyuan3D 2.0 scartato per ora (VRAM maggiore, analisi separata). Il lavoro pesante gira in un **sottoprocesso** (`core/local_3d_worker.py`): VRAM liberata a fine lavoro, crash isolati, OOM → messaggio chiaro (riprova a risoluzione 256/192/128).
- [x] **L1 — Hardware e dipendenze** (ok): sonda GPU/torch/dipendenze (`python -m core.local_3d_gen`), rifiuto se manca CUDA o VRAM < 6 GB, `requirements-3d.txt` separato, `setup` che clona TripoSR (MIT) in `third_party/` (gitignorata).
- [x] **L2 — `core/local_3d_gen.py`** (ok): orchestratore senza torch, runner iniettabile, timeout, OOM, validazione GLB.
- [x] **L3 — Integrazione nel tool** (ok): backend `auto|local|tripo` (`JARVIS_3D_BACKEND` o `config/model_gen.json`, CLI `set-3d-backend`); `auto` = Tripo se c'è la chiave, altrimenti locale se installato.
- [x] **L4 — Prova reale su GPU** (ok): "a simple chair" generata sulla RTX 4060, vedi log.
- [x] **L5 — Chiusura**: suite, `verifica.py --fast`, licenze, commit, CI, riavvio.

## Log verifiche
| Data | Step | Comando / prova | Esito |
|---|---|---|---|
| 2026-10-17 | L1-L2 | 15+ test con runner finto: successo, OOM, timeout, crash, GLB non valido, torch assente, CUDA assente, VRAM bassa, pythonw→python.exe | ok |
| 2026-10-17 | L4 | Bug 1: `torchmcubes` non è su PyPI e non compila (nessun CUDA toolkit) → sostituto con scikit-image; assi e orientamento verificati su un ellissoide (estensioni = (asse2,asse1,asse0), volume>0, watertight). Bug 2: con `transformers` 5.x il checkpoint TripoSR non carica (nomi layer ViT) → `transformers<5`, `diffusers<0.36`, `huggingface-hub<1` (`pip check` pulito). Bug 3: la mesh esce Z-up, glTF è Y-up (sedia sdraiata) → rotazione −90° su X, verificata (asse più alto = Y). Esecuzione reale: 47 s, 38k vertici, GLB 1,5 MB; immagine intermedia = sedia singola centrata | ok |
| 2026-10-17 | L4 | End-to-end: `generate_3d_model` (backend local) con `JarvisUI` offscreen → `a-simple-chair-318a73.glb`, viewer in primo piano, `status=ready`, `hologram=true`, `shaderError=""`, 1 nodo | ok. Parziale: aspetto non visto a schermo (cattura offscreen nera) |
| 2026-10-17 | L5 | pytest: 415 passati (3/3 rilanci); un solo crash di `pytest` non riprodotto in 4 rilanci. `verifica.py --fast` 38/38 | ok |
| 2026-10-17 | G1 | pytest tests/test_viewer3d.py: 9 passati. Pagina reale offscreen carica un .glb generato (2 nodi) via GLTFLoader da file://: status=ready, nodes=[part_a,part_b], viewer in primo piano; clear_model ripristina; nomi con percorsi/estensioni errate rifiutati (model_file) | ok |
| 2026-10-17 | G2 | pytest tests/test_viewer3d.py: 11 passati. Bug trovato e corretto subito: size passato come vettore -> NaN (moved=null). Dopo il fix: explode=1 con spostamenti >0.1, highlight_part imposta glow su 1 mesh e lo toglie, riassemblaggio riporta gli offset a 0 | ok. Nota: un modello a nodo unico (tipico output Tripo) ha parts=0, l'esplosione non ha effetto |
| 2026-10-17 | G3 | pytest tests/test_viewer3d.py: 12 passati. ShaderMaterial olografico (fresnel, scanline, glitch, additivo) applicato di default ai modelli; set_hologram on/off; highlight sopravvive al toggle; nessun shaderError con WebGL attivo (hook renderer.debug.onShaderError) | ok. Parziale: aspetto non visto a schermo |
