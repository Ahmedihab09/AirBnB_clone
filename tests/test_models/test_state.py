#!/usr/bin/python3

'''Test state class'''
import unittest
from models.state import State
from tests.test_models import test_base_model

class TestState(unittest.TestCase):
    def test_default_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()