---
name: "astralis-v3-implementazione-controllata"
description: "Esegue modifiche circoscritte richieste dall’utente, sulla base di un piano o di requisiti operativi chiari. Non usare per: Richiesta di soli consigli, revisione o validazione senza mandato di modifica."
metadata: {"id": "AST-S-IMPLEMENTAZIONE-CONTROLLATA", "revision": "1.1.0", "applies_to": "ASTRALIS 3.X", "category": "04_validazione_ed_esecuzione", "protocols": [3], "intents": ["implementare_piano"], "use_when": ["Esegue modifiche circoscritte richieste dall’utente, sulla base di un piano o di requisiti operativi chiari."], "avoid_when": ["Richiesta di soli consigli, revisione o validazione senza mandato di modifica."], "materials": ["Mandato di modifica, requisiti o piano, workspace e strumenti disponibili."], "prompt_ids": ["AST-P-IMPLEMENTAZIONE"], "sources": []}
---

# Implementazione controllata

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Mandato di modifica, requisiti o piano, workspace e strumenti disponibili.

Non applicare per: Richiesta di soli consigli, revisione o validazione senza mandato di modifica.

## Metodo

- Nei fix usa causa e invariante dimostrate per intervenire nel componente responsabile con il cambiamento più contenuto che elimina stabilmente il problema. Preserva contratti e proprietà dello stato; verifica chiamanti, eventi e ciclo di vita interessati. Evita duplicazioni di stato, ritardi arbitrari e bypass dei sintomi; non estendere un difetto locale a una migrazione non autorizzata.
- Leggi istruzioni locali, stato del workspace e componenti interessati; conserva modifiche preesistenti dell’utente.
- Usa il mandato già espresso: non richiedere una seconda conferma per azioni già autorizzate.
- Applica incrementi coerenti con il perimetro e verifica le proprietà che potrebbero regredire.
- Se emerge un cambiamento sostanziale di obiettivo o un blocco reale, esplicitalo. Non includere pubblicazione, messaggi, deleghe o installazioni globali non richieste.
- Concludi con risultato, verifiche eseguite e limiti; non dichiarare completato ciò che manca.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.

Metodo canonico pertinente, se accessibile: [fonte v3](../../knowledge/03_architettura_e_metodologie/strategie_testing_e_debug.md). Questa skill conserva le istruzioni essenziali anche senza accesso alla fonte.
