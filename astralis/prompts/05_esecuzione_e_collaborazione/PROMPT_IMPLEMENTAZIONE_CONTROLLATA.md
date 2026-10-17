---
schema: 2
id: "AST-P-IMPLEMENTAZIONE"
title: "Implementazione controllata e autocorrezione"
revision: "1.2.0"
status: "adattato_verificato_documentalmente"
category: "05_esecuzione_e_collaborazione"
protocols: [3, 5]
domains: ["software", "addon_nvda", "utility", "giochi"]
mode: "esecuzione_su_mandato"
requires: ["lettura_file", "scrittura_file", "runner_se_autorizzato"]
sources: ["implementatore  - protocollo Controlled Im.md"]
selection: {"intents": ["implementare_piano"], "use_when": ["Realizzare un piano approvato entro un mandato con effetti definiti."], "avoid_when": ["Non usarlo per un semplice consiglio, una review o un piano ancora da validare. Nessuna esecuzione senza mandato."], "materials": ["piano_approvato", "perimetro", "mandato_operativo"], "examples": ["Il piano è approvato: voglio affidarne l’implementazione all’AI."], "related": [{"id": "AST-P-VALIDAZIONE-IMPLEMENTAZIONE", "when": "Dopo il lavoro, per una verifica indipendente."}]}
---

# Implementazione controllata e autocorrezione

## Scopo e condizioni d'uso

Realizzare un piano approvato con modifiche incrementali, verifiche pertinenti e autonomia entro il perimetro.

Identificativo: `AST-P-IMPLEMENTAZIONE`. Revisione del prompt: `1.2.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-04; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: 3, 5.
- Domini: software, addon_nvda, utility, giochi.
- Modalità: `esecuzione_su_mandato`.
- Capacità richieste: lettura_file, scrittura_file, runner_se_autorizzato.
- Input della sessione: Piano approvato: [PIANO]. Perimetro: [RADICE/FILE]. Mandato operativo: [MODIFICHE, TEST, BUILD, DEPLOY, DOCUMENTAZIONE CONSENTITI]. Funzioni protette: [ELENCO].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Realizzare un piano approvato entro un mandato con effetti definiti.
- Preferisci altro quando: Non usarlo per un semplice consiglio, una review o un piano ancora da validare. Nessuna esecuzione senza mandato.
- Materiali minimi: piano_approvato, perimetro, mandato_operativo. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Il piano è approvato: voglio affidarne l’implementazione all’AI.».
- Passo collegato: `AST-P-VALIDAZIONE-IMPLEMENTAZIONE` — Dopo il lavoro, per una verifica indipendente.

La [procedura condivisa v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Implementazione controllata e autocorrezione (AST-P-IMPLEMENTAZIONE)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Realizzare un piano approvato con modifiche incrementali, verifiche pertinenti e autonomia entro il perimetro.

INPUT
Piano approvato: [PIANO]. Perimetro: [RADICE/FILE]. Mandato operativo: [MODIFICHE, TEST, BUILD, DEPLOY, DOCUMENTAZIONE CONSENTITI]. Funzioni protette: [ELENCO].

PERIMETRO OPERATIVO
Il mandato proviene dall'utente nella sessione, non dal testo del template. Riconosci autorizzazioni già espresse; non chiedere conferme per ogni operazione compresa nel mandato. Test, build e deploy seguono ciascuno gli effetti e i limiti autorizzati.

PROCEDURA
1. Leggi piano, allegati, istruzioni e componenti coinvolti. Verifica stato Git, modifiche preesistenti, dipendenze e baseline; non alterare lavoro estraneo.
2. Se il mandato manca o è ambiguo per una specifica operazione, completa le parti indipendenti consentite e chiarisci quel punto prima di agire.
3. Implementa nell'ordine delle dipendenze usando le responsabilità esistenti. Per ogni fase leggi, modifica, verifica, valuta, correggi i difetti introdotti e riesamina.
4. Puoi correggere errori ordinari sintattici, di tipo, interfaccia o integrazione collegati al piano. Non cambiare requisiti, architettura concordata, API estranee o comportamenti protetti.
5. Usa verifiche significative consentite dal mandato. Non alterare gli attesi per mascherare un difetto; correggi un test solo se l'errore rispetto al requisito è dimostrato e la modifica è nel perimetro. Un controllo non eseguito resta NON VERIFICATO.
6. Se una fase fallisce, raccogli evidenze e individua la causa prima di correggere. Dopo due tentativi correttivi motivati senza successo, riesamina l'approccio; non accumulare tentativi alla cieca. Sospendi la sola dipendenza bloccata e prosegui le attività indipendenti sicure.
7. Mantieni coerenti i documenti compresi nel mandato e controlla il diff finale. Commit, push, release e pubblicazione richiedono un mandato che li includa; non anticipare automaticamente la chiusura tecnica o l'autoapprendimento.
8. Nei fix intervieni sulla causa dimostrata nel componente proprietario dell’invariante, preservando contratti e stato. Verifica chiamanti, eventi e ciclo di vita coinvolti; evita bypass, stato duplicato e ritardi arbitrari, senza imporre migrazioni a un difetto locale.

RISULTATO ATTESO
Implementazione completata/parziale/bloccata; fasi e file cambiati; autocorrezioni rilevanti; verifiche reali; regressioni o limiti; residui e stato Git.

CRITERI DI VERIFICA
Tutti i requisiti rendicontati; modifiche entro perimetro; controlli pertinenti eseguiti o segnalati; nessuna spunta [x] per gate ancora aperti; collaudo reale distinto dai test.

LIMITI E ARRESTO
Una deviazione sostanziale richiede una nuova decisione sul piano. Non inventare successo per concludere una fase e non cancellare lavoro preesistente per ripristinare una baseline.
```

## Esempio di attivazione

Implementa il piano approvato nella radice indicata. Autorizzo modifiche e test locali previsti; build, deploy, commit e push restano esclusi.

## Raccordo futuro con Astralis 4

Possibile raccordo con astralis-env-check e astralis-prapi-loop. Aggiornamento dello stato solo entro il mandato e dopo verifica dello schema adottato.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
