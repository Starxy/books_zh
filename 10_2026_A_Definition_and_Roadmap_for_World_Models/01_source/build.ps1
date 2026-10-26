param([string]$OutputDirectory = (Join-Path $PSScriptRoot "../../00_books"))
$ErrorActionPreference = "Stop"
& python (Join-Path $PSScriptRoot "build.py") --output-directory $OutputDirectory
if ($LASTEXITCODE -ne 0) { throw "PDF build failed. See the compiler output above." }
