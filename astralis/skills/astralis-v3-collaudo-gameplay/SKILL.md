---
name: "astralis-v3-collaudo-gameplay"
description: "Collauda gameplay disponibile con scenari osservabili, inclusi tastiera e feedback accessibile. Non usare per: Progettazione di un gioco ancora soltanto concettuale o simulazioni descritte come prove eseguite."
metadata: {"id": "AST-S-COLLAUDO-GAMEPLAY", "revision": "1.0.0", "applies_to": "ASTRALIS 3.X", "category": "06_game_design_e_collaudo", "protocols": [2, 4], "intents": ["collaudare_gioco"], "use_when": ["Collauda gameplay disponibile con scenari osservabili, inclusi tastiera e feedback accessibile."], "avoid_when": ["Progettazione di un gioco ancora soltanto concettuale o simulazioni descritte come prove eseguite."], "materials": ["Build o prototipo, controlli, obiettivi di prova e strumenti disponibili."], "prompt_ids": ["AST-P-COLLAUDO-GAMEPLAY"], "sources": []}
---

# Collaudo del gameplay

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Build o prototipo, controlli, obiettivi di prova e strumenti disponibili.

Non applicare per: Progettazione di un gioco ancora soltanto concettuale o simulazioni descritte come prove eseguite.

## Metodo

- Identifica scenari realistici, criteri di successo e ambiente di prova riproducibile.
- Esegui soltanto controlli compatibili con gli strumenti disponibili; senza accesso al runtime prepara un piano e dichiaralo.
- Registra atteso, osservato, passi di riproduzione e impatto; considera focus, tastiera e feedback audio quando applicabili.
- Separa test automatici, sessioni reali e valutazioni euristiche. Non dichiarare usabilità NVDA o bilanciamento confermati da una semplice lettura del codice.
- Applica la matrice Astralis: validità, efficacia, coerenza, completezza, precisione per NVDA, affidabilità/prestazioni e assenza di regressioni; considera uso comune, percorsi alternativi e casi limite. Distingui simulazione e prova eseguita, dichiarando gli assi non verificabili o non applicabili.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.
