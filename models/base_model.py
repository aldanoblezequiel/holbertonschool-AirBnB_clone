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
<<<<<<< HEAD
=======
                if key != "__class__":
                    setattr(self, key, value)
>>>>>>> e046860e717cb9d89c33fab0d38c47ba05ded55a
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
<<<<<<< HEAD
        dict = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                dict[key] = value.isoformat()
            else:
                dict[key] = value
        return dict 


    def __str__(self):
        """
        Returns a string with the information of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
=======
        key_dictionary = self.__dict__.copy()
>>>>>>> e046860e717cb9d89c33fab0d38c47ba05ded55a
