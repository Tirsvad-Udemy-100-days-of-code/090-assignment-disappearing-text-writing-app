<#
.SYNOPSIS
  Takes the screenshots of the build steps in a Docker container (not on the host desktop).
.DESCRIPTION
  Builds the image from tools/screenshots/Dockerfile, runs it, and copies the four PNG
  files from the container's /out folder to docs/images.
#>
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
Push-Location $root
try {
    docker build -f tools/screenshots/Dockerfile -t disappearing-text-shots .
    if ($LASTEXITCODE -ne 0) { throw 'docker build failed' }
    New-Item -ItemType Directory -Force docs/images | Out-Null
    $container = docker create disappearing-text-shots
    try {
        docker start -a $container
        if ($LASTEXITCODE -ne 0) { throw 'docker run failed' }
        docker cp "${container}:/out/." docs/images
        if ($LASTEXITCODE -ne 0) { throw 'docker cp failed' }
    }
    finally {
        docker rm $container | Out-Null
    }
}
finally {
    Pop-Location
}
