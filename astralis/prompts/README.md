# Catalogo dei prompt operativi Astralis

Revisione del catalogo: 1.3.0. Data: 2026-10-04. Master Hub di riferimento: Astralis 3.0.21.
23 prompt canonici, sette categorie, tre ingressi storici compatibili. Adattamento documentale completato; collaudo d'uso sui diversi assistenti ancora aperto.

## Come scegliere e usare un prompt

1. Scegli il compito nell'indice; la categoria organizza i file, protocolli e domini descrivono l'applicazione.
2. Leggi la scheda e verifica input, capacità richieste e perimetro.
3. Se l'AI legge i file, indica il documento o l'identificativo presente nel catalogo; altrimenti copia il solo blocco "Testo da copiare" e compila i campi.
4. Dichiara nella richiesta gli effetti autorizzati. Una validazione positiva non autorizza applicazione; le autorizzazioni già espresse restano valide.
5. Controlla risultato, evidenze e limiti. Il catalogo non viene caricato tutto in ogni sessione.

L'identificativo aiuta a riconoscere il documento, ma non è un comando registrato automaticamente nell'AI.

- [Standard comune, modalità e migrazione](STANDARD_PROMPT_ASTRALIS.md).
- [Template per nuovi prompt](PROMPT_TEMPLATE.md).

## Percorsi frequenti

- Pianificare: AST-P-PIANIFICAZIONE; verificare il piano: AST-P-VALIDAZIONE-PIANO.
- Implementare un piano approvato: AST-P-IMPLEMENTAZIONE; verificarne il risultato: AST-P-VALIDAZIONE-IMPLEMENTAZIONE.
- Diagnosticare una sessione: AST-P-DIAGNOSI-TELEMETRIE; revisionare un diff: AST-P-REVIEW-CODICE.
- Creare o migliorare prompt: AST-P-GENERAZIONE-PROMPT e AST-P-REVISIONE-PROMPT.

## Indice per categoria

### 1. Onboarding e governance

