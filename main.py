"""
Main file for the project. Only take input and process pipeline here.
"""

import sys
import click
from cli_app.pipeline import Processor
from utils import inputs


if __name__ == "__main__":

    try:
        path, file_format, name_format = inputs.get_input(standalone_mode=False)
        pipeline = Processor(path, file_format, name_format)
        pipeline.process_directory()
    except click.exceptions.Abort:
        print(f"\nForced Stopped \t\t\t python {sys.argv[0]}")
    except click.exceptions.NoSuchOption as e:
        print(f"\nInvalid Option: {e}")
    except click.exceptions.BadParameter as e:
        print(f"\nInvalid Parameter: {e}")
    except click.exceptions.UsageError as e:
        print(f"\nInvalid Usage: {e}")
    except PermissionError as e:
        print(f"\n{e}: Please enter accessible path.")
