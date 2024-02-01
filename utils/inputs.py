"""
This module is used to get the input from the user interactively using click module.
"""

import click
from constants import choices


@click.command(add_help_option=False)
@click.option(
    "--path",
    "-p",
    type=click.Path(exists=True, resolve_path=True, readable=True, file_okay=False),
    help="Choose a directory path",
    prompt="Please select a directory path",
)
@click.option(
    "--file_format",
    "-f",
    type=click.Choice(choices.VALID_FILE_TYPES, case_sensitive=False),
    help="Choose from a list of file format",
    prompt="Please select a file type",
)
@click.option(
    "--name_format",
    "-n",
    type=click.Choice(choices.VALID_FILENAME_FORMATS, case_sensitive=False),
    help="Choose from a list of name format",
    prompt="Please select a filename format",
)
def get_input(path: str = None, file_format: str = "csv", name_format: str = "alnum"):
    """
    This function is used to get the input from the user interactively using click module.

    :param path: Path of the directory
    :param file_format: Format of the file that needs to be processed, Choices :- [csv, json, xml]
    :param name_format: Naming convention of the file that needs to be processed,
        Choices :- [num (numeric) , alpha (alphabetic), alnum(alphanumeric)]
    :return: path, file_format, name_format
    """

    return path, file_format, choices.VALID_FILENAME_FORMATS[name_format]
