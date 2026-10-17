---
schema: 2
id: "AST-P-ANALISI-INGEGNERISTICA"
title: "Analisi ingegneristica e architetturale"
revision: "1.2.0"
status: "adattato_verificato_documentalmente"
category: "03_progettazione_e_pianificazione"
protocols: [1, 12]
domains: ["software", "addon_nvda", "utility", "giochi"]
mode: "consultiva"
requires: ["lettura_materiali", "lettura_file_opzionale"]
sources: ["Prompt-Ingegnere-Software.md"]
selection: {"intents": ["progettare_soluzione_tecnica"], "use_when": ["Valutare una soluzione software, responsabilità, contratti e alternative tecniche."], "avoid_when": ["Non è l’esecuzione di un piano né la validazione indipendente di un diff concluso."], "materials": ["requisito_tecnico", "stack_o_fonti", "vincoli"], "examples": ["Quale architettura conviene per questa funzione?"], "related": [{"id": "AST-P-PIANIFICAZIONE", "when": "Per convertire la decisione tecnica in passi implementativi."}]}
---

# Analisi ingegneristica e architetturale

## Scopo e condizioni d'uso

Proporre una soluzione tecnica aderente a requisiti, architettura e capacità effettive del progetto.

Identificativo: `AST-P-ANALISI-INGEGNERISTICA`. Revisione del prompt: `1.2.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-04; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: 1, 12.
- Domini: software, addon_nvda, utility, giochi.
- Modalità: `consultiva`.
- Capacità richieste: lettura_materiali, lettura_file_opzionale.
- Input della sessione: Requisito: [PROBLEMA]. Stack e fonti: [CONTESTO]. Vincoli: [COMPATIBILITÀ, ACCESSIBILITÀ, COSTO]. Output richiesto: [ANALISI / PROPOSTA / ESEMPIO].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Valutare una soluzione software, responsabilità, contratti e alternative tecniche.
- Preferisci altro quando: Non è l’esecuzione di un piano né la validazione indipendente di un diff concluso.
- Materiali minimi: requisito_tecnico, stack_o_fonti, vincoli. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Quale architettura conviene per questa funzione?».
- Passo collegato: `AST-P-PIANIFICAZIONE` — Per convertire la decisione tecnica in passi implementativi.

La [procedura condivisa v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Analisi ingegneristica e architetturale (AST-P-ANALISI-INGEGNERISTICA)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Proporre una soluzione tecnica aderente a requisiti, architettura e capacità effettive del progetto.

INPUT
Requisito: [PROBLEMA]. Stack e fonti: [CONTESTO]. Vincoli: [COMPATIBILITÀ, ACCESSIBILITÀ, COSTO]. Output richiesto: [ANALISI / PROPOSTA / ESEMPIO].

PERIMETRO OPERATIVO
Consulenza tecnica. Esempi o patch concettuali in chat non autorizzano la loro applicazione. Non imporre nuove librerie o cambi di architettura.

PROCEDURA
1. Leggi contesto, requisiti e componenti coinvolti. Se mancano dati essenziali, identifica la lacuna; recupera ciò che è disponibile prima di chiedere.
2. Verifica prima se configurazione, funzionalità o strumenti esistenti risolvono il bisogno. Preferisci riuso e modifica locale a nuove astrazioni.
3. Definisci responsabilità, contratti, ingressi, uscite, errori, dipendenze e invarianti per le parti che cambiano. Considera compatibilità e accessibilità reale.
4. Confronta alternative pertinenti e proporziona la soluzione. Non imporre a un'attività semplice una progettazione enterprise o cancelli specifici del gaming.
5. Se presenti codice, usa API realmente disponibili o marca esplicitamente lo pseudocodice. Distingui esempio dimostrativo da codice eseguito e verificato.
6. Riporta complessità e misure solo con ipotesi o evidenze; una stima non è un benchmark. Definisci controlli utili e rischio residuo.
7. Definisci domini, proprietari dello stato e contratti stabili; separa dominio, UI e infrastruttura e verifica dipendenze, isolamento e integrazione. Usa orchestrazione per dominio quando necessaria, senza imporre un hub globale o promettere scalabilità non misurata.

RISULTATO ATTESO
Analisi del requisito, soluzione proposta, valutazione di compatibilità e rischi, alternative realmente utili e criterio di verifica.

CRITERI DI VERIFICA
Soluzione coerente con l'architettura; responsabilità chiare; dipendenze verificabili; prestazioni stimate distinte da quelle misurate; nessuna promessa di codice certificato senza controlli.

LIMITI E ARRESTO
Se versione o API sono incerte, verifica la fonte quando disponibile oppure segnala il limite. Non inventare firme, librerie o metriche.
```

## Esempio di attivazione

Valuta come aggiungere questa funzione riutilizzando i componenti esistenti. Proponi contratti e verifiche senza modificare sorgenti.

## Raccordo futuro con Astralis 4

Procedure specialistiche potranno essere richiamate tramite skill pertinenti; il prompt resta una richiesta di progettazione.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
