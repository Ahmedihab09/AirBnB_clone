#!/usr/bin/python3
"""Define FileStorage class"""

import json
from models.base_model import BaseModel
from models import base_model

class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances"""

    def __init__(self):
        self.__file_path = "file_storage.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        data = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """Deserialization the JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)

                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    obj = globals()[class_name].from_dict(obj_data)

                    # Check if an object with the same ID already exists
                    existing_obj = next((o for o in self.__objects.values() if o.id == obj.id), None)

                    if existing_obj:
                        # Update existing object's attributes
                        existing_obj.updated_at = obj.updated_at
                        # Add more attributes to update as needed
                    else:
                        # Add the new object to __objects
                        self.__objects[key] = obj

        except FileNotFoundError:
            pass