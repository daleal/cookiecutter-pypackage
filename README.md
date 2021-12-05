# PyPackage Cookiecutter

This repository is a [cookiecutter](https://cookiecutter.readthedocs.io/) to quickly start a Python package. It contains **a ton** of very useful _features_ 🐳:

- Package management through [Poetry](https://python-poetry.org/) 💖
- Multiple linters (black, flake8, isort, pylint)
- Optional type checking using MyPy
- Configured tests using PyTest
- _Automagic_ deployment to PyPi on _merges_ to the `stable` branch
- Fully configured GitHub Actions workflows to lint and test the code on each Pull Request
- Optional CLI template to get you started quickly

The only requirements for this cookiecutter to work are:

- Python
- Cookiecutter

It is also recommended that you have the following software installed and on your PATH:

- Poetry
- Git

Otherwise, some of the creation steps might fail, and you would have to run them manually.

## Usage

To use this cookiecutter, make sure to have `cookiecutter` installed, or install it with the following command:

```sh
pip3 install -U cookiecutter
```

Then, simply execute:

```sh
python3 -m cookiecutter gh:daleal/cookiecutter-pypackage
```

This will prompt you with some options for the generated project, then create a virtualenv for your project's dependencies, install them on the virtualenv and initialize a `git` repository.

After creating the package, you should follow a couple of steps to make sure everything works _automagically_. Head over to [the generated `README.md` file]({{%20cookiecutter.project_name|lower|replace('-',%20'_')|replace('%20',%20'_')%20}}/README.md) to read about the next steps and a more _in-depth_ explanation of the generated project's _features_.
