# Cybersecurity Master

This repository contains materials and practices for the Cybersecurity Master's program.

## Environment Setup

To ensure correct code execution, it is recommended to set up the development environment using **Python 3.12.3** and manage dependencies with **uv**.

### 1. UV Installation

To manage packages and Python versions, we'll use **uv**. Install it using **pipx**:

First, install **pipx** if you don't have it:

```bash
python -m pip install --user pipx
python -m pipx ensurepath
```

Then, restart your terminal for the PATH changes to take effect.

Now install **uv**:

```bash
pipx install uv
```

### 2. Environment Creation and Activation

Create a virtual environment with the Python version specified in `pyproject.toml`:

```bash
uv venv
```

**Important**: After creating the virtual environment, you need to activate it:

```bash
source .venv/bin/activate  # On Linux/macOS
# or
.venv\Scripts\activate     # On Windows
```

### 3. Dependency Installation

Install the project dependencies:

```bash
uv pip install -r requirements.txt  # If using requirements.txt
uv pip install -e .  # Install the project in editable mode
```

### 4. Installation Verification

To ensure everything is correctly configured, run:

```bash
python --version  # Should show Python 3.12.3
uv --version      # Should show the installed uv version
```

### 5. UV Usage

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

### 6. Environment Update

If you want to update dependencies to their latest versions:

```bash
uv pip freeze > requirements.txt  # Save current versions
uv pip install -U -r requirements.txt
```

### 7. Virtual Environment Removal

If you want to restart the environment from scratch:

```bash
uv venv clear
```

### 8. Deactivating the Environment

When you're done working, you can deactivate the virtual environment:

```bash
deactivate
```

---

With this configuration, you can maintain a clean and reproducible environment for your practices in the Cybersecurity Master's program. The `uv` tool will automatically handle the Python version specified in `pyproject.toml`, making the setup process much simpler.