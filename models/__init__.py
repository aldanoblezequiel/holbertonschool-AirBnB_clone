#!/usr/bin/python3
"""Module: FileStorage"""


from models.engine import file_storage
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.base_model import BaseModel


""" creates variable storage to call reload """

storage = file_storage.FileStorage()
storage.reload()
