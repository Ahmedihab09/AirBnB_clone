#!/usr/bin/python3
"""Define the base model class."""


import models
import uuid
from datetime import datetime

class BaseModel:

    """Defines all common attributes/methods for other classes"""


    def __init__(self, *args, **kwargs):
        """Initialization of the base model with *args and **kwargs support"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep

    @classmethod
    def from_dict(cls, obj_dict):
        """Recreates an instance from a dictionary representation"""
        instance = cls()
        instance.id = obj_dict.get('id', str(uuid.uuid4()))
        instance.created_at = datetime.fromisoformat(obj_dict.get("created_at"))
        instance.updated_at = datetime.fromisoformat(obj_dict.get("updated_at"))

        for key, value in obj_dict.items():
            if key not in ('id', 'created_at', 'updated_at', '__class__'):
                setattr(instance, key, value)
        return instance
