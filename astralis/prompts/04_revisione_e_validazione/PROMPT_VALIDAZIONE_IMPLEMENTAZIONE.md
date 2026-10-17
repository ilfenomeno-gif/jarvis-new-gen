---
schema: 2
id: "AST-P-VALIDAZIONE-IMPLEMENTAZIONE"
title: "Validazione indipendente di un'implementazione"
revision: "1.2.0"
status: "adattato_verificato_documentalmente"
category: "04_revisione_e_validazione"
protocols: [2, 5, 12]
domains: ["software", "addon_nvda", "utility", "giochi"]
mode: "verifica_senza_correzione"
requires: ["lettura_file", "diff_opzionale", "runner_test_se_autorizzato"]
sources: ["validatore universale.md"]
selection: {"intents": ["validare_implementazione"], "use_when": ["Confrontare codice realizzato con piano approvato, requisiti e baseline."], "avoid_when": ["Non serve a definire il piano prima dell’esecuzione; una ricerca della causa nei log richiede diagnosi."], "materials": ["piano_approvato", "codice_o_diff", "baseline_o_limite_dichiarato"], "examples": ["L’AI ha finito il codice: rispetta il piano?"], "related": [{"id": "AST-P-IMPLEMENTAZIONE", "when": "Per correggere difetti dimostrati con un nuovo mandato circoscritto."}]}
---

# Validazione indipendente di un'implementazione

## Scopo e condizioni d'uso

Confrontare implementazione, piano e baseline distinguendo correttezza statica, test ed evidenza sul campo.

Identificativo: `AST-P-VALIDAZIONE-IMPLEMENTAZIONE`. Revisione del prompt: `1.2.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-04; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: 2, 5, 12.
- Domini: software, addon_nvda, utility, giochi.
- Modalità: `verifica_senza_correzione`.
- Capacità richieste: lettura_file, diff_opzionale, runner_test_se_autorizzato.
- Input della sessione: Piano: [RIFERIMENTO]. Intervento e baseline: [DIFF/COMMIT/FILE]. Verifiche consentite: [LETTURA / COMANDI E AMBIENTE]. Collaudo disponibile: [EVIDENZE].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Confrontare codice realizzato con piano approvato, requisiti e baseline.
- Preferisci altro quando: Non serve a definire il piano prima dell’esecuzione; una ricerca della causa nei log richiede diagnosi.
- Materiali minimi: piano_approvato, codice_o_diff, baseline_o_limite_dichiarato. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «L’AI ha finito il codice: rispetta il piano?».
- Passo collegato: `AST-P-IMPLEMENTAZIONE` — Per correggere difetti dimostrati con un nuovo mandato circoscritto.

La [procedura condivisa v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Validazione indipendente di un'implementazione (AST-P-VALIDAZIONE-IMPLEMENTAZIONE)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Confrontare implementazione, piano e baseline distinguendo correttezza statica, test ed evidenza sul campo.

INPUT
Piano: [RIFERIMENTO]. Intervento e baseline: [DIFF/COMMIT/FILE]. Verifiche consentite: [LETTURA / COMANDI E AMBIENTE]. Collaudo disponibile: [EVIDENZE].

PERIMETRO OPERATIVO
La richiesta di validazione non autorizza correzioni. Esegui soltanto verifiche comprese nel mandato, dopo averne controllato effetti e ambiente; niente sorgenti modificati, refactor, cambio branch, reset, commit o deploy.

PROCEDURA
1. Leggi piano, istruzioni e resoconto dell'implementatore. Controlla codice e stato corrente; il resoconto è una dichiarazione da verificare, non una prova.
2. Separa baseline, modifiche dell'intervento e modifiche estranee. Per ciascun requisito indica SODDISFATTO, PARZIALE, NON SODDISFATTO, NON VERIFICATO o NON APPLICABILE con motivo.
3. Verifica flussi, condizioni limite, contratti, error handling, risorse, sicurezza, compatibilità e accessibilità nelle aree coinvolte. Non sostituire l'audit con un controllo dei nomi delle funzioni.
4. Esamina risultati dei test già disponibili rispetto al codice corrente e alla copertura. Se autorizzato esegui controlli pertinenti in ambiente isolato; conserva comando, contesto, esito e limiti. Non modificare attesi per ottenere PASS.
5. Distingui regressione dimostrata, rischio, problema preesistente e cambiamento intenzionale approvato. Riporta identificativo, requisito, evidenza, scenario, impatto e rettifica minima per ogni anomalia.
6. Specifica il livello probatorio Astralis raggiunto, anche se più livelli sono necessari per requisiti diversi. Compilazione, test headless e collaudo empirico sono evidenze differenti.
7. Emetti VALIDATA, VALIDATA CON RISERVE, CORREZIONI NECESSARIE, VALIDAZIONE INCOMPLETA o RESPINTA. Se manca una verifica essenziale usa VALIDAZIONE INCOMPLETA; non trasformarla in riserva non bloccante.
8. Per i fix verifica riproduzione originale, eliminazione della causa e invarianti nei percorsi correlati. Per nuovi moduli verifica contratti, direzione delle dipendenze e isolamento proporzionato. Separa prove tecniche da preferenze architetturali e collaudo utente.

RISULTATO ATTESO
Verdetto, tracciabilità dei requisiti, criticità, controlli realmente eseguiti, livello di evidenza, rettifiche prioritarie e limiti. Mantieni il report pertinente quando la documentazione interna serve al lavoro sostanziale ed è compresa nel mandato, senza richiedere ogni volta un comando separato. Per soli consigli senza mandato di salvataggio rispondi in chat.

CRITERI DI VERIFICA
Requisiti verificati sul codice corrente; prove mancanti visibili; correzioni non applicate; stato probatorio distinto dal verdetto complessivo e dalla checklist.

LIMITI E ARRESTO
Senza baseline non attribuire automaticamente un problema all'ultima modifica. Senza collaudo utente non dichiarare FULL EMPIRICAL PASS quando richiesto.
```

## Esempio di attivazione

Valida l'implementazione rispetto al piano. Sono autorizzati i test indicati in ambiente di test; non correggere codice né modificare gli attesi.

## Raccordo futuro con Astralis 4

Possibile raccordo con astralis-validation e astralis-code-reviewer; il mandato governa ogni effetto del runner.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
