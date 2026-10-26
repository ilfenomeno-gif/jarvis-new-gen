# ECC in VS Code — analisi e pilot documentale

Data analisi: 2026-10-26
Repository esaminato: `affaan-m/ECC`, README e sorgenti pubblici consultati il
2026-10-26. ECC dichiara licenza MIT; la licenza non sostituisce la revisione
del codice o della provenienza del pacchetto prima di eseguirlo.

## 1. Analisi dell'ambito

### Ambiente osservato

| Controllo | Risultato | Limite |
|---|---|---|
| `node -v` | `v24.13.1`; soddisfa il minimo Node.js 18+ indicato per il pacchetto universale ECC | Non è stata installata o eseguita alcuna versione di ECC |
| `code --version` | VS Code `1.143.1`, Windows x64 | Non certifica disponibilità dell'Agent Mode |
| `code --list-extensions --show-versions` | `GitHub.copilot` e `GitHub.copilot-chat` non compaiono; è presente `vizards.deepseek-v4-for-copilot@0.9.4` | Elenco locale delle estensioni, non stato account/licenza |
| `.vscode/settings.json` del workspace | `github.copilot.chat.codeGeneration.useInstructionFiles` è `true` | Una preferenza configurata non dimostra che Copilot sia installato, attivo o autenticato |
| Ricerca Marketplace `ecc`, `affaan-m.ecc`, `Everything Claude Code` e termini affini | Nessuna estensione ECC ufficiale identificata. Sono emersi strumenti indipendenti e solo parzialmente sovrapponibili, fra cui `AutomataLabs.copilot-mcp`, `pujie.skills-deck` e `AmitChorasiya.github-copilot-toolbox` | Risultati di ricerca indicativi; non è stata eseguita una valutazione di qualità o sicurezza degli strumenti terzi |

Il workspace ha inoltre una propria estensione JARVIS in
`jarvis-vscode-extension/`; questa è un client del servizio JARVIS, non
l'integrazione ECC.

### ECC: CLI, interazione e superfici di integrazione

Fonti primarie consultate:

