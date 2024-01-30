"""
    This module includes functions for filtering and processing files based on various criteria.
"""

import os
from constants.choices import FILENAME_FUCTIONS_MAPPING
from constants.sizes import MB_TO_BYTES


def validate_file_size(file: str, source: str, size: int) -> bool:
    """
    This function checks whether the size of given file is below given limit or not
    :param source: directory in which given file resides
    :param file: file whose size to be checked
    :param size: maximum size limit
    :return: True if the size of given file is below given size, False otherwise
    """
    return os.stat(os.path.join(source, file)).st_size / MB_TO_BYTES <= size


def validate_filename_format(file: str, key: str) -> bool:
    """
    This function checks whether filename of given file matches with given format or not
    :param file: name of the file
    :param key: name of file format
    :return: True if file name matches with given format, False otherwise
    """
    filename, _ = os.path.splitext(file)
    return FILENAME_FUCTIONS_MAPPING[key](filename)
