# PyPackage Cookiecutter

This repository is a [cookiecutter](https://cookiecutter.readthedocs.io/) to quickly start a Python package. These are the _features_:

- Package management through [Poetry](https://python-poetry.org/)
- Multiple linters (black, flake8, isort, pylint)
- Optional type checking using MyPy
- Configured tests using PyTest
- _Automagic_ deployment to PyPi on _merges_ to the `stable` branch
- Fully configured GitHub Actions workflows to lint and test the code on each Pull Request
- Optional CLI template to get you started

The only requirements for this cookiecutter to work are:

- Python
- Cookiecutter

It is also recommended that you have the following software installed and on your PATH:

- Poetry
- Git

## Usage

To use this cookiecutter, make sure to have `cookiecutter` installed and execute the following command:

```sh
cookiecutter gh:daleal/cookiecutter-pypackage
```

This will prompt you with some options for the generated project, then create a virtualenv for your project's dependencies, install them on the virtualenv and initialize a `git` repository.
