# Detailed Installation Guide

This document provides comprehensive installation instructions for the AI Experiments project.

## System Requirements

- Python 3.8 or higher
- pip (Python package installer)
- git (for version control)
- Recommended: 4GB RAM or more for machine learning experiments

## Step 1: Check Python Installation

Verify that you have Python 3.8+ installed:

```bash
python --version
# or
python3 --version
```

If Python is not installed or the version is lower than 3.8, download and install it from [python.org](https://www.python.org/downloads/).

## Step 2: Clone the Repository

```bash
git clone https://github.com/yourusername/ai-experiments.git
cd ai-experiments
```

## Step 3: Set Up a Virtual Environment

It's recommended to use a virtual environment to avoid conflicts with other Python packages:

### On macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

You should see your terminal prompt change to indicate the virtual environment is active.

## Step 4: Install the Package

Once the virtual environment is active, install the package with development dependencies:

```bash
pip install -e ".[dev]"
```

This installs:
- Core dependencies: numpy, pandas
- Development tools: pytest, black, isort, flake8, mypy

## Step 5: Verify Installation

Run the setup verification script:

```bash
python test_project_setup.py
```

You should see all checks pass.

## Step 6: Run Tests

Confirm everything is working by running the tests:

```bash
pytest
```

## Troubleshooting

### Import Errors

If you encounter import errors when running scripts or tests:

```bash
# Make sure you're in the project root directory
cd /path/to/ai-experiments

# Make sure your virtual environment is activated
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Try running with the src directory in the Python path
PYTHONPATH=src pytest
```

### Installation Errors

If you encounter errors during package installation:

1. Make sure your pip is up-to-date:
   ```bash
   pip install --upgrade pip
   ```

2. If there are issues with specific packages:
   ```bash
   pip install numpy pandas  # Install core dependencies
   pip install pytest black isort flake8 mypy  # Install dev dependencies
   ```

### Virtual Environment Issues

If you have trouble with the virtual environment:

```bash
# Remove the existing environment if it's corrupted
rm -rf .venv  # On Windows: rmdir /s /q .venv

# Create a fresh environment
python -m venv .venv
```

## Optional: IDE Configuration

### Visual Studio Code

For VS Code users, create a `.vscode/settings.json` file with:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "python.testing.nosetestsEnabled": false
}
```

### PyCharm

For PyCharm users:
1. Go to Settings → Project → Python Interpreter
2. Add Interpreter → Existing Environment
3. Select the Python executable in your `.venv/bin/` directory
