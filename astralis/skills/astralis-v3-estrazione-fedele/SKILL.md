---
name: "astralis-v3-estrazione-fedele"
description: "Estrae campi, fatti o citazioni da documenti mantenendo la provenienza e senza completare le lacune. Non usare per: Riassunto libero, generazione creativa o dati da inferire anziché estrarre."
metadata: {"id": "AST-S-ESTRAZIONE-FEDELE", "revision": "1.0.0", "applies_to": "ASTRALIS 3.X", "category": "01_analisi_e_conoscenza", "protocols": [7], "intents": ["estrarre_dati"], "use_when": ["Estrae campi, fatti o citazioni da documenti mantenendo la provenienza e senza completare le lacune."], "avoid_when": ["Riassunto libero, generazione creativa o dati da inferire anziché estrarre."], "materials": ["Fonti leggibili e campi o informazioni richiesti."], "prompt_ids": ["AST-P-ESTRAZIONE-DOCUMENTALE"], "sources": []}
---

# Estrazione documentale fedele

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Fonti leggibili e campi o informazioni richiesti.

Non applicare per: Riassunto libero, generazione creativa o dati da inferire anziché estrarre.

## Metodo

- Identifica fonti, versione e copertura effettivamente disponibile.
- Per ogni elemento richiesto, conserva valore, riferimento e stato: presente, assente, ambiguo o contraddittorio.
- Separa trascrizione fedele, normalizzazione richiesta e inferenza; non presentare inferenze come dati estratti.
- Segnala le lacune senza riempirle e conserva unità, date e qualificatori che cambiano il significato.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.
