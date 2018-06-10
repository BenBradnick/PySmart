import logging


class FileReader:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def read(self, filepath):
        try:
            with open(filepath, "r") as file:
                file_string = file.read()
            return file_string

        except IOError:
            self.logger.error("Cannot read file: {0}".format(filepath))
