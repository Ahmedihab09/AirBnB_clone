#!/usr/bin/python3
"""
test_user.py
Class to test the User class.
"""

import unittest
from models.user import User
from datetime import datetime
from tests.test_models import test_base_model

class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up for the tests."""
        self.user1 = User()
        self.user1.email = "test@example.com"
        self.user1.password = "root"
        self.user1.first_name = "John"
        self.user1.last_name = "Doe"

    def tearDown(self):
        """Tear down the test case."""
        del self.user1

    def test_instance_creation(self):
        """Test if the instance is correctly created."""
        self.assertIsInstance(self.user1, User)

    def test_attributes(self):
        """Test if the attributes are correctly assigned."""
        self.assertEqual(self.user1.email, "test@example.com")
        self.assertEqual(self.user1.password, "root")
        self.assertEqual(self.user1.first_name, "John")
        self.assertEqual(self.user1.last_name, "Doe")

    def test_inheritance(self):
        """Test if User is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.user1), User))

    def test_id(self):
        """Test if the id is a string."""
        self.assertIsInstance(self.user1.id, str)

    def test_created_at(self):
        """Test if created_at is of datetime type."""
        self.assertIsInstance(self.user1.created_at, datetime)

    def test_updated_at(self):
        """Test if updated_at is of datetime type."""
        self.assertIsInstance(self.user1.updated_at, datetime)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for JSON."""
        user_dict = self.user1.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn("email", user_dict)
        self.assertIn("password", user_dict)
        self.assertIn("first_name", user_dict)
        self.assertIn("last_name", user_dict)
        self.assertIn("__class__", user_dict)
        self.assertEqual(user_dict["__class__"], "User")

if __name__ == "__main__":
    unittest.main()
