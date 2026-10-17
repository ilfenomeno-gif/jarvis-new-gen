---
schema: 2
id: "AST-P-UPDATE-ECOSISTEMA"
title: "Aggiornamento integrativo dell'ecosistema"
revision: "1.1.0"
status: "adattato_verificato_documentalmente"
category: "01_onboarding_e_governance"
protocols: [8]
domains: ["trasversale"]
mode: "consultiva_con_applicazione_autorizzata"
requires: ["lettura_file", "confronto_versioni", "scrittura_file_per_applicazione"]
sources: ["PROMPT_AGGIORNAMENTO_ECOSISTEMA_ESISTENTE.md"]
selection: {"intents": ["aggiornare_governance"], "use_when": ["Confrontare o aggiornare governance e personalizzazioni v3 in destinazioni definite."], "avoid_when": ["Non è una migrazione ad Astralis 4; per un progetto senza governance scegliere inizializzazione."], "materials": ["sorgente_aggiornamento_v3", "destinazioni", "baseline_o_limite_dichiarato"], "examples": ["Voglio allineare questi progetti alla governance aggiornata."], "related": [{"id": "AST-P-INIT-PROGETTO", "when": "Per i candidati onboarding senza governance esistente."}]}
---

# Aggiornamento integrativo dell'ecosistema

## Scopo e condizioni d'uso

Valutare e applicare un aggiornamento preservando personalizzazioni, conoscenza locale e possibilità di recupero.

Identificativo: `AST-P-UPDATE-ECOSISTEMA`. Revisione del prompt: `1.1.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-03; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: 8.
- Domini: trasversale.
- Modalità: `consultiva_con_applicazione_autorizzata`.
- Capacità richieste: lettura_file, confronto_versioni, scrittura_file_per_applicazione.
- Input della sessione: Sorgente aggiornamento: [SORGENTE]. Destinazioni: [HUB/PROGETTI]. Baseline: [VERSIONE O NON DISPONIBILE]. Mandato: [DRY-RUN oppure APPLICAZIONE AUTORIZZATA E PERIMETRO].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Confrontare o aggiornare governance e personalizzazioni v3 in destinazioni definite.
- Preferisci altro quando: Non è una migrazione ad Astralis 4; per un progetto senza governance scegliere inizializzazione.
- Materiali minimi: sorgente_aggiornamento_v3, destinazioni, baseline_o_limite_dichiarato. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Voglio allineare questi progetti alla governance aggiornata.».
- Passo collegato: `AST-P-INIT-PROGETTO` — Per i candidati onboarding senza governance esistente.

La [procedura condivisa v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Aggiornamento integrativo dell'ecosistema (AST-P-UPDATE-ECOSISTEMA)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Valutare e applicare un aggiornamento preservando personalizzazioni, conoscenza locale e possibilità di recupero.

INPUT
Sorgente aggiornamento: [SORGENTE]. Destinazioni: [HUB/PROGETTI]. Baseline: [VERSIONE O NON DISPONIBILE]. Mandato: [DRY-RUN oppure APPLICAZIONE AUTORIZZATA E PERIMETRO].

PERIMETRO OPERATIVO
Il dry-run non modifica file. Aggiorna solo le destinazioni autorizzate; nessuna migrazione implicita fra Astralis 3 e 4. Accessi remoti ed effetti esterni seguono il mandato della sessione.

PROCEDURA
1. Leggi la governance e identifica versione della sorgente e delle destinazioni. Se le fonti discordano, presenta il conflitto senza scegliere arbitrariamente.
2. Inventaria solo i progetti nel perimetro. Classifica: da aggiornare, già allineato, candidato onboarding oppure stato non determinabile.
3. Confronta contenuti comuni, personalizzazioni e knowledge locale. Quando esiste una baseline affidabile usa il confronto tra baseline, contenuto attuale e nuova sorgente; in sua assenza proteggi gli elementi sconosciuti.
4. Produci una proposta con file coinvolti, conflitti, backup, ordine degli interventi, verifiche e recupero. Non eseguire lo script di aggiornamento prima di averne letto effetti e destinazioni.
5. Se autorizzato, effettua backup e integrazione conservativa. Aggiorna i soli router personali attivi e preserva i documenti upstream, la storia e le isole personalizzate.
6. Esegui i controlli pertinenti consentiti. Riporta separatamente aggiornamento applicato, conformità documentale e collaudo ancora aperto.

RISULTATO ATTESO
Triage dei progetti, differenze e conflitti, proposta o ricevuta di applicazione, backup disponibili, controlli e residui.

CRITERI DI VERIFICA
Ogni file modificato ha destinazione esplicita; personalizzazioni preservate; versioni e link coerenti; recupero possibile. Nessun aggiornamento dichiarato per progetti non controllati.

LIMITI E ARRESTO
Baseline assente, conflitti o destinazioni ambigue impediscono la fusione automatica del solo elemento coinvolto. Non cancellare il vecchio hub.
```

## Esempio di attivazione

Prepara un dry-run dell'aggiornamento per questi due progetti. Individua differenze e personalizzazioni, senza modificare file.

## Raccordo futuro con Astralis 4

La futura installazione affiancata e gli overlay richiedono il runtime adottato; questo prompt non implementa da solo Astralis Home.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
