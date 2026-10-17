---
schema: 2
id: "AST-P-SETUP-MACCHINA"
title: "Configurazione di una macchina"
revision: "1.1.0"
status: "adattato_verificato_documentalmente"
category: "01_onboarding_e_governance"
protocols: [9]
domains: ["trasversale"]
mode: "consultiva_con_applicazione_autorizzata"
requires: ["lettura_file", "scrittura_file_per_applicazione"]
sources: ["PROMPT_SETUP_INTERATTIVO_NUOVA_MACCHINA.md"]
selection: {"intents": ["configurare_macchina"], "use_when": ["Configurare Astralis 3 su una macchina e preparare gli assistenti scelti."], "avoid_when": ["Per un singolo repository già su una macchina configurata preferire inizializzazione progetto."], "materials": ["hub_v3", "assistenti_scelti", "preferenze_interazione"], "examples": ["Devo configurare Astralis sul nuovo computer."], "related": [{"id": "AST-P-INIT-PROGETTO", "when": "Dopo il setup, se si deve adottare Astralis in un repository."}]}
---

# Configurazione di una macchina

## Scopo e condizioni d'uso

Configurare Astralis su una macchina preservando profili esistenti e attivando soltanto gli assistenti scelti.

Identificativo: `AST-P-SETUP-MACCHINA`. Revisione del prompt: `1.1.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-03; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: 9.
- Domini: trasversale.
- Modalità: `consultiva_con_applicazione_autorizzata`.
- Capacità richieste: lettura_file, scrittura_file_per_applicazione.
- Input della sessione: Contesto: [MACCHINA E HUB]. Assistenti da usare: [AI]. Preferenze già note: [PREFERENZE]. Mandato: [ANALISI oppure APPLICAZIONE AUTORIZZATA E DESTINAZIONI].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Configurare Astralis 3 su una macchina e preparare gli assistenti scelti.
- Preferisci altro quando: Per un singolo repository già su una macchina configurata preferire inizializzazione progetto.
- Materiali minimi: hub_v3, assistenti_scelti, preferenze_interazione. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Devo configurare Astralis sul nuovo computer.».
- Passo collegato: `AST-P-INIT-PROGETTO` — Dopo il setup, se si deve adottare Astralis in un repository.

La [procedura condivisa v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Configurazione di una macchina (AST-P-SETUP-MACCHINA)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Configurare Astralis su una macchina preservando profili esistenti e attivando soltanto gli assistenti scelti.

INPUT
Contesto: [MACCHINA E HUB]. Assistenti da usare: [AI]. Preferenze già note: [PREFERENZE]. Mandato: [ANALISI oppure APPLICAZIONE AUTORIZZATA E DESTINAZIONI].

PERIMETRO OPERATIVO
La ricognizione è consultiva. Configura solo le destinazioni comprese nel mandato esplicito; la lettura di questo prompt non autorizza scritture. Non installare software né inizializzare tutti i progetti automaticamente.

PROCEDURA
1. Leggi le istruzioni disponibili e identifica il Master Hub scelto dall'utente. Rileva versione e macchina dalle fonti effettive, senza assumere che un clone sia un'installazione operativa.
2. Recupera le preferenze già dichiarate. Chiedi soltanto quelle mancanti: nome da usare, modalità di interazione e requisiti di accessibilità. Non imporre il profilo personale dell'autore a un altro utente.
3. Individua configurazioni esistenti dei soli assistenti richiesti. Distingui dati personali, regole comuni e personalizzazioni; segnala conflitti.
4. Presenta destinazioni, contenuti proposti, backup e controlli. Usa i template Astralis pertinenti; verifica sul contesto reale i percorsi del client senza inventarne configurazioni supportate.
5. Se l'applicazione è autorizzata, crea backup dei file coinvolti e integra le configurazioni senza perdere personalizzazioni. Mantieni router snelli e riferimenti alla conoscenza.
6. Verifica file generati e collegamenti. Non creare registri vuoti sopra quelli esistenti. Riporta attività concluse e verifiche ancora necessarie.

RISULTATO ATTESO
Ricevuta lineare: contesto riconosciuto, assistenti configurati o proposti, file preservati/modificati, verifiche, eventuali conflitti e prossimo passo.

CRITERI DI VERIFICA
Destinazioni corrette, preferenze confermate, backup leggibili, nessuna perdita di dati e link risolti. Il setup non certifica automaticamente il collaudo dei progetti.

LIMITI E ARRESTO
Se hub o destinazione sono ambigui, sospendi le scritture e chiarisci solo quel punto. Senza filesystem produci una proposta sulla base dei materiali forniti.
```

## Esempio di attivazione

Prepara il setup di questa macchina per Codex e Antigravity usando il Master Hub indicato. Mostrami prima la proposta; non modificare configurazioni.

## Raccordo futuro con Astralis 4

Il profilo macchina potrà essere letto dal Data Hub dopo verifica della sua disponibilità; nessun deploy automatico del Lab.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
