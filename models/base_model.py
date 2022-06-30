#!/usr/bin/python3
""" Module: BaseModel
"""
import models
from datetime import datetime
from uuid import uuid4

class BaseModel():
    """Class: BaseModel:Defines bases 
       for the rest of the classes
    """
    def __init__(self, *args, **kwargs):
        """Initializing BaseModel"""
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates the public instance attribute
        updated_at with the current datetime"""
        self.update_at = datetime.now()
        models.storage.save()
        print(datetime.now())

    def to_dict(self):
        """Returns a dictionary containing all keys/
        values of the instance"""
        key_dictionary = self.__dict__.copy()


