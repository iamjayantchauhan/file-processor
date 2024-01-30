"""
    This module handles flow of operations of this application
"""

import os
from constants.sizes import MAX_FILE_SIZE
from utils.directory_utils import copy_files
from utils.file_filters import validate_file_size, validate_filename_format


class Processor:
    """
    A class responsible for controlling the flow of execution in a program.
    It coordinates the sequence of actions and manages the overall program behavior.

    Attributes:
        path (str): Path of input directory which is going to be processed
        file_type (str): Valid file type
        filename_format (str): Valid file name format

    Methods:
        process_directory(): Process inputs and return results
        __validate_filesize_and_filename(): Validates files based on file size and file name

    """
    def __init__(self, path: str, file_type: str, filename_format: str):
        """
        Initialize new Processor instance.
        :param path: path to input directory to be processed
        :param file_type: valid file type
        :param filename_format: valid file name format
        """
        # Variable declaration
        self.path = path
        self.file_type = file_type
        self.filename_format = filename_format
        self.source_dir = os.path.join(self.path, 'source')
        self.target_dir = os.path.join(self.path, 'target')

    def __validate_filesize_and_filename(self, source: str, files: list, size: int, key: str) -> list:
        """
        This function validates file size and file format based on given criteria for given files
        :param source: path of the directory in which files resides
        :param files: list of files to validate
        :param size: maximum size limit
        :param key: name of file format
        :return: list of files passed given criteria
        """

        valid_files = list(
            filter(lambda x: validate_file_size(x, source, size) and validate_filename_format(x, key), files))

        return valid_files

    def process_directory(self):
        # code until files are processed to Source directory
        source_dated_directory = ""
        target_dated_directory = ""
        source_files = []

        # files with valid file name and file size
        accepted_files = self.__validate_filesize_and_filename(source_dated_directory, source_files, MAX_FILE_SIZE,
                                                               self.filename_format)

        # copy valid files from source directory to target directory
        copy_files(source_dated_directory, target_dated_directory, accepted_files)
