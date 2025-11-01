# Máster en Ciberseguridad

Este repositorio contiene materiales y prácticas para el programa del Máster en Ciberseguridad.

## Configuración del Entorno

Para asegurar la correcta ejecución del código, se recomienda configurar el entorno de desarrollo usando **Python 3.13** y gestionar las dependencias con **uv**.

### 1. Instalación de UV

Para gestionar paquetes y versiones de Python, utilizaremos **uv**. 

**Importante**: Las instrucciones de instalación varían según el sistema operativo y arquitectura. Por favor, consulta la documentación oficial para obtener instrucciones específicas para tu sistema:

- **Documentación oficial**: https://docs.astral.sh/uv/
- **Repositorio oficial**: https://github.com/astral-sh/uv

**Instalación según tu sistema**:

**macOS (usando Homebrew)**:
```bash
brew install uv
```

**Linux**:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows**:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Si ya tienes pipx instalado** (cualquier sistema operativo):
```bash
pipx install uv
```

Después de la instalación, reinicia tu terminal para que los cambios en el PATH surtan efecto.

### 2. Creación del Entorno Virtual

Crea un entorno virtual con Python 3.13:

```bash
uv venv --python 3.13
```

**Nota**: Si no tienes Python 3.13 instalado, uv lo descargará e instalará automáticamente.

### 3. Activación del Entorno Virtual

**Importante**: Después de crear el entorno virtual, necesitas activarlo:

```bash
source .venv/bin/activate  # En Linux/macOS
```

o

```bash
.venv\Scripts\activate     # En Windows
```

### 4. Instalación de Dependencias

Instala las dependencias del proyecto:

```bash
uv pip install -r requirements.txt
```

### 5. Verificación de la Instalación

Para asegurar que todo está correctamente configurado, ejecuta:

```bash
python --version  # Debería mostrar Python 3.13.x
uv --version      # Debería mostrar la versión instalada de uv
```

### 6. Uso de UV

**Añadir nuevos paquetes al entorno**:

```bash
uv pip install nombre-paquete
```

**Listar paquetes instalados**:

```bash
uv pip list
```

**Eliminar un paquete**:

```bash
uv pip uninstall nombre-paquete
```

### 7. Actualización del Entorno

Si deseas actualizar las dependencias a sus últimas versiones:

```bash
uv pip freeze > requirements.txt  # Guardar versiones actuales
uv pip install -U -r requirements.txt
```

### 8. Eliminación del Entorno Virtual

Si deseas reiniciar el entorno desde cero:

```bash
rm -rf .venv  # En Linux/macOS
```

o

```bash
rmdir /s .venv  # En Windows
```

Luego vuelve a crear el entorno con el paso 2.

### 9. Desactivar el Entorno

Cuando termines de trabajar, puedes desactivar el entorno virtual:

```bash
deactivate
```

---