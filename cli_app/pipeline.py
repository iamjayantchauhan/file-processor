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

    def process_directory(self):
        # extract files from input directory and create dated directory with appropriate execution number
        # path of dated directory in source
        source_dated_directory = ""

        # path of dated directory in target
        target_dated_directory = ""

        # validate file type and move to source directory
        # files with valid file type
        source_files = []

        # files with valid file name and file size
        accepted_files = list(
            filter(lambda file: validate_file_size(file, source_dated_directory, MAX_FILE_SIZE) and validate_filename_format(file, self.filename_format), source_files))

        # copy valid files from source directory to target directory
        copy_files(source_dated_directory, target_dated_directory, accepted_files)
