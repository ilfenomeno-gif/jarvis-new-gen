# Guardia condivisa Astralis 3: nessun effetto durante il caricamento.
function Get-AstralisPath {
    param([Parameter(Mandatory)][string]$Path)
    if ([string]::IsNullOrWhiteSpace($Path) -or $Path -match '(^|[\\/])\.\.([\\/]|$)') { throw 'Percorso vuoto o traversal' }
    $full = [IO.Path]::GetFullPath($Path)
    $walk = $full
    while ($walk) {
        if (Test-Path -LiteralPath $walk) {
            $item = Get-Item -LiteralPath $walk -Force
            if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw 'Junction/symlink non consentito' }
        }
        $parent = Split-Path -Parent $walk
        if ($parent -eq $walk) { break }
        $walk = $parent
    }
    return $full.TrimEnd('\','/')
}
function Assert-AstralisStaging {
    param([string]$Path,[string]$StagingRoot)
    $root = Get-AstralisPath $StagingRoot
    $target = Get-AstralisPath $Path
    $temp = Get-AstralisPath ([IO.Path]::GetTempPath())
    if (-not $root.StartsWith($temp + [IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase) -or $root -match '(?i)OneDrive') { throw 'Staging deve essere dedicato sotto TEMP, fuori OneDrive' }
    $markerPath = Join-Path $root '.astralis-staging.json'
    $marker = [IO.File]::ReadAllText($markerPath) | ConvertFrom-Json
    if ($marker.kind -ne 'astralis-v3-staging' -or -not $marker.id) { throw 'Marker staging non valido' }
    if (-not $target.StartsWith($root + [IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)) { throw 'Destinazione fuori staging' }
    $tail = $target.Substring($root.Length)
    if ($tail -match '(?i)(^|[\\/])(\.git|\.gemini|\.codex|\.claude)([\\/]|$)') { throw 'Destinazione profilo/repository protetto' }
    if (Test-Path -LiteralPath $target) {
        foreach ($item in Get-ChildItem -LiteralPath $target -Recurse -Force) {
            if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw 'Reparse point nella destinazione' }
        }
    }
    return $target
}
function Test-AstralisOverlap {
    param([string]$Source,[string]$Target)
    $a=Get-AstralisPath $Source; $b=Get-AstralisPath $Target
    if ($a -eq $b -or $a.StartsWith($b+'\',[StringComparison]::OrdinalIgnoreCase) -or $b.StartsWith($a+'\',[StringComparison]::OrdinalIgnoreCase)) { throw 'Radici sovrapposte' }
}
