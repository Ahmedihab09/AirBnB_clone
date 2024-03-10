#!/usr/bin/python3
"""Define FileStorage class"""

import json
from models.base_model import BaseModel
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
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        data = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """Deserialization the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)

                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "User":
                        obj = User(**obj_data)
                    else:
                        obj = globals()[class_name].from_dict(obj_data)

                    existing_obj = next((o for o in FileStorage.__objects.values() if o.id == obj.id), None)

                    if existing_obj:
                        existing_obj.updated_at = obj.updated_at

                    else:
                        FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass


