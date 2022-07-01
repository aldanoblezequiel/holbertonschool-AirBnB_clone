#!/usr/bin/python3

"""
Module Class: FileStorage
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class FileStorage:
    """Class: FileStorage: Serializes to
    JSON and deserializes JSON to object"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def save(self):
        """Serializes objetcs to the JSON file"""
        my_dict = {}
        for name, value in self.__objects.items():
            my_dict[name] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as json_file:
            json.dump(my_dict, json_file)

    def new(self, obj):
        """Sets in __objects the obj with the
        key <obj class name>.id"""
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def reload(self):
        """Deserializes the Json file to
        __objects"""
