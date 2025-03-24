# Cybersecurity Master

This repository contains materials and practices for the Cybersecurity Master's program.

## Environment Setup

To ensure correct code execution, it is recommended to set up the development environment using **Python 3.12.3** with **pyenv** and manage dependencies with **uv**.

### 1. Pyenv Installation

If you don't have **pyenv** installed, you can do so by following the instructions in the [official documentation](https://github.com/pyenv/pyenv#installation). Once installed, make sure to restart your terminal and run:

```bash
pyenv install 3.12.3
pyenv local 3.12.3
```

This will set **Python 3.12.3** locally in this directory.

### 2. Pipx Installation

If you don't have **pipx**, install it with:

```bash
python -m pip install --user pipx
python -m pipx ensurepath
```

Then, restart your terminal for the PATH changes to take effect.

### 3. UV Installation

To manage packages, we'll use **uv** instead of pip. Install it using **pipx**:

```bash
pipx install uv
```

### 4. Dependency Installation

If you already have a `requirements.txt` or `pyproject.toml` file, you can install dependencies with:

```bash
uv venv
uv pip install -r requirements.txt  # If using requirements.txt
uv pip install .  # If using pyproject.toml
```

### 5. Installation Verification

To ensure everything is correctly configured, run:

```bash
python --version  # Should show Python 3.12.3
uv --version      # Should show the installed uv version
```

### 6. UV Usage

To add new packages to the environment:

```bash
uv pip install package-name
```

To list installed packages:

```bash
uv pip list
```

To remove a package:

```bash
uv pip uninstall package-name
```

### 7. Environment Update

If you want to update dependencies to their latest versions:

```bash
uv pip freeze > requirements.txt  # Save current versions
uv pip install -U -r requirements.txt
```

### 8. Virtual Environment Removal

If you want to restart the environment from scratch:

```bash
uv venv clear
```

---

With this configuration, you can maintain a clean and reproducible environment for your practices in the Cybersecurity Master's program.