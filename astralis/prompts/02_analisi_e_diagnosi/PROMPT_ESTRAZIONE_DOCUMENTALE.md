---
schema: 2
id: "AST-P-ESTRAZIONE-DOCUMENTALE"
title: "Estrazione documentale con provenienza"
revision: "1.1.0"
status: "adattato_verificato_documentalmente"
category: "02_analisi_e_diagnosi"
protocols: [2]
domains: ["trasversale"]
mode: "consultiva"
requires: ["lettura_documenti"]
sources: ["prompt-Honesty-Extractor.md"]
selection: {"intents": ["estrarre_dati"], "use_when": ["Estrarre campi da fonti fornite con provenienza e gestione delle lacune."], "avoid_when": ["Non serve a completare dati mancanti da Internet o a diagnosticare sessioni software."], "materials": ["documenti", "campi_richiesti"], "examples": ["Quale prompt uso per estrarre importi e scadenze da questi documenti?"], "related": [{"id": "AST-P-RICHIESTA-UNIVERSALE", "when": "Per una semplice sintesi testuale che non richiede estrazione di campi."}]}
---

# Estrazione documentale con provenienza

## Scopo e condizioni d'uso

Estrarre campi da documenti distinguendo dati espliciti, valori mancanti e derivazioni autorizzate.

Identificativo: `AST-P-ESTRAZIONE-DOCUMENTALE`. Revisione del prompt: `1.1.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-03; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: 2.
- Domini: trasversale.
- Modalità: `consultiva`.
- Capacità richieste: lettura_documenti.
- Input della sessione: Fonti: [DOCUMENTI]. Campi: [ELENCO]. Modalità: [LETTERALE, predefinita / DERIVAZIONI DOCUMENTATE]. Formato: [ELENCO / JSON / CSV RICHIESTO].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Estrarre campi da fonti fornite con provenienza e gestione delle lacune.
- Preferisci altro quando: Non serve a completare dati mancanti da Internet o a diagnosticare sessioni software.
- Materiali minimi: documenti, campi_richiesti. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Quale prompt uso per estrarre importi e scadenze da questi documenti?».
- Passo collegato: `AST-P-RICHIESTA-UNIVERSALE` — Per una semplice sintesi testuale che non richiede estrazione di campi.

La [procedura condivisa v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Estrazione documentale con provenienza (AST-P-ESTRAZIONE-DOCUMENTALE)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Estrarre campi da documenti distinguendo dati espliciti, valori mancanti e derivazioni autorizzate.

INPUT
Fonti: [DOCUMENTI]. Campi: [ELENCO]. Modalità: [LETTERALE, predefinita / DERIVAZIONI DOCUMENTATE]. Formato: [ELENCO / JSON / CSV RICHIESTO].

PERIMETRO OPERATIVO
Usa soltanto le fonti fornite. Nessuna ricerca esterna, nessuna integrazione da conoscenza generale e nessuna scrittura di file senza mandato.

PROCEDURA
1. Verifica leggibilità, versione e perimetro dei documenti. Identifica pagina, sezione o posizione dei passaggi rilevanti.
2. In modalità LETTERALE estrai solo valori esplicitamente dichiarati. Se mancanti, ambigui o contraddittori, usa NON DISPONIBILE con motivo; in un formato strutturato usa null e un campo stato, senza confonderlo con zero o stringa vuota.
3. In modalità DERIVAZIONI DOCUMENTATE ammetti soltanto calcoli o deduzioni riproducibili dai dati presenti. Etichetta il risultato DERIVATO e indica dati di origine, formula, unità e arrotondamento. Non colmare una lacuna con una stima non richiesta.
4. Per ogni campo riporta valore, stato ESTRATTO/DERIVATO/NON DISPONIBILE/CONFLITTO e riferimento alla fonte. Mantieni distinti campi provenienti da documenti diversi.
5. Controlla completezza dei campi, citazioni, unità e conflitti. Segnala letture dubbie o limiti OCR. Non assegnare percentuali di fiducia arbitrarie.

RISULTATO ATTESO
Elenco lineare per campo: valore, stato, fonte, eventuale derivazione e motivo della lacuna. Audit finale limitato a conflitti e informazioni non determinabili. Formati tabellari solo se richiesti.

CRITERI DI VERIFICA
Ogni valore è rintracciabile; nessuna inferenza nella modalità letterale; ogni calcolo è riproducibile; tutti i campi richiesti compaiono anche se non disponibili.

LIMITI E ARRESTO
Se il documento è illeggibile, non ricostruirne il contenuto. Se la data o l'unità sono ambigue, conserva l'ambiguità.
```

## Esempio di attivazione

Estrai da questi documenti nome, importo e scadenza in modalità letterale, con riferimento alla fonte per ogni campo.

## Raccordo futuro con Astralis 4

Provenienza e stato sconosciuto restano parte del risultato; l'eventuale registrazione nel Data Hub è un'operazione separata.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
