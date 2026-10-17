# NN — Standard Piani Tecnici, Verifiche & Living Documentation

## 1. Regole di Redazione dei Piani Tecnici
- I piani in fase di lavorazione risiedono in `docs/piani/attivi/`.
- Ogni piano deve essere validato sui 7 Assi e articolato nelle 4 Fasi operative.
- Al completamento con esito positivo del collaudo, il file viene spostato in `docs/piani/completati/`.

## 2. Regola della Chiusura Tecnica (Fase 3) & Domanda Ponte
La conclusione di ogni piano richiede:
- Esecuzione commit Git, eventuale push e backup stabile.
- Aggiornamento contestuale della Living Documentation:
  - `changelog.md`: Registro sintetico delle novità e modifiche.
  - `architecture.md` (o schede `knowledge/`): Aggiornamento dell'architettura tecnica.
  - `README.md`: Allineamento di eventuali comandi o riferimenti modificati.
- Archiviazione del piano da `docs/piani/attivi/` a `docs/piani/completati/`.
- Presentazione del riepilogo sintetico lezioni 3D (Tecnica, Metodologica, Comunicativa).
- **Obbligo di Domanda Ponte**: L'assistente chiude tassativamente con:
  > *"Vuoi che avviamo ora la sessione formale di Auto-Apprendimento (Fase 4) per elaborare la bozza dettagliata delle regole e aggiornare le schede di conoscenza e governance?"*

## 3. Protocollo di Auto-Apprendimento Continuo (Fase 4)
- Al via libera di Luca, l'assistente entra formalmente in Fase 4: mappa i file di destinazione (`knowledge/`, `GEMINI.md`, Master Hub), redige i paragrafi completi pronti per l'inserimento e richiede la convalida finale prima di applicarli.

## 4. Accessibilità Cognitiva per Screen Reader
- Divieto assoluto di diagrammi 2D, tabelle ASCII con bordi complessi o frecce visive.
- Formattazione unicamente lineare a elenchi "Se... Allora", tabelle markdown semplici e sezioni con titoli chiari.