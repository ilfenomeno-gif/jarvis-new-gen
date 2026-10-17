---
name: "astralis-v3-progettazione-api"
description: "Progetta o rivede contratti API, endpoint, comandi CLI o strumenti MCP. Non usare per: Revisione generica di codice senza contratti da definire o implementazione non richiesta."
metadata: {"id": "AST-S-PROGETTAZIONE-API", "revision": "1.1.0", "applies_to": "ASTRALIS 3.X", "category": "03_ingegneria_software", "protocols": [1, 5], "intents": ["progettare_api"], "use_when": ["Progetta o rivede contratti API, endpoint, comandi CLI o strumenti MCP."], "avoid_when": ["Revisione generica di codice senza contratti da definire o implementazione non richiesta."], "materials": ["Consumatori, operazioni, stack e vincoli del contratto."], "prompt_ids": ["AST-P-ANALISI-INGEGNERISTICA"], "sources": ["skill-api-designer.md"]}
---

# Progettazione API e contratti

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Consumatori, operazioni, stack e vincoli del contratto.

Non applicare per: Revisione generica di codice senza contratti da definire o implementazione non richiesta.

## Metodo

- Assegna il contratto al dominio responsabile; esplicita proprietà dello stato, ciclo di vita e compatibilità tra chiamanti. Separa politiche di dominio dagli adattatori e orienta le dipendenze verso i contratti. Verifica sostituibilità e integrazione senza esporre stato interno o imporre un coordinatore globale.
- Definisci input, output, errori, compatibilità e semantica delle operazioni, compresa l’idempotenza quando pertinente.
- Distingui il contratto pubblico dall’implementazione e specifica esempi validi e casi di errore.
- Per MCP verifica trasporto e SDK effettivi: il logging su stderr è pertinente al canale stdio, non una regola universale per ogni API.
- Non imporre prefissi scf_, FastMCP, ManifestManager o stack SPARK senza una richiesta del progetto. Non delegare l’implementazione ad altri agenti per default.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.

Metodo canonico pertinente, se accessibile: [fonte v3](../../knowledge/03_architettura_e_metodologie/clean_architecture_e_design_pattern.md). Questa skill conserva le istruzioni essenziali anche senza accesso alla fonte.
