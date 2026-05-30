# publish.ps1 - Script para publicar nuevas versiones de ai-teacher-shared

param(
    [Parameter(Mandatory=$true)]
    [string]$Version,
    
    [Parameter(Mandatory=$true)]
    [string]$Message
)

Write-Host "Publicando ai-teacher-shared v$Version" -ForegroundColor Cyan

# Verificar que estamos en el directorio correcto
if (-not (Test-Path "pyproject.toml")) {
    Write-Host "Error: Debes ejecutar este script desde el directorio shared/" -ForegroundColor Red
    exit 1
}

# Actualizar versión en pyproject.toml
Write-Host "Actualizando version en pyproject.toml..." -ForegroundColor Yellow
$newVersionLine = "version = ""$Version"""
(Get-Content pyproject.toml) -replace 'version = ".*"', $newVersionLine | Set-Content pyproject.toml

# Actualizar versión en __init__.py
Write-Host "Actualizando version en __init__.py..." -ForegroundColor Yellow
$newInitLine = "__version__ = ""$Version"""
(Get-Content ai_teacher_shared/__init__.py) -replace '__version__ = ".*"', $newInitLine | Set-Content ai_teacher_shared/__init__.py

# Git add
Write-Host "Agregando cambios a git..." -ForegroundColor Yellow
git add .

# Git commit
Write-Host "Creando commit..." -ForegroundColor Yellow
git commit -m "Release v$Version: $Message"

# Git tag
Write-Host "Creando tag v$Version..." -ForegroundColor Yellow
git tag "v$Version"

# Git push
Write-Host "Subiendo a GitHub..." -ForegroundColor Yellow
git push
git push origin "v$Version"

Write-Host "Publicado exitosamente!" -ForegroundColor Green
Write-Host ""
Write-Host "Para usar esta version en los servicios, actualiza requirements.txt:" -ForegroundColor Cyan
Write-Host "   git+https://github.com/taktikware/ai-teacher-shared.git@v$Version" -ForegroundColor White
