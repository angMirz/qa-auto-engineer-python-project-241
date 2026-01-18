.PHONY: lint fix test test-coverage

lint:
	uv run ruff check .

fix:
	uv run ruff check --fix .

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml