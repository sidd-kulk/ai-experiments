#!/bin/bash
set -e  # Exit on any error

echo "=== Creating and activating virtual environment ==="
python -m venv .venv
source .venv/bin/activate

echo "=== Installing the package ==="
pip install -e ".[dev]"

echo "=== Running tests ==="
pytest

echo "=== Testing code formatting ==="
black --check src tests
isort --check src tests

echo "=== Running linting ==="
flake8 src tests

echo "=== Testing project structure ==="
python test_project_setup.py

echo "=== All tests complete! ==="
