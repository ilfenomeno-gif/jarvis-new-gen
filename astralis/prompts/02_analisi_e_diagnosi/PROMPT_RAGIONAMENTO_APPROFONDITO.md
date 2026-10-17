---
schema: 2
id: "AST-P-ANALISI-PROFONDA"
title: "Analisi approfondita e confronto delle alternative"
revision: "1.1.0"
status: "adattato_verificato_documentalmente"
category: "02_analisi_e_diagnosi"
protocols: [1, 12]
domains: ["trasversale"]
mode: "consultiva"
requires: ["lettura_materiali"]
sources: ["prompt-DeepReasoner.md"]
selection: {"intents": ["analizzare_decisione"], "use_when": ["Comprendere un problema complesso e confrontare alternative non necessariamente software."], "avoid_when": ["Per una specifica scelta tecnica usare analisi ingegneristica; per un piano concreto usare validazione piano."], "materials": ["problema", "obiettivo", "vincoli"], "examples": ["Aiutami a scegliere fra questi approcci con questi vincoli."], "related": [{"id": "AST-P-ANALISI-INGEGNERISTICA", "when": "Se la decisione riguarda contratti e componenti software."}]}
---

# Analisi approfondita e confronto delle alternative

## Scopo e condizioni d'uso

Esaminare un problema complesso e formulare una raccomandazione motivata e verificabile.

Identificativo: `AST-P-ANALISI-PROFONDA`. Revisione del prompt: `1.1.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-03; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: 1, 12.
- Domini: trasversale.
- Modalità: `consultiva`.
- Capacità richieste: lettura_materiali.
- Input della sessione: Problema: [DOMANDA]. Obiettivo: [RISULTATO]. Fonti: [MATERIALI]. Vincoli: [VINCOLI].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Comprendere un problema complesso e confrontare alternative non necessariamente software.
- Preferisci altro quando: Per una specifica scelta tecnica usare analisi ingegneristica; per un piano concreto usare validazione piano.
- Materiali minimi: problema, obiettivo, vincoli. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Aiutami a scegliere fra questi approcci con questi vincoli.».
- Passo collegato: `AST-P-ANALISI-INGEGNERISTICA` — Se la decisione riguarda contratti e componenti software.

La [procedura condivisa v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Analisi approfondita e confronto delle alternative (AST-P-ANALISI-PROFONDA)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Esaminare un problema complesso e formulare una raccomandazione motivata e verificabile.

INPUT
Problema: [DOMANDA]. Obiettivo: [RISULTATO]. Fonti: [MATERIALI]. Vincoli: [VINCOLI].

PERIMETRO OPERATIVO
Analisi e proposta in chat. Non applicare soluzioni né salvare documenti salvo mandato esplicito.

PROCEDURA
1. Identifica obiettivo, vincoli e decisione richiesta. Recupera il contesto pertinente e distingui fatti, ipotesi e informazioni mancanti.
2. Scomponi il problema nelle sue responsabilità e dipendenze reali. Chiedi chiarimenti solo se una lacuna impedisce una conclusione utile.
3. Per una decisione con alternative reali, confronta gli approcci usando gli stessi criteri: efficacia, costo, complessità, rischi, accessibilità e reversibilità quando pertinenti. Non inventare alternative per riempire una struttura.
4. Verifica assunzioni, controesempi e condizioni limite. Applica i cancelli Astralis pertinenti senza imporre criteri fisici o di gioco ad altri domini.
5. Formula la soluzione minima adeguata. Rivedi una conclusione se emergono evidenze contrarie; termina quando i criteri sono soddisfatti oppure il limite è dichiarato, senza cercare un punteggio perfetto.

RISULTATO ATTESO
Analisi: conclusione principale e motivazione. Dettagli: evidenze, alternative rilevanti e limiti. Raccomandazioni: azione proposta e verifica necessaria. Adatta la lunghezza alla domanda.

CRITERI DI VERIFICA
La conclusione risponde alla domanda, le assunzioni sono visibili e i limiti sono documentati. Le motivazioni sono sintetiche e controllabili, senza richiedere esposizione del ragionamento interno.

LIMITI E ARRESTO
Se le fonti mancano, consegna una valutazione condizionata e specifica ciò che serve. Non promettere certezza o prestazioni non misurate.
```

## Esempio di attivazione

Confronta due strategie di gestione dello stato rispetto a questi vincoli e raccomanda quella più semplice da verificare.

## Raccordo futuro con Astralis 4

Possibile raccordo con astralis-deep-reasoner e astralis-decision-matrix; disponibilità e interfacce da verificare nel Lab.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
