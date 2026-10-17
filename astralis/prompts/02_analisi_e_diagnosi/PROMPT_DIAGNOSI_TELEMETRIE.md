---
schema: 2
id: "AST-P-DIAGNOSI-TELEMETRIE"
title: "Diagnosi forense di log e telemetrie"
revision: "1.2.0"
status: "adattato_verificato_documentalmente"
category: "02_analisi_e_diagnosi"
protocols: [4, 10, 12]
domains: ["trasversale"]
mode: "consultiva"
requires: ["lettura_log", "lettura_file", "git_opzionale"]
sources: ["analizzatore di telemetrie.md"]
selection: {"intents": ["diagnosticare_sessione"], "use_when": ["Ricostruire un errore o comportamento già osservato partendo da log e telemetrie."], "avoid_when": ["Per verificare codice contro un piano usare validazione implementazione; per interagire col gioco usare collaudo gameplay."], "materials": ["log_o_telemetrie", "sessioni", "comportamento_atteso"], "examples": ["Ho i log delle ultime due sessioni fallite e cerco la causa."], "related": [{"id": "AST-P-PIANIFICAZIONE", "when": "Dopo la diagnosi, per definire una correzione verificabile."}]}
---

# Diagnosi forense di log e telemetrie

## Scopo e condizioni d'uso

Ricostruire il comportamento osservato e individuare cause radice prima di progettare una correzione.

Identificativo: `AST-P-DIAGNOSI-TELEMETRIE`. Revisione del prompt: `1.2.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-04; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: 4, 10, 12.
- Domini: trasversale.
- Modalità: `consultiva`.
- Capacità richieste: lettura_log, lettura_file, git_opzionale.
- Input della sessione: Sintomo: [SINTOMO]. Sessioni: [INTERVALLO/ID]. Fonti: [LOG, TELEMETRIE, SNAPSHOT]. Atteso e baseline: [RIFERIMENTI].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Ricostruire un errore o comportamento già osservato partendo da log e telemetrie.
- Preferisci altro quando: Per verificare codice contro un piano usare validazione implementazione; per interagire col gioco usare collaudo gameplay.
- Materiali minimi: log_o_telemetrie, sessioni, comportamento_atteso. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Ho i log delle ultime due sessioni fallite e cerco la causa.».
- Passo collegato: `AST-P-PIANIFICAZIONE` — Dopo la diagnosi, per definire una correzione verificabile.

La [procedura condivisa v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Diagnosi forense di log e telemetrie (AST-P-DIAGNOSI-TELEMETRIE)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Ricostruire il comportamento osservato e individuare cause radice prima di progettare una correzione.

INPUT
Sintomo: [SINTOMO]. Sessioni: [INTERVALLO/ID]. Fonti: [LOG, TELEMETRIE, SNAPSHOT]. Atteso e baseline: [RIFERIMENTI].

PERIMETRO OPERATIVO
Diagnosi in sola lettura. Non riprodurre il problema nell'ambiente reale, non alterare log, salvataggi, configurazioni o sorgenti. Un rapporto su file richiede un mandato documentale.

PROCEDURA
1. Identifica progetto, sessioni e periodo effettivamente documentato. Usa identificativi e timestamp; segnala differenze di fuso, log mancanti o rotazioni che limitano la ricostruzione.
2. Parti dai dati, poi dal codice. Correlali per sessione, input, decisioni, stati, errore, recupero e risultato finale. Usa snapshot e dati spaziali solo se il dominio li prevede.
3. Per ogni evento anomalo ricostruisci prima, evento e dopo. Confronta atteso e osservato; non confondere correlazione temporale con causalità.
4. Leggi il flusso sorgente necessario a spiegare l'evento, incluse guardie a monte, ciclo di vita, dipendenze e fallback. Evita un audit indiscriminato.
5. Per ogni anomalia registra identificativo, osservato, atteso, evidenza, componente, causa dimostrata o ipotesi, impatto e prova ancora necessaria. Distingui problema preesistente, regressione dimostrata e rischio plausibile.
6. Verifica cause comuni e proponi intervento minimo con controllo causale pertinente. Non aggirare un gate fallito forzando gli eventi a valle.
7. Esprimi il livello di evidenza raggiunto secondo la tassonomia Astralis. Una telemetria osservata non è un collaudo empirico completato.
8. Traccia ingresso, dispatcher, gestori ed esito e identifica proprietario e invariante violata sulla base di prove. Se la causa è ignota mantieni ipotesi separate; correggere nel gestore finale è legittimo se possiede il contratto, senza bypass o timeout arbitrari.

RISULTATO ATTESO
Perimetro e sessioni; anomalie prioritarie con riferimenti e stato dell'evidenza; cause o ipotesi; regressioni; proposta correttiva e verifiche mancanti. Timeline analizzata cronologicamente; eventuali aggiornamenti del report in ordine inverso.

CRITERI DI VERIFICA
Ogni diagnosi è collegata a dati reali; sessioni separate; cause non confuse con sintomi; test proposti distinti da quelli eseguiti; limiti espliciti.

LIMITI E ARRESTO
Se manca la via di comunicazione o una guardia respinge l'operazione, descrivi il gate prima di giudicare il componente a valle. Non dichiarare la causa confermata senza evidenza sufficiente.
```

## Esempio di attivazione

Analizza le ultime due sessioni indicate nei log. Ricostruisci l'errore e proponi il controllo minimo per confermare la causa; non applicare fix.

## Raccordo futuro con Astralis 4

Possibile raccordo con astralis-deep-reasoner e dati di percorso del Lab, senza presumere che i dati siano aggiornati.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
