"""
    This module provides a set of utility functions for common tasks related
    to directory operations.
"""

import os
import shutil
import datetime as dt


def copy_files(source_directory: str, target_directory: str, files: list):
    """
    Copy given files from one directory to another directory
    :param source_directory: path of directory from where files to be copied
    :param target_directory: path of directory where copied files to be pasted
    :param files: list of files to be copied
    """
    for file in files:
        shutil.copy(
            os.path.join(source_directory, file), os.path.join(target_directory, file)
        )


def move_files(source_directory: str, target_directory: str, files: list):
    """
    This function moves files from given source directory to given target directory
    from given list of files.

    :param source_directory: path of directory from where files to be moved
    :param target_directory: path of directory where files to be moved
    :param files: list of files to be moved
    """
    for file in files:
        shutil.move(os.path.join(source_directory, file), target_directory)


def create_directory_ifnot(path: str):
    """
    Checks if directory at given path exists otherwise creates it
    """
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError as e:
            print(e, " at create_directory_ifnot method")


def producer_dated_dir(path: str) -> str:
    """
    Create dated directories in the source and target directories based on the current date.

    Parameters:
    - path (str): The path to directory where the dated subdirectories will be created.

    Returns:
    string: A string containing the path of the newly created dated directories.
    """

    today_date = dt.datetime.now().strftime("%d%m%Y")

    try:
        folders_date = list(filter(lambda x: today_date in x, os.listdir(path)))
        new_dated_folder = os.path.join(
            path, today_date + "_" + str(len(folders_date) + 1)
        )

        os.mkdir(path)
        return new_dated_folder
    except OSError as e:
        print(e, " at ", producer_dated_dir)
        return ""
