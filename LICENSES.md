# Licenze dei componenti

Questa repository raccoglie progetti distinti: non esiste una licenza root che
conceda diritti sull'intero contenuto. La presenza di una licenza in una
cartella non estende automaticamente i suoi termini alle altre.

| Componente | Licenza o stato dichiarato | File/metadata |
|---|---|---|
| App JARVIS | CC BY-NC 4.0; uso commerciale non consentito dai termini indicati | [`Mark-LIV-main/LICENSE`](./Mark-LIV-main/LICENSE) |
| ASTRALIS | Apache-2.0 | [`astralis/LICENSE`](./astralis/LICENSE) |
| Sorgenti God's Eye View inclusi nel progetto e copie GEV top-level | MIT, con note aggiuntive nel file | [`Mark-LIV-main/gods-eye-view-main/_gev-clone/LICENSE`](./Mark-LIV-main/gods-eye-view-main/_gev-clone/LICENSE) e licenze nelle rispettive copie |
| Three.js 0.186.1 (incluso minificato in `Mark-LIV-main/assets/viewer3d/viewer.bundle.js`, con GLTFLoader) | MIT, Copyright 2010-2026 three.js authors | [`Mark-LIV-main/assets/viewer3d/README.md`](./Mark-LIV-main/assets/viewer3d/README.md) |
| `@dimforge/rapier3d-compat` 0.19.3 (WASM incluso nel bundle del viewer) | Apache-2.0, package metadata npm | [`RAPIER-NOTICE.txt`](./Mark-LIV-main/assets/viewer3d/licenses/RAPIER-NOTICE.txt), [`Apache-2.0.txt`](./Mark-LIV-main/assets/viewer3d/licenses/Apache-2.0.txt), [`package.json`](./Mark-LIV-main/assets/viewer3d/package.json), [`package-lock.json`](./Mark-LIV-main/assets/viewer3d/package-lock.json), [upstream](https://github.com/dimforge/rapier.js) |
| tripo3d 1.0.0 (dipendenza opzionale, non inclusa nel repository) | MIT (metadati del pacchetto) | `Mark-LIV-main/requirements-optional.txt` |
| TripoSR (clonato in `third_party/`, non versionato) | MIT | [github.com/VAST-AI-Research/TripoSR](https://github.com/VAST-AI-Research/TripoSR) |
| SD-Turbo (pesi scaricati da Hugging Face, non inclusi) | Stability AI: artefatto di ricerca, uso commerciale soggetto a [stability.ai/license](https://stability.ai/license) | [huggingface.co/stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) |
| torch, diffusers, transformers, rembg, trimesh, scikit-image (opzionali, non inclusi) | Licenze dei rispettivi pacchetti, da verificare prima di redistribuire | `Mark-LIV-main/requirements-3d.txt` |
| Estensione VS Code | Nessun file `LICENSE` o campo `license` dichiarato nel `package.json` al momento della verifica | [`jarvis-vscode-extension/package.json`](./jarvis-vscode-extension/package.json) |
| Documentazione di analisi e altri snapshot | Verificare i singoli file e le attribuzioni; nessuna licenza unica dedotta dalla root | Cartelle rispettive |

Prima di copiare, modificare o distribuire un componente, leggi il testo della
sua licenza e le eventuali note su dati, marchi e asset di terze parti.
L'estensione VS Code e i materiali senza licenza esplicita non devono essere
considerati liberamente riutilizzabili. Una distribuzione combinata richiede
una verifica delle licenze dei singoli componenti e delle loro dipendenze.
