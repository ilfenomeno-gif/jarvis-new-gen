---
name: "astralis-v3-validazione-piano"
description: "Verifica un piano esistente prima dell’esecuzione: dipendenze, fattibilità, copertura e verifiche. Non usare per: Creazione di un piano da zero o collaudo di un’implementazione già realizzata."
metadata: {"id": "AST-S-VALIDAZIONE-PIANO", "revision": "1.0.0", "applies_to": "ASTRALIS 3.X", "category": "04_validazione_ed_esecuzione", "protocols": [2, 12], "intents": ["validare_piano"], "use_when": ["Verifica un piano esistente prima dell’esecuzione: dipendenze, fattibilità, copertura e verifiche."], "avoid_when": ["Creazione di un piano da zero o collaudo di un’implementazione già realizzata."], "materials": ["Piano, obiettivo, contesto operativo e vincoli."], "prompt_ids": ["AST-P-VALIDAZIONE-PIANO"], "sources": []}
---

# Validazione del piano

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Piano, obiettivo, contesto operativo e vincoli.

Non applicare per: Creazione di un piano da zero o collaudo di un’implementazione già realizzata.

## Metodo

- Controlla copertura dei requisiti, ordine delle dipendenze e prerequisiti mancanti.
- Cerca passi non verificabili, stime non fondate e effetti che eccedono il mandato.
- Valuta rollback o ripristino dove la natura della modifica lo richiede.
- Indica le correzioni necessarie e cosa resta ignoto. L’esito riguarda il piano, non il comportamento di codice inesistente.
- Applica la matrice Astralis: validità, efficacia, coerenza, completezza, precisione per NVDA, affidabilità/prestazioni e assenza di regressioni; considera uso comune, percorsi alternativi e casi limite. Distingui simulazione e prova eseguita, dichiarando gli assi non verificabili o non applicabili.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.
