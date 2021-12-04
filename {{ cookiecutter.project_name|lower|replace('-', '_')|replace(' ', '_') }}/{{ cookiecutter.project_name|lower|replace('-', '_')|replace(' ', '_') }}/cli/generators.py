"""
A module to hold the CLI parser generators.
"""

from argparse import ArgumentParser {%- if cookiecutter.include_type_checking == "yes" %}, _SubParsersAction{% endif %}

import {{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }}
from {{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }}.cli.utils import setup_subparser_arguments

{% if cookiecutter.include_type_checking == "yes" %}
def generate_main_parser() -> ArgumentParser:
{%- else %}
def generate_main_parser():
{%- endif %}
    """Generates the main parser."""
    # Create parser
    parser = ArgumentParser(
        description="Command line interface tool for {{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }}."
    )

    # Add version flag
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }} version {% raw %}{{% endraw %}{{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }}.__version__{% raw %}}{% endraw %}",
    )

    # In order to allow the CLI utility grow, the parser will include an
    # initial argumment to determine which subparser will be executed.

    # Create subparsers
    subparsers = parser.add_subparsers(help="Action to be executed.")

    # Echo parser
    generate_echo_subparser(subparsers)

    # Hash parser
    generate_hash_subparser(subparsers)

    return parser

{% if cookiecutter.include_type_checking == "yes" %}
def generate_echo_subparser(subparsers: _SubParsersAction) -> ArgumentParser:
{%- else %}
def generate_echo_subparser(subparsers):
{%- endif %}
    """Generates the subparser for the echo option."""
    subparser = subparsers.add_parser("echo")
    subparser.set_defaults(action="echo")
    return setup_subparser_arguments(subparser)

{% if cookiecutter.include_type_checking == "yes" %}
def generate_hash_subparser(subparsers: _SubParsersAction) -> ArgumentParser:
{%- else %}
def generate_hash_subparser(subparsers):
{%- endif %}
    """Generates the subparser for the hash option."""
    subparser = subparsers.add_parser("hash")
    subparser.set_defaults(action="hash")
    return setup_subparser_arguments(subparser)
