---
name: "astralis-v3-revisione-codice"
description: "Rivede codice o diff e segnala difetti, regressioni e rischi concreti con riferimenti. Non usare per: Puro refactoring estetico, validazione di una strategia o diagnosi senza codice disponibile."
metadata: {"id": "AST-S-REVISIONE-CODICE", "revision": "1.1.0", "applies_to": "ASTRALIS 3.X", "category": "03_ingegneria_software", "protocols": [5], "intents": ["revisionare_codice"], "use_when": ["Rivede codice o diff e segnala difetti, regressioni e rischi concreti con riferimenti."], "avoid_when": ["Puro refactoring estetico, validazione di una strategia o diagnosi senza codice disponibile."], "materials": ["Codice o diff, comportamento atteso e contesto necessario."], "prompt_ids": ["AST-P-REVIEW-CODICE"], "sources": ["skill-code-reviewer.md"]}
---

# Revisione del codice

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Codice o diff, comportamento atteso e contesto necessario.

Non applicare per: Puro refactoring estetico, validazione di una strategia o diagnosi senza codice disponibile.

## Metodo

- Ricostruisci la catena causale del rilievo e raggruppa sintomi con una causa condivisa; indica proprietario e invariante violata. Suggerisci una correzione nel punto responsabile e controlli sui chiamanti interessati. La preferenza per modularità non prova un difetto; una review non autorizza fix o migrazioni.
- Leggi il contesto e i chiamanti necessari a verificare le osservazioni, senza presumere bug da uno stile diverso.
- Per ogni rilievo concreto indica posizione, condizione che lo attiva, conseguenza e correzione suggerita.
- Valuta severità rispetto all’impatto reale; separa difetti da suggerimenti facoltativi.
- Dichiara le aree non verificate e i test effettivamente eseguiti. Se non trovi problemi, dillo senza inventare rilievi; applica correzioni soltanto se incluse nel mandato.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.

Metodo canonico pertinente, se accessibile: [fonte v3](../../knowledge/03_architettura_e_metodologie/strategie_testing_e_debug.md). Questa skill conserva le istruzioni essenziali anche senza accesso alla fonte.
