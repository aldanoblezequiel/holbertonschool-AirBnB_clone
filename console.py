#!/usr/bin/python3

""" import modules"""

import sys
import encodings
import cmd
import json
from sys import argv
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity

""" file class HBNBCommand """


class HBNBCommand(cmd.Cmd):
    """class"""

    prompt = "(hbnb) "
    clases = ["BaseModel", "City", "User", "Place",
            "State", "Review", "Amenity"]

    def do_quit(self, arg):
        """command Quit to exit the program"""
        sys.exit()

    def do_EOF(self, arg):
        """command EOF to exit the program """
        sys.exit()

    def emptyline(self):
        """line command"""
        pass

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
