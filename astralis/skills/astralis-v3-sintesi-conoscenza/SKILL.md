---
name: "astralis-v3-sintesi-conoscenza"
description: "Sintetizza testi lunghi, tecnici o narrativi, conservandone struttura e punti essenziali. Non usare per: Estrazione letterale di campi, giudizio critico su un progetto o diagnosi di un errore."
metadata: {"id": "AST-S-SINTESI-CONOSCENZA", "revision": "1.0.0", "applies_to": "ASTRALIS 3.X", "category": "01_analisi_e_conoscenza", "protocols": [7], "intents": ["sintetizzare_documento"], "use_when": ["Sintetizza testi lunghi, tecnici o narrativi, conservandone struttura e punti essenziali."], "avoid_when": ["Estrazione letterale di campi, giudizio critico su un progetto o diagnosi di un errore."], "materials": ["Testo o documenti leggibili e scopo della sintesi."], "prompt_ids": [], "sources": ["skill-knowledge-extractor.md"]}
---

# Sintesi della conoscenza

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Testo o documenti leggibili e scopo della sintesi.

Non applicare per: Estrazione letterale di campi, giudizio critico su un progetto o diagnosi di un errore.

## Metodo

- Dichiara quali documenti o porzioni hai effettivamente letto, soprattutto in caso di troncamento.
- Separa temi tecnici, narrativi e misti soltanto quando aiuta a capire il contenuto.
- Rendi rintracciabili i punti essenziali con sezioni o riferimenti alla fonte; preserva voce e intenzioni autoriali.
- Distingui ciò che dice il documento dalle tue osservazioni. Estrarre conoscenza non autorizza a salvarla nella knowledge o a riscrivere la fonte.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.
