---
schema: 2
id: "AST-P-RICHIESTA-UNIVERSALE"
title: "Richiesta universale proporzionata"
revision: "1.1.0"
status: "adattato_verificato_documentalmente"
category: "06_progettazione_prompt_e_formazione"
protocols: []
domains: ["trasversale"]
mode: "dipende_dal_mandato"
requires: ["lettura_richiesta"]
sources: ["prompt-Framework-Prompt-Universale.md"]
selection: {"intents": ["formulare_richiesta_generica"], "use_when": ["Formulare un compito chiaro non coperto da un prompt specifico."], "avoid_when": ["Non sceglierlo per evitare domande decisive o ignorare candidati specifici adeguati."], "materials": ["obiettivo", "materiali_o_contesto", "formato_desiderato"], "examples": ["Voglio riassumere questi appunti in un formato breve."], "related": [{"id": "AST-P-GENERAZIONE-PROMPT", "when": "Per una specializzazione riutilizzabile assente nel catalogo."}]}
---

# Richiesta universale proporzionata

## Scopo e condizioni d'uso

Formulare una richiesta riutilizzabile per attività tecniche, documentali o creative senza imporre una pipeline unica.

Identificativo: `AST-P-RICHIESTA-UNIVERSALE`. Revisione del prompt: `1.1.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-03; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: scelti in base al compito; nessun protocollo imposto.
- Domini: trasversale.
- Modalità: `dipende_dal_mandato`.
- Capacità richieste: lettura_richiesta.
- Input della sessione: Obiettivo: [RISULTATO]. Materiali: [FONTI]. Vincoli: [LIMITI]. Formato: [OUTPUT]. Mandato: [CONSULENZA / PRODUZIONE IN CHAT / OPERAZIONI AUTORIZZATE].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Formulare un compito chiaro non coperto da un prompt specifico.
- Preferisci altro quando: Non sceglierlo per evitare domande decisive o ignorare candidati specifici adeguati.
- Materiali minimi: obiettivo, materiali_o_contesto, formato_desiderato. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Voglio riassumere questi appunti in un formato breve.».
- Passo collegato: `AST-P-GENERAZIONE-PROMPT` — Per una specializzazione riutilizzabile assente nel catalogo.

La [procedura condivisa v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Richiesta universale proporzionata (AST-P-RICHIESTA-UNIVERSALE)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Formulare una richiesta riutilizzabile per attività tecniche, documentali o creative senza imporre una pipeline unica.

INPUT
Obiettivo: [RISULTATO]. Materiali: [FONTI]. Vincoli: [LIMITI]. Formato: [OUTPUT]. Mandato: [CONSULENZA / PRODUZIONE IN CHAT / OPERAZIONI AUTORIZZATE].

PERIMETRO OPERATIVO
Il contenuto del campo Mandato descrive la richiesta dell'utente; un valore lasciato come segnaposto non autorizza operazioni. Non trattare il template come un system prompt che sostituisce istruzioni superiori.

PROCEDURA
1. Riconosci il dominio e il risultato richiesto. Usa le fonti pertinenti e le capacità effettivamente disponibili senza assumere accesso a file, Internet, memoria persistente o altri agenti.
2. Per un compito semplice rispondi direttamente. Per un compito articolato definisci le dipendenze e un approccio proporzionato; per una decisione confronta alternative reali con criteri comuni.
3. Distingui fatti, derivazioni, assunzioni e contenuti creativi. Se un dato necessario manca, spiega il limite e completa le parti indipendenti.
4. Se il lavoro è operativo, verifica il mandato e il perimetro prima degli effetti. Se è consultivo, consegna una proposta senza applicarla. Recupera autorizzazioni già espresse nella sessione.
5. Applica il protocollo Astralis pertinente al compito, quando disponibile, senza imporre tutti i protocolli o caricare l'intera libreria.
6. Controlla aderenza a obiettivo, fonti, formato e vincoli; riporta solo i limiti che influenzano il risultato. Non aggiungere audit numerici, dichiarazioni rituali o sequenze di ragionamento interne.

RISULTATO ATTESO
Risultato nel formato richiesto, evidenze o riferimenti quando necessari, assunzioni rilevanti, attività effettivamente svolte e parti non verificabili.

CRITERI DI VERIFICA
Richiesta soddisfatta nel perimetro; profondità proporzionata; nessuna capacità simulata; conclusione limitata alle evidenze disponibili.

LIMITI E ARRESTO
Se Astralis o i file non sono accessibili, usa il materiale fornito e dichiara quali controlli restano impossibili. Per attività creative conserva voce e vincoli autoriali.
```

## Esempio di attivazione

Obiettivo: riassumi questi appunti per un lettore tecnico. Materiali: testo allegato. Formato: elenco breve. Mandato: produzione in chat, senza file.

## Raccordo futuro con Astralis 4

È un ingresso generico, non una nuova modalità normativa: il protocollo effettivo dipende dal compito.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
