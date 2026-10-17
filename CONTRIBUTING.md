# Contribuire

Questa repository contiene più componenti indipendenti. Prima di modificare,
individua il progetto interessato nel [README](./README.md) e leggi le sue
istruzioni e convenzioni locali.

## Modifiche e verifiche

- Mantieni le modifiche circoscritte al componente richiesto.
- Per JARVIS, esegui i test pertinenti dalla cartella `Mark-LIV-main/`:
  `python -m pytest -q`; per le sole modifiche GEV puoi eseguire
  `python -m pytest -q tests/test_gev_plugin.py tests/test_gev_mcp_client.py`.
- Dichiara quali test hai eseguito e quali prove live (Gemini, GUI, audio,
  browser o dati GEV) non hai potuto effettuare.
- Non includere chiavi API, certificati, file `.env`, memoria locale, runtime,
  ambienti virtuali o dipendenze generate.
- Controlla la licenza del componente in [`LICENSES.md`](./LICENSES.md) prima
  di proporre modifiche o redistribuzioni che coinvolgano più progetti.

Per le modifiche, apri una pull request su
[ilfenomeno-gif/jarvis-new-gen](https://github.com/ilfenomeno-gif/jarvis-new-gen)
con una descrizione dell'obiettivo, dei file coinvolti e delle verifiche
effettuate. Segnala separatamente eventuali regressioni o test bloccati.
