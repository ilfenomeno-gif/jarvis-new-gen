---
schema: 2
id: "AST-P-INIT-PROGETTO"
title: "Inizializzazione e adozione in un progetto"
revision: "1.1.0"
status: "adattato_verificato_documentalmente"
category: "01_onboarding_e_governance"
protocols: [9, 1]
domains: ["trasversale"]
mode: "consultiva_con_applicazione_autorizzata"
requires: ["lettura_file", "git_opzionale", "scrittura_file_per_applicazione"]
sources: ["PROMPT_INIZIALIZZAZIONE_ECOSISTEMA_REGOLE_UNIVERSALE.md"]
selection: {"intents": ["inizializzare_progetto"], "use_when": ["Adottare Astralis 3 in un progetto nuovo o esistente preservando la storia."], "avoid_when": ["Per allineare un progetto già governato a una nuova baseline usare aggiornamento ecosistema."], "materials": ["radice_progetto", "hub_v3", "assistenti_scelti"], "examples": ["Come inizializzo questo repository con Astralis?"], "related": [{"id": "AST-P-UPDATE-ECOSISTEMA", "when": "Se il progetto possiede già governance da aggiornare."}]}
---

# Inizializzazione e adozione in un progetto

## Scopo e condizioni d'uso

Integrare Astralis in un progetto nuovo o esistente, preservando codice, storia e conoscenza locale.

Identificativo: `AST-P-INIT-PROGETTO`. Revisione del prompt: `1.1.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-03; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: 9, 1.
- Domini: trasversale.
- Modalità: `consultiva_con_applicazione_autorizzata`.
- Capacità richieste: lettura_file, git_opzionale, scrittura_file_per_applicazione.
- Input della sessione: Progetto: [RADICE]. Obiettivo dell'adozione: [OBIETTIVO]. Assistenti: [AI]. Mandato: [ANALISI oppure APPLICAZIONE AUTORIZZATA E FILE].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Adottare Astralis 3 in un progetto nuovo o esistente preservando la storia.
- Preferisci altro quando: Per allineare un progetto già governato a una nuova baseline usare aggiornamento ecosistema.
- Materiali minimi: radice_progetto, hub_v3, assistenti_scelti. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Come inizializzo questo repository con Astralis?».
- Passo collegato: `AST-P-UPDATE-ECOSISTEMA` — Se il progetto possiede già governance da aggiornare.

La [procedura condivisa v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Inizializzazione e adozione in un progetto (AST-P-INIT-PROGETTO)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Integrare Astralis in un progetto nuovo o esistente, preservando codice, storia e conoscenza locale.

INPUT
Progetto: [RADICE]. Obiettivo dell'adozione: [OBIETTIVO]. Assistenti: [AI]. Mandato: [ANALISI oppure APPLICAZIONE AUTORIZZATA E FILE].

PERIMETRO OPERATIVO
Analizza il progetto in lettura. L'applicazione documentale richiede un mandato esplicito e non autorizza modifiche funzionali, build, deploy, commit o push.

PROCEDURA
1. Conferma radice e istruzioni del progetto. Rileva linguaggi, runtime, strumenti, struttura e domini effettivi; più domini possono coesistere.
2. Leggi i router e gli indici esistenti, poi solo le fonti pertinenti. Consulta una porzione motivata della storia Git quando presente. Non dedurre automaticamente una cronologia di release dai soli commit.
3. Inventaria documenti, knowledge, preferenze, prerequisiti e personalizzazioni da preservare. Separa dati macchina dalla conoscenza tecnica portabile.
4. Proponi una struttura aderente ai template e alle convenzioni già in uso: router dei soli assistenti richiesti, knowledge locale, piani, strategie, report e registri quando necessari. Mantieni il README rivolto agli utenti del progetto.
5. Se l'applicazione è autorizzata, integra i file con backup e senza rinumerare schede o alterare link storici inutilmente. Per la versione iniziale usa evidenze e scelta dell'utente; marca le ricostruzioni incerte come proposte.
6. Controlla link, coerenza, perimetro e recuperabilità. Consegna una ricevuta e distingue onboarding documentale da validazione del software.

RISULTATO ATTESO
Inventario essenziale, domini riconosciuti, proposta o elenco delle modifiche, contenuti preservati, controlli e decisioni aperte.

CRITERI DI VERIFICA
Nessuna perdita di storia; router collegati alla knowledge; istruzioni di build/test tratte da fonti reali; profilo personale escluso dai documenti portabili dove previsto.

LIMITI E ARRESTO
Senza baseline o documentazione sufficiente evita ricostruzioni certe. Se un file è già gestito da altri sistemi, segnala il conflitto prima di riscriverlo.
```

## Esempio di attivazione

Analizza questo repository e proponi l'adozione di Astralis preservando tutti i documenti presenti. Non applicare ancora la proposta.

## Raccordo futuro con Astralis 4

Il manifest di progetto e la lettura dello stato potranno sostituire la discovery manuale solo nel modello v4 realmente adottato.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
