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
    classes = ["BaseModel", "City", "User", "Place",
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

    def do_help(self):
        """help documentation"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id."""
        if not arg:
            print("** class doesn't exist **")
        elif not arg in HBNBCommand.classes:
            print("** class name missing **")
        else:
            new_obj = eval(arg)()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """Print the string representation
        of an instance based on the class
        name and id"""
        array = arg.split()
        dict_obj = storage.all()
        new_list = []

        if len(array) < 1:
            print("** class name missing **")
        elif array[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(array) < 2:
            print("** instance id missing **")
        else:
            for key, value in dict_obj.items():
                if value.__class__.__name__ == array[0]:
                    new_list.append(value)
            for instance in new_list:
                if instance.id == array[1]:
                    print(instance)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class
        name and id"""
        array = arg.split()

        if len(array) < 1:
            print("** class name missing **")
        elif array[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(array) < 2:
            print("** instance id missing **")
        else:
            new_list = ""

            with open("file.json", "r", encoding="utf-8") as flj:
                list = json.load(flj)
            for key in list:
                ar = key.split(".")
                if array[1] == ar[1]:
                    new_list = f"{array[0]}.{ar[1]}"
                if len(new_list) < 1:
                    print("** no instance found **")
                    return
                list.pop(new_list)
            with open("file.json", 'w', encoding="utf-8") as f:
                json.dump(list, f)
                return 

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name."""
        array = arg.split()
        new_list = []
        dict_obj = storage.all()

        if not arg:
            for key, value in dict_obj.items():
                new_list.append(str(value))
                print(new_list)
        elif array[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            for key, value in dict_obj.items():
                if value.__class__.__name__ == arg:
                    new_list.append(str(value))
            print(new_list)        

    def do_update(selfi, arg):
        """Updates an instance based on the
        class name and id by adding or 
        updating attribute"""
        array = arg.split()
        if len(array) < 1:
            print("** class name missing **")
            return
        elif array[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(array) < 2:
            print("** instance id missing **")
            return
        elif len(array) >= 2:
            with open("file.json", "r", encoding="utf-8") as flj:
                list = json.load(flj)
                new_key = ""
                for key in list:
                    ar = key.split(".")
                    if array[1] == ar[1]:
                        if len(array) < 3:
                            print("** attribute name missing **")
                            return
                        elif len(array) < 4:
                            print("** value missing **")
                            return
                        else:
                            new_key = f"{array[0]}.{ar[1]}"
                if len(new_key) < 1:
                    print("** no instance found **")
                    return

        list[new_key].update({f"{array[2]}": f"{array[3]}"})
        with open("file.json", 'w', encoding="utf-8") as f:
            json.dump(list, f)

    def default(self, arg):
        """Update a command interpreter by default """
        array = arg.split(".")
        if array[0] in HBNBCommand.classes:
            if array[1] == "all()":
                return self.do_all(array[0])
            if array[1] == "count()":
                return self.do_count(array[0])
            if array[1][0:4] == "show":
                new_array = array[1].split("(")
                new_new_array = new_array[1].split(")")
                new_arg = array[0] + " " + new_new_array[0]
                return self.do_show(new_arg)
            if array[1][0:7] == "destroy":
                new_array = array[1].split("(")
                new_new_array = new_array[1].split(")")
                new_arg = array[0] + " " + new_new_array[0]
                return self.do_destroy(new_arg)
            if array[1][0:6] == "update":
                new_array = array[1].split("(")
                new_new_array = new_array[1].split(")")
                ar = new_new_array[0].split(",")
                new_arg = array[0] + " " + ar[0] + " " + ar[1] + " " + ar[2]
                return self.do_update(new_arg)

    def do_count(self, arg):
        """Count the number of instances of a class"""
        new_arg = arg.split(".")
        with open("file.json", "r", encoding="utf-8") as f:
            dict = json.load(f)
            count = 0
            all_key = dict.keys()
            for element in all_key:
                new_key = element.split(".")
                if new_key[0] == new_arg[0]:
                    count += 1
        print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
