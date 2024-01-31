"""
    This module provides a set of utility functions for common tasks related to directory operations.
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
        shutil.copy(os.path.join(source_directory, file), os.path.join(target_directory, file))
