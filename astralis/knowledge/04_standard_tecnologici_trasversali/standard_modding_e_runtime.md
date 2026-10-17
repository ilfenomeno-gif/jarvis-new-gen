# Standard Modding, Mod Loader e Gestione Runtime Congelati (v3.0.0)
# Autore: Luca (Sviluppatore Senior Non Vedente con Screen Reader NVDA)
# Target AI: Antigravity (Senior AI Pair Programmer & Software Engineer)
# Ambito: Globale / Universale

Questo documento definisce i criteri di stabilitÃ , sicurezza e isolamento per il modding di videogiochi, runtime di terze parti e gestione dei fork open-source.

---

## ðŸ›¡ï¸ 1. GESTIONE RUNTIME CONGELATI E PROTETTI

1. **Versioni Fissate e Protezione Aggiornamenti**:
   - Le versioni degli eseguibili di gioco e dei mod loader (es. SKSE, RED4ext, CET, SMAPI, Fabric) devono essere censite e congelate.
   - Proteggere i file di manifesto (es. `appmanifest_*.acf` su Steam) per impedire aggiornamenti automatici silenti che corrompano i binari.

2. **Isolamento dei Salvataggi (Profili di Test)**:
   - Utilizzare sempre profili di mod organizer separati (es. MO2 con `LocalSaves=true`).
   - Mai caricare salvataggi di campagne reali su profili di debug/test.

---

## ðŸŒ 2. DISCIPLINA FORK OPEN-SOURCE E MULTILINGUA (I18N)

1. **IntegritÃ  dei File Upstream**:
   - I file di configurazione, documentazione e traduzione in lingua inglese (`*_ENGLISH.txt`) devono rimanere in inglese puro per consentire pull request pulite verso i repository open-source a monte.
2. **Localizzazione Italiana Isolata**:
   - Tutte le traduzioni e le ottimizzazioni in lingua italiana devono essere isolate nei file dedicati (`*_ITALIAN.txt`, `it_it.json`), garantendo zero conflitti con l'albero di sviluppo upstream.

---

## ðŸ”Œ 3. STANDARD PROTOCOLLI MULTIPLAYER CLIENT-SERVER & OFFLINE UUIDS

1. **Topologia e Calcolo Offline UUIDs (ModalitÃ  Mista LAN/Dedicata)**:
   - Nei server di sviluppo o dedicati operanti in modalitÃ  `online-mode=false`, l'UUID del giocatore non viene interrogato sui server di autenticazione centralizzati ma Ã¨ calcolato in locale tramite RFC 4122 v3 (MD5 dei byte UTF-8 della stringa `"OfflinePlayer:" + username`):
     $$\text{UUID}_{\text{offline}} = \text{UUID.nameUUIDFromBytes}\left(\text{"OfflinePlayer:"} + \text{username}\right)$$
   - Nei file di permessi e ruoli amministrativi del server (`ops.json`, permessi mod), registrare sempre **sia l'UUID online ufficiale che l'UUID offline calcolato**, garantendo che il giocatore mantenga ininterrottamente i privilegi di amministratore a prescindere dal tipo di sessione o profilo attivo.
2. **IntegritÃ  dei Parametri di Rete e Lunghezza Username**:
   - I protocolli di rete voxel/multiplayer (es. `ServerboundHelloPacket`) impongono limiti rigidi e tassativi sulla lunghezza del nickname (massimo **16 caratteri**).
   - Nelle automazioni di configurazione launcher (es. PrismLauncher, MultiMC), verificare che il campo `userName` sia popolato esclusivamente con il nickname puro (`username`), impedendo fallback involontari su etichette di visualizzazione del launcher (es. `"Nickname (Microsoft)"`, lunghe $> 16$ caratteri) che generano errori `EncoderException: String too big`.

---

## ðŸ•¹ï¸ 4. STANDARD GESTIONE INPUT, BINDINGS E PREFERENZE UTENTE

