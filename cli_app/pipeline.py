import os


class Processor:
    def __init__(self, path: str, file_type: str, filename_format: str):
        # Variable declaration
        self.path = path
        self.file_type = file_type
        self.filename_format = filename_format
        self.source_dir = os.path.join(self.path, 'source')
        self.target_dir = os.path.join(self.path, 'target')


        # Pipline function call



#  Validate directory Methods