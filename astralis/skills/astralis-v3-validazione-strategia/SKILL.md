---
name: "astralis-v3-validazione-strategia"
description: "Valuta se una strategia proposta è coerente con obiettivo, assunzioni e vincoli prima del piano. Non usare per: Definizione di una strategia nuova, validazione del piano dettagliato o verifica del codice realizzato."
metadata: {"id": "AST-S-VALIDAZIONE-STRATEGIA", "revision": "1.0.0", "applies_to": "ASTRALIS 3.X", "category": "04_validazione_ed_esecuzione", "protocols": [2], "intents": ["validare_strategia"], "use_when": ["Valuta se una strategia proposta è coerente con obiettivo, assunzioni e vincoli prima del piano."], "avoid_when": ["Definizione di una strategia nuova, validazione del piano dettagliato o verifica del codice realizzato."], "materials": ["Strategia proposta, obiettivo, criteri di successo e vincoli."], "prompt_ids": ["AST-P-VALIDAZIONE-STRATEGIA"], "sources": []}
---

# Validazione della strategia

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Strategia proposta, obiettivo, criteri di successo e vincoli.

Non applicare per: Definizione di una strategia nuova, validazione del piano dettagliato o verifica del codice realizzato.

## Metodo

- Controlla la relazione tra problema, scelta strategica ed effetti attesi.
- Metti alla prova le assunzioni decisive con controesempi o evidenze disponibili.
- Distingui criticità bloccanti, condizioni da verificare e miglioramenti facoltativi.
- Restituisci un giudizio motivato e le condizioni per procedere, senza promettere risultati non verificati o autorizzare l’esecuzione.
- Applica la matrice Astralis: validità, efficacia, coerenza, completezza, precisione per NVDA, affidabilità/prestazioni e assenza di regressioni; considera uso comune, percorsi alternativi e casi limite. Distingui simulazione e prova eseguita, dichiarando gli assi non verificabili o non applicabili.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.