1. **Pre-Audit di Collisione Input a Doppio Livello (Livello Engine/Vanilla vs Livello Mod)**:
   - Quando si progetta una combinazione con tasti modificatori (`Alt`, `Ctrl`, `Shift`) in mod di gioco o applicazioni native, verificare tassativamente che il tasto base non sia intercettato a monte dai gestori nativi dell'engine senza controllo modificatori (es. in Minecraft `T` apre la chat, `E` apre l'inventario, `Q` getta l'oggetto anche se combinati con `Alt`).
   - Assegnare unicamente tasti neutri e privi di binding nativi (es. `B`, `P`) per evitare che l'engine consumi l'evento prima della logica di modding.

2. **Sincronizzazione Obbligatoria della Cache Preferenze Utente (`options.txt` / cfg / ini)**:
   - I motori di gioco danno prioritÃ  assoluta ai binding serializzati nei file di opzioni utente (`options.txt`) rispetto ai valori di default (`withDefault`) definiti nel codice Java/C#.
   - **Vincolo di Deploy**: Se durante una sessione di refactoring viene modificato il tasto di default di un comando precedentemente distribuito e testato, l'assistente deve aggiornare programmaticamente anche i file di opzioni delle istanze attive prima di richiedere il collaudo manuale.

3. **Gestione Asincrona del Ciclo di Vita Input (Pattern Tripla Barriera per Press, Release e Click Accumulator)**:
   - I sistemi di binding moddati o i framework UI ad alto livello consumano tipicamente solo l'evento di pressione (`action == 1`, `KEY_PRESS`). Tuttavia, molti motori di gioco (es. Minecraft, Unity, Unreal) legano determinate funzioni native al rilascio del tasto (`action == 0`, `KEY_RELEASE`) o ad accumulatori di click per tick (`consumeClick()`).
   - Se la mod consuma solo il press, l'engine riceve il release "a vuoto" e attiva la funzione nativa indesiderata (es. apertura Debug Screen su release di `F3`), oppure accumula click nel contatore interno (es. cambio prospettiva su `F5` o toggle HUD su `F1`).
   - **Regola Standard della Tripla Barriera Non Invasiva**:
     * *Barriera 1 (Layer Binding)*: Soppressione dell'evento press nel framework di keybinding;
     * *Barriera 2 (Target Component Override)*: Neutralizzazione diretta a monte del componente o metodo di business nativo (es. Mixin con `ci.cancel()` su `toggleDebugOverlay()`);
     * *Barriera 3 (Accumulator Drain)*: Svuotamento preventivo a vuoto dei click pendenti (`while (keyMapping.consumeClick())`) all'inizio del tick di input.

4. **Simmetria Hardware Obbligatoria per Tasti Modificatori**:
   - Nei livelli grafici/input a basso livello (GLFW, Win32, X11), i tasti `Control`, `Alt` e `Shift` presentano keycode e scancode distinti per lato sinistro e destro (`GLFW_KEY_LEFT_CONTROL` vs `GLFW_KEY_RIGHT_CONTROL`, `VK_LCONTROL` vs `VK_RCONTROL`).
   - Molti framework o helper interrogano unicamente il tasto sinistro o una maschera generica.
   - **Regola di AccessibilitÃ **: Le routine di verifica dei modificatori (`hasControl()`, `hasAlt()`, `hasShift()`) devono interrogare sempre e congiuntamente sia il tasto sinistro che il tasto destro dell'hardware. L'asimmetria spezza l'ergonomia per sviluppatori e giocatori non vedenti che utilizzano comandi a due mani o manovrano il tastierino numerico.

---

## âš™ï¸ 5. STANDARD CLOTH CONFIG, AUTOCONFIG & REFLECTION SAFETY

1. **Esclusione Obbligatoria di Campi Statici e Singleton (`@ConfigEntry.Gui.Excluded`)**:
   - Le librerie di configurazione basate su reflection (es. Cloth Config / AutoConfig per Fabric, NeoForge e Forge) analizzano per riflessione tutti i campi dichiarati nelle classi `@Config`.
   - I campi statici di utilitÃ , logger e istanze singleton (`private static Config instance;`) devono essere tassativamente marcati con `@ConfigEntry.Gui.Excluded`.
   - In assenza di questa annotazione, la reflection tenta di istanziare un widget di editing GUI per l'oggetto stesso, generando errori a runtime nei log (`No GUI provider registered for field`).

