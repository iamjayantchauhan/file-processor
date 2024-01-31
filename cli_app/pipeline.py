"""
    This module handles flow of operations of this application
"""

import os

from constants.sizes import MAX_FILE_SIZE
from utils.directory_utils import copy_files, move_files
from utils.file_filters import (
    validate_file_size,
    validate_filename_format,
    validate_file_type,
)


# pylint: disable=too-many-instance-attributes
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
        file_operation_summary_display(): Displays final summary

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
        self.source_dir = os.path.join(self.path, "source")
        self.target_dir = os.path.join(self.path, "target")
        self.total_file_count = 0
        self.source_file_count = 0
        self.target_file_count = 0

    def file_operation_summary_display(self):
        """
        This is a simple function which displays the final summary of the process.
        """
        print(
            f"(i) {self.source_file_count} file(s) out of a total of "
            f"{self.total_file_count} files are matched with your given file type."
        )
        print(
            f"(ii) {self.target_file_count} file(s) processed to the target directory."
        )
        print(
            f"(iii) {self.source_file_count - self.target_file_count} file(s) were rejected. "
            f"Exceeding the size limit OR file name format mismatch."
        )

    def process_directory(self):
        """
        This method handles the flow of application
        """
        # create source and target directory if not exists

        # create dated directory with appropriate execution number

        # path of dated directory in source
        source_dated_directory = ""

        # path of dated directory in target
        target_dated_directory = ""

        # list files in the user given path
        files = os.listdir(self.path)

        # assigning total file count at user given path
        self.total_file_count = len(files) - 2

        # files with valid file type
        matched_file_type_list = list(
            filter(lambda file: validate_file_type(file, self.file_type), files)
        )

        # assigning source file count
        self.source_file_count = len(matched_file_type_list)

        # move valid files from user given path to source dated directory
        move_files(self.path, source_dated_directory, matched_file_type_list)

        # files with valid file name and file size
        accepted_files = list(
            filter(
                lambda file: validate_file_size(
                    file, source_dated_directory, MAX_FILE_SIZE
                )
                and validate_filename_format(file, self.filename_format),
                matched_file_type_list,
            )
        )

        # assigning target file count
        self.target_file_count = len(accepted_files)

        # copy valid files from source directory to target directory
        copy_files(source_dated_directory, target_dated_directory, accepted_files)

        # display summary
        self.file_operation_summary_display()
