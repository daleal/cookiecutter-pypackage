# {{ cookiecutter.project_name }}

Welcome! If you're reading this it means that you just started your ✨ _shiny_ ✨ new Python package! This template should help you write the package that you always dreamt of without having to spend hours and hours trying to figure out how to configure a ton of misc stuff (that time I already spent for you 💖). Let's get started!

## First steps

Once the project has been created, two branches should exist: `{{ cookiecutter.git_main_branch }}` and `stable`. The first thing that you need to do is to create a repository on GitHub and _push_ both branches of this project to that repository. It is important that you push **both branches** and not only `{{ cookiecutter.git_main_branch }}`, as both will need to be used later on the process.

After your package has been uploaded to GitHub, create an API token for your PyPi account and add it as a GitHub secret to a `PYPI_API_TOKEN` named secret. This will allow GitHub to make _releases_ to PyPi.

Now that you've created you're project, uploaded it to GitHub and added a PyPi API token, let's move out attention to your local machine. Notice that there is a `.venv` folder on the root of the repository. This corresponds to the virtualenv that has your project's dependencies. To use the virtualenv, you can prepend every command with `poetry run`. Poetry will make sure to use the `python` interpreter inside the virtual environment:

```sh
poetry run python some_file.py
```

You can also "activate" the virtual environment to always use its interpreter:

```sh
. .venv/bin/activate
```

Now, every command will use the interpreter of the virtual environment. Remember to turn off the virtual environment once you stop using it:

```sh
deactivate
```

## The project structure

As you can see, your new project includes this `README.md` file, an MIT `LICENSE` (you can change it if you desire, I love the MIT license so I _defaulted_ it), some configuration files, a `.github` folder (which includes every GitHub workflow and GitHub related stuff), a `scripts` folder (which includes every script external to the library itself), a `tests` folder (for you to write your library's tests) and a `{{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }}` folder. That last folder will contain every bit of code for your project!

To create a new module inside of your `{{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }}` folder, create a folder and add an `__init__.py` file inside of the new empty folder. This will allow you to import stuff from that module to other parts of your package using a syntax like this:

```py
from {{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }}.module.inner_file import my_function
```

On this scenario, your repository tree would look something like:

```sh
{{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }}
├── .github
│   └── ...
├── {{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }}
│   ├── __init__.py
│   ├── module
│   │   ├── __init__.py
│   │   └── inner_file.py
│   └── file.py
├── scripts
│   └── bump.sh
├── tests
│   ├── __init__.py
│   ├── module
│   │   ├── __init__.py
│   │   └── test_inner_file.py
│   └── test_file.py
├── ...
├── LICENSE
└── README.md
```

## The `Makefile`

As you can see, there is a `Makefile` on the root of the repository. That `Makefile` is used as an aggregator for different meta-functionalities, such as linters and tests. Take a look at the file yourself! Notice that some instructions end using a `!` character. This means that those instructions will somehow change a file when executed (for example, running `make isort` will only lint your files and warn you about import sorting issues, but `make isort!` will _automagically_ fix them for you).

There is also a `bump!` instruction, that will be useful to change your project's version.

## The correct workflow

Now that some of the functionalities are sort of explained, let's take a look at the **expected** workflow. This template is **heavily** reliant on the correct usage of `git` and branches, so pay close attention.

Your _staging_ code will live on your `{{ cookiecutter.git_main_branch }}` branch (the main branch of your repository). **This branch does not correspond to the code on PyPi**. New _features_ must be created by creating a new branch from the `{{ cookiecutter.git_main_branch }}` branch. Then, a Pull Request must be created, from the _feature_ branch to the `{{ cookiecutter.git_main_branch }}` branch. This Pull Request will _automagically_ run the tests and linters on GitHub. If anything fails, GitHub will tell you. It will also check the coverage of your tests.

Once every _feature_ that you want for your package's next version is on the `{{ cookiecutter.git_main_branch }}` branch, run the following commands:

```sh
git switch {{ cookiecutter.git_main_branch }}
make bump! minor  # you can also bump! major and patch
```

This will create a new branch, bump the version of your `pyproject.toml` and `{{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }}/version.py`, then add and commit those changes. You now need to manually push the new branch to GitHub, create a Pull Request to your `{{ cookiecutter.git_main_branch }}` branch and merge it.

Finally, your `{{ cookiecutter.git_main_branch }}` branch has now all of the _features_ that you want for your package's next version and the version has been bumped. All that's left is to make a Pull Request from your `{{ cookiecutter.git_main_branch }}` branch to your `stable` branch. On this Pull Request, use [this file](.github/PULL_REQUEST_TEMPLATE/release.md) as a template for the Pull Request description. The description of this Pull Request will be _automagically_ added to the GitHub _releases_, so use it as a changelog ([here](https://github.com/daleal/asymmetric/releases) you can find an example). Once every linter and test has passed, merge the `{{ cookiecutter.git_main_branch }}` branch to `stable`. This will trigger a _release_ to PyPi of the new version of your package, and a new GitHub tag and _release_.
