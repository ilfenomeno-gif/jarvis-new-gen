---
schema: 2
id: "AST-P-IDEA-RFC"
title: "Ideazione e chiarimento del bisogno"
revision: "1.0.0"
status: "nuovo_verificato_documentalmente"
category: "03_progettazione_e_pianificazione"
protocols: [1]
domains: ["trasversale"]
mode: "consultiva"
requires: ["lettura_materiali", "strumenti_pertinenti_se_autorizzati"]
sources: []
selection: {"intents": ["chiarire_idea"], "use_when": ["Chiarisce un’idea embrionale o un bisogno ancora incompleto prima di scegliere una soluzione."], "avoid_when": ["Requisito già chiaro, strategia già elaborata, piano esecutivo o implementazione."], "materials": ["Intuizione o bisogno, destinatari e contesto disponibile; lacune ammesse."], "examples": ["Ho questa intuizione: aiutami a capire il problema e se vale la pena approfondirla."], "related": [{"id": "AST-P-STRATEGIA-LOGICA", "when": "Quando occorre sviluppare un modello concettuale del bisogno chiarito."}]}
---

# Ideazione e chiarimento del bisogno

## Scopo e condizioni d'uso

Chiarisce un’idea embrionale o un bisogno ancora incompleto prima di scegliere una soluzione.
Identificativo: `AST-P-IDEA-RFC`. Revisione 1.0.0; non è una versione del framework. Collaudo d'uso dei client aperto.
Consulta lo [standard](../STANDARD_PROMPT_ASTRALIS.md) e la [procedura di selezione v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md).

## Scheda operativa

- Protocolli: 1.
- Ambito: trasversale, specializzato sul contesto effettivo.
- Modalità: consultiva; non concede permessi.
- Materiali: Intuizione o bisogno, destinatari e contesto disponibile; lacune ammesse.
- Provenienza: capacità nuova derivata dalle esigenze e dalla tassonomia v3; nessuna sorgente storica attribuita.

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Chiarisce un’idea embrionale o un bisogno ancora incompleto prima di scegliere una soluzione.
- Evitalo quando: Requisito già chiaro, strategia già elaborata, piano esecutivo o implementazione.
- Materiali: Intuizione o bisogno, destinatari e contesto disponibile; lacune ammesse.
- Esempio: Ho questa intuizione: aiutami a capire il problema e se vale la pena approfondirla.
- Passo collegato: `AST-P-STRATEGIA-LOGICA` — Quando occorre sviluppare un modello concettuale del bisogno chiarito.

## Testo da copiare

```text
ASTRALIS — Ideazione e chiarimento del bisogno — AST-P-IDEA-RFC

CONTESTO E VINCOLI ESSENZIALI
Rispetta istruzioni attive, mandato già dato e conoscenza pertinente accessibile. Questo prompt non conferisce permessi.
Separa fatti, ipotesi, simulazioni e prove. Usa italiano lineare e navigabile con NVDA; non esporre ragionamento interno privato.

OBIETTIVO
Chiarisce un’idea embrionale o un bisogno ancora incompleto prima di scegliere una soluzione.

INPUT
Richiesta e obiettivo: [RICHIESTA]. Materiali: [FONTI]. Contesto e vincoli: [CONTESTO]. Modalità e mandato: [PROGETTAZIONE / REALIZZAZIONE / ESECUZIONE, SE PERTINENTI].

PERIMETRO OPERATIVO
Svolgi soltanto il compito richiesto. Persistenza utile e modifiche seguono il mandato già disponibile; niente implementazione, invio, delega, deploy o pubblicazione impliciti. Non chiedere una nuova conferma per azioni già autorizzate.

PROCEDURA
1. Parti dalla situazione osservabile, da chi incontra il problema e dal beneficio riconoscibile; non confondere la prima soluzione suggerita con il bisogno.
2. Separa fatti, assunzioni e domande aperte. Recupera il contesto disponibile e chiedi soltanto ciò che cambia la decisione.
3. Considera alternative plausibili, riuso e non intervenire quando utile; non imporre un numero di idee.
4. Produci problema/opportunità, beneficio, ipotesi, vincoli e decisione richiesta. Se serve persistenza nel mandato usa IDEA_RFC_TEMPLATE.md e docs/idee nella radice documentale risolta.
5. Distingui esito IN ATTESA, ACCOLTA, RESPINTA o RINVIATA con motivazione reale. Un’idea accolta non autorizza strategia, piano o codice fuori dall’incarico. Per un requisito già chiaro passa al metodo pertinente senza retrocederlo.

RISULTATO ATTESO
Risultato coerente con la modalità richiesta, fonti, assunzioni, limiti, evidenze e prossimo passo pertinente. Per test distinguere piano, test realizzati e prove effettivamente eseguite; per idea e strategia separare proposta e convalida.

CRITERI DI VERIFICA
Il risultato risponde al bisogno, conserva vincoli e decisioni esistenti, rende esplicite lacune e prove mancanti, senza passaggi automatici fuori dal mandato.

LIMITI E ARRESTO
Se manca un input decisivo completa il lavoro indipendente e chiedi quel dato. Se runtime o strumenti non sono disponibili dichiara il limite; non inventare risultati.
```

## Esempio di attivazione

Ho questa intuizione: aiutami a capire il problema e se vale la pena approfondirla.

## Raccordo futuro con Astralis 4

Identità, criteri e metodo sono trasferibili solo dopo valutazione della futura architettura. Nessuna dipendenza o attivazione del Lab v4 è inclusa.

Nel Master Hub v3, la mappa `ciclo_sviluppo_e_selezione_strumenti_astralis.md` raccorda anche skill e template.
