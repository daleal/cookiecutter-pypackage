"""Example module for the {{ cookiecutter.project_name }} package."""

import hashlib


class ExampleEngine:

    """
    This class represents a sample engine for
    the {{ cookiecutter.project_name }} package.
    """

    def __init__(self, secret: str):
        self.__secret = secret

    def get_secret(self) -> str:
        """Get the secret of the engine (wow, so secret)."""
        return self.__secret

    def get_scrambled_secret(self) -> str:
        """Get the SHA256 hash of the secret of the engine."""
        scrambled = hashlib.sha256()
        scrambled.update(str.encode(self.__secret))
        return scrambled.hexdigest()
