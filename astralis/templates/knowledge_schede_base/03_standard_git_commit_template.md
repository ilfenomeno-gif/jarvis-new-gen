# 03 — Standard Git, Branching, Commit & Fork I18N

## 1. Convenzione di Commit (Conventional Commits)
- `feat:` Nuove funzionalità
- `fix:` Risoluzione di bug
- `docs:` Aggiornamento documentazione e regole
- `refactor:` Riorganizzazione codice senza cambi funzionali
- `test:` Aggiunta o modifica test
- `chore:` Manutenzione build e dipendenze

## 2. Criterio di Branching Proporzionato
- **Branch Dedicato (`feat/*`, `fix/*`)**: Nuove feature complesse, PR upstream, refactoring rilevanti.
- **Fast Path su Master**: Aggiornamento Living Documentation (`changelog`, `knowledge`, `README`), ritocchi di costanti, one-line fix approvati.

## 3. Disciplina Bilingue & Fork Open-Source (I18N)
- **Documentazione Interna & Piani**: Rigorosamente in **Italiano**.
- **Codice & Commit**: Standard tecnico convenzionale.
- **Fork Upstream & PR Pubbliche**: I file destinati a PR internazionali (`*_ENGLISH`) restano in inglese puro; i contenuti italiani vivono nei moduli di localizzazione dedicati (`*_ITALIAN`, `it_it.json`).