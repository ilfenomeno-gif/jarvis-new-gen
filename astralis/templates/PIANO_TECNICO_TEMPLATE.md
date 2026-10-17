# PIANO-TECNICO: [ID e titolo descrittivo]

## 📌 Metadati del Documento

- **ID Documento**: [ID univoco nel progetto]
- **Tipo Documento**: PIANO-TECNICO
- **Esito Classificazione**: [CONFERMATA / PROPOSTA / DA CLASSIFICARE]
- **Intento Operativo**: [IMPLEMENTAZIONE / CORREZIONE / REFACTORING / DIAGNOSI-VERIFICA]
- **Ambito**: [MASTER-HUB-LOCALE / PROGETTO:nome / MODULO:progetto/modulo]
- **Stato Documento**: [BOZZA / IN REVISIONE / APPROVATO / ANNULLATO / SUPERATO / ARCHIVIATO]
- **Stato Lavoro**: [NON APPLICABILE / NON AVVIATO / IN ESECUZIONE / IN VERIFICA / COMPLETATO / SOSPESO]
- **Gate Operativo**: [CONSULTIVO / IN ATTESA DI AUTORIZZAZIONE / ESECUZIONE AUTORIZZATA / ESECUZIONE CONCLUSA]
- **Evidenza del Gate**: [Mandato reale, oggetto, data e fase / NON APPLICABILE]
- **Partecipanti e Ruoli**:
  - **Responsabile Decisionale**: [Responsabile effettivo]
  - **Coordinatore Operativo**: [AI effettiva / NON ASSEGNATO]
  - **Esecutore Previsto**: [Esecutore effettivo / NON ASSEGNATO / NON APPLICABILE]
  - **Revisori**: [Revisori reali / NESSUNO]
  - **Collaudatore Finale**: [Persona reale / NON APPLICABILE]
- **Modalità Operativa**: [SINGOLA / PAIR / TRIADE]
- **Documenti Correlati**: [Origine, piano, strategia, report o RRU con link verificati / NON APPLICABILE]
- **Riferimenti Git**: [SHA e ramo verificati / NON APPLICABILE; non usare HEAD come SHA]
- **Ultimo Aggiornamento**: [YYYY-MM-DD HH:mm Europe/Rome]

## 🎯 Obiettivo

[Risultato richiesto e perimetro del documento; il suo stato non concede permessi.]

## 🧭 Origine, perimetro e precondizioni

- **Origine del Requisito**: [Richiesta diretta, Idea/RFC, Strategia o Voce RRU]
- **Archetipo**: [Implementativo / Correttivo / Refactoring / Bonifica / Migrazione / Testing / Spike, se pertinente]
- **Scopo ed Esclusioni**: [Risultato e confini richiesti]
- **Precondizioni**: [Radice codice e documentazione, stato verificato, dipendenze, strumenti e ambiente]
- **Impatto Versione AVF**: [Proposta motivata / NON APPLICABILE; non forzare release per ogni documento]

## 🏛️ Contratti e componenti

Per ogni contratto D0..DN o S1..SN pertinente:

- **Contratto e Responsabilità**: [Decisione o unità esecutiva circoscritta]
- **Precondizioni / Postcondizioni**: [Input, stato richiesto e output osservabile]
- **Invarianti**: [Comportamenti da preservare e provenienza dalla strategia, se presente]
- **Causa e Responsabilità del Fix**: [Solo per correzioni: causa dimostrata, invariante violata e componente proprietario; altrimenti NON APPLICABILE]
- **Confini e Impatto**: [Domini, stato, contratti, dipendenze e percorsi correlati interessati; verifiche in isolamento e integrazione proporzionate]
- **Componenti Coinvolti**: [File, dati, interfacce e risorse previsti; per nuovi moduli e suite di test verificare il partizionamento per dominio/categoria senza accodamento inerziale a file monolitici; non dichiararli modificati]
- **Verifica Associata**: [Evidenza statica, automatica, telemetrica o utente per questo contratto]

## 🛠️ Passi esecutivi e avanzamento

[Ordine delle attività secondo dipendenze, risultati verificabili e ripristino proporzionato. Per un intervento semplice bastano poche unità.]

- `[ ]`: non avviato.
- `[/]`: realizzato, in attesa delle verifiche o della convalida richiesta.
- `[x]`: convalidato per il perimetro indicato, con evidenza reale. Approvazione del disegno, test tecnici e collaudo utente restano distinti.

## 🛡️ Audit e matrice di simulazione

- **Sei Cancelli Pertinenti**: [Causa reale; input fisico e hitbox solo se rilevanti; contratti; clock controllato nei test temporali; budget e assenza di duplicazioni]
- **Sette Assi**: [Validità, efficacia, coerenza, completezza, precisione NVDA, affidabilità/prestazioni, non-regressione; motivare non applicabile o non verificabile]
- **Uso Ordinario**: [Stato iniziale, azione, atteso ed evidenza prevista]
- **Alternative o Concorrenza**: [Scenario pertinente]
- **Casi Limite**: [Confini, input assente, errore o recupero pertinenti]

Le simulazioni preventive non sono test eseguiti. Determinismo a tempo virtuale riguarda test che lo consentono, non una promessa di esecuzione di tutti i test in zero millisecondi.

## 🧪 Verifiche, collaudo e documentazione

[Comandi effettivi dello stack quando noti; fixture e isolamento; risultato atteso; collaudo runtime/NVDA quando pertinente; evidenze mancanti.]
Il report pertinente documenta il lavoro sostanziale autorizzato quando serve continuità. I18N, ordinamento JSON IT/EN, volumi e geometria sono specializzazioni dei progetti che li richiedono, non obblighi per ogni piano.

## 🤝 Punto di stop e mandato

- **Punto di Stop**: [Confine fra redazione/validazione 1A e realizzazione 1B]
- **Mandato Disponibile**: [Oggetto e fase già autorizzati; non chiedere conferme duplicate]
- **Azioni Esterne**: [Build, deploy, commit, push o pubblicazione solo se pertinenti e compresi nel mandato; altrimenti non previsti]

L'approvazione del piano e l'autorizzazione a eseguirlo sono informazioni separate. La checklist non concede permessi. Chiusura e archiviazione seguono convalida richiesta e verifica dei puntatori; nessuna spunta preventiva.
