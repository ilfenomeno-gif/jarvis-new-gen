# Jarvis New Gen

Repository multi-progetto per JARVIS, God's Eye View (GEV), l'estensione per
VS Code e il framework di riferimento ASTRALIS. La root raccoglie i progetti:
non è un singolo pacchetto installabile.

## Da dove iniziare

L'app desktop JARVIS mantenuta in questo repository si trova in
[`Mark-LIV-main/`](./Mark-LIV-main/). Il suo entry point è
[`main.py`](./Mark-LIV-main/main.py); GEV è collegato come plugin locale.

```powershell
git clone https://github.com/ilfenomeno-gif/jarvis-new-gen.git
Set-Location jarvis-new-gen\Mark-LIV-main
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install
```

Il progetto documenta Python 3.11 come requisito minimo e registra verifiche
locali fino a Python 3.13.7; non dichiara una compatibilità certificata con
versioni successive. La compatibilità dipende anche dalle dipendenze native
installate. Windows è la piattaforma principale per l'automazione desktop.

Prima di avviare JARVIS, crea localmente `config/api_keys.json`:

```json
{
  "gemini_api_key": "inserire-la-propria-chiave"
}
```

Il file è escluso dal controllo versione. Non inserire chiavi o token nel
codice, nei log o nei commit. Per avviare l'app:

```powershell
python main.py
```

## GEV e runtime Node

Il plugin e il dispatcher GEV si trovano in
[`plugins/gev_plugin.py`](./Mark-LIV-main/plugins/gev_plugin.py); il trasporto
MCP è in [`plugins/_gev_mcp_client.py`](./Mark-LIV-main/plugins/_gev_mcp_client.py).
L'albero GEV usato dal plugin è
[`gods-eye-view-main/_gev-clone/`](./Mark-LIV-main/gods-eye-view-main/_gev-clone/);
il suo `package-lock.json` è versionato, così come i test di integrazione
[`test_gev_plugin.py`](./Mark-LIV-main/tests/test_gev_plugin.py) e
[`test_gev_mcp_client.py`](./Mark-LIV-main/tests/test_gev_mcp_client.py).

Il runtime portatile Node non è incluso nel repository: il plugin **non lo
scarica** e segnala un errore se mancano `.node/node.exe` o
`.node/node_modules/npm/bin/npm-cli.js`. Se `node_modules/` non è già presente,
il primo avvio GEV esegue `npm ci` usando il lockfile versionato. Questa
installazione richiede accesso al registry npm e può eseguire gli script di
installazione dei pacchetti. Il runtime `v24.14.0` è stato osservato solo
nell'ambiente locale, non è un artefatto versionato; verifica la provenienza
del runtime e delle dipendenze prima di avviare GEV. I dettagli di provisioning
sono raccolti in
[`rigenerare-node-portatile.md`](./GEV-Jarvis-Project/07-procedure/rigenerare-node-portatile.md);
la procedura descrive il controllo SHA-256 dell'archivio scaricato.

I test automatici non richiedono una chiave Gemini:

```powershell
python -m pytest -q
```

JARVIS compone dichiarazioni e dispatch da tre fonti: tool core, azioni
built-in e plugin. I moduli `actions/*.py` con contratto `TOOL` sono scoperti
da `core/action_loader.py`; i plugin continuano a usare
`core/plugin_loader.py` e le integrazioni MCP esistenti. La VS Code extension è
un client del servizio locale, non un secondo runtime per i tool. Skill
dichiarative e workflow multi-step non sono ancora implementati.

La suite non sostituisce la convalida live dell'interfaccia, del microfono,
dell'audio, di Gemini o dei provider dati GEV.

## Mappa del repository

| Percorso | Contenuto |
|---|---|
| [`Mark-LIV-main/`](./Mark-LIV-main/) | App desktop Python JARVIS, codice, plugin e test |
| [`Mark-LIV-main/gods-eye-view-main/_gev-clone/`](./Mark-LIV-main/gods-eye-view-main/_gev-clone/) | Sorgenti GEV collegati al plugin JARVIS |
| [`GEV-Jarvis-Project/`](./GEV-Jarvis-Project/) | Archivio di analisi e procedure: la sua valutazione iniziale è storica |
| [`gods-eye-view-main/`](./gods-eye-view-main/) | Copie e materiale GEV separati; non sono l'entry point di JARVIS |
| [`jarvis-vscode-extension/`](./jarvis-vscode-extension/) | Estensione VS Code separata, con propri script e test |
| [`astralis/`](./astralis/) | Framework di conoscenza e template; non è una dipendenza runtime di JARVIS |
| [`.github/copilot-instructions.md`](./.github/copilot-instructions.md) | Istruzioni condivise per l'assistenza al codice nel workspace |

Per dettagli e passaggi di sviluppo, consulta
[`Mark-LIV-main/readme.md`](./Mark-LIV-main/readme.md) e
[`Mark-LIV-main/IMPLEMENTATION.md`](./Mark-LIV-main/IMPLEMENTATION.md).
Per configurare l'estensione VS Code, segui
[`jarvis-vscode-extension/README.md`](./jarvis-vscode-extension/README.md).
L'archivio GEV descrive fotografie precedenti del lavoro: non usare la
percentuale riportata nei suoi documenti come misura dello stato corrente.

## Licenze e contributi

Non c'è una licenza unica che copra l'intera raccolta. I componenti mantengono
le proprie licenze; alcuni percorsi non dichiarano una licenza. Leggi
[`LICENSES.md`](./LICENSES.md) prima di riutilizzare o distribuire codice.

Le indicazioni per segnalazioni e modifiche sono in
[`CONTRIBUTING.md`](./CONTRIBUTING.md).
