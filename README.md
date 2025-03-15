# AI Experiments

A Python project for experimenting with AI algorithms and utilities.

## Prerequisites

Before starting, make sure you have:

1. **Python 3.8+** installed on your system
2. **pip** (Python package installer)
3. **git** (for cloning the repository)

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ai-experiments.git
cd ai-experiments
```

### Option 1: Quick Setup (Recommended)

The project includes a verification script that sets up everything for you:

```bash
chmod +x verify_setup.sh
./verify_setup.sh
```

This script will:
- Create a virtual environment
- Install all dependencies
- Run tests to verify everything works

### Option 2: Manual Setup

Set up a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Install the package in development mode:

```bash
pip install -e ".[dev]"
```

To verify everything is set up correctly:

```bash
python test_project_setup.py
```

## Required Dependencies

The project automatically installs:

- **Core Dependencies**:
  - numpy (≥ 1.20.0)
  - pandas (≥ 1.3.0)

- **Development Dependencies** (installed with `[dev]` extra):
  - pytest (≥ 6.0.0)
  - black (≥ 22.0.0)
  - isort (≥ 5.0.0)
  - flake8 (≥ 4.0.0)
  - mypy (≥ 0.9.0)

## Project Structure

```
ai-experiments/
│
├── src/ai_experiments/    # Source code
│   ├── __init__.py
│   ├── utils.py          # Utility functions
│   └── models/           # ML models
│       ├── __init__.py
│       └── base.py       # Base model class
│
├── tests/                # Test suite
│   ├── __init__.py
│   └── test_utils.py    
│
├── pyproject.toml        # Project configuration
├── setup.py              # Package setup
└── requirements.txt      # Dependencies
```

## Usage

```python
from ai_experiments.utils import setup_logger

# Set up logging
logger = setup_logger()
logger.info("Starting AI experiment")
```

## Development

Run tests:

```bash
pytest
```

Format code:

```bash
black src tests
isort src tests
```

For convenience, these common tasks are available via make:

```bash
make install  # Install package and dependencies
make format   # Format code with black and isort
make lint     # Run linters (flake8, mypy)
make test     # Run tests
make clean    # Clean build artifacts
```

## License

[MIT](LICENSE)
