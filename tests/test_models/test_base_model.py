import time
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import os

class TestBaseModel(unittest.TestCase):

    def test_new_instance(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertEqual(type(model.id), str)
        self.assertEqual(type(model.created_at), datetime)
        self.assertEqual(type(model.updated_at), datetime)

    def test_save_method(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        print("Initial updated_at:", initial_updated_at)
        time.sleep(5)
        model.save()
        print("Updated updated_at:", model.updated_at)
        self.assertGreater(model.updated_at, initial_updated_at, "Timestamp should be updated")

    def test_to_dict_method(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_reload_method(self):
        model = BaseModel()
        model.save()

        new_storage = FileStorage()
        new_storage.reload()

        loaded_model = new_storage.all()['BaseModel.{}'.format(model.id)]

        self.assertIsNotNone(loaded_model)
        self.assertIsInstance(loaded_model, BaseModel)
        self.assertEqual(loaded_model.id, model.id)
        self.assertEqual(loaded_model.created_at, model.created_at)
        self.assertEqual(loaded_model.updated_at, model.updated_at)

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

if __name__ == '__main__':
    unittest.main()