$ErrorActionPreference = 'Stop'
python (Join-Path $PSScriptRoot 'build.py') @args
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
