"""
A module to route the {{ cookiecutter.project_name }} package CLI traffic.
"""

import sys

{%- if cookiecutter.include_type_checking == "yes" %}
from typing import Any
{%- endif %}

from {{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }} import ExampleEngine
from {{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }}.cli.generators import generate_main_parser

{% if cookiecutter.include_type_checking == "yes" %}
def dispatcher(*args: Any, **kwargs: Any) -> None:
{%- else %}
def dispatcher(*args, **kwargs):
{%- endif %}
    """
    Main CLI method, recieves the command line action and dispatches it to
    the corresponding method.
    """
    parser = generate_main_parser()
    parsed_args = parser.parse_args(*args, **kwargs)

    engine = ExampleEngine(parsed_args.secret)

    try:
        if parsed_args.action == "echo":
            print(engine.get_secret())
        elif parsed_args.action == "hash":
            print(engine.get_scrambled_secret())
    except AttributeError:
        print("An argument is required for this CLI.")
        parser.print_help()
        sys.exit(1)
