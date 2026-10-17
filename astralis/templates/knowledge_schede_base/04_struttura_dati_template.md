# 04 — Struttura Progetto, Gestione Dati & Profili di Test

## 1. Mappa Gerarchica delle Cartelle
- Gerarchia pulita con percorsi relativi (`./`, `%~dp0`, `$PSScriptRoot`).
- Isolamento tra codice sorgente, documentazione (`docs/`), conoscenza (`knowledge/`) e asset.

## 2. Profili di Test Isolati & Sicurezza Salvataggi
- Utilizzo di cartelle o profili di test separati (`LocalSaves=true`) durante lo sviluppo per proteggere le partite e le configurazioni reali da anomalie.

## 3. Routing Multi-Macchina & Sincronizzazione Cloud
- Identificazione automatica del computer attivo tramite `$env:COMPUTERNAME` (es. Desktop vs Laptop).
- Gestione percorsi cloud tramite variabili d'ambiente (`$env:USERPROFILE`, `$env:OneDrive`, `$env:APPDATA`).