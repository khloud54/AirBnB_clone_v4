#!/usr/bin/python3
from models.base_model import BaseModel

"""
Module class city
"""

class City(BaseModel):
    ''' class city definition '''
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """ constructor method """
        super().__init__(self, *args, **kwargs)
