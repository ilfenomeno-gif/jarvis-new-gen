---
name: "astralis-v3-selezione-prompt"
description: "Consiglia quale prompt del catalogo Astralis 3.X usare in un contesto, anche con una domanda breve. Non usare per: Richiesta di eseguire direttamente un compito senza chiedere quale prompt scegliere."
metadata: {"id": "AST-S-SELEZIONE-PROMPT", "revision": "1.0.0", "applies_to": "ASTRALIS 3.X", "category": "05_prompt_e_documentazione", "protocols": [7], "intents": ["consigliare_prompt"], "use_when": ["Consiglia quale prompt del catalogo Astralis 3.X usare in un contesto, anche con una domanda breve."], "avoid_when": ["Richiesta di eseguire direttamente un compito senza chiedere quale prompt scegliere."], "materials": ["Contesto dell’utente e accesso al catalogo del Master Hub Astralis 3.X."], "prompt_ids": [], "sources": []}
---

# Selezione di prompt Astralis

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Contesto dell’utente e accesso al catalogo del Master Hub Astralis 3.X.

Non applicare per: Richiesta di eseguire direttamente un compito senza chiedere quale prompt scegliere.

## Metodo

- Risolvi il Master Hub 3.X dalle istruzioni attive, senza cercare nel Lab 4 o supporre un percorso installato.
- Consulta prompts/INDICE_SELEZIONE.json e la procedura knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md; poi leggi la scheda canonica del candidato.
- Usa obiettivo, fase, materiali, dominio e strumenti; distingui strategia, piano, implementazione e diagnosi.
- Restituisci titolo, ID, link, motivo, materiali, esempio di attivazione e limite. Se manca un dato decisivo chiedi quel dato; se non esiste un candidato adatto dillo.
- Se hub o indice non sono accessibili, dichiara il limite senza inventare titoli. La raccomandazione non attiva il prompt.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.
