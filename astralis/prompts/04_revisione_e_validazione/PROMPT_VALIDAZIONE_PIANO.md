---
schema: 2
id: "AST-P-VALIDAZIONE-PIANO"
title: "Validazione di un piano tecnico"
revision: "1.1.0"
status: "adattato_verificato_documentalmente"
category: "04_revisione_e_validazione"
protocols: [2, 12]
domains: ["software", "addon_nvda", "utility", "giochi"]
mode: "consultiva"
requires: ["lettura_piano", "lettura_file"]
sources: ["validatore di piani tecnici.md"]
selection: {"intents": ["validare_piano"], "use_when": ["Verificare fattibilità e tracciabilità dei test di un piano tecnico non ancora applicato."], "avoid_when": ["Se il codice è già realizzato e si deve controllarne il risultato scegliere validazione implementazione."], "materials": ["piano_tecnico", "sorgenti_pertinenti_o_limite", "criteri_accettazione"], "examples": ["Verifica questo piano prima di passarlo all’implementatore."], "related": [{"id": "AST-P-IMPLEMENTAZIONE", "when": "Solo dopo validazione e mandato operativo dell’utente."}]}
---

# Validazione di un piano tecnico

## Scopo e condizioni d'uso

Accertare che un piano sia implementabile sul codice esistente e che i test verifichino i requisiti reali.

Identificativo: `AST-P-VALIDAZIONE-PIANO`. Revisione del prompt: `1.1.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-03; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: 2, 12.
- Domini: software, addon_nvda, utility, giochi.
- Modalità: `consultiva`.
- Capacità richieste: lettura_piano, lettura_file.
- Input della sessione: Piano: [PIANO]. Rettifiche proposte: [ELENCO O NESSUNA]. Fonti e baseline: [RIFERIMENTI]. Funzioni protette: [ELENCO].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Verificare fattibilità e tracciabilità dei test di un piano tecnico non ancora applicato.
- Preferisci altro quando: Se il codice è già realizzato e si deve controllarne il risultato scegliere validazione implementazione.
- Materiali minimi: piano_tecnico, sorgenti_pertinenti_o_limite, criteri_accettazione. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Verifica questo piano prima di passarlo all’implementatore.».
- Passo collegato: `AST-P-IMPLEMENTAZIONE` — Solo dopo validazione e mandato operativo dell’utente.

La [procedura condivisa v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Validazione di un piano tecnico (AST-P-VALIDAZIONE-PIANO)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Accertare che un piano sia implementabile sul codice esistente e che i test verifichino i requisiti reali.

INPUT
Piano: [PIANO]. Rettifiche proposte: [ELENCO O NESSUNA]. Fonti e baseline: [RIFERIMENTI]. Funzioni protette: [ELENCO].

PERIMETRO OPERATIVO
Analisi del piano in sola lettura. Non eseguire test, build o deploy e non modificare documenti o codice. Il consolidamento documentale richiede mandato esplicito.

PROCEDURA
1. Leggi integralmente piano e allegati pertinenti. Consulta codice, fixture, decisioni e telemetria necessari a verificarne la fattibilità. Non assumere corrette le proposte di nessun assistente.
2. Per ogni rettifica proposta restituisci CONFERMATA, RETTIFICATA CON EVIDENZA o RESPINTA CON EVIDENZA, con riferimento controllabile.
3. Verifica cause radice, responsabilità, ordine delle fasi, dipendenze, condizioni di ingresso e uscita, errori, fallback e funzionalità da proteggere. Il piano deve descrivere comportamento concreto del runtime.
4. Collega ogni requisito al ramo decisionale, fixture, asserzione e risultato atteso. Cerca test che passano senza attraversare il flusso interessato, scenari mancanti e dipendenze d'ambiente.
5. Applica sette assi e simulazione a tre livelli dove pertinenti. Usa KISS e YAGNI; evita nuovi stati, manager o refactor quando bastano precisazioni locali.
6. Emetti VALIDATO, VALIDATO CON RETTIFICHE, DA RIVEDERE o NON VERIFICABILE. Specifica sezioni da consolidare, condizioni bloccanti e controlli futuri. La validazione resta teorica e non autorizza implementazione.

RISULTATO ATTESO
Esito delle rettifiche, lacune sistemiche, adeguamenti alle fixture, modifiche minime al piano e verdetto di implementabilità.

CRITERI DI VERIFICA
Requisiti collegati a flussi reali e controlli pertinenti; nessun riferimento rigido a Macro R4 o a un progetto particolare; evidenze insufficienti esplicite.

LIMITI E ARRESTO
Se codice o fixture non sono accessibili, delimita ciò che puoi verificare. Non dichiarare collaudata una decisione soltanto perché è descritta nel piano.
```

## Esempio di attivazione

Valida questo piano e le tre rettifiche allegate contro il codice corrente. Controlla la tracciabilità dei test, senza eseguirli.

## Raccordo futuro con Astralis 4

Possibile raccordo con astralis-validation; eventuale aggiornamento di project_state richiede mandato distinto.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