- [README ECC](https://github.com/affaan-m/ECC#readme)
- [package.json ECC](https://github.com/affaan-m/ECC/blob/main/package.json)
- [dispatcher CLI ECC](https://github.com/affaan-m/ECC/blob/main/scripts/ecc.js)
- [doctor ECC](https://github.com/affaan-m/ECC/blob/main/scripts/doctor.js)
- [server memoria MCP ECC](https://github.com/affaan-m/ECC/blob/main/scripts/memory-mcp.mjs)
- [adattamento manuale ECC per harness non nativi](https://github.com/affaan-m/ECC/blob/main/docs/MANUAL-ADAPTATION-GUIDE.md)
- [configurazione MCP in VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers)

Risultati:

1. **Invocazione CLI:** il pacchetto `ecc-universal` 2.2.3 espone i bin `ecc`
   ed `ecc-universal`. Il README documenta, fra gli altri,
   `npx ecc-universal@2.2.3 setup`, `install`, `consult` e `doctor`. `setup` è
   un wizard per i target supportati; non è un comando generico per analizzare
   il sorgente del workspace.
2. **Modalità senza interazione e JSON:** esistono comandi con flag espliciti
   come `--yes`, `--dry-run` e `--json`. In particolare,
   `ecc doctor --target copilot --json` restituisce una diagnostica JSON
   sull'installazione ECC gestita. Il CLI non documenta un generico
   `ecc analyze --json`: `doctor` non esegue analisi statica del codice.
   Per i target supportati il dispatcher invia argomenti espliciti al comando
   selezionato; ciò non implica che ogni comando sia non interattivo.
3. **MCP/API:** il pacchetto contiene `ecc-memory-mcp`, un server MCP stdio
   per operazioni di memoria ECC (`memory_save`, `memory_search`,
   `memory_read`, `memory_doctor`). Non è un server MCP che espone tutti gli
   agenti, le skill o i comandi ECC; l'API esportata da `package.json` punta
   all'implementazione OpenCode e non costituisce un'API pubblica generica per
   l'analisi di workspace.
4. **Workspace:** i comandi di installazione possono applicare target e file
   di progetto alla directory selezionata; il comando `doctor` combina il
   percorso di progetto corrente con lo stato nella home dell'utente.
   L'adattamento manuale documentato seleziona a mano singoli file di skill
   e istruzioni. Quindi ECC non è un analizzatore stateless confinato a una
   cartella arbitraria; il perimetro va scelto per comando e configurazione.
5. **VS Code/Copilot:** il README ECC dichiara un adattatore Copilot, ma lo
   descrive come distribuzione di skill e agenti per **Copilot CLI**, con
   istruzioni e prompt; non documenta un'estensione ECC ufficiale per VS Code.
   La documentazione Microsoft corrente descrive `.mcp.json` per server di
   workspace e configurazioni MCP di VS Code, non la chiave
   `github.copilot.chat.mcp.servers` ipotizzata nella richiesta. L'MCP memoria
   non equivale a importare skill/agent mode ECC.

### Diagnosi

Node non è un ostacolo. I blocchi concreti per una integrazione eseguibile
sono la mancanza di Copilot installato nel profilo verificato, l'assenza di
un comando ECC che analizzi il codice del workspace e la differenza fra le
superfici Copilot CLI documentate e il Copilot Agent Mode in VS Code. Una
configurazione MCP limitata alla memoria non coprirebbe l'obiettivo più ampio.

Non è stata eseguita alcuna installazione, invocazione `npx`, modifica di
configurazione personale o prova di autenticazione; non si afferma quindi che
Copilot Agent Mode sia disponibile o autenticato in questo ambiente.

## 2. Piano e criteri di fattibilità GO/NO-GO

### Criteri scritti prima dell'implementazione

Il candidato è GO soltanto se:

1. il setup richiesto all'utente è inferiore a 30 minuti;
2. non richiede modifiche al core JARVIS né a VS Code;
3. non installa dipendenze globali e non accede a `SecretStorage`;
4. il perimetro e le limitazioni sono dichiarati senza presentare un adattamento
   testuale come hook o agenti nativi;
5. la documentazione può essere verificata senza eseguire codice di terze parti
   né accedere a file fuori dal workspace.

**Gate:** C è GO limitatamente a un pilot documentale; A e B sono NO-GO come
integrazione verificabile in questo ambiente. L'Opzione C non dichiara che ECC
sia installato o integrato in Copilot.

### Alternative considerate

| Opzione | Pro | Contro e dipendenze | Rischi di sicurezza | Stima e decisione |
|---|---|---|---|---|
| **A — estensione TypeScript**, `OutputChannel` e `ECC: Analyze Workspace` che avvia `npx ecc` | UX VS Code dedicata; output e annullamento/timeout controllabili nel processo figlio | ECC non documenta un comando generico di analisi del codice. `doctor --json` controlla installazioni, non sorgenti. Richiederebbe progetto extension, Node/npm/npx e accesso alla rete al primo download; Copilot non è disponibile per testare l'Agent Mode | `npx` esegue codice di pacchetto; il CLI può leggere stato nella home e scrivere in base ai target. Il requisito “nessun file fuori workspace” non è dimostrato dal comportamento di `doctor`; serve isolamento e audit del comando effettivo | 60–90 min; **NO-GO** |
| **B — server MCP configurato in VS Code** | Collegamento agent-tool standard senza estensione custom; trasporto stdio supportato da VS Code | L'MCP ECC individuato fornisce strumenti di memoria, non l'intero sistema di skill/agenti né un analizzatore del repository. Occorrono configurazione MCP, runtime/dipendenze, approvazione del server e Copilot Agent Mode verificabile | Un server locale esegue codice e può leggere/scrivere i propri archivi di memoria. `npx` può richiedere rete al primo avvio; non va confuso con strumenti confinati al workspace. Nessun secret di JARVIS va fornito | 30–60 min; **NO-GO** per l'obiettivo completo |
| **C — pilot documentale di pattern selezionati** | Nessuna installazione, rete, dipendenza, modifica VS Code/core o accesso a segreti; il materiale ECC e i limiti si possono valutare in modo reversibile | Non offre discovery automatica, slash command reali, hook eseguibili, orchestrazione nativa o parità funzionale ECC; richiede selezione/revisione manuale delle skill | Rischio ridotto: non copiare pacchetti o hook eseguibili; selezionare solo testo necessario, trattarlo come input non attendibile e rispettare licenze e segreti | <30 min; **GO** limitato alla documentazione |

### Piano dell'Opzione C

Per una successiva prova manuale in un repository scelto dall'utente:

1. scegliere una o due skill ECC pertinenti al linguaggio e al task, più al
   massimo un workflow di verifica;
2. leggere e adattare le condizioni di attivazione e i passi essenziali senza
   copiare l'intero catalogo o aggiungere hook/script;
3. usare prompt cues espliciti per pianificazione, test, implementazione e
   verifica; chiamarli convenzioni d'istruzione, non comandi eseguibili;
4. trascrivere l'intento dei hook come checklist prima/dopo il lavoro, chiarendo
   che non è enforcement automatico;
5. fare un task sintetico e valutare aderenza alle istruzioni e accuratezza
   della dichiarazione dei limiti. Nessuna credenziale deve essere copiata nei
   prompt o nella documentazione.

**Rollback:** rimuovere il solo bundle documentale dal contesto del pilot;
non occorre disinstallare componenti o ripristinare configurazioni.

## 3. Implementazione autorizzata

Confermata dall'utente il 2026-10-26 l'Opzione C. In questa fase si documentano
soltanto il piano, i pattern e i loro limiti. Non vengono creati file di
estensione, prompt/skill installati, configurazioni MCP o modifiche al core
JARVIS.

## 4. Test, risultati e diagnosi post-test

Essendo un'attività solo documentale, non si eseguono test di codice, `npx`,
installazioni o verifiche live dell'Agent Mode. La convalida consiste nel
controllo di coerenza del documento con il README/CLI ECC consultati, con le
istruzioni MCP VS Code e con i controlli locali sopra registrati.

| Criterio | Esito | Evidenza / limite |
|---|---|---|
| Node.js 18+ | VERIFICATO-LIVE | `node -v` ha restituito `v24.13.1` |
| Comandi ECC e opzioni non interattive/JSON | VERIFICATO-LIVE | README, `package.json`, `scripts/ecc.js` e `scripts/doctor.js` pubblici consultati; `ecc doctor --json` non è un'analisi del codice |
| MCP ECC e perimetro funzionale | VERIFICATO-LIVE | Sorgente pubblico `scripts/memory-mcp.mjs`: strumenti di memoria; nessun MCP generale per tutto ECC identificato |
| Estensione ECC e Copilot nel VS Code corrente | PARZIALE | Ricerca Marketplace e `code --list-extensions --show-versions`; nessuna estensione ECC ufficiale identificata e Copilot non elencato. Login/account e Agent Mode live non verificati |
| Pilot C: setup sotto 30 minuti, senza codice o dipendenze | VERIFICATO-TEST | Solo documentazione; nessuna installazione o modifica di VS Code/core |
| Nessun accesso fuori workspace/nessuna esposizione segreti | VERIFICATO-TEST | Nessun processo ECC eseguito e nessun segreto letto; il confinamento runtime di A/B non è dimostrato |

Diagnosi post-test: il gate consente il pilot C solo come adattamento manuale e
documentale. A e B restano NO-GO per una integrazione funzionale verificata
senza prerequisiti aggiuntivi. Non sono provati aderenza di Copilot a skill
adattate, comportamento di agent mode, timeout di un subprocesso, output
workspace analysis o isolamento runtime dei file.

## 5. Prossimi passi condizionati

- Per una prova funzionale, prima verificare/installare Copilot VS Code e
  autenticarsi; richiede un nuovo consenso prima di modifiche o installazioni.
- Valutare B separatamente solo se l'obiettivo è esplicitamente limitato agli
  strumenti di memoria MCP.
- Rivalutare A soltanto dopo aver scelto un comando ECC adatto al task e
  dimostrato mediante test che rispetti timeout, workspace root e assenza di
  accessi esterni al workspace.
- Nessuna di queste attività è autorizzata dalla decisione C corrente.
