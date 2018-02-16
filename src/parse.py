import argparse


def prepare_parser():
    """
    Setup the program arguments.

    Returns
    -------
    parser : argparse.ArgumentParser
        Parser object set up with the program arguments.
    """
    parser = argparse.ArgumentParser(
        description='Save and restore qpdfview tab and bookmark sessions'
    )
    parser.add_argument(
        '--list',
        help='List the current sessions',
        default=False,
        action='store_true',
    )
    parser.add_argument(
        '--save',
        help='Save the current session with the given name',
        metavar='name'
    )
    parser.add_argument(
        '--restore',
        help='Restore the session with the given name',
        metavar='name'
    )
    parser.add_argument(
        '--delete',
        help='Delete the session with the given name',
        metavar='name'
    )
    parser.add_argument(
        '--backup',
        help='Backup all the saved sessions',
        default=False,
        action='store_true',
    )
    parser.add_argument(
        '--clean',
        help='Clean the current session',
        default=False,
        action='store_true'
    )
    return parser
