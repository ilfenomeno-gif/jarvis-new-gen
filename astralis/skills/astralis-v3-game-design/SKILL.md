---
name: "astralis-v3-game-design"
description: "Progetta o rivede sistemi di gioco: ciclo principale, meccaniche, progressione e accessibilità. Non usare per: Collaudo di gameplay già implementato o progetto software senza meccaniche ludiche."
metadata: {"id": "AST-S-GAME-DESIGN", "revision": "1.0.0", "applies_to": "ASTRALIS 3.X", "category": "06_game_design_e_collaudo", "protocols": [1, 2], "intents": ["progettare_gioco"], "use_when": ["Progetta o rivede sistemi di gioco: ciclo principale, meccaniche, progressione e accessibilità."], "avoid_when": ["Collaudo di gameplay già implementato o progetto software senza meccaniche ludiche."], "materials": ["Idea o progetto, pubblico, piattaforma, vincoli e meccaniche esistenti."], "prompt_ids": ["AST-P-GAME-DESIGN"], "sources": ["skill-game-design-engine.md"]}
---

# Progettazione di giochi

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Idea o progetto, pubblico, piattaforma, vincoli e meccaniche esistenti.

Non applicare per: Collaudo di gameplay già implementato o progetto software senza meccaniche ludiche.

## Metodo

- Parti dall’esperienza desiderata e ricostruisci il ciclo azione, feedback, scelta e progressione.
- Verifica coerenza tra meccaniche, economia, difficoltà e pubblico, distinguendo analisi di un gioco esistente da proposta nuova.
- Integra tastiera, feedback non visivo e leggibilità delle informazioni quando pertinenti; non presumere Evennia, MUD o ECS.
- Proponi esperimenti di prototipo con esiti osservabili; non inventare prove di giocatori e non delegare automaticamente la realizzazione.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.
