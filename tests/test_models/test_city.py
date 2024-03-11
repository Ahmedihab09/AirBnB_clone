#!/usr/bin/python3
'''Test city Class'''

import unittest
from models.city import City
from tests.test_models import test_base_model

class TestCity(unittest.TestCase):
    def test_default_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == '__main__':
    unittest.main()