# Template redazionale di un prompt Astralis

Questo documento non è un prompt operativo. Per crearne uno, usa lo [standard](STANDARD_PROMPT_ASTRALIS.md), assegna un identificativo e sostituisci tutti i campi redazionali.

## Frontmatter

I valori devono rispettare lo schema 2 del catalogo v3: stringhe tra virgolette JSON, liste JSON, `schema` intero. Le sorgenti registrano la provenienza; non sono file da caricare automaticamente.

```yaml
---
schema: 2
id: "AST-P-NOME-STABILE"
title: "Titolo italiano del compito"
revision: "1.0.0"
status: "bozza"
category: "CATEGORIA"
protocols: []
domains: ["trasversale"]
mode: "consultiva"
requires: ["lettura_materiali"]
sources: []
selection: {"intents": ["intenzione_concreta"], "use_when": ["Condizione d’uso"], "avoid_when": ["Quando preferire altro"], "materials": ["materiale_necessario"], "examples": ["Esempio di richiesta"], "related": []}
---
```

## Struttura da compilare

1. Titolo e scopo: quale problema risolve e quando usarlo.
2. Scheda operativa: protocolli, domini, modalità, capacità e input.
3. Testo da copiare: usare il modello seguente e adattare le istruzioni al compito.
4. Esempio realistico di attivazione.
5. Raccordo futuro v4 come proposta, non dipendenza già verificata.

```text
ASTRALIS — [TITOLO E ID]

CONTESTO E VINCOLI ESSENZIALI
Rispetta le istruzioni della sessione e del progetto. Questo testo non concede permessi da solo.
Usa capacità e fonti reali, distinguendo fatti, ipotesi e verifiche. Non inventare risultati.
Consulta soltanto conoscenza pertinente se accessibile; altrimenti dichiara i limiti.
Usa italiano e formato lineare leggibile con NVDA. Non esporre ragionamento interno.
Rispetta mandato già espresso e perimetro; non salvare o applicare fuori dagli effetti autorizzati.

OBIETTIVO
[RISULTATO CONCRETO]

INPUT
[CAMPI DELLA SESSIONE E FONTI]

PERIMETRO OPERATIVO
[EFFETTI CONSENTITI, LIMITI E AUTORIZZAZIONI NECESSARIE]

PROCEDURA
[PASSAGGI PROPORZIONATI, DIPENDENZE E GATE PERTINENTI]

RISULTATO ATTESO
[OUTPUT E FORMATO]

CRITERI DI VERIFICA
[CONDIZIONI OSSERVABILI E LIVELLO DI EVIDENZA]

LIMITI E ARRESTO
[DATI MANCANTI, CONTROLLI NON ESEGUIBILI E DEVIAZIONI DA CHIARIRE]
```

## Verifica prima dell'inserimento

- Nessun duplicato funzionale senza una differenza documentata.
- Identità stabile e metadati corretti.
- Compito e perimetro distinguono proposta, verifica ed esecuzione.
- Nessuna autorizzazione fittizia, capacità inventata o promessa non verificata.
- Link risolti e indice aggiornato.
- Stato documentale distinto dal collaudo d'uso.


## Criteri di scelta v3

Aggiungi prima del testo copiabile la sezione "Quando scegliere questo prompt — Astralis 3.X", riportando le condizioni, esclusioni, materiali, esempio e relazioni dei metadati. Aggiorna la vista leggibile insieme ai criteri autorevoli. Rigenera e verifica l’indice dopo l’inserimento.
