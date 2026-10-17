---
name: "astralis-v3-ideazione"
description: "Chiarisce un’idea embrionale o un bisogno ancora incompleto prima di scegliere una soluzione. Non usare per: Requisito già chiaro, strategia già elaborata, piano esecutivo o implementazione."
metadata: {"id": "AST-S-IDEAZIONE", "revision": "1.0.0", "applies_to": "ASTRALIS 3.X", "category": "02_decisione_e_pianificazione", "protocols": [1], "intents": ["chiarire_idea"], "use_when": ["Chiarisce un’idea embrionale o un bisogno ancora incompleto prima di scegliere una soluzione."], "avoid_when": ["Requisito già chiaro, strategia già elaborata, piano esecutivo o implementazione."], "materials": ["Intuizione o bisogno, destinatari e contesto disponibile; lacune ammesse."], "prompt_ids": ["AST-P-IDEA-RFC"], "sources": []}
---

# Ideazione e chiarimento del bisogno

## Ambito e materiali

Metodo del catalogo Astralis 3.X. Intuizione o bisogno, destinatari e contesto disponibile; lacune ammesse.
Rispetta il mandato già espresso, le istruzioni attive e l’accessibilità NVDA; la selezione non concede nuovi permessi. Questo metodo non dipende da Astralis 4.

## Metodo

- Parti dalla situazione osservabile, da chi incontra il problema e dal beneficio riconoscibile; non confondere la prima soluzione suggerita con il bisogno.
- Separa fatti, assunzioni e domande aperte. Recupera il contesto disponibile e chiedi soltanto ciò che cambia la decisione.
- Considera alternative plausibili, riuso e non intervenire quando utile; non imporre un numero di idee.
- Produci problema/opportunità, beneficio, ipotesi, vincoli e decisione richiesta. Se serve persistenza nel mandato usa IDEA_RFC_TEMPLATE.md e docs/idee nella radice documentale risolta.
- Distingui esito IN ATTESA, ACCOLTA, RESPINTA o RINVIATA con motivazione reale. Un’idea accolta non autorizza strategia, piano o codice fuori dall’incarico. Per un requisito già chiaro passa al metodo pertinente senza retrocederlo.

## Raccordo

Il prompt nei metadati è una forma esplicita di incarico, non una dipendenza obbligatoria. Se il Master Hub v3 è accessibile consulta la mappa ciclo_sviluppo_e_selezione_strumenti_astralis.md e la tassonomia nella knowledge di architettura per i dettagli pertinenti. Questo SKILL.md contiene il metodo essenziale; non fingere strumenti o letture non disponibili.
