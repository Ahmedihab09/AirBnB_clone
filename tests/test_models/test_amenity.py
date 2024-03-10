#!/usr/bin/python3
'''Test ameity class'''
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_default_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

if __name__ == '__main__':
    unittest.main()