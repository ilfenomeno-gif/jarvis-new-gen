[CmdletBinding()]
param(
    [string]$HubRoot=(Split-Path -Parent $PSScriptRoot),
    [ValidateSet('check','apply')][string]$Mode='check',
    [string]$StagingRoot='',
    [string]$BackupDir='',
    [string]$MockProfileRoot=''
)
$ErrorActionPreference='Stop'
try {
    . (Join-Path $PSScriptRoot 'astralis_staging_guard.ps1')
    $root=Get-AstralisPath $HubRoot
    if ($Mode -eq 'apply') {$null=Assert-AstralisStaging $root $StagingRoot}
    $layout=if (Test-Path -LiteralPath (Join-Path $root 'knowledge/README.md')) {'knowledge_globale'} elseif (Test-Path -LiteralPath (Join-Path $root 'knowledge/README.md')) {'knowledge'} else {throw 'Layout HUB non verificabile'}
    $required=@('README.md','CHANGELOG.md','ISTRUZIONI_DI_AVVIO.md','prompts/INDICE_SELEZIONE.json','skills/INDICE_SELEZIONE.json','templates/GEMINI_TEMPLATE.md',"$layout/README.md", "$layout/03_architettura_e_metodologie/catalogo_protocolli_operativi_astralis.md")
    $missing=@($required | Where-Object {-not (Test-Path -LiteralPath (Join-Path $root $_) -PathType Leaf)})
    if ($missing.Count) {throw ('Fonti mancanti: '+($missing -join ', '))}
    $readme=[IO.File]::ReadAllText((Join-Path $root 'README.md'))
    if ($readme -notmatch '(?m)^# Versione:\s*(3\.\d+\.\d+)') {throw 'Baseline v3 assente'}
    $version=$matches[1]
    foreach ($kind in @('prompts','skills')) {
        $index=[IO.File]::ReadAllText((Join-Path $root "$kind/INDICE_SELEZIONE.json")) | ConvertFrom-Json
        $countExpected=if ($kind -eq 'prompts') {23} else {27}
        if ($index.schema -ne 1 -or $index.applies_to -ne 'ASTRALIS 3.X' -or @($index.$kind).Count -ne $countExpected) {throw 'Schema o conteggio catalogo non valido'}
        if ($index.framework_baseline -ne $version) {throw 'Baseline catalogo non coerente'}
        foreach ($entry in $index.$kind) {
            $file=Get-AstralisPath (Join-Path $root "$kind/$($entry.path)")
            if (-not $file.StartsWith($root+'\',[StringComparison]::OrdinalIgnoreCase)) {throw 'Indice fuori HUB'}
            if ((Get-FileHash -LiteralPath $file -Algorithm SHA256).Hash.ToLowerInvariant() -ne $entry.sha256) {throw "Hash catalogo errato: $($entry.path)"}
        }
    }
    $backups=@{}
    if ($MockProfileRoot) {
        $profile=Assert-AstralisStaging $MockProfileRoot $StagingRoot
        if (-not $BackupDir) {throw 'BackupDir esplicito richiesto per mock'}
        $backup=Assert-AstralisStaging $BackupDir $StagingRoot
        Test-AstralisOverlap $profile $backup
        foreach ($rel in @('.gemini/config/GEMINI.md','.codex/AGENTS.md','.claude/CLAUDE.md')) {
            $file=Join-Path $profile $rel
            $null=Get-AstralisPath $file
            if (Test-Path -LiteralPath $file -PathType Leaf) {$backups[$rel]=[IO.File]::ReadAllBytes($file)}
        }
    } elseif ($BackupDir) {throw 'BackupDir senza mock: profili reali esclusi'}
    if ($Mode -eq 'apply') {
        foreach ($rel in $backups.Keys) {
            $dest=Join-Path $backup ($rel+'.bak')
            $null=New-Item -ItemType Directory -Path (Split-Path -Parent $dest) -Force
            [IO.File]::WriteAllBytes($dest,$backups[$rel])
        }
    }
    Write-Host "[PASS] Audit ${Mode}: v$version; nessun self-healing, accesso profili reali o scansione del padre. Backup mock previsti: $($backups.Count)."
    exit 0
} catch {Write-Error $_ -ErrorAction Continue; exit 1}
