---
name: "astralis-v3-refactoring"
description: "Pianifica o applica refactoring a codice funzionante preservando il comportamento pubblico. Non usare per: Correzione di un bug ancora non diagnosticato o riscrittura integrale non richiesta."
metadata: {"id": "AST-S-REFACTORING", "revision": "1.1.0", "applies_to": "ASTRALIS 3.X", "category": "03_ingegneria_software", "protocols": [5, 11], "intents": ["rifattorizzare_codice"], "use_when": ["Pianifica o applica refactoring a codice funzionante preservando il comportamento pubblico."], "avoid_when": ["Correzione di un bug ancora non diagnosticato o riscrittura integrale non richiesta."], "materials": ["Codice, comportamento da preservare e obiettivo del refactoring."], "prompt_ids": [], "sources": ["skill-refactor-guide.md"]}
---

# Refactoring mirato

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Codice, comportamento da preservare e obiettivo del refactoring.

Non applicare per: Correzione di un bug ancora non diagnosticato o riscrittura integrale non richiesta.

## Metodo

- Rendi espliciti confini di dominio, proprietà dello stato e direzione delle dipendenze prima di spostare responsabilità. Conserva contratti pubblici e comportamento, verificando isolamento e integrazione pertinenti. Una causa di bug non dimostrata richiede diagnosi; non nascondere cambi funzionali dentro un riordino.
- Rendi esplicita l’invariante da conservare: contratto pubblico, output, stato o prestazioni richieste.
- Seleziona il cambiamento minimo che risolve il problema di manutenzione dimostrato.
- Distingui piano e applicazione secondo il mandato; non far crescere un riordino locale in una migrazione architetturale.
- Verifica l’invariante con test o confronto appropriato. Preserva convenzioni, commenti utili e modifiche dell’utente non correlate.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.

Metodo canonico pertinente, se accessibile: [fonte v3](../../knowledge/03_architettura_e_metodologie/strategie_testing_e_debug.md). Questa skill conserva le istruzioni essenziali anche senza accesso alla fonte.
