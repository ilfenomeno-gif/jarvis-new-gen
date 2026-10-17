# Standard di Sviluppo Python, Virtual Environment e Tipizzazione
# Autore: Luca (Sviluppatore Senior Non Vedente con Screen Reader NVDA)
# Target AI: Antigravity (Senior AI Pair Programmer & Software Engineer)
# Ambito: Globale / Universale

Questo documento definisce le convenzioni, lo stile e le linee guida per i progetti sviluppati in linguaggio Python.

---

## 🐍 1. VIRTUAL ENVIRONMENT & GESTIONE DIPENDENZE

1. **Isolamento Obbligatorio (`venv`)**:
   - Ogni progetto Python deve avere il proprio ambiente virtuale dedicato (`.venv/` o `venv/`), mai installare package a livello di sistema globale.
   - Tracciamento delle dipendenze con `requirements.txt` o `pyproject.toml`.

2. **Tipizzazione Statica (Type Hints)**:
   - Utilizzo sistematico delle annotazioni di tipo su parametri di funzione e valori di ritorno (`from typing import Optional, List, Dict, Callable`).
   - Convalida statica con `mypy` ove applicabile.

3. **Stile di Codice (PEP 8)**:
   - Naming: `snake_case` per funzioni e variabili, `PascalCase` per le classi, `UPPER_SNAKE_CASE` per le costanti.
   - Lunghezza linea massima: 100-120 caratteri. Docstring chiare in lingua Italiana per tutte le classi e metodi pubblici.

---

## 🧪 2. ESECUZIONE TEST CON PYTEST

- Organizzare i test nella cartella `tests/`.
- Esecuzione con comando standard: `python -m pytest tests/ -v`.
- Utilizzo di fixture `conftest.py` per setup di dati condivisi.
