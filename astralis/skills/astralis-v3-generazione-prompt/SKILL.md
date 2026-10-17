---
name: "astralis-v3-generazione-prompt"
description: "Crea un prompt nuovo per un obiettivo, con input, perimetro e risultato verificabile. Non usare per: Miglioramento di un prompt già scritto o esecuzione diretta della normale richiesta dell’utente."
metadata: {"id": "AST-S-GENERAZIONE-PROMPT", "revision": "1.0.0", "applies_to": "ASTRALIS 3.X", "category": "05_prompt_e_documentazione", "protocols": [7], "intents": ["creare_prompt"], "use_when": ["Crea un prompt nuovo per un obiettivo, con input, perimetro e risultato verificabile."], "avoid_when": ["Miglioramento di un prompt già scritto o esecuzione diretta della normale richiesta dell’utente."], "materials": ["Obiettivo, destinatario, contesto e vincoli del prompt."], "prompt_ids": ["AST-P-GENERAZIONE-PROMPT"], "sources": ["skill-prompt-architect.md"]}
---

# Generazione di prompt

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Obiettivo, destinatario, contesto e vincoli del prompt.

Non applicare per: Miglioramento di un prompt già scritto o esecuzione diretta della normale richiesta dell’utente.

## Metodo

- Usa obiettivo, contesto, input, vincoli e output come struttura funzionale; evita ruoli ornamentali e sezioni vuote.
- Se il catalogo Astralis 3 è disponibile, valuta riuso o adattamento del prompt pertinente prima di duplicarlo.
- Rendi espliciti materiali mancanti e confini delle azioni; non aggiungere autorizzazioni o requisiti SPARK.
- Consegna testo copiabile e un esempio d’uso utile. Non consultare obbligatoriamente librerie remote e non eseguire il prompt appena creato senza mandato.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.
