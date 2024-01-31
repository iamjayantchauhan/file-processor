"""
    This module contains mapping of constant values with function.
"""

# directory that maps formats with their validating functions
FILENAME_FUCTIONS_MAPPING = {
    'alphabetic': lambda name: name.isalpha(),
    'numeric': lambda name: name.isnumeric(),
    'alphanumeric': lambda name: name.isalnum(),
}
