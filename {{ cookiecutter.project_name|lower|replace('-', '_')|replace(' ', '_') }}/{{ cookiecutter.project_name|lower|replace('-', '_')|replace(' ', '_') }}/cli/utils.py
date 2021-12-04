from argparse import ArgumentParser


def setup_subparser_arguments(parser: ArgumentParser) -> ArgumentParser:
    """
    Setup the arguments for any of the subparsers (both subparsers
    use the same arguments on this reduced example).
    """
    parser.add_argument(
        "-s",
        "--secret",
        dest="secret",
        default="super-secret-stuff",
        help="Secret stuff or something...",
    )

    return parser
