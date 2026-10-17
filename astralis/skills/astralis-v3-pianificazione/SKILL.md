---
name: "astralis-v3-pianificazione"
description: "Traduce un obiettivo o una scelta già presa in piano operativo; per software formalizza contratti, file e verifiche proporzionate. Non usare per: confronto di opzioni aperte, validazione del piano o implementazione."
metadata: {"id": "AST-S-PIANIFICAZIONE", "revision": "1.2.0", "applies_to": "ASTRALIS 3.X", "category": "02_decisione_e_pianificazione", "protocols": [1], "intents": ["pianificare_attivita", "redigere_piano_tecnico"], "use_when": ["Traduce un obiettivo o una scelta già presa in piano operativo; per software formalizza contratti, file e verifiche proporzionate."], "avoid_when": ["Confronto di opzioni ancora aperte, validazione di un piano esistente o richiesta di eseguire codice."], "materials": ["Obiettivo, stato attuale, decisioni già prese e vincoli."], "prompt_ids": ["AST-P-PIANIFICAZIONE"], "sources": ["skill-strategic-planner.md"]}
---

# Pianificazione delle attività

## Ambito Astralis 3.X

Questa skill appartiene al catalogo v3 e non dipende da Astralis 4. Applica il metodo soltanto al compito pertinente. Rispetta le istruzioni attive e il mandato già espresso; la selezione automatica non concede permessi aggiuntivi. Carica conoscenza di progetto e standard Astralis soltanto quando pertinenti e accessibili. Mantieni l’output lineare e navigabile con NVDA, senza tabelle complesse o ASCII art.

## Materiali e confini

Obiettivo, stato attuale, decisioni già prese e vincoli.

Non applicare per: Confronto di opzioni ancora aperte, validazione di un piano esistente o richiesta di eseguire codice.

## Metodo

- Per interventi software identifica confini, proprietari dello stato, contratti e dipendenze dei componenti coinvolti. Alloca nuovi sottosistemi e nuove suite di test in file partizionati per dominio e categoria anziché accodarli per inerzia a file già estesi o monolitici, preservando invece la struttura dei file upstream nei fork su fix locali. Nei fix collega causa dimostrata e invariante alla responsabilità corretta; per nuove funzionalità non inventare una causa. Prevedi impatto su chiamanti, eventi e ciclo di vita, prove in isolamento e integrazione proporzionate.
- Preserva le scelte esplicite; riapri soltanto quelle rese impraticabili da evidenze nuove.
- Definisci risultato atteso, perimetro ed esclusioni rilevanti.
- Ordina le attività per dipendenze, con prerequisiti, artefatti e criteri di completamento osservabili.
- Distingui stime da impegni e segnala rischi e punti di verifica proporzionati. Un piano non concede un mandato nuovo di esecuzione.

## Modalità tecnica proporzionata

Se il piano riguarda software e richiede formalizzazione, applica la tassonomia PIANO-TECNICO e il template v3 se accessibile. Recupera origine, perimetro, radici e precondizioni reali; conserva le invarianti già convalidate. Definisci contratti D/S solo nelle unità che servono, con pre/postcondizioni, componenti previsti e verifica osservabile per contratto.
Considera scenari comuni, alternativi e limite e i sette assi pertinenti, distinguendo simulazione e prova. Usa Testata Universale Compatta quando il documento va salvato nel mandato; stato documento, stato lavoro e gate restano separati. Impatto AVF può essere NON APPLICABILE. Per un compito semplice usa un piano breve, senza inventare strategie o classi.
Indica il confine 1A/1B e le azioni già autorizzate: approvazione del disegno non è automaticamente esecuzione. Non inserire deploy, commit, push o installazioni se non pertinenti e compresi nell'incarico. Collega il report utile alla continuità senza duplicare il piano.

## Collegamento al catalogo

Gli ID nei metadati indicano prompt complementari, non dipendenze da caricare automaticamente. Se serve il testo di un prompt, risolvi il suo percorso in prompts/INDICE_SELEZIONE.json sotto il Master Hub v3 attivo. Questo SKILL.md contiene il metodo operativo e può essere letto anche senza il prompt.

Metodo canonico pertinente, se accessibile: [fonte v3](../../knowledge/03_architettura_e_metodologie/clean_architecture_e_design_pattern.md). Questa skill conserva le istruzioni essenziali anche senza accesso alla fonte.
