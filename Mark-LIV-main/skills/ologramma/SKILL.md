---
name: ologramma
description: >
  Crea e controlla ologrammi 3D nel visualizzatore centrale. Usa questa
  skill quando l'utente chiede "crea un ologramma di", "mostrami in 3D",
  "spiegami visivamente", "smontalo" o "evidenzia" una parte. Non usarla
  per mappe o voli: per quelli basta viewer_3d.
triggers: crea un ologramma, mostrami in 3D, spiegami visivamente, smontalo, evidenzia
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
