#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """ constructor method """
        super().__init__(*args, **kwargs)
        self.name = ""