2. **Trattamento Polimorfico delle Interfacce GUI nei Classloader Modulari**:
   - Nei runtime con classloader avanzati (es. Knot di Fabric), non dare per scontate le classi concrete sottostanti agli oggetti dell'engine.
   - Trattare sempre le categorie, menu e tab tramite le relative interfacce polimorfiche pubbliche evitando downcast forzati a classi concrete non universali.

3. **Estrazione Identificatori di Registro vs toString() in Ambienti Mojmap Moderni (1.21+ / 26.2)**:
   - In Minecraft moderno, molte entitÃ  e categorie (es. `RecipeBookCategory`, `CreativeModeTab`, `Biome`, `Block`) sono registrate dinamicamente e non implementano un `.toString()` user-friendly, restituendo il puntatore Java di default (`NomeClasse@hashcode`).
   - **Risoluzione da Registro Tassativa**: Utilizzare sempre `BuiltInRegistries.<REGISTRO>.getKey(oggetto)` per ottenere l'`Identifier` univoco (`namespace:path`).
   - **Supporto Enum e Search Tabs**: Gestire con pattern matching `instanceof` le implementazioni enum polimorfiche (es. `SearchRecipeBookCategory`).
   - **Fallback Resilienti No-Hash**: Qualsiasi fallback `toString()` deve verificare `if (fallback.contains("@")) return I18n.get("chiave.sconosciuto");` per prevenire la pronuncia di hash esadecimali all'utente non vedente.
4. **Disciplina dei Campi di Configurazione Persistiti Legacy (De-Risking GUI vs Schema)**:
   - *Verifica Preliminare di Persistenza*: Prima di eliminare, rinominare o marcare `transient` un campo di configurazione, Ã¨ fatto obbligo di verificare se esso sia presente nei file di configurazione reali su disco e se appartenga a contratti di compatibilitÃ , rollback o downgrade.
   - *De-Risking Visivo Temporaneo*: Se la conservazione dei dati pregressi Ã¨ necessaria, il campo resta temporaneamente serializzabile e puÃ² essere escluso dalla GUI tramite il meccanismo supportato dal framework (es. `@ConfigEntry.Gui.Excluded`). L'esclusione visiva dalla GUI non equivale alla cancellazione del dato e non costituisce automaticamente una soluzione permanente.
   - *Criterio di Rimozione Definitiva*: La rimozione definitiva del campo Ã¨ ammessa esclusivamente in presenza di una procedura di migrazione esplicita e versionata, corredata da snapshot di backup, criteri di compatibilitÃ  e test deterministici.
   - *Matrice Minima di Test di Serializzazione*: La verifica deve impiegare, per quanto possibile, la pipeline di serializzazione produttiva e comprendere almeno:
     1. Campo presente con valore reale d'uso;
     2. Campo presente con valore alternativo;
     3. Valore limite significativo (boundary o zero);
     4. Campo assente (validazione del default);
     5. Ciclo di salvataggio e rilettura;
     6. Ispezione riflessiva dell'annotazione di esclusione GUI, se tale meccanismo Ã¨ stato adottato.

---

## ðŸŒ¿ 6. DISCIPLINA DUAL-TRACK CHANGELOG NEI FORK & ISOLAMENTO PR UPSTREAM

Quando si opera all'interno di un repository derivato da un progetto open-source di terzi (fork), l'assistente applica tassativamente il modello di disaccoppiamento strategico in due binari:

1. **Binario Pubblico Upstream (`CHANGELOG.md` di radice)**:
   - Redatto nella lingua ufficiale dell'upstream (es. Inglese puro) adottando lo standard *Keep a Changelog*;
   - Utilizza esclusivamente la sezione **`## [Unreleased]`** in cima al file per raccogliere tutte le feature, modifiche e fix sviluppati nel fork;
   - **Zero Version Forcing**: Non impone numeri di versione ufficiali che spetterebbero ai maintainer upstream, garantendo Pull Request pulite, eleganti e immediatamente mergeabili senza conflitti.

