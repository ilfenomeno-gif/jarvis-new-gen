# Standard per Addon NVDA, Thread Asincroni e GUI wxPython
# Autore: Luca (Sviluppatore Senior Non Vedente con Screen Reader NVDA)
# Target AI: Antigravity (Senior AI Pair Programmer & Software Engineer)
# Ambito: Globale / Universale

Questo documento stabilisce le regole per la creazione di addon, plugin per screen reader NVDA e interfacce grafiche con wxPython.

---

## 🔌 1. ARCHITETTURA ADDON PER NVDA

1. **Moduli e Struttura Standard**:
   - `globalPlugins/`: Per funzionalità e comandi globali attivi su tutto il sistema operativo.
   - `appModules/`: Per logiche contestuali vincolate a una specifica applicazione (es. `appModules/skyrimse.py`, `appModules/mushclient.py`).
   - `manifest.ini`: Conforme alle versioni di compatibilità di NVDA (`minVersion`, `lastTestedVersion`).

2. **Integrazione API NVDA (`speech`, `braille`, `ui`)**:
   - Chiamate standard per sintesi: `ui.message("testo")` o `speech.speakTextInfo(...)`.
   - Evitare blocchi del thread principale di NVDA.

---

## 🧵 2. THREAD ASINCRONI & FLUIDITÀ DELLO SCREEN READER

1. **Divieto di Operazioni Bloccanti sul Main Thread**:
   - Chiamate di rete, I/O su disco pesante o elaborazioni complesse devono essere eseguite in thread separati (`threading.Thread`).
2. **Aggiornamenti GUI Thread-Safe**:
   - In wxPython, richiamare le modifiche all'interfaccia o alla sintesi vocale da un thread secondario utilizzando sempre `wx.CallAfter(funzione, *args)`.

---

## 🖼️ 3. GUI ACCESSIBILI CON WXPYTHON

- Assegnare sempre etichette esplicite a tutti i controlli (`wx.StaticText` associato a `wx.TextCtrl`).
- Raggruppare i controlli correlati all'interno di `wx.StaticBoxSizer` con titoli parlanti.
- Assicurare che la navigazione con `Tab` e `Frecce Direzionali` scorra fluidamente senza elementi inaccessibili.
