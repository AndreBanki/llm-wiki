# serve.ps1 — Inicia o servidor local do MkDocs
# Uso: .\serve.ps1
# Acesse http://localhost:8000 no navegador após executar

$ErrorActionPreference = "Stop"

# Verifica se o mkdocs está instalado
if (-not (Get-Command mkdocs -ErrorAction SilentlyContinue)) {
    Write-Host "MkDocs não encontrado. Instalando dependências..." -ForegroundColor Yellow
    pip install -r requirements.txt
}

Write-Host ""
Write-Host "Iniciando servidor MkDocs em http://localhost:8000" -ForegroundColor Green
Write-Host "Pressione Ctrl+C para encerrar." -ForegroundColor Gray
Write-Host ""

mkdocs serve
