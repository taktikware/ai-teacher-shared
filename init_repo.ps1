# init_repo.ps1 - Script para inicializar el repositorio ai-teacher-shared

Write-Host "Inicializando repositorio ai-teacher-shared" -ForegroundColor Cyan

# Verificar que estamos en el directorio correcto
if (-not (Test-Path "pyproject.toml")) {
    Write-Host "Error: Debes ejecutar este script desde el directorio shared/" -ForegroundColor Red
    exit 1
}

# Inicializar git
Write-Host "Inicializando git..." -ForegroundColor Yellow
git init

# Añadir archivos
Write-Host "Agregando archivos..." -ForegroundColor Yellow
git add .

# Primer commit
Write-Host "Creando primer commit..." -ForegroundColor Yellow
git commit -m "Initial release v1.0.0"

# Crear tag
Write-Host "Creando tag v1.0.0..." -ForegroundColor Yellow
git tag v1.0.0

# Añadir remote
Write-Host "Añadiendo remote de GitHub..." -ForegroundColor Yellow
git remote add origin https://github.com/taktikware/ai-teacher-shared.git

# Rename branch to main if needed
$currentBranch = git branch --show-current
if ($currentBranch -ne "main") {
    Write-Host "Renombrando branch a main..." -ForegroundColor Yellow
    git branch -M main
}

# Push
Write-Host "Subiendo a GitHub..." -ForegroundColor Yellow
git push -u origin main
git push origin v1.0.0

Write-Host "Repositorio inicializado exitosamente!" -ForegroundColor Green
Write-Host ""
Write-Host "Los servicios ya estan configurados para usar:" -ForegroundColor Cyan
Write-Host "   git+https://github.com/taktikware/ai-teacher-shared.git@v1.0.0" -ForegroundColor White
