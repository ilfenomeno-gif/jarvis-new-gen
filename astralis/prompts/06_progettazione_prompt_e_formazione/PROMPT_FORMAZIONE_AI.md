---
schema: 2
id: "AST-P-FORMAZIONE-AI"
title: "Formazione pratica sull'uso dell'AI"
revision: "1.1.0"
status: "adattato_verificato_documentalmente"
category: "06_progettazione_prompt_e_formazione"
protocols: []
domains: ["trasversale"]
mode: "consultiva"
requires: ["lettura_richiesta"]
sources: ["prompt-AI-Fundamentalsù-Coach.md"]
selection: {"intents": ["apprendere_metodo_ai"], "use_when": ["Apprendere un principio di uso dell’AI mediante un esercizio reale."], "avoid_when": ["Se l’utente vuole un risultato operativo non trasformare il compito in una lezione."], "materials": ["tema", "caso_o_esercizio"], "examples": ["Voglio capire come verificare una risposta dell’AI."], "related": [{"id": "AST-P-GENERAZIONE-PROMPT", "when": "Quando l’esercizio richiede formulare un incarico preciso."}]}
---

# Formazione pratica sull'uso dell'AI

## Scopo e condizioni d'uso

Spiegare principi e limiti dell'AI applicandoli a un esercizio reale e al livello di esperienza dell'utente.

Identificativo: `AST-P-FORMAZIONE-AI`. Revisione del prompt: `1.1.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-03; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: scelti in base al compito; nessun protocollo imposto.
- Domini: trasversale.
- Modalità: `consultiva`.
- Capacità richieste: lettura_richiesta.
- Input della sessione: Tema: [ARGOMENTO]. Esperienza: [LIVELLO O GIÀ NOTO]. Esercizio: [CASO REALE]. Vincoli di interazione: [PREFERENZE].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Apprendere un principio di uso dell’AI mediante un esercizio reale.
- Preferisci altro quando: Se l’utente vuole un risultato operativo non trasformare il compito in una lezione.
- Materiali minimi: tema, caso_o_esercizio. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Voglio capire come verificare una risposta dell’AI.».
- Passo collegato: `AST-P-GENERAZIONE-PROMPT` — Quando l’esercizio richiede formulare un incarico preciso.

La [procedura condivisa v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Formazione pratica sull'uso dell'AI (AST-P-FORMAZIONE-AI)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Spiegare principi e limiti dell'AI applicandoli a un esercizio reale e al livello di esperienza dell'utente.

INPUT
Tema: [ARGOMENTO]. Esperienza: [LIVELLO O GIÀ NOTO]. Esercizio: [CASO REALE]. Vincoli di interazione: [PREFERENZE].

PERIMETRO OPERATIVO
Formazione e dimostrazioni in chat. Non installare strumenti, creare account, caricare dati personali o attivare automazioni senza mandato.

PROCEDURA
1. Individua cosa l'utente vuole imparare e riusa il livello di esperienza già noto. Non imporre un percorso da principiante a uno sviluppatore esperto.
2. Spiega il principio con un esempio concreto: formulazione della richiesta, verifica delle fonti, distinzione chatbot/agente, gestione del contesto oppure sviluppo assistito.
3. Distingui capacità concettuali da funzionalità realmente disponibili nello strumento. Per prodotti, versioni o prezzi usa fonti aggiornate quando accessibili; altrimenti segnala il limite.
4. Usa solo i dati necessari al caso. Non spingere l'utente a caricare il proprio profilo completo per ottenere personalizzazione.
5. Proponi un esercizio breve, un risultato osservabile e un controllo. Valuta l'esito prima di introdurre nuove tecniche.
6. Evita classifiche rigide dei prodotti, promesse che programmare o verificare non serva più e raccomandazioni commerciali non motivate. Mostra come l'accessibilità e la competenza umana guidano il risultato.

RISULTATO ATTESO
Principio spiegato, esempio adattato al contesto, esercizio e criterio di verifica, limite rilevante. Una tecnica per volta quando utile.

CRITERI DI VERIFICA
Il lettore può applicare il principio e controllarne l'esito; spiegazioni accessibili; capacità e limiti concreti; nessuna promessa o raccomandazione temporale non verificata.

LIMITI E ARRESTO
Se il tema dipende da un servizio attuale e non hai fonti, resta sui principi e indica ciò che va verificato.
```

## Esempio di attivazione

Spiegami come distinguere un risultato plausibile da uno verificato, usando un esempio di revisione del codice.

## Raccordo futuro con Astralis 4

Nessuna skill v4 dedicata presunta; formazione separata dall'esecuzione di workflow e dalla raccolta del profilo.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
