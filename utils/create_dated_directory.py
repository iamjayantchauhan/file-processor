"""
create_dated_dir Module

This module provides a function for creating dated directories in the source and target directories
based on the current date. The created directories follow a specific naming convention with the
current date and an execution number.

"""

import datetime as dt
import os


def producer_dated_dir(source_dir: str, target_dir: str) -> tuple:
    """
    Create dated directories in the source and target directories based on the current date.

    Parameters:
    - source_dir (str): The source directory where the dated subdirectories will be created.
    - target_dir (str): The target directory where corresponding dated subdirectories will be created.

    Returns:
    tuple: A tuple containing the paths of the newly created source and target directories.
    """

    today_date = dt.datetime.now().strftime("%d%m%Y")

    try:
        folders_date = list(filter(lambda x: today_date in x, os.listdir(source_dir)))
        source_new_folder = os.path.join(
            source_dir, today_date + "_" + str(len(folders_date) + 1)
        )
        target_new_folder = os.path.join(
            target_dir, today_date + "_" + str(len(folders_date) + 1)
        )
        os.mkdir(source_new_folder)
        os.mkdir(target_new_folder)
        return source_new_folder, target_new_folder
    except OSError as e:
        print(e, " at ", producer_dated_dir)
        return None, None