2. **Binario Sovrano Personale (`knowledge/NN_diario_modifiche_e_contributi_fork.md`)**:
   - Redatto in **lingua Italiana** all'interno della cartella `knowledge/`;
   - Applica la disciplina del **Versionamento Semantico Sovrano AVF a 3+1 livelli** (`V.A.R[.M]`) per le build personali/locali dello sviluppatore;
   - Raccoglie il razionale architetturale, le note di accessibilitÃ  per screen reader NVDA e la cronologia completa delle versioni locali;
   - **Clausola di SovranitÃ  & Zero Lock-In**: Qualora lo sviluppatore decida in futuro di distribuire la mod come software autonomo o hard fork, il diario sovrano AVF costituisce giÃ  un changelog storico valido e completo sin dal giorno zero.

3. **Regola di Isolamento Assoluto delle Pull Request Upstream**:
   - Quando si crea un branch per una PR verso il repository a monte (es. `pr/feature-name` basato su `upstream/dev`):
     * **Incluso nella PR**: Unicamente il codice sorgente modificato, i file di risorse/lingua pertinenti, i test unitari e le righe descrittive sotto `## [Unreleased]` in `CHANGELOG.md`.
     * **Tassativamente Escluso dalla PR**: `gemini.md`, l'intera cartella `knowledge/`, le cartelle `docs/piani/` e `docs/report/`, i prompt e qualsiasi file di governance locale di ASTRALIS.

---

## â˜• 7. DISCIPLINA RUNTIME GRADLE & CONFIGURAZIONE DETERMINISTICA MULTI-JDK

Nei progetti di modding avanzato (es. Minecraft 26.2 con requisiti Java 25) che operano su macchine di sviluppo dotate di versioni JDK eterogenee:

1. **Il Rischio di Conflitto JVM di Sistema**:
   - Quando la shell di sistema (PowerShell/CMD) ha una variabile `JAVA_HOME` o `Path` puntata su un JDK legacy (es. Java 22 o 17), l'invocazione di `gradlew` con task inter-progetto (`:fabric:test`, `:neoforge:test`) puÃ² fallire con errori di incompatibilitÃ  binaria (`Dependency resolution is looking for a library compatible with JVM runtime version 22, but root project is only compatible with JVM runtime version 25 or newer`).
2. **La Soluzione Deterministica in `gradle.properties`**:
   - Impostare tassativamente sia il percorso di runtime sia i percorsi di installazione in `gradle.properties`:
     ```properties
     org.gradle.java.home=C:/Users/<Username>/AppData/Roaming/PrismLauncher/java/java-runtime-epsilon
     org.gradle.java.installations.paths=C:/Users/<Username>/AppData/Roaming/PrismLauncher/java/java-runtime-epsilon
     ```
   - Questa configurazione garantisce che Gradle utilizzi la JVM corretta fin dal processo di bootstrap del daemon/single-use runner, rendendo la compilazione `shadowJar` e l'esecuzione dei test 100% riproducibili indipendentemente dallo stato globale del sistema operativo.

---

## ðŸ–¥ï¸ 8. STANDARD DISPLAY TWEAKS, MODALITÃ€ BORDERLESS & STABILITÃ€ ALT-TAB CON SCREEN READER

1. **Configurazione Borderless e Minimizzazione Forzata (`ForceMinimize=true`)**:
   - Nelle mod di ottimizzazione video (es. SSE Display Tweaks, Special K o wrapper DXGI), la modalitÃ  Borderless Windowed deve sempre essere accompagnata dalla minimizzazione forzata alla perdita di focus (`ForceMinimize=true`) accanto a `Fullscreen=false` e `Borderless=true`.
   - Questo garantisce che, quando il gioco perde il focus, la finestra grafica 3D a pieno schermo si riduca a icona senza rimanere in sovrimpressione, consentendo allo screen reader (NVDA/JAWS) di interagire con il desktop e con le altre applicazioni.
