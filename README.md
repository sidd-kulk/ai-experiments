# AI Experiments

A Python project for experimenting with AI algorithms and utilities.

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ai-experiments.git
cd ai-experiments
```

Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the package in development mode:

```bash
pip install -e ".[dev]"
```

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

## License

[MIT](LICENSE)
