#!/usr/bin/python3
""" test of User class """

import unittest
import console
from console import HBNBCommand


class TestUser(unittest.TestCase):
    """ Test User Class """

    def test_docstring(self):
        """ Test if all docstring were written """
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand().do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand().do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand().emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand().do_create.__doc__)
        self.assertIsNotNone(HBNBCommand().do_show.__doc__)
        self.assertIsNotNone(HBNBCommand().do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand().do_all.__doc__)


if __name__ == '__main__':
    unittest.main()