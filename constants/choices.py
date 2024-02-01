"""
    This module contains mapping of constant values with function.
"""

# directory that maps formats with their validating functions
FILENAME_FUNCTIONS_MAPPING = {
    "alphabetic": lambda name: name.isalpha(),
    "numeric": lambda name: name.isnumeric(),
    "alphanumeric": lambda name: name.isalnum(),
}

# valid file types
VALID_FILE_TYPES = ["csv", "json", "xml"]

# valid filename formats
VALID_FILENAME_FORMATS = {
    "alpha": "alphabetic",
    "num": "numeric",
    "alnum": "alphanumeric",
}
