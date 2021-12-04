# Env stuff
.PHONY: build-env
build-env:
	python3 -m venv .venv
	poetry run pip install --upgrade pip
	poetry run poetry install

# Tests
.PHONY: tests
tests:
	poetry run pytest --cov={{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }} --cov-report=term-missing --cov-report=xml tests

# Passive linters
.PHONY: black
black:
	poetry run black {{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }} tests --check

.PHONY: flake8
flake8:
	poetry run flake8 {{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }} tests

.PHONY: isort
isort:
	poetry run isort {{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }} tests --profile=black --check

.PHONY: pylint
pylint:
	poetry run pylint {{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }}

{% if cookiecutter.include_type_checking == "yes" -%}

.PHONY: mypy
mypy:
	poetry run mypy {{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }} tests

{%- endif %}

# Aggresive linters
.PHONY: black!
black!:
	poetry run black {{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }} tests

.PHONY: isort!
isort!:
	poetry run isort {{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }} tests --profile=black

# Utilities
.PHONY: bump!
bump!:
	sh scripts/bump.sh $(filter-out $@,$(MAKECMDGOALS))

# Receive args (use like `$(filter-out $@,$(MAKECMDGOALS))`)
%:
	@:
