#!/usr/bin/python3
""" test of BaseModel class """

import unittest
from models.engine import file_storage as file_storage_module
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """ Test BaseModel Class """

    def test_docstring(self):
        """ Test if all docstring were written """
        self.assertIsNotNone(file_storage_module.__doc__)
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_attributes(self):
        """ Check required attribute are created """
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))


if __name__ == '__main__':
    unittest.main()
