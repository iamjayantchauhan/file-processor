"""
    This module includes functions for filtering and processing files based on various criteria.
"""

import os

from constants.choices import FILENAME_FUNCTIONS_MAPPING
from constants.sizes import MB_TO_BYTES


def validate_file_size(file: str, source: str, size: int) -> bool:
    """
    This function checks whether the size of given file is below given limit or not
    :param source: directory in which given file resides
    :param file: file whose size to be checked
    :param size: maximum size limit
    :return: True if the size of given file is below given size, False otherwise
    """
    file_path = os.path.join(source, file)
    if not os.path.exists(file_path):
        print(f"Path :'{file_path}' Does not exist while checking valid size. ")
        return False
    flag = os.path.getsize(file_path) / MB_TO_BYTES <= size
    return flag


def validate_filename_format(file: str, key: str) -> bool:
    """
    This function checks whether filename of given file matches with given format or not
    :param file: name of the file
    :param key: name of file format
    :return: True if file name matches with given format, False otherwise
    """
    filename, _ = os.path.splitext(file)
    return FILENAME_FUNCTIONS_MAPPING[key](filename)


def validate_file_type(file: str, valid_file_type: str) -> bool:
    """
    :param file: name of the file
    :param valid_file_type: valid file type given by user
    :return: True if file matches with given valid_file_type, False otherwise
    """
    flag = file.casefold().endswith(str(".") + valid_file_type.casefold())
    return flag
