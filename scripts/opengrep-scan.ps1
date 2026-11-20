<#
.SYNOPSIS
  Runs opengrep over src/ and tests/ with the project rules. Run it before every push.
.DESCRIPTION
  Uses the opengrep binary at ~\.opengrep\cli\latest\opengrep.exe. A finding gives a
  non-zero exit code. Output is also written to .opengrep-report/ (ignored by git).
#>
[CmdletBinding()]
param(
    [string] $Binary = (Join-Path $HOME '.opengrep\cli\latest\opengrep.exe')
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
if (-not (Test-Path $Binary)) {
    throw "opengrep not found at $Binary"
}
New-Item -ItemType Directory -Force (Join-Path $root '.opengrep-report') | Out-Null
Push-Location $root
try {
    & $Binary scan --config .opengrep/rules.yml --error --sarif-output=.opengrep-report/opengrep.sarif src tests
    exit $LASTEXITCODE
}
finally {
    Pop-Location
}
