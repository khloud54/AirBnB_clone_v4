#!/usr/bin/python3
from models.base_models import BaseModel
from models.user import user
from models.place import place

class Review(BaseModel):
    """Class representing a review"""

    text = ""
    place_id = ""
    user_id = ""

    def __init__(self, *args, **kwargs):
        """Initializes Review"""
        super().__init(*args, **kwargs)
