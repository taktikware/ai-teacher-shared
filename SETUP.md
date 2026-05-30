# 📦 AI Teacher Shared - Setup Instructions

Este documento explica cómo publicar y usar el paquete `ai-teacher-shared`.

## 🚀 Publicar en GitHub (Primera vez)

```powershell
# 1. Navega al directorio shared
cd c:\Users\xbisb\Documents\ai-teacher\shared

# 2. Inicializa git (si no está inicializado)
git init

# 3. Añade los archivos
git add .

# 4. Haz el primer commit
git commit -m "Initial release v1.0.0"

# 5. Crea un tag para la versión
git tag v1.0.0

# 6. Añade el remote de GitHub
git remote add origin https://github.com/taktikware/ai-teacher-shared.git

# 7. Sube el código y el tag
git push -u origin main
git push origin v1.0.0
```

## 🔄 Actualizar una nueva versión

```powershell
# 1. Actualiza la versión en pyproject.toml y __init__.py
# Por ejemplo, de 1.0.0 a 1.1.0

# 2. Añade y comitea los cambios
git add .
git commit -m "Release v1.1.0: descripción de cambios"

# 3. Crea un nuevo tag
git tag v1.1.0

# 4. Sube los cambios
git push
git push origin v1.1.0
```

## 📝 Actualizar servicios que usan el paquete

Cuando publiques una nueva versión, actualiza los `requirements.txt` de los servicios:

```txt
# Cambiar de:
git+https://github.com/taktikware/ai-teacher-shared.git@v1.0.0

# A:
git+https://github.com/taktikware/ai-teacher-shared.git@v1.1.0
```

Servicios que usan este paquete:
- ✅ align-service
- ✅ pronunciation-service

## 🧪 Probar localmente antes de publicar

```powershell
# Instala en modo editable
cd c:\Users\xbisb\Documents\ai-teacher\shared
pip install -e .

# Prueba el import
python -c "from ai_teacher_shared import validate_language; print('OK')"
```

## 📁 Estructura del paquete

```
shared/
├── ai_teacher_shared/          # Paquete principal
│   ├── __init__.py            # Exports
│   ├── utils.py               # Utilidades
│   ├── validators.py          # Validadores
│   └── map/                   # Datos de fonemas
│       ├── english_uk_mfa_valid_phones.yaml
│       ├── english_us_mfa_valid_phones.yaml
│       └── ...
├── pyproject.toml             # Configuración del paquete
├── MANIFEST.in                # Incluir archivos no-.py
├── README.md                  # Documentación
├── LICENSE                    # Licencia MIT
└── .gitignore                 # Archivos ignorados
```

## 🎯 Ventajas de esta solución

✅ **Sin duplicación**: Un solo lugar para el código compartido  
✅ **Versionado**: Control de qué versión usa cada servicio  
✅ **Instalación simple**: `pip install` desde GitHub  
✅ **Caché Docker**: Mejor aprovechamiento de capas  
✅ **Actualización fácil**: Solo cambiar el tag de versión
