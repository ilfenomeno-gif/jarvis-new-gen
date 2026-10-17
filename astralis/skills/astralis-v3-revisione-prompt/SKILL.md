---
name: "astralis-v3-revisione-prompt"
description: "Migliora un prompt esistente preservando intento, vincoli e destinatario. Non usare per: Prompt da creare senza una bozza o normale richiesta che non chiede di migliorare il prompt."
metadata: {"id": "AST-S-REVISIONE-PROMPT", "revision": "1.0.0", "applies_to": "ASTRALIS 3.X", "category": "05_prompt_e_documentazione", "protocols": [7], "intents": ["migliorare_prompt"], "use_when": ["Migliora un prompt esistente preservando intento, vincoli e destinatario."], "avoid_when": ["Prompt da creare senza una bozza o normale richiesta che non chiede di migliorare il prompt."], "materials": ["Prompt originale, scopo e problemi da correggere se noti."], "prompt_ids": ["AST-P-REVISIONE-PROMPT"], "sources": ["skill-ottimizza-prompt.md"]}
---

# Revisione di prompt

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Prompt originale, scopo e problemi da correggere se noti.

Non applicare per: Prompt da creare senza una bozza o normale richiesta che non chiede di migliorare il prompt.

## Metodo

- Identifica ambiguità, contraddizioni, materiali mancanti e vincoli che cambiano il risultato.
- Preserva i vincoli espliciti e distingui chiarimenti da nuove assunzioni.
- Riscrivi quanto necessario, senza imporre tono sarcastico, hack, cicli di perfezionamento o stack SPARK.
- Mostra il prompt migliorato e le modifiche significative. La revisione non comporta l’esecuzione automatica del prompt; eseguilo solo se richiesto.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.
