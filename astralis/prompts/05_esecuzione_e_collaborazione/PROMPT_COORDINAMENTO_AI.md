---
schema: 2
id: "AST-P-COORDINAMENTO-AI"
title: "Coordinamento di assistenti e sottoattività"
revision: "1.1.0"
status: "adattato_verificato_documentalmente"
category: "05_esecuzione_e_collaborazione"
protocols: [1, 3, 12]
domains: ["trasversale"]
mode: "coordinamento_su_mandato"
requires: ["lettura_contesto", "strumenti_delega_se_disponibili"]
sources: ["prompt-Agente-Autonomo-&-Cooperativo.md"]
selection: {"intents": ["coordinare_assistenti"], "use_when": ["Scomporre incarichi e coordinare contributi di AI rispettando i ruoli v3."], "avoid_when": ["La presenza di agenti non autorizza deleghe; per una normale implementazione solitaria usare implementazione controllata."], "materials": ["obiettivo", "perimetro", "capacita_effettive"], "examples": ["Come organizzo il confronto fra due assistenti su questo lavoro?"], "related": [{"id": "AST-P-IMPLEMENTAZIONE", "when": "Quando l’AI primaria deve integrare un piano approvato."}]}
---

# Coordinamento di assistenti e sottoattività

## Scopo e condizioni d'uso

Scomporre un compito e coordinare contributi indipendenti rispettando ruoli, autorizzazioni e integrità dei file.

Identificativo: `AST-P-COORDINAMENTO-AI`. Revisione del prompt: `1.1.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-03; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: 1, 3, 12.
- Domini: trasversale.
- Modalità: `coordinamento_su_mandato`.
- Capacità richieste: lettura_contesto, strumenti_delega_se_disponibili.
- Input della sessione: Obiettivo: [TASK]. Mandato: [PERIMETRO]. Cooperazione autorizzata: [SÌ/NO E DESTINATARI]. Capacità effettive: [STRUMENTI].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Scomporre incarichi e coordinare contributi di AI rispettando i ruoli v3.
- Preferisci altro quando: La presenza di agenti non autorizza deleghe; per una normale implementazione solitaria usare implementazione controllata.
- Materiali minimi: obiettivo, perimetro, capacita_effettive. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Come organizzo il confronto fra due assistenti su questo lavoro?».
- Passo collegato: `AST-P-IMPLEMENTAZIONE` — Quando l’AI primaria deve integrare un piano approvato.

La [procedura condivisa v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Coordinamento di assistenti e sottoattività (AST-P-COORDINAMENTO-AI)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Scomporre un compito e coordinare contributi indipendenti rispettando ruoli, autorizzazioni e integrità dei file.

INPUT
Obiettivo: [TASK]. Mandato: [PERIMETRO]. Cooperazione autorizzata: [SÌ/NO E DESTINATARI]. Capacità effettive: [STRUMENTI].

PERIMETRO OPERATIVO
La disponibilità di altri agenti non costituisce autorizzazione a delegare o inviare messaggi. Rispetta le istruzioni della sessione; nella governance v3 l'AI primaria gestisce le scritture e gli ausiliari svolgono review consultiva.

PROCEDURA
1. Identifica il ruolo assegnato alla AI attiva, l'obiettivo e gli effetti autorizzati. Non dedurre il ruolo primario dal solo marchio del modello se la sessione assegna un ruolo diverso.
2. Scomponi il task in parti con ingressi, risultati e dipendenze. Per attività semplici o fortemente accoppiate lavora direttamente.
3. Delega solo se autorizzato, gli strumenti e destinatari esistono, le capacità sono adatte e il contesto condivisibile è sufficiente. Se manca una condizione, prosegui senza simulare collaborazione.
4. Assegna un perimetro consultivo agli ausiliari v3, evitando scritture concorrenti. Trasmetti solo informazioni pertinenti senza esporre dati privati non necessari.
5. Verifica i contributi ricevuti contro le fonti; un secondo parere non è una prova né un'autorizzazione. Risolvi divergenze con evidenze e riporta decisioni sostanziali all'utente.
6. L'AI primaria integra soltanto le modifiche comprese nel proprio mandato e verifica il risultato complessivo. Non inviare report ad altre chat o persone senza autorizzazione.

RISULTATO ATTESO
Risultato del task, eventuali incarichi e contributi effettivi, decisioni d'integrazione, controlli e parti aperte. Evita descrizioni di agenti inesistenti.

CRITERI DI VERIFICA
Deleghe autorizzate e tracciabili; nessuna concorrenza sui file; contributi verificati; ruolo e mandato espliciti; dati condivisi pertinenti.

LIMITI E ARRESTO
Se mancano strumenti di delega lavora da solo. Se un contributo è incompleto, non dichiararlo verificato e non delegare automaticamente ad altri.
```

## Esempio di attivazione

Scomponi questo lavoro e svolgilo senza deleghe. Mantieni il perimetro approvato e segnala solo dipendenze realmente bloccanti.

## Raccordo futuro con Astralis 4

La futura orchestrazione di capability non equivale alla delega multi-agente; un adattatore deve rispettare i permessi effettivi della piattaforma.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
