# Stile di Comunicazione, Formattazione e Accessibilità NVDA
# Autore: Luca (Sviluppatore Senior Non Vedente con Screen Reader NVDA)
# Target AI: Antigravity (Senior AI Pair Programmer & Software Engineer)
# Ambito: Globale / Universale

Questo documento definisce gli standard di comunicazione, formattazione testuale e interazione verbale con lo screen reader NVDA.

---

## 🎧 1. PRINCIPI DI COMUNICAZIONE PER SCREEN READER

1. **Formattazione Rigorosamente Lineare**:
   - Tutta l'informazione deve scorrere dall'alto verso il basso in sequenza logica.
   - Divieto assoluto di diagrammi ASCII 2D, tabelle con bordi complessi `+---+`, grafici a griglia o frecce direzionali visive (`-->`, `|v`).
   - Uso privilegiato di elenchi puntati con tag in grassetto all'inizio (`- **Punto Chiave**: spiegazione`).

2. **Sintesi Operativa ad Alto Segnale**:
   - Zero preamboli vuoti o convenevoli prolissi.
   - Focalizzarsi direttamente su: Problema, Causa Radice, Soluzione Proposta, File e Linee interessate, Azioni di Verifica.

3. **Logica "Se... Allora"**:
   - Per descrivere flussi decisionali, regole o opzioni, utilizzare strutture condizionali esplicite:
     - *Se [Condizione A]*: allora [Azione o Comportamento A].
     - *Se [Condizione B]*: allora [Azione o Comportamento B].

---

## 📄 2. STANDARD DI DOCUMENTAZIONE & MARKDOWN

1. **Intestazioni Gerarchiche**:
   - Uso ordinato di `#`, `##`, `###` per consentire la navigazione rapida tramite il tasto `H` (Heading) di NVDA.
2. **Nomi di File, Comandi e Codice**:
   - Racchiudere sempre percorsi, comandi terminale, variabili e nomi di funzioni nei backtick (`` `inline code` ``) o blocchi di codice recintati (fenced code blocks) con linguaggio specificato.
3. **Collegamenti Cliccabili**:
   - Utilizzare collegamenti standard markdown in formato `[nome_file](file:///percorso/assoluto/del/file)` per consentire l'apertura rapida.

---

## 🧭 3. PRINCIPIO DEL REPORT A PUNTATORI & CRONOLOGIA INVERSA (POINTER HUB PATTERN)

1. **Il Vantaggio Cognitivo della Cronologia Inversa**:
   - Nei documenti di dialogo operativo, telemetria e passaggio consegne (`REPORT_SESSIONE_[TASK].md`), i messaggi e gli aggiornamenti si dispongono **tassativamente in ordine cronologico inverso (il più recente sempre in alto)**.
   - All'apertura del file con screen reader NVDA, il cursore si trova in cima: con una sola pressione del tasto rapido `H` (Intestazione successiva), l'utente atterra istantaneamente sull'ultimo aggiornamento, decisione o stato del collaudo, eliminando la necessità di scorrere a fine file (`Ctrl + Fine`) e risalire faticosamente a tentoni.
2. **Lo Standard di Sintesi a Puntatori (No Log Bloat)**:
   - È vietato incollare dump di decine di righe di log o blocchi massivi di codice all'interno dei report.
   - Ogni messaggio adotta lo standard a 4 campi compatti: Contesto/Sintomo ($\le 2$ righe), Causa Radice, Approccio Risolutivo, e Puntatori Espliciti (`file:///...`) a sorgenti, metodi, righe di `latest.log` e test seams.
   - Questo mantiene i file di report leggeri (5-20 KB), rapidi da scansionare ed ergonomici al 100% per la sintesi vocale.
