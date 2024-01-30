"""
    This module contains mapping of constant values with function.
"""

# directory that maps formats with their validating functions
FILENAME_FUCTIONS_MAPPING = {
    'alphabetic': lambda x: x.isalpha(),
    'numeric': lambda x: x.isnumeric(),
    'alphanumeric': lambda x: x.isalnum(),
}
