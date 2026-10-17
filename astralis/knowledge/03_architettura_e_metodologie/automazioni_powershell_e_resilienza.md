# Automazioni PowerShell, Script Batch e Resilienza Multi-Computer (v3.0.0)
# Autore: Luca (Sviluppatore Senior Non Vedente con Screen Reader NVDA)
# Target AI: Antigravity (Senior AI Pair Programmer & Software Engineer)
# Ambito: Globale / Universale

Questo documento definisce gli standard per la creazione di script di sistema, tool di automazione e configurazioni portabili.

---

## 💻 1. RISOLUZIONE DINAMICA DEI PERCORSI (ZERO HARDCODING)

1. **Divieto Assoluto di Percorsi Statici**:
   - Mai inserire lettere di unità assolute hardcoded (es. `<user-home> fisso).
   - Utilizzare esclusivamente variabili d'ambiente di sistema e percorsi relativi:
     - PowerShell: `$env:USERPROFILE`, `$env:OneDrive`, `$env:APPDATA`, `$PSScriptRoot`.
     - Batch: `%USERPROFILE%`, `%ONEDRIVE%`, `%APPDATA%`, `%~dp0`.
     - Python: `os.environ`, `pathlib.Path.home()`, `Path(__file__).parent`.

2. **Topologia Multi-Macchina (Desktop vs Laptop)**:
   - Rilevare dinamicamente l'hostname attivo tramite `$env:COMPUTERNAME` per applicare impostazioni hardware specifiche (risoluzione schermo, path locali secondari, profili audio).

---

## 🛡️ 2. PREVENZIONE AZIONI DISTRUTTIVE & IDEMPOTENZA

1. **Controllo Preventivo Esistenza (Pre-Flight)**:
   - Prima di scrivere, spostare o leggere un file, verificare sempre l'esistenza del path sorgente e di destinazione (`Test-Path`, `os.path.exists`).
2. **Idempotenza degli Script**:
   - Uno script di setup o bootstrap deve poter essere eseguito più volte di seguito senza generare errori, duplicazioni o stati corrotti.
3. **Messaggistica Chiara per NVDA**:
   - Gli script devono emettere log lineari a terminale: `[INFO]`, `[OK]`, `[ERRORE]` per facilitare la revisione con lo screen reader.

---

## 📦 3. COMPRESSIONE ARCHIVI & PATTERN DI STAGING TEMPORANEO

1. **Prevenzione Conflitti e File Lock**:
   - Quando uno script PowerShell deve comprimere una cartella complessa (o l'intero Master Hub), non creare mai il file `.zip` direttamente all'interno della cartella sorgente.
   - Creare l'archivio compresso in una cartella di staging temporanea (es. `$env:TEMP`) escludendo preventivamente eventuali file `.zip` preesistenti, e spostarlo a destinazione solo a compressione ultimata.

---

## 🔄 4. PATTERN DI SELF-HEALING & UPGRADE NON-DISTRUTTIVO

4. **Pattern di Ripristino Automatico (Self-Healing)**:
   - Gli script e i prompt di aggiornamento non devono mai fallire in presenza di installazioni parziali o corrotte. Se mancano file di radice (`CHANGELOG.md`, `README.md`, `ISTRUZIONI_DI_AVVIO.md`) o moduli standard, la procedura provvede a ripristinarli e allinearli automaticamente alla versione più recente.
2. **Doppio Backup Preventivo del Genoma**:
   - Prima di applicare modifiche strutturali al file di configurazione centrale dell'utente (`~/.gemini/config/GEMINI.md`), creare sempre una copia fissa (`GEMINI.md.bak`) e una copia timestampata (`GEMINI_YYYYMMDD_HHMMSS.bak`).
3. **Fusione Non-Distruttiva delle Regole**:
   - Separare nettamente il livello dei dati utente (nome, modalità screen reader/mouse, path specifici) dal livello delle regole di governance. In fase di aggiornamento, i dati utente vengono estratti e preservati intatti, mentre il blocco delle regole, dei dispatcher e dei moduli viene sincronizzato all'ultima versione.

---

## 🏛️ 5. PATTERN COMPONENT-BASED DISCOVERY DUAL & RELEASES HUB VERSIONATI

1. **Discovery Deterministico a Marker Strutturali Interni (Supporto Duale)**:
   - Negli script che interagiscono con il Master Hub o con repository di configurazione globale, non assumere mai una posizione fissa sul filesystem;
   - *Principio di Discovery Duale*: La libreria delle schede può essere denominata `knowledge/` (nel repository pubblico distribuibile) o `knowledge/` (nel Master Hub locale). Gli script devono verificare che sia presente `(Test-Path "knowledge") -or (Test-Path "knowledge_globale")` insieme agli altri marker (`prompts/`, `templates/`, `scripts/`, `CHANGELOG.md`). Se tutti i marker sono presenti, la radice del sistema è validata con certezza al 100%.
2. **Istituzione della Cartella `releases/` & Zero Desktop Clutter**:
   - Tutti gli archivi compressi, pacchetti di distribuzione o Starter Kit generati devono risiedere nella cartella dedicata `releases/` all'interno del Master Hub;
   - Divieto assoluto di rilasciare archivi di sistema sul Desktop dell'utente.
3. **Generazione Duale & Versioning Immutabile**:
   - Ogni rilascio genera un archivio immutabile con SemVer esplicito (`{Nome}_v{VERSIONE}.zip`, es. `ASTRALIS_Universal_Starter_Kit_v3.0.0.zip`);
   - Mantenere parallelamente aggiornato un puntatore fisso `{Nome}_latest.zip` per facilitare il bootstrap e la condivisione rapida;
   - Escludere tassativamente la cartella `releases/` durante la scansione ricorsiva per impedire annidamenti di ZIP storici dentro i nuovi archivi.
4. **Flessibilità delle Release Personalizzate dell'Utente**:
   - Gli script di packaging devono accettare parametri dinamici (`-Version`, `-CustomTag`, `-DestinationDir`) per consentire all'utente di esportare versioni custom con etichette personalizzate su qualsiasi supporto o cartella.

---

## ☁️ 6. GESTIONE RESILIENTE DEI CLOUD LOCK (ONEDRIVE / DROPBOX) SULLE DIRECTORY DI BUILD

1. **La Diagnostica del Lock da Provider Cloud**:
   - Quando un repository risiede all'interno di una cartella sincronizzata da OneDrive o Dropbox, i file intermedi generati dai compilatori (es. `.class`, `.jar`, estratti `.json` in `build/` o `target/`) vengono indicizzati in background dal servizio cloud.
   - Questo provoca errori bloccanti nei task di pulizia o ricompilazione incrementale: `Cannot snapshot ... not a regular file` oppure `Unable to delete directory 'build'`.
2. **Strategia di Bonifica Atomica a 3 Livelli**:
   - *Livello 1 (Arresto Daemon)*: Arrestare preventivamente eventuali processi di background con `.\gradlew.bat --stop`.
   - *Livello 2 (Rimozione Forzata Nativa PowerShell)*: Scavalcare i limiti del tool di compilazione eseguendo un comando atomico nativo con soppressione errori e verifica booleana:
     ```powershell
     Remove-Item -Recurse -Force build -ErrorAction SilentlyContinue; Test-Path build
     ```
   - *Livello 3 (Compilazione Isolata)*: Rieseguire il task di compilazione/test con il flag obbligatorio `--no-daemon`, prevenendo l'aggancio di file da parte di worker orfani.
   - *Livello 4 (Disattivazione File System Watcher `--no-watch-fs`)*:
     - Nei runner di compilazione e test (in particolare Gradle su Windows), associare sistematicamente il flag `--no-watch-fs` per impedire al watcher interno di scansionare i reparse points e i file segnaposto cloud di OneDrive/Dropbox, azzerando gli errori di tipo `IOException: Cannot snapshot ... not a regular file`:
     ```powershell
     .\gradlew.bat --no-daemon --no-watch-fs test
     ```

---

## 🛡️ 6. ARCHITETTURA MULTI-CANALE DI RESILIENZA, VERSIONAMENTO & CLOUD (ASTRALIS v3.0.0)

1. **Disaccoppiamento dei 4 Canali per Scopo Funzionale**:
   - I servizi di archiviazione e cloud (Git, OneDrive, Google Drive) non sono intercambiabili né ridondanti, ma assolvono a ruoli complementari:
     * **Canale 1 — Versionamento del Codice (VCS / GitHub)**: Storia atomica dei sorgenti, diff, branch, PR. Esclusione tassativa di binari > 10 MB, cartelle saves o cache pesanti;
     * **Canale 2 — Ponte Operativo Multi-Macchina (Operational Hot Bridge)**: Sincronizzazione dinamica in tempo reale di salvataggi runtime, dati di test e profili tra computer diversi (es. Desktop Salotto <-> Laptop MSI) su cartella cloud dedicata;
     * **Canale 3 — Archivio Storico & Disaster Recovery (Cold Storage)**: Conservazione di snapshot di sicurezza preventivi (es. pre-fill), build release compilate e backup consolidati di lungo periodo;
     * **Canale 4 — Backup Primario Resiliente (Sostitutivo di Git per Progetti No-VCS)**: Per utenti o progetti non tecnici che non usano Git, ASTRALIS esegue snapshot zip timestampati in cloud ad ogni chiusura tecnica.

2. **Probing Adattivo in Bootstrap & Aggiornamento**:
   - Durante il bootstrap (Protocollo 9) e l'aggiornamento (Protocollo 8), ASTRALIS rileva automaticamente la configurazione del progetto:
     * *Se `.git` è presente*: rileva remote e branch attivo;
     * *Se `.git` è assente*: consiglia con linguaggio semplice e non tedioso l'adozione di Git; se rifiutato, richiede e configura la cartella cloud per il Canale 4.

3. **Resilienza ai Lock Cloud**:
   - Nei processi di build (Gradle, Maven, PyInstaller), passare sempre flag anti-demone (`--no-daemon`) e usare directory temporanee `$env:TEMP` per prevenire lock di file da parte del client di sincronizzazione OneDrive/Google Drive.

---

## 💻 7. IGIENE DEI CARATTERI SPECIALI & CODEPAGE CONSOLE IN POWERSHELL

1. **La Diagnostica del Lock da Codepage (Windows PowerShell 5.1 vs Core 7)**:
   - Su console Windows tradizionali con codepage legacy (`chcp 850` / `Windows-1252`), caratteri tipografici multibyte non-ASCII (come trattini lunghi em-dash `—`, virgolette curve o simboli grafici complessi) nelle stringhe dei comandi `Write-Host` o nei commenti possono provocare fallimenti di parsing immediati (`ParseException: AmpersandNotAllowed` o terminatori di stringa mancanti);
2. **Standard di Scrittura Resiliente per Script di Sistema**:
   - *Separatori e Titoli*: Usare esclusivamente caratteri ASCII standard per i separatori di testo (es. `--` o `==`, mai trattini tipografici lunghi);
   - *Caratteri Riservati PowerShell*: Qualsiasi `&` presente in stringhe di output deve essere opportunamente racchiusa tra virgolette o passata in stringhe letterali (`'@ ... '@`);
   - *Igiene File UTF-8*: Tutti gli script `.ps1` devono essere codificati in UTF-8 senza BOM (`New-Object System.Text.UTF8Encoding($false)`) per garantire massima portabilità cross-platform.
   - *Prevenzione BOM UTF-8 per la Generazione di Codice e Risorse (`javac` compatibility)*:
     * I cmdlet nativi di Windows PowerShell 5.1 (`Set-Content -Encoding UTF8` o `Out-File -Encoding UTF8`) inseriscono sistematicamente il marcatore BOM a 3 byte (`0xEF, 0xBB, 0xBF`) all'inizio del file;
     * Quando script di automazione generano o modificano file sorgente (`.java`, `.json`, `.c`), la presenza del BOM causa il fallimento istantaneo del compilatore Java (`javac`) con l'errore: `error: illegal character: '\ufeff'`;
     * **Canone Obbligatorio di Scrittura**: Qualsiasi file di progetto generato tramite automazioni PowerShell deve essere scritto tramite API .NET esplicita priva di BOM:
       ```powershell
       $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
       [System.IO.File]::WriteAllText($path, $content.Replace("`n","`r`n"), $utf8NoBom)
       ```

---

## ⏱️ 8. RUNNER TEST RESILIENTI, WATCHDOG TIMEOUT & PREVENZIONE FREEZE CONSOLE

1. **Limiti di `Start-Process -Wait` e Rischio Deadlock**:
   - Il costrutto nativo `Start-Process -Wait` non dispone di timeout e attende indefinitamente se il processo figlio entra in loop, si blocca all'avvio dell'engine o se la console Windows (`conhost.exe`) entra in modalità di selezione/pausa QuickEdit.
   - Nello sviluppo con screen reader (NVDA), un runner bloccato causa silenzio assoluto e disorientamento per lo sviluppatore non vedente.

2. **Pattern Canonico Watchdog Basato su `.NET System.Diagnostics.Process`**:
   - Avviare il processo child tramite `[System.Diagnostics.Process]::Start($psi)` (impostando `UseShellExecute = $false`).
   - Applicare sempre un timeout perentorio tramite `$proc.WaitForExit($timeoutMs)` (es. 15.000 ms per singolo test unitario).
   - In caso di superamento del timeout (`-not $finishedInTime`), abbattere forzatamente il processo con `try { $proc.Kill() } catch {}`, registrare il fallimento con messaggio chiaro per NVDA e proseguire con il resto della suite senza bloccare il terminale.
   - Eseguire all'avvio del runner una pulizia preventiva di eventuali processi orfani rimasti congelati in memoria (`Get-Process | Where-Object { ... } | Stop-Process -Force -ErrorAction SilentlyContinue`).
   - Fornire sempre un indicatore di avanzamento progressivo lineare (es. `[$CurrentIndex/$TotalCount] Esecuzione: $TestName...`) che NVDA possa leggere riga per riga.
