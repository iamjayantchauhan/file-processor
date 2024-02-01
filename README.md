# file-processor

This is a sample CLI application developed using Python and Poetry Framework. The application pipeline moves the data from source to destination depending on the configuration provided.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Tests](#tests)
- [Project Structure](#project-structure)
- [Validations](#validations)
- [Contributing](#contributing)

## Features

- Move files in source directory based on user-specified criteria for files.
- Copy files from source directory to target directory based on user-specified criteria for file name format.
- Create a dated folder for each execution in the source and target directory.
- Handle duplicate folder names for the same day.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.11](https://kinsta.com/knowledgebase/install-python/#how-to-install-python "Click here for installation instructions")  or higher
- Pycharm or any other IDE of your choice ([Pycharm](https://beginnersbook.com/2018/01/python-install-pycharm-windows-mac-linux/ "Click here for installation instructions") is recommended)
- [Git CLI](https://kinsta.com/knowledgebase/install-git/ "Click here for installation instructions") for tracking changes
- [Poetry](https://python-poetry.org/ "Click here for installation instructions") framework


## Installation
1. Make sure you have installed all prerequisites.

2. Clone the repository using the command `git clone` or download the zip file

3. Open the project in any IDE and in terminal, run the command `poetry install` to install the dependencies and creating a virtual environment

## Tests

Run the application using the following command:

```bash
python main.py [OPTIONS]
```
Options:
- **-d, --directory DIRECTORY:** Specify the directory path.
- **-t, --file_type [csv|xml|json]:** Choose the file type (csv, xml, or json).
- **-f, --filename_format [numeric|alphanumeric|alphabetic]:** Select the filename format (numeric, alphanumeric, or alphabetic).

## Project Structure

```plaintext
file-processor/
|-- cli_app/
|   |-- __init__.py
|   |-- pipeline.py
|-- constants/
|   |-- __init__.py
|   |-- choices.py
|   |-- sizes.py
|-- utils/
|   |-- __init__.py
|   |-- directory_utils.py
|   |-- file_filters.py
|-- .gitignore
|-- .pre-commit-config.yaml
|-- commitlint.config.js
|-- poetry.lock
|-- pyproject.toml
|-- main.py
|-- README.md
```


## Validations

- Validate file path and folder structure.
- Validate file type, file size and filename format
- Handle related exceptions to prevent application crashes.

## Contributing

1. Fork the repository.
2. Create a new branch using git checkout -b feature/<feature-name>.
3. Commit your change using git commit.
4. Push to the branch using git push origin feature/<feature-name>.
5. Submit a pull request.
