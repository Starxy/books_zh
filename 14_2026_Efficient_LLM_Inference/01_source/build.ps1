$ErrorActionPreference = 'Stop'
python (Join-Path $PSScriptRoot 'build.py') @args
exit $LASTEXITCODE
