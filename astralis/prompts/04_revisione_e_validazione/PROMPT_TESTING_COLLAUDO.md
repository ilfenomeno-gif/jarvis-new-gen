---
schema: 2
id: "AST-P-TESTING-COLLAUDO"
title: "Progettazione ed esecuzione di test e collaudo"
revision: "1.0.0"
status: "nuovo_verificato_documentalmente"
category: "04_revisione_e_validazione"
protocols: [2, 3, 4]
domains: ["trasversale"]
mode: "dipende_dal_mandato"
requires: ["lettura_materiali", "strumenti_pertinenti_se_autorizzati"]
sources: []
selection: {"intents": ["progettare_test", "realizzare_test", "eseguire_test", "collaudare_software"], "use_when": ["Progetta, realizza o esegue test e collaudi di software generico secondo modalità e mandato, con prove tracciabili."], "avoid_when": ["Sola code review, giudizio su una strategia o collaudo delle meccaniche gameplay senza verifiche software generali."], "materials": ["Requisiti o contratti, codice se disponibile, ambiente, strumenti e mandato; dichiarare materiali mancanti."], "examples": ["Progetta ed esegui nel workspace di prova i test di regressione per questi contratti."], "related": [{"id": "AST-P-VALIDAZIONE-IMPLEMENTAZIONE", "when": "Per valutare il risultato complessivo rispetto ai requisiti, oltre alle singole prove."}, {"id": "AST-P-COLLAUDO-GAMEPLAY", "when": "Solo per la specializzazione sulle meccaniche di gioco."}]}
---

# Progettazione ed esecuzione di test e collaudo

## Scopo e condizioni d'uso

Progetta, realizza o esegue test e collaudi di software generico secondo modalità e mandato, con prove tracciabili.
Identificativo: `AST-P-TESTING-COLLAUDO`. Revisione 1.0.0; non è una versione del framework. Collaudo d'uso dei client aperto.
Consulta lo [standard](../STANDARD_PROMPT_ASTRALIS.md) e la [procedura di selezione v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md).

## Scheda operativa

- Protocolli: 2, 3, 4.
- Ambito: trasversale, specializzato sul contesto effettivo.
- Modalità: dipende_dal_mandato; non concede permessi.
- Materiali: Requisiti o contratti, codice se disponibile, ambiente, strumenti e mandato; dichiarare materiali mancanti.
- Provenienza: capacità nuova derivata dalle esigenze e dalla tassonomia v3; nessuna sorgente storica attribuita.

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Progetta, realizza o esegue test e collaudi di software generico secondo modalità e mandato, con prove tracciabili.
- Evitalo quando: Sola code review, giudizio su una strategia o collaudo delle meccaniche gameplay senza verifiche software generali.
- Materiali: Requisiti o contratti, codice se disponibile, ambiente, strumenti e mandato; dichiarare materiali mancanti.
- Esempio: Progetta ed esegui nel workspace di prova i test di regressione per questi contratti.
- Passo collegato: `AST-P-VALIDAZIONE-IMPLEMENTAZIONE` — Per valutare il risultato complessivo rispetto ai requisiti, oltre alle singole prove.
- Passo collegato: `AST-P-COLLAUDO-GAMEPLAY` — Solo per la specializzazione sulle meccaniche di gioco.

## Testo da copiare

```text
ASTRALIS — Progettazione ed esecuzione di test e collaudo — AST-P-TESTING-COLLAUDO

CONTESTO E VINCOLI ESSENZIALI
Rispetta istruzioni attive, mandato già dato e conoscenza pertinente accessibile. Questo prompt non conferisce permessi.
Separa fatti, ipotesi, simulazioni e prove. Usa italiano lineare e navigabile con NVDA; non esporre ragionamento interno privato.

OBIETTIVO
Progetta, realizza o esegue test e collaudi di software generico secondo modalità e mandato, con prove tracciabili.

INPUT
Richiesta e obiettivo: [RICHIESTA]. Materiali: [FONTI]. Contesto e vincoli: [CONTESTO]. Modalità e mandato: [PROGETTAZIONE / REALIZZAZIONE / ESECUZIONE, SE PERTINENTI].

PERIMETRO OPERATIVO
Svolgi soltanto il compito richiesto. Persistenza utile e modifiche seguono il mandato già disponibile; niente implementazione, invio, delega, deploy o pubblicazione impliciti. Non chiedere una nuova conferma per azioni già autorizzate.

PROCEDURA
1. Identifica la modalità richiesta: progettazione, realizzazione o esecuzione. Una richiesta di piano di test non autorizza a scrivere test; realizzare test non autorizza correzioni al prodotto o deploy.
2. Risolvi radici codice/documentazione/runtime, istruzioni e ambiente. Collega ciascun requisito o contratto a proprietà osservabili e scegli statico, unitario, integrazione, end-to-end o prova utente in base al rischio.
3. Definisci attesi indipendenti dall’implementazione, fixture, isolamento e casi comuni, alternativi e limite. Evita test che copiano il codice o verificano soltanto il nome di una funzione.
4. Nei test temporali usa la stessa sorgente di tempo controllata per creazione, avanzamento e scadenza quando possibile. Non promettere runtime a zero millisecondi per test di integrazione o in-game.
5. Scrivi o esegui solo ciò che il mandato e gli strumenti consentono. Usa comandi effettivi dello stack; non installare dipendenze o cambiare ambiente implicitamente. Prima di test con effetti esterni definisci isolamento e risorse interessate.
6. Conserva comando, contesto, baseline e artefatto quando pertinente, esito e prove mancanti. Distingui fallimento del prodotto, del test e dell’ambiente; non alterare gli attesi per ottenere PASS.
7. Riporta verificato, fallito o non verificabile per proprietà. Test automatici, build, deploy e collaudo runtime/NVDA sono evidenze diverse; senza runtime prepara istruzioni e dichiara la prova non eseguita.
8. Durante lavoro sostanziale autorizzato mantieni il report pertinente quando serve continuità. Per gameplay usa anche il metodo specializzato soltanto se necessario alla richiesta; non avviare una catena automatica.
9. Nei fix scegli prove che distinguano la causa e verifichino il comportamento corretto e i percorsi correlati. Per moduli nuovi testa contratti in isolamento e integrazione ai confini, con attesi indipendenti e senza infrastrutture sproporzionate.

RISULTATO ATTESO
Risultato coerente con la modalità richiesta, fonti, assunzioni, limiti, evidenze e prossimo passo pertinente. Per test distinguere piano, test realizzati e prove effettivamente eseguite; per idea e strategia separare proposta e convalida.

CRITERI DI VERIFICA
Il risultato risponde al bisogno, conserva vincoli e decisioni esistenti, rende esplicite lacune e prove mancanti, senza passaggi automatici fuori dal mandato.

LIMITI E ARRESTO
Se manca un input decisivo completa il lavoro indipendente e chiedi quel dato. Se runtime o strumenti non sono disponibili dichiara il limite; non inventare risultati.
```

## Esempio di attivazione

Progetta ed esegui nel workspace di prova i test di regressione per questi contratti.

## Raccordo futuro con Astralis 4

Identità, criteri e metodo sono trasferibili solo dopo valutazione della futura architettura. Nessuna dipendenza o attivazione del Lab v4 è inclusa.

Nel Master Hub v3, la mappa `ciclo_sviluppo_e_selezione_strumenti_astralis.md` raccorda anche skill e template.
