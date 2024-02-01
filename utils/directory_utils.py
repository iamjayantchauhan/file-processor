"""
    This module provides a set of utility functions for common tasks related
    to directory operations.
"""

import os
import shutil


def copy_files(source_directory: str, target_directory: str, files: list):
    """
    Copy given files from one directory to another directory
    :param source_directory: path of directory from where files to be copied
    :param target_directory: path of directory where copied files to be pasted
    :param files: list of files to be copied
    """

    for file in files:
        try:
            shutil.copy(
                os.path.join(source_directory, file), os.path.join(target_directory, file)
            )
        except OSError as e:
            print(f"{e} occurred while copying files from {source_directory} to {target_directory}")


def move_files(source_directory: str, target_directory: str, files: list):
    """
    This function moves files from given source directory to given target directory
    from given list of files.

    :param source_directory: path of directory from where files to be moved
    :param target_directory: path of directory where files to be moved
    :param files: list of files to be moved
    """
    for file in files:
        try:
            shutil.move(os.path.join(source_directory, file), target_directory)
        except OSError as e:
            print(f"{e} occurred while moving files from {source_directory} to {target_directory}")