---
name: "astralis-v3-confronto-opzioni"
description: "Confronta almeno due opzioni note per aiutare una scelta motivata e contestabile. Non usare per: Alternative non ancora definite o scelta dell’utente già conclusa."
metadata: {"id": "AST-S-CONFRONTO-OPZIONI", "revision": "1.0.0", "applies_to": "ASTRALIS 3.X", "category": "02_decisione_e_pianificazione", "protocols": [1], "intents": ["scegliere_opzioni"], "use_when": ["Confronta almeno due opzioni note per aiutare una scelta motivata e contestabile."], "avoid_when": ["Alternative non ancora definite o scelta dell’utente già conclusa."], "materials": ["Opzioni, obiettivo, criteri e vincoli decisivi."], "prompt_ids": ["AST-P-ANALISI-PROFONDA"], "sources": ["skill-decision-matrix.md"]}
---

# Confronto di opzioni

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Opzioni, obiettivo, criteri e vincoli decisivi.

Non applicare per: Alternative non ancora definite o scelta dell’utente già conclusa.

## Metodo

- Applica prima i vincoli obbligatori: un’opzione incompatibile non viene salvata da un buon punteggio.
- Definisci criteri pertinenti al dominio; distingui pesi forniti dall’utente da pesi proposti.
- Usa punteggi solo se aggiungono chiarezza, con scala, formula e motivazione; le stime non sono misure oggettive.
- Verifica se una piccola variazione dei pesi cambia la scelta. Esponi il confronto in forma lineare accessibile e conserva l’incertezza.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.
