#!/usr/bin/python3
"""
Module Class: Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class: Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
