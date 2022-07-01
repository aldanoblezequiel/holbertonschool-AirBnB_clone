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
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(my_dict, f)

    def new(self, obj):
        """Sets in __objects the obj with the
        key <obj class name>.id"""
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def reload(self):
        """Deserializes the Json file to
        __objects"""
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, "r", encoding="utf-8") as fd:
                dictj = json.load(fd)
                for key, value in dictj.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
