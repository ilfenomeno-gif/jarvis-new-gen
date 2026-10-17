# Ciclo di sviluppo e selezione degli strumenti — Astralis 3.X

Revisione: 1.1.0. Baseline: 3.0.21. Applicabilità: solo Master Hub Astralis 3.X.

## Selezione contestuale

Individua obiettivo, fase effettiva, materiali disponibili ed effetti autorizzati. Consulta gli indici [skill](../../skills/INDICE_SELEZIONE.json) e [prompt](../../prompts/INDICE_SELEZIONE.json), quindi leggi soltanto il metodo candidato. La skill guida il lavoro; il prompt serve a formulare o trasferire una richiesta. Non occorre applicarli entrambi per duplicare la stessa attività.

1. **Idea embrionale**: chiarire problema, destinatari, beneficio e ipotesi. Skill [ideazione](../../skills/astralis-v3-ideazione/SKILL.md), AST-S-IDEAZIONE; prompt [IDEA/RFC](../../prompts/03_progettazione_e_pianificazione/PROMPT_IDEA_RFC.md), AST-P-IDEA-RFC. Sono ammessi input incompleti. [Template IDEA/RFC](../../templates/IDEA_RFC_TEMPLATE.md).
2. **Strategia logica da creare**: modellare comportamento, alternative, invarianti e decisione concettuale. Skill [strategia-logica](../../skills/astralis-v3-strategia-logica/SKILL.md), AST-S-STRATEGIA-LOGICA; prompt [strategia logica](../../prompts/03_progettazione_e_pianificazione/PROMPT_STRATEGIA_LOGICA.md), AST-P-STRATEGIA-LOGICA. [Template strategia](../../templates/STRATEGIA_COGNITIVA_TEMPLATE.md).
3. **Piano tecnico da redigere**: tradurre una direzione scelta in contratti, file interessati, dipendenze e prove per ciascun contratto. Skill [pianificazione](../../skills/astralis-v3-pianificazione/SKILL.md), AST-S-PIANIFICAZIONE; prompt [pianificazione](../../prompts/03_progettazione_e_pianificazione/PROMPT_PIANIFICAZIONE_ATTIVITA.md), AST-P-PIANIFICAZIONE. [Template piano tecnico](../../templates/PIANO_TECNICO_TEMPLATE.md).
4. **Analisi e validazione**: per problemi incerti usare analisi-progettuale o ragionamento-approfondito; per un documento già esistente scegliere validazione-strategia o validazione-piano. Per un risultato realizzato scegliere validazione-implementazione. Verificare requisiti, fattibilità, coerenza ed evidenze; una conclusione positiva non aggiunge autorizzazioni.
5. **Revisione**: usare revisione-codice per difetti concreti nel codice o nel diff, diagnosi per log e comportamento osservato. La review produce rilievi, non avvia correzioni implicite.
6. **Test e collaudo generale**: skill [testing-e-collaudo](../../skills/astralis-v3-testing-e-collaudo/SKILL.md), AST-S-TESTING-E-COLLAUDO; prompt [testing e collaudo](../../prompts/04_revisione_e_validazione/PROMPT_TESTING_COLLAUDO.md), AST-P-TESTING-COLLAUDO. Distinguere progettazione delle prove, scrittura dei test ed esecuzione. Per scenari giocabili utilizzare la specializzazione collaudo-gameplay quando pertinente.

Gli identificativi di selezione distinguono `chiarire_idea`, `creare_strategia_logica`, `redigere_piano_tecnico`, `progettare_test`, `realizzare_test`, `eseguire_test` e `collaudare_software`. Sono metadati descrittivi: comprendere richieste naturali senza esigere queste parole esatte.

## Architettura e correzioni sistemiche

Per progettare domini modulari scegliere [analisi-progettuale](../../skills/astralis-v3-analisi-progettuale/SKILL.md); per i soli contratti di interfaccia scegliere [progettazione-api](../../skills/astralis-v3-progettazione-api/SKILL.md). Strategia e piano servono quando occorre rispettivamente scegliere una direzione o organizzare l'attuazione. Applicare il [metodo architetturale, sezione 27](clean_architecture_e_design_pattern.md) senza imporre un hub globale.

Se la causa è ignota scegliere diagnosi; se è dimostrata e la correzione è autorizzata usare implementazione-controllata. Review e refactoring conservano i loro mandati distinti. Il [metodo causale, sezione 10](strategie_testing_e_debug.md) guida la scelta del componente responsabile, anche locale; testing e validazione raccolgono prove pertinenti senza attivare una pipeline obbligatoria.

## Proporzionalità e limiti

Il percorso è flessibile. Una correzione circoscritta con causa nota può partire dal piano minimo o dall'implementazione autorizzata. Creare una strategia e validarne una esistente sono compiti distinti. Le relazioni tra schede suggeriscono il prossimo metodo soltanto se il mandato lo comprende: non attivare automaticamente tutta la catena.

Applicare i protocolli 1 e 12 alla documentazione e alla convergenza; 2, 3 e 4 alle prove, revisioni e correzioni pertinenti. I sei cancelli e i sette assi vanno motivati; un cancello di dominio non pertinente è NON APPLICABILE, non una prova superata. La tassonomia e la testata universale vigenti prevalgono sui formati storici.

Usare [gestione report e continuità](gestione_report_e_continuita_sessioni.md) nel lavoro sostanziale autorizzato. Separare radice codice, documentazione e runtime; non inventare risultati se mancano strumenti o ambiente. Registrare comando, esito, evidenza e limiti, distinguendo controllo documentale, test automatico e collaudo sul campo.

## Ingressi e futuro raccordo

Gli ingressi locali e i template AI richiamano questa mappa. La selezione tramite lettura dell'hub richiede che l'AI possa accedervi; non configura discovery nativa, profili globali o router già distribuiti. Cataloghi e identificativi stabili preparano una migrazione futura, senza dipendere da Astralis 4 o modificarne il Lab.
