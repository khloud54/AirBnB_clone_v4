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

class State(BaseModel, Base):
    if storage_type == 'db':
        @property
        def cities(self):
            """
            A method that rtrives and returns the list of city objects
            associated with the current State from the storage system.
            """
            cities = []
            for city in list(models.storage.all(city).values()):
                if city.state_id == self.id:
                    cities.append(city)
            return cities
