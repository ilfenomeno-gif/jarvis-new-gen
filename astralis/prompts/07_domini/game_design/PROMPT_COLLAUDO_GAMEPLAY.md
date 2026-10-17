---
schema: 2
id: "AST-P-COLLAUDO-GAMEPLAY"
title: "Collaudo del gameplay senza correzioni implicite"
revision: "1.1.0"
status: "adattato_verificato_documentalmente"
category: "07_domini/game_design"
protocols: [3, 4, 5]
domains: ["giochi"]
mode: "collaudo_su_mandato_senza_correzione"
requires: ["controllo_ui_o_runner", "lettura_log", "ambiente_test"]
sources: ["prompt-agente-test-automatico (.md"]
selection: {"intents": ["collaudare_gioco"], "use_when": ["Interagire con una build di test e controllare scenari e accessibilità del gameplay."], "avoid_when": ["Per log già raccolti usare diagnosi; senza ambiente o strumenti proporre un piano manuale, senza simulare interazioni."], "materials": ["build_test", "scenari_e_attesi", "ambiente_isolato", "mandato_interazioni"], "examples": ["Devo verificare le meccaniche nella build di test senza applicare fix."], "related": [{"id": "AST-P-DIAGNOSI-TELEMETRIE", "when": "Se gli scenari producono log da analizzare per risalire alla causa."}]}
---

# Collaudo del gameplay senza correzioni implicite

## Scopo e condizioni d'uso

Verificare scenari di gioco riproducibili, accessibilità e regressioni senza alterare il comportamento per far passare i test.

Identificativo: `AST-P-COLLAUDO-GAMEPLAY`. Revisione del prompt: `1.1.0`; non è la versione del framework.
Verificato documentalmente il 2026-10-03; collaudo d'uso con AI e utente ancora da effettuare.
Consulta lo [standard del catalogo](../../STANDARD_PROMPT_ASTRALIS.md) per modalità, tassonomia probatoria e migrazione.

## Scheda operativa

- Protocolli: 3, 4, 5.
- Domini: giochi.
- Modalità: `collaudo_su_mandato_senza_correzione`.
- Capacità richieste: controllo_ui_o_runner, lettura_log, ambiente_test.
- Input della sessione: Build e ambiente: [VERSIONE/ISTANZA]. Scenari: [ELENCO]. Attesi: [REQUISITI]. Mandato: [INTERAZIONI, DATI DI TEST E LIMITI]. Budget: [DURATA/TENTATIVI].

## Quando scegliere questo prompt — Astralis 3.X

- Usalo quando: Interagire con una build di test e controllare scenari e accessibilità del gameplay.
- Preferisci altro quando: Per log già raccolti usare diagnosi; senza ambiente o strumenti proporre un piano manuale, senza simulare interazioni.
- Materiali minimi: build_test, scenari_e_attesi, ambiente_isolato, mandato_interazioni. Se mancano, il consiglio è condizionato alla loro disponibilità.
- Richiesta riconoscibile: «Devo verificare le meccaniche nella build di test senza applicare fix.».
- Passo collegato: `AST-P-DIAGNOSI-TELEMETRIE` — Se gli scenari producono log da analizzare per risalire alla causa.

La [procedura condivisa v3](../../../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) governa il consiglio; i criteri autorevoli sono nei metadati `selection`.

## Testo da copiare

Copia soltanto il blocco seguente e compila i campi necessari. Un segnaposto non costituisce un dato né un'autorizzazione.

