---
schema: 2
id: "AST-P-PIANIFICAZIONE"
title: "Pianificazione proporzionata di un'attività"
revision: "1.2.0"
status: "adattato_verificato_documentalmente"
category: "03_progettazione_e_pianificazione"
protocols: [1, 2]
domains: ["trasversale"]
mode: "consultiva"
requires: ["lettura_materiali"]
sources: ["prompt-Problem-Solver-a-4-Fasi.md"]
selection: {"intents": ["pianificare_attivita", "redigere_piano_tecnico"], "use_when": ["Definire attività, ordine, dipendenze e criteri prima di agire."], "avoid_when": ["Se il piano esiste e si vuole verificarlo scegliere validazione piano; se è approvato e si vuole realizzarlo scegliere implementazione."], "materials": ["attivita", "obiettivo", "vincoli"], "examples": ["Voglio un piano per riorganizzare questa documentazione."], "related": [{"id": "AST-P-VALIDAZIONE-PIANO", "when": "Quando la pianificazione produce un piano tecnico da verificare."}]}
---

# Pianificazione proporzionata di un'attività

## Scopo e condizioni d'uso

Trasformare una richiesta in un piano eseguibile con dipendenze, verifiche e perimetro chiari.

Identificativo: `AST-P-PIANIFICAZIONE`. Revisione del prompt: `1.2.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-04; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: 1, 2.
- Domini: trasversale.
- Modalità: `consultiva`.
- Capacità richieste: lettura_materiali.
- Input della sessione: Attività: [RICHIESTA]. Obiettivo: [RISULTATO]. Vincoli e fonti: [CONTESTO]. Profondità: [AUTOMATICA / BREVE / DETTAGLIATA].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Definire attività, ordine, dipendenze e criteri prima di agire.
- Preferisci altro quando: Se il piano esiste e si vuole verificarlo scegliere validazione piano; se è approvato e si vuole realizzarlo scegliere implementazione.
- Materiali minimi: attivita, obiettivo, vincoli. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Voglio un piano per riorganizzare questa documentazione.».
- Passo collegato: `AST-P-VALIDAZIONE-PIANO` — Quando la pianificazione produce un piano tecnico da verificare.

La [procedura condivisa v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Pianificazione proporzionata di un'attività (AST-P-PIANIFICAZIONE)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Trasformare una richiesta in un piano eseguibile con dipendenze, verifiche e perimetro chiari.

INPUT
Attività: [RICHIESTA]. Obiettivo: [RISULTATO]. Vincoli e fonti: [CONTESTO]. Profondità: [AUTOMATICA / BREVE / DETTAGLIATA].

PERIMETRO OPERATIVO
Definisci il piano in chat. Non avviare l'attività né salvare il documento senza mandato. Non richiedere approvazioni dopo ogni ordinaria fase analitica.

PROCEDURA
1. Comprendi obiettivo e criteri di successo. Recupera il contesto disponibile; chiedi soltanto chiarimenti che incidono su risultato, perimetro o autorizzazione.
2. Proponi un approccio con passaggi ordinati, responsabilità e dipendenze. Per attività semplici usa un piano breve; per attività complesse separa decisioni strategiche e passi implementativi.
3. Confronta l'approccio con i vincoli e segnala assunzioni, rischi reali e alternative utili. Non inventare un numero minimo di rischi o passaggi.
4. Definisci per ogni fase ingresso, azione, risultato e controllo di accettazione. Specifica test, build, deploy e documentazione previsti e gli effetti attesi.
5. Verifica gli assi e scenari Astralis pertinenti. Se il piano riguarda software, usa Testata Universale Compatta e template tecnico proporzionato, origine del requisito, invarianti, contratti D/S e verifica per contratto; separa stato documento, stato lavoro e gate 1A/1B, senza deploy o pubblicazione impliciti; per scrittura conserva voce autoriale, destinatari e continuità.
6. Presenta il piano con stati [ ] per le attività future. Distingui validazione teorica, implementazione e collaudo; la proposta non costituisce autorizzazione a eseguire.
7. Per ogni unità pertinente esplicita responsabilità, confini, dipendenze, impatto sui chiamanti ed evidenza prevista. Nei fix associa causa dimostrata e invariante al componente responsabile; nelle nuove funzionalità non inventare una causa.

RISULTATO ATTESO
Obiettivo, perimetro, fonti, sequenza con dipendenze, criteri di accettazione, rischi e assunzioni, operazioni da autorizzare per l'esecuzione.

CRITERI DI VERIFICA
Ogni fase ha un risultato verificabile; il piano risponde all'obiettivo; responsabilità e dipendenze sono chiare; nessuna spunta preventiva.

LIMITI E ARRESTO
Se un requisito essenziale manca, completa le parti indipendenti e segnala la decisione necessaria. Non imporre un questionario già risolto dal contesto.
```

## Esempio di attivazione

Prepara un piano per riorganizzare questi documenti, preservando riferimenti e storia. Presenta prima il piano senza applicarlo.

## Raccordo futuro con Astralis 4

Possibile raccordo con astralis-validation e project_state, mantenendo distinta la proposta dall'aggiornamento dello stato.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
