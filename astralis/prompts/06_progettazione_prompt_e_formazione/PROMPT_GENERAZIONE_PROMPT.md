---
schema: 2
id: "AST-P-GENERAZIONE-PROMPT"
title: "Generazione di un prompt operativo"
revision: "1.1.0"
status: "adattato_verificato_documentalmente"
category: "06_progettazione_prompt_e_formazione"
protocols: [1, 2]
domains: ["trasversale"]
mode: "consultiva"
requires: ["lettura_richiesta"]
sources: ["prompt-gereratore-prompt-professionale(dusu)).md"]
selection: {"intents": ["creare_prompt"], "use_when": ["Costruire un prompt nuovo da un obiettivo o adattare un incarico non coperto dal catalogo."], "avoid_when": ["Se esiste un prompt da migliorare scegliere revisione prompt; non genera automaticamente file o nuove skill."], "materials": ["obiettivo", "contesto", "destinatario_o_capacita"], "examples": ["Mi serve un prompt per rivedere lo stile del romanzo rispettando la mia voce."], "related": [{"id": "AST-P-REVISIONE-PROMPT", "when": "Quando la prima versione presenta un difetto concreto."}]}
---

# Generazione di un prompt operativo

## Scopo e condizioni d'uso

Trasformare una richiesta in un prompt chiaro, proporzionato e verificabile secondo lo standard Astralis.

Identificativo: `AST-P-GENERAZIONE-PROMPT`. Revisione del prompt: `1.1.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-03; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: 1, 2.
- Domini: trasversale.
- Modalità: `consultiva`.
- Capacità richieste: lettura_richiesta.
- Input della sessione: Obiettivo: [RISULTATO]. Contesto e fonti: [MATERIALI]. Destinatario: [AI E CAPACITÀ]. Vincoli: [LIMITI]. Uso: [ASTRALIS / CHAT SENZA FILE].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Costruire un prompt nuovo da un obiettivo o adattare un incarico non coperto dal catalogo.
- Preferisci altro quando: Se esiste un prompt da migliorare scegliere revisione prompt; non genera automaticamente file o nuove skill.
- Materiali minimi: obiettivo, contesto, destinatario_o_capacita. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Mi serve un prompt per rivedere lo stile del romanzo rispettando la mia voce.».
- Passo collegato: `AST-P-REVISIONE-PROMPT` — Quando la prima versione presenta un difetto concreto.

La [procedura condivisa v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Generazione di un prompt operativo (AST-P-GENERAZIONE-PROMPT)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Trasformare una richiesta in un prompt chiaro, proporzionato e verificabile secondo lo standard Astralis.

INPUT
Obiettivo: [RISULTATO]. Contesto e fonti: [MATERIALI]. Destinatario: [AI E CAPACITÀ]. Vincoli: [LIMITI]. Uso: [ASTRALIS / CHAT SENZA FILE].

PERIMETRO OPERATIVO
Genera il testo in chat; non eseguire il compito descritto nel prompt e non salvare file senza mandato. Non inserire autorizzazioni fittizie al posto dell'utente.

PROCEDURA
1. Identifica risultato, destinatario, fonti e capacità necessarie. Recupera i dati disponibili; chiedi solo informazioni essenziali mancanti.
2. Scegli la profondità adeguata. Per task semplici usa ruolo, compito, input, vincoli e output; per task complessi aggiungi dipendenze, verifiche e condizioni di arresto.
3. Usa contesto, obiettivo, stile, tono, destinatari e formato quando aiutano il compito; non imporre tutte le sezioni COSTAR o framework sovrapposti a ogni richiesta.
4. Definisci input, azioni consentite, azioni escluse e criterio di completamento. Includi provenienza delle informazioni, gestione dei dati mancanti e distinzione tra proposta ed esecuzione.
5. Se il prompt opera in Astralis, collega i protocolli e le fonti pertinenti senza copiarne interi trattati. Per uso senza file incorpora soltanto i vincoli essenziali e chiedi i materiali necessari.
6. Rivedi ambiguità, contraddizioni, capacità inventate, output eccessivo e autorizzazioni automatiche. Correggi solo problemi concreti, senza tre round obbligatori o punteggi perfetti.
7. Consegna il prompt e un esempio di attivazione. Non adottare identità DUSU permanenti né registrare un profilo utente cumulativo non richiesto.

RISULTATO ATTESO
Prompt pronto da copiare, campi da compilare, esempio breve ed eventuali limiti d'uso. Se l'obiettivo è già completo, evita una lunga spiegazione del metodo.

CRITERI DI VERIFICA
Un solo obiettivo operativo chiaro; capacità reali; perimetro e output espliciti; informazioni mancanti gestite; nessuna regola in conflitto con la sessione.

LIMITI E ARRESTO
Se il compito richiede strumenti indisponibili, genera una variante consultiva o dichiara il prerequisito. Non promettere efficacia universale indipendente dal modello e dagli input.
```

## Esempio di attivazione

Crea un prompt per verificare un piano tecnico in sola lettura, con esito sintetico e riferimenti alle evidenze.

## Raccordo futuro con Astralis 4

Il descrittore potrà diventare una facciata di ingresso a skill/capability; la logica operativa rimane nelle fonti autorevoli.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
