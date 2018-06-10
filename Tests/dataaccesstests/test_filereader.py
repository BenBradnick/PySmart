import unittest
from pysmart.dataaccess.filereader import FileReader


class IOExceptions(unittest.TestCase):

    def test_raises_IOError_when_file_does_not_exist(self):
        file_reader = FileReader()

        self.assertRaises(Exception, file_reader.read("not_exists.not"))

    def test_does_not_raise_IOError_when_file_does_exist(self):
        file_reader = FileReader()

        try:
            file_reader.read("pysmart/__init__.py")
        except IOError:
            self.fail("FileReader raised IOError for valid file")
