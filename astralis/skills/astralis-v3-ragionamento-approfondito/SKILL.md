---
name: "astralis-v3-ragionamento-approfondito"
description: "Analizza una questione concettuale complessa con assunzioni o conseguenze incerte. Non usare per: Una risposta semplice, una scelta tra opzioni già definite o un errore concreto da diagnosticare."
metadata: {"id": "AST-S-RAGIONAMENTO-APPROFONDITO", "revision": "1.0.0", "applies_to": "ASTRALIS 3.X", "category": "01_analisi_e_conoscenza", "protocols": [12], "intents": ["analizzare_decisione"], "use_when": ["Analizza una questione concettuale complessa con assunzioni o conseguenze incerte."], "avoid_when": ["Una risposta semplice, una scelta tra opzioni già definite o un errore concreto da diagnosticare."], "materials": ["Questione, contesto e vincoli noti."], "prompt_ids": ["AST-P-ANALISI-PROFONDA"], "sources": ["skill-deep-reasoner.md"]}
---

# Ragionamento approfondito

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Questione, contesto e vincoli noti.

Non applicare per: Una risposta semplice, una scelta tra opzioni già definite o un errore concreto da diagnosticare.

## Metodo

- Isola la domanda decisiva e le assunzioni che possono cambiare la risposta.
- Distingui evidenze, inferenze e dati mancanti; considera controesempi pertinenti.
- Confronta le interpretazioni plausibili senza imporre quantità di alternative o punteggi.
- Concludi con una spiegazione verificabile, l’incertezza residua e il dato che la ridurrebbe; non esporre il ragionamento interno privato.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.
