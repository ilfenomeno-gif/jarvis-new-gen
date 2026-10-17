---
name: ologramma
description: >
  Crea e controlla ologrammi 3D nel visualizzatore centrale. Usa questa
  skill quando l'utente chiede "crea un ologramma di", "mostrami in 3D",
  "spiegami visivamente", "smontalo" o "evidenzia" una parte. Non usarla
  per mappe o voli: per quelli basta viewer_3d.
triggers: crea un ologramma, mostrami in 3D, spiegami visivamente, smontalo, evidenzia, blueprint, modalità solida, materiale realistico, torna all'ologramma, spiega un motore, smonta un pc, cosa sto guardando, che cos'è questa
tool_refs: generate_3d_model, viewer_3d
risk_class: write
status: active
---
# Procedura
1. Per un oggetto nuovo chiama `generate_3d_model` con `prompt` breve e descrittivo. Col generatore locale (GPU) è gratis e richiede circa un minuto; con Tripo consuma crediti: avvisa l'utente.
   Se la generazione con Tripo fallisce per crediti, o se l'utente chiede di usare il generatore locale, richiama immediatamente il tool `generate_3d_model` impostando `engine='local'` (senza chiedere conferma e senza riprovare con Tripo). Riporta all'utente l'errore esatto se anche il locale fallisce.
2. Il modello viene caricato da solo come ologramma; non serve altro `show`.
3. "Smontalo": `viewer_3d` con `mode=explode_model` e `on=true` (`on=false` per ricomporre).
4. "Evidenzia X": `viewer_3d` con `mode=highlight_part` e `part=X`.
5. Se `explode_model` non muove nulla, il modello ha un solo nodo: dillo all'utente.
6. Per tornare al globo: `viewer_3d` con `mode=clear_model`.
7. Se manca un generatore, spiega le due strade: chiave Tripo (`python -m core.registry_cli set-tripo-key`) oppure generatore locale (`python -m core.local_3d_gen setup`).
8. Stile del materiale: "mostralo in blueprint / solido / tecnico" → `viewer_3d` con `mode=set_material_style` e `style=blueprint` (blu solido con bordi ciano da CAD). `style=realistic` mostra le texture originali, `style=hologram` torna all'ologramma (predefinito).
9. Descrizioni al passaggio del mouse: chiama `viewer_3d` con `mode=list_parts` e `model=<file .glb>` per leggere i nomi reali delle parti, poi `mode=set_part_info` con `part_info` = testo JSON `{"nome_parte": "descrizione breve"}` usando SOLO i nomi restituiti. Se le parti non hanno nome (modelli CAD Khronos del motore) il viewer le etichetta `Parte 1`, `Parte 2`, ... per posizione: usa quei nomi solo dopo aver visto il tooltip, non inventare corrispondenze. Poi di' all'utente: "passa il mouse sulla parte per vederne la descrizione". Se `list_parts` ne restituisce una sola o nessuna (tipico dei modelli generati), dillo e non promettere tooltip per i singoli componenti.
10. Comandi vocali di stile: "mostrami questo in blueprint" / "metti il globo in blueprint" → `set_material_style` con `style=blueprint`; "passa al materiale realistico" → `style=realistic`; "torna all'ologramma" → `style=hologram`. Lo stile è ricordato e applicato al prossimo modello anche se ora c'è solo il globo; il globo non ha stili: dillo.
11. "Spiega un motore", "smonta un PC / un cambio / una sega": NON generare con l'IA (i modelli generati hanno un solo nodo e non si smontano). Chiama `viewer_3d` con `mode=list_models`, poi `mode=load_model` con `model=cad/engine.glb` (anche `cad/pc.glb`, `cad/gearbox.glb`, `cad/saw.glb`, `cad/milk_truck.glb`) e `mode=explode_model`. "Spiega un PC" / "smonta il computer" → `load_model` con `model=cad/pc.glb` (parti con nome: case, motherboard, cpu, cpu_cooler, ram_1, ram_2, gpu, psu, fan; puoi usarle con `highlight_part`). Il PC è un modello semplificato generato dal codice (`python -m core.make_pc_cad`, incluso in `download-cad-models`): dillo se serve. Se i CAD non sono scaricati, di' di eseguire `python -m core.registry_cli download-cad-models`. Un PC reale e dettagliato non esiste tra i CAD disponibili: non inventare componenti oltre a quelli elencati.
12. "Cosa sto guardando?" / "Che cos'è questa?": chiama `viewer_3d` con `mode=hovered_part` e rispondi con il nome e la descrizione ricevuti; se il mouse non è su nessuna parte, dillo. Non indovinare la parte.
13. Mouse: con un modello caricato l'utente può trascinare per ruotarlo, usare la rotellina per lo zoom e il tasto destro per spostare la vista; dillo quando mostri un modello. `viewer_3d` con `mode=set_controls` e `on=false/true` disattiva/riattiva i controlli.
14. I modelli generati in locale vengono mostrati automaticamente in stile `blueprint` (solido pulito: le texture di TripoSR sono sfocate). Se l'utente chiede "mostrami le texture originali", usa `set_material_style` con `style=realistic`; "torna all'ologramma" → `style=hologram`. Per mobili o oggetti cavi (armadio, credenza) passa un prompt inglese semplice (es. "a closed wooden wardrobe"): il generatore aggiunge già i suggerimenti di forma.
