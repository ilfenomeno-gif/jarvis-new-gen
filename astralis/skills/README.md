# Catalogo delle skill Astralis 3.X

Revisione: 1.3.0. Baseline framework: 3.0.21. Stato: verificabile documentalmente; collaudo d’uso aperto.

27 skill: 14 adattate dalle sorgenti storiche, sette ricavate dai metodi dei prompt, tre dedicate al ciclo dei report e tre al completamento del ciclo di sviluppo; redazione-report aggiornata alla revisione 1.1.0. Le categorie organizzano questo indice; ogni skill ha una cartella autonoma per facilitarne il confezionamento.

## 01 analisi e conoscenza

- [Ragionamento approfondito](astralis-v3-ragionamento-approfondito/SKILL.md): Analizza una questione concettuale complessa con assunzioni o conseguenze incerte.
- [Sintesi della conoscenza](astralis-v3-sintesi-conoscenza/SKILL.md): Sintetizza testi lunghi, tecnici o narrativi, conservandone struttura e punti essenziali.
- [Estrazione documentale fedele](astralis-v3-estrazione-fedele/SKILL.md): Estrae campi, fatti o citazioni da documenti mantenendo la provenienza e senza completare le lacune.

## 02 decisione e pianificazione

- [Ideazione](astralis-v3-ideazione/SKILL.md): Chiarisce un’idea embrionale e le ipotesi da verificare.
- [Strategia logica](astralis-v3-strategia-logica/SKILL.md): Crea un modello concettuale con alternative e invarianti.

- [Esplorazione di scenari](astralis-v3-scenari/SKILL.md): Esplora alternative ancora aperte, tecniche, strategiche o narrative, e le loro conseguenze.
- [Confronto di opzioni](astralis-v3-confronto-opzioni/SKILL.md): Confronta almeno due opzioni note per aiutare una scelta motivata e contestabile.
- [Pianificazione delle attività](astralis-v3-pianificazione/SKILL.md): Traduce una decisione in un piano proporzionato; per un piano tecnico definisce contratti, file e verifiche per contratto.

## 03 ingegneria software

- [Analisi e progettazione tecnica](astralis-v3-analisi-progettuale/SKILL.md): Analizza un’architettura esistente o progetta una soluzione tecnica con confini, dati e contratti.
- [Progettazione API e contratti](astralis-v3-progettazione-api/SKILL.md): Progetta o rivede contratti API, endpoint, comandi CLI o strumenti MCP.
- [Revisione del codice](astralis-v3-revisione-codice/SKILL.md): Rivede codice o diff e segnala difetti, regressioni e rischi concreti con riferimenti.
- [Diagnosi di errori e telemetrie](astralis-v3-diagnosi/SKILL.md): Diagnostica errori, stack trace, regressioni e sessioni osservate tramite log o telemetrie.
- [Refactoring mirato](astralis-v3-refactoring/SKILL.md): Pianifica o applica refactoring a codice funzionante preservando il comportamento pubblico.

## 04 validazione ed esecuzione

- [Testing e collaudo](astralis-v3-testing-e-collaudo/SKILL.md): Progetta, realizza o esegue prove generali secondo il mandato.

- [Validazione della strategia](astralis-v3-validazione-strategia/SKILL.md): Valuta se una strategia proposta è coerente con obiettivo, assunzioni e vincoli prima del piano.
- [Validazione del piano](astralis-v3-validazione-piano/SKILL.md): Verifica un piano esistente prima dell’esecuzione: dipendenze, fattibilità, copertura e verifiche.
- [Validazione dell’implementazione](astralis-v3-validazione-implementazione/SKILL.md): Verifica un risultato già realizzato rispetto a requisiti, contratti e prove di accettazione.
- [Implementazione controllata](astralis-v3-implementazione-controllata/SKILL.md): Esegue modifiche circoscritte richieste dall’utente, sulla base di un piano o di requisiti operativi chiari.

## 05 prompt e documentazione

- [Generazione di prompt](astralis-v3-generazione-prompt/SKILL.md): Crea un prompt nuovo per un obiettivo, con input, perimetro e risultato verificabile.
- [Revisione di prompt](astralis-v3-revisione-prompt/SKILL.md): Migliora un prompt esistente preservando intento, vincoli e destinatario.
- [Redazione di report](astralis-v3-redazione-report/SKILL.md): Redige resoconti tecnici, incident report o ricevute di verifica da evidenze disponibili.
- [Selezione di prompt Astralis](astralis-v3-selezione-prompt/SKILL.md): Consiglia quale prompt del catalogo Astralis 3.X usare in un contesto, anche con una domanda breve.

- [Lettura dei report](astralis-v3-lettura-report/SKILL.md): Ripresa selettiva e verifica di fonti esterne.
- [Continuità di sessione](astralis-v3-continuita-sessione/SKILL.md): Sospensione e passaggio di consegne senza nuovi permessi.
- [Chiusura dei report](astralis-v3-chiusura-report/SKILL.md): Archiviazione convalidata e coerenza dei puntatori.

## 06 game design e collaudo

- [Progettazione di giochi](astralis-v3-game-design/SKILL.md): Progetta o rivede sistemi di gioco: ciclo principale, meccaniche, progressione e accessibilità.
- [Collaudo del gameplay](astralis-v3-collaudo-gameplay/SKILL.md): Collauda gameplay disponibile con scenari osservabili, inclusi tastiera e feedback accessibile.

## Selezione e distribuzione

La [procedura comune](../knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_skill_astralis.md) governa la selezione tramite l'[indice derivato](./INDICE_SELEZIONE.json). Le skill possono essere selezionate implicitamente quando il compito coincide con descrizione e confini. Non sono installate nei profili globali dei client.

Negli ambienti senza discovery nativa, un ingresso collegato al Master Hub consulta l’indice e legge soltanto la skill pertinente. Per discovery nativa, occorre distribuire le cartelle secondo il formato e il percorso verificati per il client; il catalogo da solo non lo configura. Una sessione già avviata potrebbe richiedere il ricaricamento delle istruzioni.

Le skill di onboarding, coordinamento tra AI e formazione non sono state create automaticamente: i prompt restano disponibili e tali capacità richiedono una definizione specifica di ambiente, mandato o percorso didattico.

## Manutenzione

Modificare la scheda canonica, poi rigenerare l’indice con `python -B scripts/genera_indice_skill.py`. Verificare senza scrivere con `python -B scripts/genera_indice_skill.py --check`. Per confrontare gli originali aggiungere `--source-root` con il percorso della cartella storica.

[Standard e template](STANDARD_SKILL_ASTRALIS.md), provenienza e hash (manifest privato non distribuito) e [collaudo d’uso](COLLAUDO_SKILL.md). L’esportatore pubblico attuale non distribuisce questo catalogo: la pubblicazione resta una fase successiva, distinta dal lavoro nel Master Hub v3.

Per il ciclo dei report: [procedura comune](../knowledge/03_architettura_e_metodologie/gestione_report_e_continuita_sessioni.md) e [collaudo specifico](COLLAUDO_REPORT.md).
