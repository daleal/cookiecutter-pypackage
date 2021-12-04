"""Example module for the {{ cookiecutter.project_name }} package."""

import hashlib


class ExampleEngine:

    """
    This class represents a sample engine for
    the {{ cookiecutter.project_name }} package.
    """

{% if cookiecutter.include_type_checking == "yes" -%}

    def __init__(self, secret: str):

{%- else -%}

    def __init__(self, secret):

{%- endif -%}

        self.__secret = secret

{% if cookiecutter.include_type_checking == "yes" -%}

    def get_secret(self) -> str:

{%- else -%}

    def get_secret(self):

{%- endif -%}

        """Get the secret of the engine (wow, so secret)."""
        return self.__secret

{% if cookiecutter.include_type_checking == "yes" -%}

    def get_scrambled_secret(self) -> str:

{%- else -%}

    def get_scrambled_secret(self):

{%- endif -%}

        """Get the SHA256 hash of the secret of the engine."""
        scrambled = hashlib.sha256()
        scrambled.update(str.encode(self.__secret))
        return scrambled.hexdigest()
