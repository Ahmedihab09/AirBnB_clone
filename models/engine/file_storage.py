#!/usr/bin/python3
"""Define FileStorage class"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ Sets obj with key in __objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        for obj in FileStorage.__objects.keys():
            obj_dict = {obj: FileStorage.__objects[obj].to_dict()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
        except Exception:
            pass