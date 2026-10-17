# [NOME PROGETTO] — Direttive di Progetto per Anthropic Claude (ASTRALIS v3.0.5)
# Autore: [NOME SVILUPPATORE] (Default da user_preferences.md)
# Target AI: Claude / Claude Code ([RUOLO: AI Primaria / Copilota Ausiliario])
# Framework: ASTRALIS v3.0.5
# Eredita da: %USERPROFILE%\.claude\CLAUDE.md (Direttive Globali Macchina)
# Hub di Contesto Master: GEMINI.md
# Master Hub: <astralis-hub>

Questo repository implementa il progetto **[NOME PROGETTO]** in pair programming secondo il profilo configurato in `user_preferences.md` (Default: screen reader **NVDA**, Zero Mouse).
Tutta la comunicazione deve essere in **Italiano al 100%**, strutturata in forma rigorosamente lineare (zero tabelle o layout 2D ASCII).

---

## ⚡ 1. MODALITÀ OPERATIVA & BUDGET DI CONTESTO

- **Lettura Selettiva On-Demand**: Consulta unicamente le 1-3 schede rilevanti in `knowledge/` senza caricare l'intera base di conoscenza.
- **Formattazione per Screen Reader**: Utilizza elenchi puntati compatti e costrutti sequenziali `Se [Condizione] -> Allora [Azione]`.

---

## 🏛️ 2. RETE DOCUMENTALE FLESSIBILE (DRY)

- `GEMINI.md`: Hub master di contesto con i parametri di configurazione.
- `knowledge/`: Moduli tematici architetturali del progetto.
- `docs/idee/`: Idee/RFC pertinenti, secondo la tassonomia v3.
- `docs/strategie/attive/`: Strategie cognitive UPCS (Fase 0).
- `docs/piani/attivi/`: Piani tecnici formali approvati (Fase 1).
- `docs/report/REGISTRO_REVISIONI.md`: Registro revisioni attivo e telemetria live.

---

## 🛡️ 3. REGOLE AUREE INVIOLABILI

1. **Regola 0 (Default Consultivo)**: Attendi sempre il comando esplicito di Luca (*"procedi"*, *"applica"*) prima di modificare file o eseguire comandi distruttivi.
2. **Accessibilità Vocale Assoluta**: Nessun elemento visivo o mouse dipendente. Interazione 100% da tastiera.
3. **Disciplina di Ruolo**:
   - [Se AI Primaria]: Conduci le implementazioni, build e test automatici;
   - [Se Copilota Ausiliario]: Fornisci dialettica avversariale, review indipendenti e suggerimenti algoritmici in sola lettura.
4. **Meta-Governance**: Rispetta i 6 Canoni Architetturali (router <= 250 righe, UTF-8 no BOM, CRLF).

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