- [Configurazione di una macchina](01_onboarding_e_governance/PROMPT_SETUP_MACCHINA.md) — `AST-P-SETUP-MACCHINA`. Configurare Astralis su una macchina preservando profili esistenti e attivando soltanto gli assistenti scelti.
- [Inizializzazione e adozione in un progetto](01_onboarding_e_governance/PROMPT_INIZIALIZZAZIONE_PROGETTO.md) — `AST-P-INIT-PROGETTO`. Integrare Astralis in un progetto nuovo o esistente, preservando codice, storia e conoscenza locale.
- [Aggiornamento integrativo dell'ecosistema](01_onboarding_e_governance/PROMPT_AGGIORNAMENTO_ECOSISTEMA.md) — `AST-P-UPDATE-ECOSISTEMA`. Valutare e applicare un aggiornamento preservando personalizzazioni, conoscenza locale e possibilità di recupero.

### 2. Analisi e diagnosi

- [Analisi approfondita e confronto delle alternative](02_analisi_e_diagnosi/PROMPT_RAGIONAMENTO_APPROFONDITO.md) — `AST-P-ANALISI-PROFONDA`. Esaminare un problema complesso e formulare una raccomandazione motivata e verificabile.
- [Estrazione documentale con provenienza](02_analisi_e_diagnosi/PROMPT_ESTRAZIONE_DOCUMENTALE.md) — `AST-P-ESTRAZIONE-DOCUMENTALE`. Estrarre campi da documenti distinguendo dati espliciti, valori mancanti e derivazioni autorizzate.
- [Diagnosi forense di log e telemetrie](02_analisi_e_diagnosi/PROMPT_DIAGNOSI_TELEMETRIE.md) — `AST-P-DIAGNOSI-TELEMETRIE`. Ricostruire il comportamento osservato e individuare cause radice prima di progettare una correzione.

### 3. Progettazione e pianificazione

- [Idea embrionale e IDEA/RFC](03_progettazione_e_pianificazione/PROMPT_IDEA_RFC.md) — `AST-P-IDEA-RFC`. Chiarire problema, beneficio e ipotesi.
- [Strategia logica](03_progettazione_e_pianificazione/PROMPT_STRATEGIA_LOGICA.md) — `AST-P-STRATEGIA-LOGICA`. Creare il modello concettuale prima del piano.

- [Analisi ingegneristica e architetturale](03_progettazione_e_pianificazione/PROMPT_ANALISI_INGEGNERISTICA.md) — `AST-P-ANALISI-INGEGNERISTICA`. Proporre una soluzione tecnica aderente a requisiti, architettura e capacità effettive del progetto.
- [Pianificazione proporzionata di un'attività](03_progettazione_e_pianificazione/PROMPT_PIANIFICAZIONE_ATTIVITA.md) — `AST-P-PIANIFICAZIONE`. Trasformare una richiesta in un piano eseguibile con dipendenze, verifiche e perimetro chiari.

### 4. Revisione e validazione

- [Testing e collaudo generale](04_revisione_e_validazione/PROMPT_TESTING_COLLAUDO.md) — `AST-P-TESTING-COLLAUDO`. Progettare, realizzare o eseguire prove secondo il mandato.

- [Revisione del codice basata su evidenze](04_revisione_e_validazione/PROMPT_REVISIONE_CODICE.md) — `AST-P-REVIEW-CODICE`. Individuare difetti concreti nel codice e proporre rettifiche minime senza correggere durante la review.
- [Validazione di una strategia](04_revisione_e_validazione/PROMPT_VALIDAZIONE_STRATEGIA.md) — `AST-P-VALIDAZIONE-STRATEGIA`. Verificare che una strategia affronti il problema corretto e abbia un percorso praticabile senza implementarla.
- [Validazione di un piano tecnico](04_revisione_e_validazione/PROMPT_VALIDAZIONE_PIANO.md) — `AST-P-VALIDAZIONE-PIANO`. Accertare che un piano sia implementabile sul codice esistente e che i test verifichino i requisiti reali.
- [Validazione indipendente di un'implementazione](04_revisione_e_validazione/PROMPT_VALIDAZIONE_IMPLEMENTAZIONE.md) — `AST-P-VALIDAZIONE-IMPLEMENTAZIONE`. Confrontare implementazione, piano e baseline distinguendo correttezza statica, test ed evidenza sul campo.

### 5. Esecuzione e collaborazione

- [Implementazione controllata e autocorrezione](05_esecuzione_e_collaborazione/PROMPT_IMPLEMENTAZIONE_CONTROLLATA.md) — `AST-P-IMPLEMENTAZIONE`. Realizzare un piano approvato con modifiche incrementali, verifiche pertinenti e autonomia entro il perimetro.
- [Coordinamento di assistenti e sottoattività](05_esecuzione_e_collaborazione/PROMPT_COORDINAMENTO_AI.md) — `AST-P-COORDINAMENTO-AI`. Scomporre un compito e coordinare contributi indipendenti rispettando ruoli, autorizzazioni e integrità dei file.

### 6. Progettazione dei prompt e formazione

- [Generazione di un prompt operativo](06_progettazione_prompt_e_formazione/PROMPT_GENERAZIONE_PROMPT.md) — `AST-P-GENERAZIONE-PROMPT`. Trasformare una richiesta in un prompt chiaro, proporzionato e verificabile secondo lo standard Astralis.
- [Revisione e miglioramento di un prompt](06_progettazione_prompt_e_formazione/PROMPT_REVISIONE_PROMPT.md) — `AST-P-REVISIONE-PROMPT`. Migliorare un prompt esistente preservando l'intento e correggendo debolezze effettive.
- [Richiesta universale proporzionata](06_progettazione_prompt_e_formazione/PROMPT_RICHIESTA_UNIVERSALE.md) — `AST-P-RICHIESTA-UNIVERSALE`. Formulare una richiesta riutilizzabile per attività tecniche, documentali o creative senza imporre una pipeline unica.
- [Formazione pratica sull'uso dell'AI](06_progettazione_prompt_e_formazione/PROMPT_FORMAZIONE_AI.md) — `AST-P-FORMAZIONE-AI`. Spiegare principi e limiti dell'AI applicandoli a un esercizio reale e al livello di esperienza dell'utente.

### 7. Domini: game design

- [Progettazione di un gioco accessibile](07_domini/game_design/PROMPT_PROGETTAZIONE_GIOCO.md) — `AST-P-GAME-DESIGN`. Trasformare un'idea di gioco in una proposta giocabile, accessibile e proporzionata.
- [Collaudo del gameplay senza correzioni implicite](07_domini/game_design/PROMPT_COLLAUDO_GAMEPLAY.md) — `AST-P-COLLAUDO-GAMEPLAY`. Verificare scenari di gioco riproducibili, accessibilità e regressioni senza alterare il comportamento per far passare i test.

## File comuni nella root

I 23 prompt operativi canonici si trovano nelle cartelle di categoria. Nella root restano i documenti comuni: questo indice, lo standard del catalogo e il template redazionale.

## Rimandi di compatibilità

I tre file storici elencati sotto conservano i percorsi già usati dalle istruzioni e dagli strumenti. Sono rimandi ai prompt canonici nelle categorie, senza una procedura operativa separata. Per avviare un incarico o copiare il testo, usa il documento canonico collegato.

- Rimando di compatibilità: [PROMPT_SETUP_INTERATTIVO_NUOVA_MACCHINA.md](PROMPT_SETUP_INTERATTIVO_NUOVA_MACCHINA.md). Prompt canonico: [Configurazione di una macchina](01_onboarding_e_governance/PROMPT_SETUP_MACCHINA.md), `AST-P-SETUP-MACCHINA`.
- Rimando di compatibilità: [PROMPT_INIZIALIZZAZIONE_ECOSISTEMA_REGOLE_UNIVERSALE.md](PROMPT_INIZIALIZZAZIONE_ECOSISTEMA_REGOLE_UNIVERSALE.md). Prompt canonico: [Inizializzazione di un progetto](01_onboarding_e_governance/PROMPT_INIZIALIZZAZIONE_PROGETTO.md), `AST-P-INIT-PROGETTO`.
- Rimando di compatibilità: [PROMPT_AGGIORNAMENTO_ECOSISTEMA_ESISTENTE.md](PROMPT_AGGIORNAMENTO_ECOSISTEMA_ESISTENTE.md). Prompt canonico: [Aggiornamento dell'ecosistema](01_onboarding_e_governance/PROMPT_AGGIORNAMENTO_ECOSISTEMA.md), `AST-P-UPDATE-ECOSISTEMA`.

## Provenienza e copertura

Le 18 sorgenti storiche sono state adattate in 17 prompt: le due varianti di game design sono consolidate in un documento. I tre prompt preesistenti del Master Hub sono stati standardizzati: totale storico 20; tre nuovi metodi del ciclo di sviluppo portano il catalogo a 23.
Le sorgenti restano nella loro cartella. I metadati di ogni prompt registrano i nomi di provenienza; snapshot dei tre ingressi precedenti e inventario hash sono nel rapporto interno del Master Hub.
Il README storico non è importato: contiene un riepilogo precedente e collegamenti remoti temporanei non necessari al catalogo.

Le procedure di chiusura, autoapprendimento e bonifica restano nei protocolli 6, 7 e 11. Questa raccolta non introduce prompt dedicati per ogni protocollo né una nuova gerarchia normativa.
I prompt trasversali coprono anche scrittura e documentazione; nuove specializzazioni verranno aggiunte sulla base di esigenze reali.

## Preparazione alla migrazione

Identificativi e input restano stabili; gli abbinamenti alle skill v4 sono candidati da verificare. Le copie storiche già nel Lab dovranno essere riconciliate, senza sincronizzazione automatica.
Il catalogo non modifica il Lab, i suoi progetti di test, configurazioni globali o il repository pubblico.

## Verifica e distribuzione

Dalla radice del Master Hub: `python scripts/verifica_catalogo_prompt.py`.
Lo Starter Kit include ricorsivamente i documenti. L'esportatore pubblico è stato adattato alla struttura: esporta i Markdown del catalogo e converte i riferimenti alla knowledge secondo la mappa pubblica.
L'esportazione del catalogo viene verificata in staging isolato. Il catalogo non è stato pubblicato né è stata eseguita la sincronizzazione del repository pubblico.
La revisione 1.0.0 del catalogo non incrementa automaticamente la versione del framework o genera una release.


## Consiglio contestuale — Astralis 3.X

Puoi chiedere all’AI collegata: «Quale prompt Astralis 3 mi consigli per questo contesto?».
La [procedura nella conoscenza v3](../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md) usa l’[indice generato](./INDICE_SELEZIONE.json) e verifica il documento candidato.
Il consiglio include prompt, motivo, materiali necessari, esempio di attivazione e limite; non avvia il lavoro.
Ogni scheda descrive quando usarla e quando scegliere altro. Se i materiali mancano, la raccomandazione resta condizionata; se nessun candidato è adeguato, l’AI lo dichiara.
Indice derivato: `python -B scripts/genera_indice_prompt.py`; controllo senza scritture: aggiungere `--check`. I comandi si eseguono dalla radice del Master Hub 3.X.
I template aggiornati e gli ingressi locali del Master Hub contengono il richiamo; i router di altri progetti non vengono aggiornati automaticamente.
