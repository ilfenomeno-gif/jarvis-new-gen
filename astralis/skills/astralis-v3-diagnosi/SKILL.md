---
name: "astralis-v3-diagnosi"
description: "Diagnostica errori, stack trace, regressioni e sessioni osservate tramite log o telemetrie. Non usare per: Revisione generale del codice o giudizio su una proposta senza un problema osservato."
metadata: {"id": "AST-S-DIAGNOSI", "revision": "1.1.0", "applies_to": "ASTRALIS 3.X", "category": "03_ingegneria_software", "protocols": [4, 10], "intents": ["diagnosticare_sessione"], "use_when": ["Diagnostica errori, stack trace, regressioni e sessioni osservate tramite log o telemetrie."], "avoid_when": ["Revisione generale del codice o giudizio su una proposta senza un problema osservato."], "materials": ["Sintomo, atteso contro osservato, ambiente e log o riproduzione disponibili."], "prompt_ids": ["AST-P-DIAGNOSI-TELEMETRIE"], "sources": ["skill-debug-assistant.md"]}
---

# Diagnosi di errori e telemetrie

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Sintomo, atteso contro osservato, ambiente e log o riproduzione disponibili.

Non applicare per: Revisione generale del codice o giudizio su una proposta senza un problema osservato.

## Metodo

- Traccia ingresso, dispatcher, gestori ed esito; collega la causa dimostrata al proprietario dell’invariante violata. Verifica filtri, ordine, priorità e ciclo di vita pertinenti. Se la causa manca, mantieni ipotesi e prove separate. Un fix autorizzato elimina la causa nel componente responsabile, anche nel gestore finale; evita timeout arbitrari e bypass, senza escludere adattatori richiesti da confini reali.
- Ricostruisci la sequenza temporale e distingui eventi osservati da interpretazioni; proteggi dati sensibili nei log.
- Formula ipotesi falsificabili e scegli la prova minima che le distingue, senza numeri obbligatori di ipotesi o confidenze arbitrarie.
- Una firma nota è un indizio: errori SQLite o MCP non dimostrano da soli una causa specifica.
- Se il mandato comprende la correzione, applica il cambiamento circoscritto e verifica la riproduzione. Riavvii, svuotamento cache e operazioni remote richiedono il contesto e l’autorizzazione già previsti dal compito.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.

Metodo canonico pertinente, se accessibile: [fonte v3](../../knowledge/03_architettura_e_metodologie/strategie_testing_e_debug.md). Questa skill conserva le istruzioni essenziali anche senza accesso alla fonte.
