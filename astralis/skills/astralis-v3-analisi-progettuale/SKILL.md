---
name: "astralis-v3-analisi-progettuale"
description: "Analizza un’architettura esistente o progetta una soluzione tecnica con confini, dati e contratti. Non usare per: Revisione di una patch, errore riproducibile o confronto di sole opzioni organizzative."
metadata: {"id": "AST-S-ANALISI-PROGETTUALE", "revision": "1.1.0", "applies_to": "ASTRALIS 3.X", "category": "03_ingegneria_software", "protocols": [1, 5], "intents": ["progettare_soluzione_tecnica"], "use_when": ["Analizza un’architettura esistente o progetta una soluzione tecnica con confini, dati e contratti."], "avoid_when": ["Revisione di una patch, errore riproducibile o confronto di sole opzioni organizzative."], "materials": ["Requisiti, architettura o vincoli tecnici disponibili."], "prompt_ids": ["AST-P-ANALISI-INGEGNERISTICA"], "sources": ["skill-design-analyzer.md"]}
---

# Analisi e progettazione tecnica

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Requisiti, architettura o vincoli tecnici disponibili.

Non applicare per: Revisione di una patch, errore riproducibile o confronto di sole opzioni organizzative.

## Metodo

- Individua domini, invarianti e proprietari dello stato; separa dominio, UI e infrastruttura e verifica la direzione delle dipendenze. Definisci contratti di integrazione e prove in isolamento. Coordina risorse condivise nel dominio responsabile, usando orchestratori solo se necessari; per sistemi piccoli preferisci strutture semplici. Motiva impatti e limiti di scalabilità senza promettere impatto zero.
- In modalità analisi ricostruisci i flussi reali; in modalità progetto parti dai requisiti senza inventare componenti già esistenti.
- Valuta responsabilità, dipendenze, contratti, gestione dello stato e failure mode pertinenti.
- Separa difetti dimostrati, rischi e preferenze di stile. Collega le osservazioni a componenti o requisiti.
- Proponi la soluzione più semplice che soddisfa modularità, accessibilità e vincoli; mostra impatto e verifiche senza riscrivere il sistema per principio.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.

Metodo canonico pertinente, se accessibile: [fonte v3](../../knowledge/03_architettura_e_metodologie/clean_architecture_e_design_pattern.md). Questa skill conserva le istruzioni essenziali anche senza accesso alla fonte.
