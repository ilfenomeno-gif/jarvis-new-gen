---
schema: 2
id: "AST-P-STRATEGIA-LOGICA"
title: "Redazione di una strategia logica"
revision: "1.0.0"
status: "nuovo_verificato_documentalmente"
category: "03_progettazione_e_pianificazione"
protocols: [1, 12]
domains: ["trasversale"]
mode: "consultiva"
requires: ["lettura_materiali", "strumenti_pertinenti_se_autorizzati"]
sources: []
selection: {"intents": ["creare_strategia_logica"], "use_when": ["Costruisce modello mentale, tesi e invarianti di una strategia per un problema compreso ma senza approccio concettuale definito."], "avoid_when": ["Validazione di una strategia già fornita, piano tecnico dettagliato o hotfix semplice con causa e soluzione note."], "materials": ["Problema, obiettivo, contesto e vincoli; evidenze o idea di origine se presenti."], "examples": ["Il bisogno è chiaro: definiamo modello mentale e invarianti prima dei dettagli tecnici."], "related": [{"id": "AST-P-VALIDAZIONE-STRATEGIA", "when": "Per un giudizio indipendente sulla strategia prodotta."}, {"id": "AST-P-PIANIFICAZIONE", "when": "Per tradurre le decisioni e le invarianti nel piano quando il mandato lo comprende."}]}
---

# Redazione di una strategia logica

## Scopo e condizioni d'uso

Costruisce modello mentale, tesi e invarianti di una strategia per un problema compreso ma senza approccio concettuale definito.
Identificativo: `AST-P-STRATEGIA-LOGICA`. Revisione 1.0.0; non è una versione del framework. Collaudo d'uso dei client aperto.
Consulta lo [standard](../STANDARD_PROMPT_ASTRALIS.md) e la [procedura di selezione v3](../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md).

## Scheda operativa

- Protocolli: 1, 12.
- Ambito: trasversale, specializzato sul contesto effettivo.
- Modalità: consultiva; non concede permessi.
- Materiali: Problema, obiettivo, contesto e vincoli; evidenze o idea di origine se presenti.
- Provenienza: capacità nuova derivata dalle esigenze e dalla tassonomia v3; nessuna sorgente storica attribuita.

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Costruisce modello mentale, tesi e invarianti di una strategia per un problema compreso ma senza approccio concettuale definito.
- Evitalo quando: Validazione di una strategia già fornita, piano tecnico dettagliato o hotfix semplice con causa e soluzione note.
- Materiali: Problema, obiettivo, contesto e vincoli; evidenze o idea di origine se presenti.
- Esempio: Il bisogno è chiaro: definiamo modello mentale e invarianti prima dei dettagli tecnici.
- Passo collegato: `AST-P-VALIDAZIONE-STRATEGIA` — Per un giudizio indipendente sulla strategia prodotta.
- Passo collegato: `AST-P-PIANIFICAZIONE` — Per tradurre le decisioni e le invarianti nel piano quando il mandato lo comprende.

## Testo da copiare

```text
ASTRALIS — Redazione di una strategia logica — AST-P-STRATEGIA-LOGICA

CONTESTO E VINCOLI ESSENZIALI
Rispetta istruzioni attive, mandato già dato e conoscenza pertinente accessibile. Questo prompt non conferisce permessi.
Separa fatti, ipotesi, simulazioni e prove. Usa italiano lineare e navigabile con NVDA; non esporre ragionamento interno privato.

OBIETTIVO
Costruisce modello mentale, tesi e invarianti di una strategia per un problema compreso ma senza approccio concettuale definito.

INPUT
Richiesta e obiettivo: [RICHIESTA]. Materiali: [FONTI]. Contesto e vincoli: [CONTESTO]. Modalità e mandato: [PROGETTAZIONE / REALIZZAZIONE / ESECUZIONE, SE PERTINENTI].

PERIMETRO OPERATIVO
Svolgi soltanto il compito richiesto. Persistenza utile e modifiche seguono il mandato già disponibile; niente implementazione, invio, delega, deploy o pubblicazione impliciti. Non chiedere una nuova conferma per azioni già autorizzate.

PROCEDURA
1. Definisci dilemma, comportamento desiderato e modello mentale dal punto di vista di utente e sistema. Prima considera capacità native, configurazione e riuso.
2. Scegli un archetipo pertinente: concettuale, diagnostico, refactoring, accessibilità, dialettico, interoperabilità o migrazione. Non trasformarlo in sette processi obbligatori.
3. Confronta soltanto alternative plausibili e motiva la tesi proposta; separa ipotesi da decisioni già convalidate.
4. Definisci invarianti concettuali e rischi negli scenari comuni, alternativi e limite. Applica i sei cancelli nelle dimensioni pertinenti, senza imporre input fisico o hitbox a un’API.
5. Registra punti aperti, convergenza preliminare e invarianti convalidate con fonte reale della decisione. Contratti D/S dettagliati, patch e sequenze esecutive appartengono al piano.
6. Concludi con criterio di conversione e prossimo passo. Se la persistenza è utile e compresa nel mandato usa STRATEGIA_COGNITIVA_TEMPLATE.md nella radice documentale. Se una strategia è già fornita per un giudizio, usare validazione-strategia; nessuna implementazione implicita.
7. Nel modello concettuale chiarisci confini dei domini e proprietà dello stato; confronta integrazione e coordinamento proporzionati, senza imporre un orchestratore globale o anticipare classi e patch.

RISULTATO ATTESO
Risultato coerente con la modalità richiesta, fonti, assunzioni, limiti, evidenze e prossimo passo pertinente. Per test distinguere piano, test realizzati e prove effettivamente eseguite; per idea e strategia separare proposta e convalida.

CRITERI DI VERIFICA
Il risultato risponde al bisogno, conserva vincoli e decisioni esistenti, rende esplicite lacune e prove mancanti, senza passaggi automatici fuori dal mandato.

LIMITI E ARRESTO
Se manca un input decisivo completa il lavoro indipendente e chiedi quel dato. Se runtime o strumenti non sono disponibili dichiara il limite; non inventare risultati.
```

## Esempio di attivazione

Il bisogno è chiaro: definiamo modello mentale e invarianti prima dei dettagli tecnici.

## Raccordo futuro con Astralis 4

Identità, criteri e metodo sono trasferibili solo dopo valutazione della futura architettura. Nessuna dipendenza o attivazione del Lab v4 è inclusa.

Nel Master Hub v3, la mappa `ciclo_sviluppo_e_selezione_strumenti_astralis.md` raccorda anche skill e template.
