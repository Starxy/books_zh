param([string]$OutputDirectory = (Join-Path $PSScriptRoot "../../00_books"))
$ErrorActionPreference = "Stop"
& python (Join-Path $PSScriptRoot "build.py") --output-directory $OutputDirectory
if ($LASTEXITCODE -ne 0) { throw "编译失败，请查看终端报告的临时目录。" }
