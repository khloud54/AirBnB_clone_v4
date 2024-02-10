#!/usr/bin/python3
from models.base_models import BaseModel
from models.user import user
from models.place import place

"""
Module class Review
"""

class Review(BaseModel):
    """Class representing a review"""

    text = ""
    place_id = ""
    user_id = ""

    def __init__(self, *args, **kwargs):
        """ constructor method """
        super().__init__(self, *args, **kwargs)
