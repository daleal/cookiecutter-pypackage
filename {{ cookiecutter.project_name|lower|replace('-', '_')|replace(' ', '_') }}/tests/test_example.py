import hashlib

from {{ cookiecutter.project_name|lower|replace('-', '_')|replace(' ', '_') }}.example import ExampleEngine


class TestExampleEngine:

    """Very dumb test class to execute some example tests."""

    def setup_method(self):
        comparer = hashlib.sha256()

        self.secret = "this is a ultra secret string (I wish)"
        comparer.update(str.encode(self.secret))
        self.scrambled_secret = comparer.hexdigest()

        self.example_engine = ExampleEngine(self.secret)

    def test_secret_getter(self):
        """
        Assert that the `get_secret` method returns the original secret
        and not the scrambled one.
        """
        accessed_secret = self.example_engine.get_secret()
        assert accessed_secret != self.scrambled_secret
        assert accessed_secret == self.secret

    def test_scrambled_secret_getter(self):
        """
        Assert that the `get_scrambled_secret` method returns the scrambled
        secret and not the original one.
        """
        scrambled_secret = self.example_engine.get_scrambled_secret()
        assert scrambled_secret != self.secret
        assert scrambled_secret == self.scrambled_secret
