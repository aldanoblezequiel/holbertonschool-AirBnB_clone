#!/usr/bin/python3
"""
Module Class: FileStorage
"""
import json
from os import path
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
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        "Amenity": Amenity,
        "City": City,
        "State": State,
        "Place": Place,
        "Review": Review
               }
    
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
