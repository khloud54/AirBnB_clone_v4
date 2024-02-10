#!/usr/bin/python3
from models.base_model import BaseModel

"""
Class MOdule: Amenity

"""

class Amenity(BaseModel):
    """Class Amenity's definition"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialization method """
        super().__init__(self, *args, **kwargs)
