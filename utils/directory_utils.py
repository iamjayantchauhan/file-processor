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
    if not (os.path.exists(source_directory) or os.path.exists(target_directory)):
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

    if not (os.path.exists(source_directory) or os.path.exists(target_directory)):
        for file in files:
            try:
                shutil.move(os.path.join(source_directory, file), target_directory)
            except OSError as e:
                print(f"{e} occurred while moving files from {source_directory} to {target_directory}")

                
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
    folders_date = list(
        filter(
            lambda x: today_date in x and (os.path.isdir(os.path.join(path, x))),
            os.listdir(path),
        )
    )
    execution_no = [x.split("_")[1] for x in folders_date]
    new_dated_folder = ""
    last_execution = 0

    if len(folders_date) != 0:
        last_execution = max(int(x) for x in execution_no)
    try:
        new_dated_folder = os.path.join(
            path, today_date + "_" + str(last_execution + 1)
        )
        os.mkdir(new_dated_folder)
    except OSError as e:
        print(e, " at ", producer_dated_dir)
    return new_dated_folder