```text
ASTRALIS — Collaudo del gameplay senza correzioni implicite (AST-P-COLLAUDO-GAMEPLAY)

CONTESTO E VINCOLI ESSENZIALI
Agisci nel ruolo richiesto dal compito usando solo le capacità realmente disponibili. Rispetta le istruzioni della sessione e del progetto: questo prompt non le sostituisce e non concede permessi da solo.
Consulta soltanto la conoscenza Astralis pertinente, se accessibile. Se non hai accesso ai file, lavora sui materiali forniti e dichiara i controlli impossibili.
Distingui fatti, ipotesi e risultati verificati; non inventare fonti, test, misure o agenti. La validazione tecnica non è autorizzazione a eseguire.
Usa italiano e formato lineare leggibile con NVDA, con sintesi in chat e riferimenti alle evidenze. Non esporre ragionamento interno; fornisci motivazioni controllabili. Non salvare documenti né dati personali fuori dal mandato.
Rispetta autorizzazioni già espresse, perimetro e limitazioni operative: non chiedere conferme per passaggi già autorizzati, né estendere implicitamente gli effetti.

OBIETTIVO
Verificare scenari di gioco riproducibili, accessibilità e regressioni senza alterare il comportamento per far passare i test.

INPUT
Build e ambiente: [VERSIONE/ISTANZA]. Scenari: [ELENCO]. Attesi: [REQUISITI]. Mandato: [INTERAZIONI, DATI DI TEST E LIMITI]. Budget: [DURATA/TENTATIVI].

PERIMETRO OPERATIVO
Il collaudo interattivo modifica lo stato della partita: eseguilo solo nel mandato e nell'istanza di test indicata. Non toccare salvataggi reali, sorgenti, bilanciamento o configurazioni operative. Nessuna injection, override o evento forzato per mascherare un difetto.

PROCEDURA
1. Verifica build, ambiente isolato, dati di test, strumenti disponibili e criteri di accettazione. Se manca una condizione indispensabile non iniziare la partita.
2. Definisci una matrice di scenari rappresentativi e casi limite per le meccaniche effettive. Un percorso completo non dimostra copertura di tutte le combinazioni; limita durata e tentativi.
3. Registra stato iniziale, input, atteso, osservato e prova per ogni scenario. Usa UI, DOM, log o runner realmente disponibili senza simulare interazioni.
4. Controlla creazione, navigazione, azioni, errore, recupero, salvataggio e caricamento quando presenti. Esercita tastiera, ordine del focus, nomi accessibili e feedback vocale; distingue misure automatiche dal riscontro NVDA dell'utente.
5. Valuta anche presentazione visiva e canali alternativi pertinenti. Misura latenza o distribuzioni casuali solo con un metodo e soglie motivate dal requisito; non imporre 200 ms o cento campioni come garanzia universale.
6. Se il gioco fallisce, registra il primo difetto e conserva le evidenze. Ritenta solo entro il budget e se il riavvio è previsto e sicuro; non proseguire uno scenario impossibile come se fosse riuscito.
7. Distingui SODDISFATTO, NON SODDISFATTO, PARZIALE, NON VERIFICATO e NON APPLICABILE; specifica livello probatorio e copertura. Proponi correzioni senza applicarle. Il collaudo empirico richiesto resta aperto fino al feedback reale dell'utente.

RISULTATO ATTESO
Ambiente e build, scenari e copertura, difetti con riproduzione, evidenze, controlli di accessibilità, limiti e rettifiche proposte. Nessun successo per meccaniche non esercitate.

CRITERI DI VERIFICA
Partita eseguita solo in test; attesi non alterati; bug documentati senza masking; strumenti e input reali; regressioni riferite a baseline; feedback umano distinto da automazione.

LIMITI E ARRESTO
Se manca il controllo della UI o il gioco non si avvia, consegna il limite e un piano di collaudo manuale. Bilanciamento statistico richiede campionamento adeguato e analisi, non correzione automatica dell'RNG.
```

## Esempio di attivazione

Collauda questi scenari nella build di test con i dati isolati indicati. Autorizzo le interazioni previste; non correggere codice o bilanciamento.

## Raccordo futuro con Astralis 4

Runner e skill di dominio potranno fornire strumenti di verifica; nessuna skill può sostituire il riscontro empirico necessario.
Il raccordo è una proposta di migrazione, non una dipendenza attiva o un'installazione già collaudata.
