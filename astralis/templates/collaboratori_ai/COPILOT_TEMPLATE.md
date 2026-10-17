# [NOME PROGETTO] — Istruzioni di Repository per GitHub Copilot (ASTRALIS v3.0.5)
# Autore: [NOME SVILUPPATORE] (Default da user_preferences.md)
# Target AI: GitHub Copilot (Assistente al Completamento & Copilota Ausiliario)
# Framework: ASTRALIS v3.0.5
# Master Hub: <astralis-hub>

## 🛡️ LINEE GUIDA FONDAMENTALI
1. **Accessibilità Tastiera & Zero Mouse**: Non proporre mai logiche o controlli dipendenti da coordinate del cursore del mouse.
2. **Formattazione Lineare NVDA**: Commenti e documentazione in linea devono essere puliti, lineari e privi di artefatti grafici ASCII.
3. **Lingua**: Commenti e documentazione in **Italiano**.
4. **Convenzioni di Codice**: Consulta le convenzioni architetturali definite in `knowledge/` prima di proporre completamenti o refactoring complessi.
5. **Regola 0**: Proponi modifiche e completamenti lasciando sempre il pieno controllo decisionale all'utente prima dell'applicazione.

## Routing operativo — Astralis 3.X
HUB è il Master Hub dinamico dichiarato in testata; risolvi la variabile nell’ambiente e verifica il percorso.
Le destinazioni seguenti sono relative a HUB; consulta soltanto quelle pertinenti al mandato.
- Conoscenze: `knowledge/README.md`.
- Prompt: `knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md`; `prompts/INDICE_SELEZIONE.json`.
- Skill: `knowledge/03_architettura_e_metodologie/selezione_e_utilizzo_skill_astralis.md`; `skills/INDICE_SELEZIONE.json`.
- Report: `knowledge/03_architettura_e_metodologie/gestione_report_e_continuita_sessioni.md`.
- Ciclo di sviluppo: `knowledge/03_architettura_e_metodologie/ciclo_sviluppo_e_selezione_strumenti_astralis.md`.
Leggi il candidato prima dell’uso; non caricare entrambi gli indici per default né ripetere fonti già lette e ancora attuali.
Consigliare o selezionare non concede permessi; usa il mandato già dato. Mantieni report utili alla continuità, senza crearli per chiarimenti banali.
Fallback: indice assente/obsoleto → catalogo README e scheda sotto lo stesso HUB, se leggibili; non rigenerare o installare automaticamente.
HUB/procedura non accessibile → indica percorso ed errore reali, limita il risultato; non simulare letture né cercare nel Lab/v4.