2. **La Dinamica di Alt-Tab su Finestra Singola (Windows 11) & Lezione Architetturale**:
   - Su Windows 11 `Alt+Tab` commuta unicamente tra finestre applicative attive e non include il desktop puro.
   - PoichÃ© `ForceMinimize` si innesca solo quando la finestra riceve `WM_KILLFOCUS`, se il gioco Ã¨ l'unica applicazione aperta, Windows 11 non trova target verso cui passare il focus e non genera la perdita di focus, trattenendo il giocatore nella finestra.
   - *Best Practice Operativa (Soluzione Minima Efficace)*: Tenere sempre aperta almeno un'applicazione di supporto in background (es. launcher, mod organizer, blocco note) prima di avviare il gioco per consentire il normale transito di `Alt+Tab`.
   - *Rifiuto dell'Overengineering a Basso Livello*: L'ipotesi di intercettare combinazioni come `Win+M` o `Win+D` via plugin C++ a basso livello (richiedendo vtable hook, latch FSM, atomici e subclassing Win32 `WndProc` per tracciare il ciclo di vita asincrono della finestra) introduce una complessitÃ  e fragilitÃ  manutentiva del tutto sproporzionata rispetto al problema reale. La configurazione display esistente unita alla presenza di una finestra concorrente costituisce la soluzione corretta e architetturalmente sana.


---

## ðŸ”¤ 9. DISCIPLINA DEI MOTORI DI TRADUZIONE NATIVI C++ (LOOKUP ESATTO SENZA TRIM)

1. **Il Rischio di Fallback Inglese Silente**:
   - Se il layer di localizzazione nativo C++ effettua una ricerca esatta in mappa hash (`std::unordered_map::find(englishKey)`) senza normalizzazione (trim degli spazi bianchi o conversione case-insensitive), qualsiasi minima divergenza tipografica genera il fallimento del lookup e il fallback silente alla stringa inglese originaria.
2. **Regola di ConformitÃ  Tipografica nei File di Lingua**:
   - Censire preliminarmente l'intero catalogo di chiamate `TR(...)` o chiavi inglesi upstream;
   - Mappare esplicitamente nei file di traduzione dedicati sia le varianti con maiuscole/minuscole differenti (es. `Armor` vs `armor`, `Empty` vs `empty`, `Up` vs `up`), sia le chiavi con spazi significativi iniziali o finali (es. `perks to increase: ` con spazio finale, ` of `, `, you have `), garantendo una copertura al 100% priva di lacune vocali.

---

## ðŸŽ® 10. INIEZIONE EVENTI SINTETICI NEI RUNTIME COMPLESSI (PRE-DISPATCHER CHAIN VS POST-DISPATCHER BYPASS)

Quando un'applicazione di accessibilitÃ  o una mod C++/C#/Java necessita di sintetizzare eventi di input (mouse, tastiera, gamepad) all'interno di motori di gioco complessi a stati (es. Creation Engine, Unity, Unreal Engine):

1. **Divieto di Bypass a Valle Non Motivato**:
   - Non invocare direttamente un gestore di basso livello finchÃ© non siano state ricostruite la proprietÃ  del flusso, le precondizioni e l'eventuale elaborazione svolta dal dispatcher.
   - I gestori possono dipendere da validazioni interne di stato (`CanProcess`), contesti modali, stringhe semantiche e curve di sensibilitÃ . L'ingresso diretto Ã¨ lecito soltanto quando l'API documentata assegna al gestore la proprietÃ  completa dell'operazione e una prova mirata lo conferma.
2. **Pre-Dispatcher Chaining Condizionato alla ProprietÃ  Nativa**:
   - Se filtri, ordine dei gestori, sensibilitÃ  e controlli di stato appartengono al dispatcher centrale, la via corretta consiste nell'iniettare l'evento in cima alla catena nativa (`eventHead`) prima della sua unica elaborazione originale.
   - Inserendo l'evento in testa alla lista (`event->next = head`), il motore puÃ² applicare la propria pipeline completa e preservare la coesistenza tra periferiche fisiche ed eventi sintetici. Questo pattern non va generalizzato ai runtime nei quali la proprietÃ  Ã¨ esposta in modo diverso.
3. **Rispetto delle Semantiche di Memoria & Gestione RAII**:
   - Allocare le strutture dati dell'evento con l'allocatore richiesto dall'host e distinguere quattro operazioni: memoria grezza, eventuale posizionamento della vtable, costruzione dei soli oggetti o sottoggetti previsti dall'API, deallocazione finale.
   - `std::construct_at` non va usato per dichiarare costruito un oggetto completo quando il costruttore non Ã¨ esposto o non Ã¨ il meccanismo del runtime. `std::destroy_at` deve essere applicato simmetricamente soltanto agli oggetti o sottoggetti realmente costruiti, prima del rilascio con l'allocatore corretto.
