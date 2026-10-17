---
schema: 2
id: "AST-P-VALIDAZIONE-STRATEGIA"
title: "Validazione di una strategia"
revision: "1.1.0"
status: "adattato_verificato_documentalmente"
category: "04_revisione_e_validazione"
protocols: [1, 2, 12]
domains: ["trasversale"]
mode: "consultiva"
requires: ["lettura_materiali", "lettura_file_opzionale"]
sources: ["prompt-strategy--validator.md"]
selection: {"intents": ["validare_strategia"], "use_when": ["Verificare premesse e approccio generale di una strategia prima del piano dettagliato."], "avoid_when": ["Per sequenza implementativa, fixture e criteri concreti scegliere validazione piano; il verdetto non avvia implementazione."], "materials": ["strategia", "obiettivi", "fonti_o_baseline"], "examples": ["Questa strategia risolve davvero il problema?"], "related": [{"id": "AST-P-PIANIFICAZIONE", "when": "Dopo una strategia valida, per formalizzare il piano."}]}
---

# Validazione di una strategia

## Scopo e condizioni d'uso

Verificare che una strategia affronti il problema corretto e abbia un percorso praticabile senza implementarla.

Identificativo: `AST-P-VALIDAZIONE-STRATEGIA`. Revisione del prompt: `1.1.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-03; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: 1, 2, 12.
- Domini: trasversale.
- Modalità: `consultiva`.
- Capacità richieste: lettura_materiali, lettura_file_opzionale.
- Input della sessione: Strategia: [TESTO/PERCORSO]. Obiettivi: [OBIETTIVI]. Baseline e invarianti: [FONTI]. Perimetro: [AMBITO].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Verificare premesse e approccio generale di una strategia prima del piano dettagliato.
- Preferisci altro quando: Per sequenza implementativa, fixture e criteri concreti scegliere validazione piano; il verdetto non avvia implementazione.
- Materiali minimi: strategia, obiettivi, fonti_o_baseline. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Questa strategia risolve davvero il problema?».
- Passo collegato: `AST-P-PIANIFICAZIONE` — Dopo una strategia valida, per formalizzare il piano.

La [procedura condivisa v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Validazione di una strategia (AST-P-VALIDAZIONE-STRATEGIA)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Verificare che una strategia affronti il problema corretto e abbia un percorso praticabile senza implementarla.

INPUT
Strategia: [TESTO/PERCORSO]. Obiettivi: [OBIETTIVI]. Baseline e invarianti: [FONTI]. Perimetro: [AMBITO].

PERIMETRO OPERATIVO
Validazione in lettura. Puoi proporre rettifiche in chat; il verdetto non autorizza scritture, correzioni della strategia su file né implementazione.

PROCEDURA
1. Leggi la strategia e verifica le premesse contro le fonti effettive. Distingui problema dimostrato e ipotesi; controlla l'esistenza dei componenti citati.
2. Verifica efficacia, necessità degli interventi e responsabilità. Valuta prima alternative più semplici tramite configurazione, strumenti o meccanismi esistenti.
3. Esamina dipendenze, ordine, impatti, preservazione delle funzioni stabili, errori e recupero. Applica i sette assi Astralis: validità, efficacia, coerenza, completezza, precisione, affidabilità/prestazioni, assenza di regressioni.
4. Simula scenario ordinario, alternative e condizioni limite. Segnala quali risultati sono soltanto teorici e quali poggiano su evidenze già disponibili.
5. Per ogni lacuna proponi la rettifica minima indicando sezione, motivazione ed effetto. Gli snippet concettuali sono opzionali, limitati al necessario e non certificati come applicati.
6. Emetti VALIDATA, VALIDATA CON RETTIFICHE, DA RIVEDERE oppure NON VERIFICABILE. Indica condizioni per passare alla pianificazione o all'esecuzione; non avviare la fase successiva.

RISULTATO ATTESO
Verdetto, premesse confermate o dubbie, lacune prioritarie, rettifiche minime, ordine delle dipendenze e verifiche mancanti.

CRITERI DI VERIFICA
Verdetto sostenuto da fonti; nessuna autoautorizzazione; strategia distinta dal piano implementativo; simulazione non presentata come test eseguito.

LIMITI E ARRESTO
Se manca una premessa decisiva, usa NON VERIFICABILE per quella parte. Una strategia formalmente coerente può restare empiricamente non convalidata.
```

## Esempio di attivazione

Valida questa strategia rispetto alle fonti e agli invarianti indicati. Proponi rettifiche ma non modificare documenti né codice.

## Raccordo futuro con Astralis 4

Possibile raccordo con astralis-validation e astralis-decision-matrix; contratti del Lab da verificare.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
