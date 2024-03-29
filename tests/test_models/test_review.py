#!/usr/bin/python3

'''Tesy review class'''
import unittest
from models.review import Review
from tests.test_models import test_base_model

class TestReview(unittest.TestCase):
    def test_default_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

if __name__ == '__main__':
    unittest.main()