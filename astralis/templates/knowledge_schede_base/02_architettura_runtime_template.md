# 02 — Architettura Stack, Runtime & Toolchain Dinamiche

## 1. Stack Tecnologico di Progetto
- **Linguaggio Primario**: [LINGUAGGIO]
- **Build Tool**: [BUILD_TOOL]
- **Framework & Librerie**: [LIBRERIE]
- **Layer Accessibilità**: [NVDA DLL / Tolk / SAPI / Sound Engine]

## 2. Risoluzione Dinamica delle Toolchain
- Pattern wildcard per interpreti e compilatori (es. `$env:ProgramFiles\Microsoft\jdk-*`, `$env:JAVA_HOME`).
- Nessun percorso rigido cablato nel codice.

## 3. Pre-Flight Environment Check
- Script/comando rapido per validare l'ambiente prima di ogni compilazione.