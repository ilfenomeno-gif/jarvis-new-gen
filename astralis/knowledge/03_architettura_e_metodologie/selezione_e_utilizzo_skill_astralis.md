# Selezione e utilizzo delle skill — Astralis 3.X

Revisione: 1.0.0. Ambito esclusivo: Master Hub Astralis 3.X.

## Ruolo nel sistema

Le skill sono metodi operativi caricabili quando un compito li richiede. Si inseriscono nei tre livelli della governance e nei [12 protocolli](catalogo_protocolli_operativi_astralis.md); non costituiscono un quarto livello né una nuova architettura del framework.
La conoscenza stabilisce convenzioni e contesto; il prompt formula un incarico; la skill applica un metodo. Gli ID comuni collegano gli elementi senza imporre di caricarli tutti. Il mandato dell'utente e le istruzioni attive governano gli effetti.

Fonti: [catalogo per categorie](../../skills/README.md), [indice derivato](../../skills/INDICE_SELEZIONE.json), [standard](../../skills/STANDARD_SKILL_ASTRALIS.md) e [collaudo](../../skills/COLLAUDO_SKILL.md).

## Selezione implicita

Quando il lavoro coincide con una capacità del catalogo, selezionare il metodo senza richiedere parole chiave o il nome della skill. Non imporre una selezione visibile a ogni risposta né interrompere richieste semplici con un processo aggiuntivo.

1. Risolvere il Master Hub 3.X dalle istruzioni attive. Se manca l'accesso al catalogo, dichiarare il limite quando rilevante; non cercare un sostituto nel Lab 4.
2. Consultare nome, descrizione, intenti, condizioni ed esclusioni nell'indice. Valutare prima l'obiettivo richiesto, poi fase, materiali e strumenti effettivi. Il tipo di file da solo non determina il compito.
3. Leggere il solo SKILL.md pertinente prima di applicarlo. Caricare gli standard tecnologici o la knowledge del progetto soltanto se necessari. Non eseguire una catena di skill sulla base dei collegamenti.
4. Se manca un materiale decisivo, chiedere quello o produrre la parte utile dichiarando il limite. Se il compito è ambiguo tra valutazione ed esecuzione, usare il mandato già espresso nella sessione; non inventarne uno.
5. Applicare il metodo preservando perimetro, accessibilità e decisioni già prese. La selezione automatica non autorizza installazioni, modifiche ulteriori, deleghe, invii o pubblicazione.

Un compito può richiedere più metodi, ad esempio diagnosi seguita da correzione autorizzata. Passare al metodo successivo soltanto quando necessario al risultato richiesto. Per i normali compiti non pertinenti a nessuna skill, procedere senza forzare un candidato.

## Distinzioni che evitano instradamenti errati

- Testo lungo da riassumere: sintesi; campi con provenienza e assenze: estrazione fedele. Il contenuto tecnico non autorizza una critica al posto della sintesi.
- Alternative non definite: scenari; opzioni note: confronto; scelta presa: pianificazione. Non riaprire automaticamente una decisione conclusa.
- Contratti API: progettazione API; confini e dipendenze del sistema: analisi progettuale; difetti di un diff: revisione codice; sintomo osservato: diagnosi.
- Strategia proposta: validazione strategia; sequenza di attività: validazione piano; risultato realizzato: validazione implementazione. Una simulazione non dimostra il comportamento runtime.
- Prompt nuovo: generazione; bozza da migliorare: revisione; consiglio su quale prompt usare: selezione prompt. Una normale richiesta non va riscritta ed eseguita attraverso un prompt aggiuntivo.
- Meccaniche da progettare: game design; build disponibile da provare: collaudo gameplay. Senza runtime si prepara il collaudo, non si dichiara eseguito.

## Matrice, evidenze e autorizzazione

I numeri in `protocols` sono riferimenti al catalogo ufficiale, non comandi. In validazione applicare i sette assi e i tre livelli del protocollo 2, distinguendo pertinente, non applicabile e non verificabile. Non imporre un punteggio di perfezione o un numero fisso di difetti.

Distinguere sempre evidenza osservata, inferenza, ipotesi, simulazione e prova eseguita. Conservare le evidenze sufficienti a rendere contestabile il risultato. L'autorizzazione già data persiste: non creare un nuovo passaggio di approvazione per azioni comprese nel mandato. Una richiesta di soli consigli non diventa una richiesta di modifiche.

## Discovery nativa e lettura attraverso gli ingressi

Nel Master Hub gli ingressi AGENTS.md e GEMINI.md e i sei template richiamano questa procedura. Un'AI che riceve tali istruzioni e può leggere l'hub può usare il catalogo come conoscenza, senza installazione nativa.

La discovery nativa richiede un adattatore verificato per ciascun client: percorso, schema dei metadati, disponibilità della skill nella sessione e modalità di ricaricamento. Il prefisso `astralis-v3-` separa le identità di questa serie. Le cartelle contengono il metodo senza dipendenze obbligatorie dai prompt; la skill di selezione prompt richiede invece accesso al catalogo v3, dichiarato nei prerequisiti.

Questa integrazione non installa skill nei profili globali, non aggiorna ingressi di altri progetti e non garantisce discovery nativa per qualsiasi AI. I template valgono per collegamenti futuri finché non vengono applicati. Se l'indice manca o è obsoleto, leggere il catalogo e le schede canoniche senza rigenerarlo durante un semplice consiglio.

## Manutenzione e migrazione futura

Modificare gli SKILL.md canonici, rigenerare l'indice e verificare riferimenti, hash e casi di collaudo interessati. Il generatore usa i metadati dei prompt canonici e rifiuta una baseline diversa da 3.X.
ID, categorie, criteri e provenienza preparano il trasferimento futuro; la migrazione richiederà una valutazione separata dopo il completamento di Astralis 4. L'esportatore pubblico e i pacchetti già rilasciati non distribuiscono automaticamente queste skill.
