---
name: "astralis-v3-testing-e-collaudo"
description: "Progetta, realizza o esegue test e collaudi di software generico secondo modalità e mandato, con prove tracciabili. Non usare per: Sola code review, giudizio su una strategia o collaudo delle meccaniche gameplay senza verifiche software generali."
metadata: {"id": "AST-S-TESTING-E-COLLAUDO", "revision": "1.1.0", "applies_to": "ASTRALIS 3.X", "category": "04_validazione_ed_esecuzione", "protocols": [2, 3, 4], "intents": ["progettare_test", "realizzare_test", "eseguire_test", "collaudare_software"], "use_when": ["Progetta, realizza o esegue test e collaudi di software generico secondo modalità e mandato, con prove tracciabili."], "avoid_when": ["Sola code review, giudizio su una strategia o collaudo delle meccaniche gameplay senza verifiche software generali."], "materials": ["Requisiti o contratti, codice se disponibile, ambiente, strumenti e mandato; dichiarare materiali mancanti."], "prompt_ids": ["AST-P-TESTING-COLLAUDO"], "sources": []}
---

# Progettazione ed esecuzione di test e collaudo

## Ambito e materiali

Metodo del catalogo Astralis 3.X. Requisiti o contratti, codice se disponibile, ambiente, strumenti e mandato; dichiarare materiali mancanti.
Rispetta il mandato già espresso, le istruzioni attive e l’accessibilità NVDA; la selezione non concede nuovi permessi. Questo metodo non dipende da Astralis 4.

## Metodo

- Per correzioni scegli prove che riproducano il difetto e distinguano la causa, poi controlla esito corretto e percorsi correlati: chiamanti, guardie, priorità o ciclo di vita solo quando interessati. Per moduli nuovi verifica il contratto in isolamento e l’integrazione al confine, con attesi indipendenti. Evita strutture di test sproporzionate al rischio.
- Identifica la modalità richiesta: progettazione, realizzazione o esecuzione. Una richiesta di piano di test non autorizza a scrivere test; realizzare test non autorizza correzioni al prodotto o deploy.
- Risolvi radici codice/documentazione/runtime, istruzioni e ambiente. Collega ciascun requisito o contratto a proprietà osservabili e scegli statico, unitario, integrazione, end-to-end o prova utente in base al rischio.
- Definisci attesi indipendenti dall’implementazione, fixture, isolamento e casi comuni, alternativi e limite. Partiziona i nuovi test in file dedicati per dominio e categoria con fixture condivise separate, evitando di accodare per inerzia nuove suite a file monolitici o contenitori generici. Evita test che copiano il codice o verificano soltanto il nome di una funzione.
- Nei test temporali usa la stessa sorgente di tempo controllata per creazione, avanzamento e scadenza quando possibile. Non promettere runtime a zero millisecondi per test di integrazione o in-game.
- Scrivi o esegui solo ciò che il mandato e gli strumenti consentono. Usa comandi effettivi dello stack; non installare dipendenze o cambiare ambiente implicitamente. Prima di test con effetti esterni definisci isolamento e risorse interessate.
- Conserva comando, contesto, baseline e artefatto quando pertinente, esito e prove mancanti. Distingui fallimento del prodotto, del test e dell’ambiente; non alterare gli attesi per ottenere PASS.
- Riporta verificato, fallito o non verificabile per proprietà. Test automatici, build, deploy e collaudo runtime/NVDA sono evidenze diverse; senza runtime prepara istruzioni e dichiara la prova non eseguita.
- Durante lavoro sostanziale autorizzato mantieni il report pertinente quando serve continuità. Per gameplay usa anche il metodo specializzato soltanto se necessario alla richiesta; non avviare una catena automatica.

## Raccordo

Il prompt nei metadati è una forma esplicita di incarico, non una dipendenza obbligatoria. Se il Master Hub v3 è accessibile consulta la mappa ciclo_sviluppo_e_selezione_strumenti_astralis.md e la tassonomia nella knowledge di architettura per i dettagli pertinenti. Questo SKILL.md contiene il metodo essenziale; non fingere strumenti o letture non disponibili.

Metodo canonico pertinente, se accessibile: [fonte v3](../../knowledge/03_architettura_e_metodologie/strategie_testing_e_debug.md). Questa skill conserva le istruzioni essenziali anche senza accesso alla fonte.
