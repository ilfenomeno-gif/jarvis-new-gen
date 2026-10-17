[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$TargetDir,
    [Parameter(Mandatory)][string]$HubRoot,
    [ValidateSet('check','apply')][string]$Mode='check',
    [Parameter(Mandatory)][string]$StagingRoot,
    [ValidateSet('GEMINI','AGENTS','CLAUDE','COPILOT','GPT','CUSTOM')][string]$AI='GEMINI',
    [string]$ProjectName='Progetto Astralis'
)
$ErrorActionPreference='Stop'
try {
    . (Join-Path $PSScriptRoot 'astralis_staging_guard.ps1')
    $source=Get-AstralisPath $HubRoot
    $target=Assert-AstralisStaging $TargetDir $StagingRoot
    Test-AstralisOverlap $source $target
    if ($Mode -eq 'apply') { $null=Assert-AstralisStaging $source $StagingRoot }
    $layout=if (Test-Path -LiteralPath (Join-Path $source 'knowledge\README.md')) {'knowledge_globale'} elseif (Test-Path -LiteralPath (Join-Path $source 'knowledge\README.md')) {'knowledge'} else {throw 'Layout HUB assente'}
    $destinations=@("$layout/README.md", "$layout/03_architettura_e_metodologie/selezione_e_utilizzo_prompt_astralis.md", 'prompts/INDICE_SELEZIONE.json', "$layout/03_architettura_e_metodologie/selezione_e_utilizzo_skill_astralis.md", 'skills/INDICE_SELEZIONE.json', "$layout/03_architettura_e_metodologie/gestione_report_e_continuita_sessioni.md", "$layout/03_architettura_e_metodologie/ciclo_sviluppo_e_selezione_strumenti_astralis.md")
    foreach ($rel in $destinations) { if (-not (Test-Path -LiteralPath (Join-Path $source $rel) -PathType Leaf)) {throw "Destinazione HUB mancante: $rel"} }
    $mapping=[ordered]@{
        '00_consuetudini_operative_template.md'='00_consuetudini_operative_e_sinergia_assistente.md'
        '01_accessibilita_vocale_template.md'='01_accessibilita_vocale_e_interazione_tastiera.md'
        '02_architettura_runtime_template.md'='02_architettura_stack_e_runtime.md'
        '03_standard_git_commit_template.md'='03_standard_git_branching_e_commit.md'
        '04_struttura_dati_template.md'='04_struttura_progetto_e_gestione_dati.md'
        'NN_registro_bug_soluzioni_template.md'='09_registro_bug_e_soluzioni.md'
        'NN_living_documentation_template.md'='10_standard_piani_verifiche_e_living_documentation.md'
    }
    $templates=@{GEMINI='GEMINI_TEMPLATE.md';AGENTS='AGENTS_TEMPLATE.md';CLAUDE='collaboratori_ai/CLAUDE_TEMPLATE.md';COPILOT='collaboratori_ai/COPILOT_TEMPLATE.md';GPT='collaboratori_ai/AGENTS_GPT_TEMPLATE.md';CUSTOM='collaboratori_ai/CUSTOM_AI_TEMPLATE.md'}
    $outputNames=@{GEMINI='GEMINI.md';AGENTS='AGENTS.md';CLAUDE='CLAUDE.md';COPILOT='COPILOT.md';GPT='AGENTS.md';CUSTOM='AI.md'}
    $inputs=[ordered]@{}
    foreach ($key in $mapping.Keys) {$inputs["knowledge/$($mapping[$key])"]=Join-Path $source "templates/knowledge_schede_base/$key"}
    foreach ($pair in @(@('REGISTRO_REVISIONI_TEMPLATE.md','docs/report/REGISTRO_REVISIONI.md'),@('ARCHIVIO_REVISIONI_TEMPLATE.md','docs/report/ARCHIVIO_REVISIONI.md'),@('README_PROGETTO_TEMPLATE.md','README.md'),@('CHANGELOG_PROGETTO_TEMPLATE.md','CHANGELOG.md'))) {$inputs[$pair[1]]=Join-Path $source "templates/$($pair[0])"}
    $inputs[$outputNames[$AI]]=Join-Path $source "templates/$($templates[$AI])"
    $planned=[ordered]@{}; $utf8=[Text.UTF8Encoding]::new($false,$true)
    foreach ($rel in $inputs.Keys) {
        $path=Get-AstralisPath $inputs[$rel]
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {throw "Template mancante: $path"}
        $text=[IO.File]::ReadAllText($path,$utf8)
        if ($rel -eq $outputNames[$AI]) {
            $text=[regex]::Replace($text,'(?m)^# Master Hub:.*$', ('# Master Hub: '+$source))
            $text=$text.Replace('knowledge/',$layout+'/').Replace('[NOME PROGETTO]',$ProjectName)
            $localLines=($mapping.Values | ForEach-Object {"- [$_](./knowledge/$_)"}) -join "`n"
            $text=[regex]::Replace($text,'(?ms)^## [^\r\n]*Indice Ragionato[^\r\n]*\r?\n.*?(?=^---)',("## Conoscenza locale inizializzata`n`n"+$localLines+"`n`n"))
            $text=$text.Replace('file:///knowledge/','./knowledge/')
        }
        $planned[$rel]=$text.Replace("`r`n","`n").Replace("`n","`r`n")
    }
    $created=[Collections.Generic.List[string]]::new()
    try {
        if ($Mode -eq 'apply') {
            foreach ($rel in $planned.Keys) {
                $dest=Join-Path $target $rel
                if (-not (Test-Path -LiteralPath $dest)) {
                    $null=New-Item -ItemType Directory -Path (Split-Path -Parent $dest) -Force
                    [IO.File]::WriteAllText($dest,$planned[$rel],[Text.UTF8Encoding]::new($false)); $created.Add($dest)
                }
            }
            foreach ($folder in @('docs/piani/attivi','docs/piani/completati','docs/strategie/attive','docs/strategie/archiviate','docs/report/archivio','docs/report/allegati','docs/idee','docs/manuali')) {$null=New-Item -ItemType Directory -Path (Join-Path $target $folder) -Force}
        }
    } catch { Write-Host ('[INCOMPLETO] File nuovi: '+($created -join ', ')); throw }
    Write-Host "[PASS] Bootstrap $Mode; HUB verificato, $($planned.Count) artefatti previsti; file esistenti preservati."
    if (Test-Path -LiteralPath (Join-Path $target $outputNames[$AI])) {Write-Host '[INFO] Ingresso esistente conservato: eventuale riallineamento richiede incarico distinto.'}
    exit 0
} catch { Write-Error $_ -ErrorAction Continue; exit 1 }
