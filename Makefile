pre-commit:
	make clean lint test
clean:
	poetry run isort .
	poetry run black .
lint:
	poetry run flake8
	poetry run mypy .
	poetry run pylint ./**/*.py
static:
	poetry run mypy .
test:
	poetry run pytest
verbose-test:
	poetry run pytest -s -vvv
