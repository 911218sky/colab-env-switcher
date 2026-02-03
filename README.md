# Colab Environment Switcher

A simple Python library to easily switch Python versions in Google Colab environments.

## Features

- 🚀 Quick Python version switching in Google Colab
- 📦 Automatic pip installation for the new Python version
- ✅ Simple one-line API
- 🔧 Optional uv package manager installation

## Installation

### From PyPI (Recommended)

```python
# Install directly from PyPI
!pip install colab-env-switcher
```

### From GitHub Release

```bash
# Install from GitHub Release wheel file
pip install https://github.com/911218sky/colab-env-switcher/releases/latest/download/colab_env_switcher-0.1.0-py3-none-any.whl
```

### From GitHub Source

```python
# Install latest version from GitHub source
!pip install git+https://github.com/911218sky/colab-env-switcher.git
```

### Local Development

```bash
pip install -e .
```

## Usage

### Basic Usage

```python
from colab_env_switcher import switch_python_version

# Switch to Python 3.11
switch_python_version("3.11")
```

### With uv Package Manager

```python
from colab_env_switcher import switch_python_version

# Switch to Python 3.10 and install uv
switch_python_version("3.10", install_uv=True)
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `version` | str | required | Python version to switch to (e.g., "3.11") |
| `install_uv` | bool | False | Install uv package manager after switching |

## Supported Python Versions

- Python 3.7
- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12
- Python 3.13 (if available)
- Python 3.14 (experimental, if available)

**Note:** Newer Python versions (3.13+) may have limited package availability. For production use, we recommend Python 3.10-3.12.

## Example in Colab

```python
# Install the library
!pip install colab-env-switcher

# Import and use
from colab_env_switcher import switch_python_version

# Switch to Python 3.11
switch_python_version("3.11")

# Verify the version
import sys
print(sys.version)

# Reinstall your required packages
!pip install numpy pandas matplotlib
```

## Important Notes

⚠️ **After switching Python versions:**
- You need to reinstall all required packages

## License

MIT License