4. **Taratura Empirica Obiettiva Ancorata all'Hardware Reale**:
   - L'ampiezza e la cadenza dei delta di input sintetici non devono mai essere decise in base a stime ipotetiche o costanti arbitrarie.
   - Condurre preliminarmente una sessione di telemetria passiva sul dispositivo fisico reale per misurare i valori raw generati dall'hardware (es. delta Y e millisecondi tra i pacchetti), calibrando l'iniezione sintetica esattamente su tali grandezze per garantire una risposta naturale e perfettamente percettibile.

---

## ðŸ›¡ï¸ 11. STANDARD PROXY DLL X64 NATIVO & PIPELINE PURE FORWARDER ZERO-STUB (`lib.exe` -> `.exp` + `link.exe`)

Nel reverse engineering, hooking e modding nativo su architettura x64 (Windows C++):

1. **Il Limite del Proxying Manuale con Stub C++**:
   - Scrivere funzioni stub C/C++ per decine o centinaia di export (es. 130 funzioni di una libreria grafica come DevIL o DirectX) introduce complessitÃ  enorme, rischio di disallineamento della convenzione di chiamata (`__cdecl`, `__stdcall`, `__fastcall`), alterazione dei registri volatili (`RAX`, `RCX`, `RDX`, `R8`, `R9`) e overhead prestazionale.
2. **La Trappola di `link.exe /DEF` Diretto su x64**:
   - Su architettura x64, passare un file `.def` con direttive di export forwarding puro (`NomeSimbolo=Originale.NomeSimbolo`) direttamente a `link.exe /DEF:exports.def` genera falsi errori di collegamento `LNK2001: unresolved external symbol NomeSimbolo`.
   - Il linker MSVC a 64-bit richiede che il simbolo forwardato sia preliminarmente risolto in un file di esportazione binario (`.exp`).
3. **Pipeline di Generazione Deterministica a 2 Stadi (Zero-Stub Integrity)**:
   - *Stadio 1 (Generazione .exp e .lib)*: Invocare il bibliotecario MSVC:
     `lib.exe /DEF:exports.def /MACHINE:X64 /OUT:exports.lib`
     Questo comando produce deterministicamente sia `exports.lib` sia il fondamentale `exports.exp`.
   - *Stadio 2 (Collegamento Diretto)*: Invocare il linker passando `exports.exp` tra gli input del comando:
     `link.exe /DLL /OUT:proxy.dll proxy_main.obj exports.exp ...`
   - *Risultato Architetturale*: Il loader di Windows risolve il forwarding a livello di tabella degli export (`EAT`) al 100% nativo. Il proxy DLL contiene 0 righe di stub C++ per le funzioni inoltrate, garantendo zero overhead, zero desincronizzazione ABI e massima pulizia manutentiva.
4. **Vincolo sul Naming della DLL Originale Forwardata**:
   - Evitare tassativamente nomi contenenti doppi punti o estensioni multiple (es. non usare `DevIL.original.dll`).
   - Il parser del loader delle direttive di forward interpreta il punto come separatore tra modulo e funzione (`NomeDLL.NomeSimbolo`). Usare sempre l'underscore (es. `DevIL_original.dll`).

---

## 🔐 12. STANDARD WINDOWS 11 SMART APP CONTROL (SAC), CODE INTEGRITY & IL PARADOSSO DEI CERTIFICATI AUTOFIRMATI (MODALITÀ NOTSIGNED)

