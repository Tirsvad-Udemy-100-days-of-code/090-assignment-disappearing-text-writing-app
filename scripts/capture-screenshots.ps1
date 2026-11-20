<#
.SYNOPSIS
  Takes the screenshots of the build steps in a Docker container (not on the host desktop).
.DESCRIPTION
  Builds the image from tools/screenshots/Dockerfile, runs it with docs/images mapped to
  /out, and the four PNG files appear in docs/images.
#>
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
Push-Location $root
try {
    docker build -f tools/screenshots/Dockerfile -t disappearing-text-shots .
    if ($LASTEXITCODE -ne 0) { throw 'docker build failed' }
    New-Item -ItemType Directory -Force docs/images | Out-Null
    docker run --rm -v "${root}/docs/images:/out" disappearing-text-shots
    if ($LASTEXITCODE -ne 0) { throw 'docker run failed' }
}
finally {
    Pop-Location
}
