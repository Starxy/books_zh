param([string]$OutputDirectory = (Join-Path $PSScriptRoot "../../00_books"))
$ErrorActionPreference = "Stop"
& python (Join-Path $PSScriptRoot "build.py") --output-directory $OutputDirectory
if ($LASTEXITCODE -ne 0) { throw "尚未生成PDF，请查看上方说明和README_build.txt。" }