1. **La Politica di Blocco Kernel (Smart App Control & Code Integrity)**:
   - Su Windows 11 moderno, quando Smart App Control (SAC) o le policy di Device Guard/WDAC sono attive (`VerifiedAndReputablePolicyState: 1` nel Registro di sistema), il sottosistema Code Integrity del kernel verifica la reputazione e l'integrità di ogni libreria caricata dai processi.
   - *Sintomo Forense*: Finestra di dialogo: *"Errore durante il caricamento della DLL <nome>.dll"* all'avvio, oppure arresto istantaneo a 0 ms. Nel log `Microsoft-Windows-CodeIntegrity/Operational` compaiono gli Event ID `3077`, `3033`, `3118` con `WinError 4551` (`ERROR_HVCI_POLICY_VIOLATION`: *"Un criterio di controllo dell'applicazione ha bloccato il file"*).

2. **La Falsa Pista dei Certificati Autofirmati Locali**:
   - Una prima analisi teorica suggerirebbe di apporre una firma Authenticode generata con un certificato autofirmato locale (`New-SelfSignedCertificate`).
   - **La Trappola di Smart App Control**: Un certificato autofirmato locale generato nello store utente/macchina è privo di una Catena CA fidata e riconosciuta (`Status: UnknownError`). Quando Smart App Control ispeziona un file dotato di una firma non fidata, lo classifica come firma anomala/corrotta e **interviene attivamente a livello di kernel bloccando il caricamento della DLL** con codice 4551.

3. **La Soluzione Canonica Universale: Il Paradigma NotSigned (Non Firmato)**:
   - Come dimostrato dall'esperienza empirica consolidata su molteplici progetti di modding (es. `Civ-V-Access` con `lua51_Win32.dll`, `SkyrimAccess` con `LevelLook.dll` e `PowerRevolutionAccess` con `DevIL.dll`), le librerie proxy modded collocate direttamente nelle cartelle applicative locali del gioco (Steam, GOG, ecc.) **non devono essere firmate** con certificati autofirmati.
   - Un binario non firmato (`NotSigned`) non innesca il rifiuto per firma corrotta/non valida da parte di Code Integrity e viene caricato regolarmente e all'istante (`LoadLibraryW` codice 0).
   - **Regola di Governance Universale**: Nei file di compilazione (`build.ps1`), escludere tassativamente l'auto-firma Authenticode con certificati locali fittizi. Lasciare il binario in stato `NotSigned`, garantendo compatibilità universale e assenza totale di blocchi 4551 su Windows 11.

---

## 🎬 13. STANDARD SINCRONIZZAZIONE AVVIO CON VIDEO DIRECTSHOW / INTRO SPLASH & LOG WATCHER DIFFERENZIALE

1. **Il Problema del Mascheramento Temporale**:
   - Molti motori di gioco complessi (es. Eversim in *Power & Revolution*) riproducono filmati introduttivi DirectShow a schermo intero (`vid/intro.AVI`) per diversi secondi prima di istanziare e renderizzare l'interfaccia grafica reale (`Accueil`).
   - Aprire un menu virtuale o avviare la navigazione vocale subito dopo la creazione della finestra di rendering crea una grave desincronizzazione: l'utente non vedente crede di interagire con il menu mentre a schermo scorre un video, e gli input rischiano di collidere con il player multimediale.

2. **Monitor Asincrono Differenziale del Log di Sistema**:
   - Avviare un thread asincrono a basso impatto che monitora il file di log diagnostico dell'engine (es. `_error.txt` in Documenti).
   - Calcolare l'offset iniziale (`startOffset`) ed eseguire letture non bloccanti solo sui nuovi byte scritti (`FILE_SHARE_READ | FILE_SHARE_WRITE`).
   - Alla comparsa della stringa indicante la riproduzione del filmato (`vid/intro`), emettere tempestivamente l'istruzione vocale per saltare con Spazio (*"Premere Spazio per continuare al Menu Principale"*).

3. **Pass-Through Trasparente di Interruzione Video**:
   - Alla pressione del tasto di skip (`VK_SPACE`), l'hook di input della mod **non deve sopprimere il messaggio**, ma inoltrarlo trasparentemente alla `WndProc` originale del motore (`CallWindowProcW`) per interrompere immediatamente il filmato, fornendo contemporaneamente feedback vocale immediato (*"Caricamento Menu Principale..."*).
   - Solo al rilevamento effettivo della schermata di destinazione nel log (`Accueil` / `bootgameend`), il sistema attiva automaticamente l'albero del menu virtuale accessibile con pattern `firstRead`.
