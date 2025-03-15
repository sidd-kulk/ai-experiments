.PHONY: install format lint test clean

install:
	pip install -e ".[dev]"

format:
	black src tests
	isort src tests

lint:
	flake8 src tests
	mypy src tests

test:
	pytest -xvs

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .coverage -exec rm -rf {} +
