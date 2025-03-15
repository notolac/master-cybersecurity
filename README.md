# Máster en Ciberseguridad

Este repositorio contiene materiales y prácticas para el Máster en Ciberseguridad.

## Configuración del Entorno

Para asegurar la correcta ejecución del código, se recomienda configurar el entorno de desarrollo utilizando **Python 3.12.3** con **pyenv** y gestionar las dependencias con **uv**.

### 1. Instalación de pyenv

Si no tienes **pyenv** instalado, puedes hacerlo siguiendo las instrucciones de la [documentación oficial](https://github.com/pyenv/pyenv#installation). Una vez instalado, asegúrate de reiniciar tu terminal y ejecutar:

```bash
pyenv install 3.12.3
pyenv local 3.12.3
```

Esto establecerá la versión **Python 3.12.3** a nivel local en este directorio.

### 2. Instalación de pipx

Si no tienes **pipx**, instálalo con:

```bash
python -m pip install --user pipx
python -m pipx ensurepath
```

Luego, reinicia tu terminal para que los cambios en el PATH surtan efecto.

### 3. Instalación de uv

Para gestionar paquetes, utilizaremos **uv** en lugar de pip. Instálalo usando **pipx**:

```bash
pipx install uv
```

### 4. Instalación de dependencias

Si ya tienes un archivo `requirements.txt` o `pyproject.toml`, puedes instalar las dependencias con:

```bash
uv venv
uv pip install -r requirements.txt  # Si usas requirements.txt
uv pip install .  # Si usas pyproject.toml
```

### 5. Verificación de instalación

Para asegurarte de que todo está correctamente configurado, ejecuta:

```bash
python --version  # Debería mostrar Python 3.12.3
uv --version      # Debería mostrar la versión instalada de uv
```

### 6. Uso de uv

Para agregar paquetes nuevos al entorno:

```bash
uv pip install nombre-del-paquete
```

Para listar los paquetes instalados:

```bash
uv pip list
```

Para eliminar un paquete:

```bash
uv pip uninstall nombre-del-paquete
```

### 7. Actualización del entorno

Si deseas actualizar las dependencias a sus versiones más recientes:

```bash
uv pip freeze > requirements.txt  # Guarda las versiones actuales
uv pip install -U -r requirements.txt
```

### 8. Eliminación del entorno virtual

Si deseas reiniciar el entorno desde cero:

```bash
uv venv clear
```

---

Con esta configuración, puedes mantener un entorno limpio y reproducible para tus prácticas en el Máster en Ciberseguridad.

