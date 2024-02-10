#!/usr/bin/python3
"""
Module for the State class.
"""
from models.base_model import BaseModel

class State(BaseModel):
    """
    definition for class State
    """
    name =""

    def __init__(self, *args, **kwargs):
        """ constructor method """
        super().__init__(self, *args, **kwargs)
