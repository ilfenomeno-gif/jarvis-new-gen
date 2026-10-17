---
schema: 2
id: "AST-P-REVIEW-CODICE"
title: "Revisione del codice basata su evidenze"
revision: "1.2.0"
status: "adattato_verificato_documentalmente"
category: "04_revisione_e_validazione"
protocols: [5, 12]
domains: ["software", "addon_nvda", "utility", "giochi"]
mode: "consultiva"
requires: ["lettura_file", "diff_opzionale"]
sources: ["prompt-analista-revisore.md"]
selection: {"intents": ["revisionare_codice"], "use_when": ["Cercare difetti concreti nel codice o diff con una review consultiva."], "avoid_when": ["Se si deve dimostrare aderenza a un piano completo scegliere validazione implementazione."], "materials": ["codice_o_diff", "requisiti_o_contesto"], "examples": ["Ho un diff da controllare, senza un piano implementativo completo."], "related": [{"id": "AST-P-VALIDAZIONE-IMPLEMENTAZIONE", "when": "Se il piano e la baseline permettono una validazione del risultato."}]}
---

# Revisione del codice basata su evidenze

## Scopo e condizioni d'uso

Individuare difetti concreti nel codice e proporre rettifiche minime senza correggere durante la review.

Identificativo: `AST-P-REVIEW-CODICE`. Revisione del prompt: `1.2.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-04; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: 5, 12.
- Domini: software, addon_nvda, utility, giochi.
- Modalità: `consultiva`.
- Capacità richieste: lettura_file, diff_opzionale.
- Input della sessione: Perimetro: [FILE/DIFF]. Baseline: [RIFERIMENTO]. Requisiti e aree protette: [VINCOLI]. Priorità: [AREE DI RISCHIO].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Cercare difetti concreti nel codice o diff con una review consultiva.
- Preferisci altro quando: Se si deve dimostrare aderenza a un piano completo scegliere validazione implementazione.
- Materiali minimi: codice_o_diff, requisiti_o_contesto. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Ho un diff da controllare, senza un piano implementativo completo.».
- Passo collegato: `AST-P-VALIDAZIONE-IMPLEMENTAZIONE` — Se il piano e la baseline permettono una validazione del risultato.

La [procedura condivisa v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Revisione del codice basata su evidenze (AST-P-REVIEW-CODICE)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Individuare difetti concreti nel codice e proporre rettifiche minime senza correggere durante la review.

INPUT
Perimetro: [FILE/DIFF]. Baseline: [RIFERIMENTO]. Requisiti e aree protette: [VINCOLI]. Priorità: [AREE DI RISCHIO].

PERIMETRO OPERATIVO
Review in lettura. Nessuna patch, refactor, build, modifica di test, commit o delega automatica. La correzione passa a un mandato distinto di implementazione.

PROCEDURA
1. Leggi istruzioni, diff e codice attuale. Separa modifiche dell'intervento da quelle preesistenti. Approfondisci le dipendenze necessarie, non l'intera codebase per default.
2. Esamina correttezza, sicurezza, prestazioni, compatibilità, gestione risorse e accessibilità quando pertinenti. Lo stile conta solo se causa un problema concreto o viola un contratto richiesto.
3. Per ogni sospetto verifica percorso d'esecuzione, prerequisiti e controesempi. Non dichiarare un bug dal solo nome di una funzione o da un pattern astratto.
4. Registra identificativo, gravità, requisito, file e funzione o righe verificate, scenario che attiva il difetto, impatto, prova disponibile e correzione minima proposta.
5. Distingui bug dimostrato, rischio non verificato e problema preesistente. Raggruppa segnalazioni con la stessa causa; non inventare anomalie per riempire una sezione.
6. Presenta solo rilievi azionabili e limita la conclusione al perimetro letto. Se serve un test, descrivilo oppure eseguilo solo quando autorizzato e dopo controllo degli effetti.
7. Collega ogni difetto alla catena causale e al componente responsabile; raggruppa sintomi con causa comune e indica prove sui chiamanti interessati. La preferenza per modularità non dimostra un bug e la review non autorizza correzioni.

RISULTATO ATTESO
Rilievi ordinati per gravità con evidenza e scenario, rettifiche proposte, limiti della review. Se non emergono difetti sostanziali, dichiaralo precisando il perimetro.

CRITERI DI VERIFICA
Ogni rilievo descrive un comportamento plausibile e una prova controllabile; nessuna modifica durante l'audit; ipotesi e fatti distinti.

LIMITI E ARRESTO
Accesso al repository necessario per una review del codice reale; senza file esamina soltanto gli estratti forniti e dichiara la copertura limitata.
```

## Esempio di attivazione

Revisiona questo diff rispetto al requisito approvato. Segnala difetti concreti con scenario e riferimento; non applicare correzioni.

## Raccordo futuro con Astralis 4

Possibile raccordo con astralis-code-reviewer; non riutilizzare il ciclo legacy che applicava fix durante la review.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
