#!/usr/bin/python3
from models.base_model import BaseModel

class City(BaseModel):
    """

    Represents a city.

    Attributes:
    state_id (str): The state ID.
    name (str): The name of the city.

    """

    def __init__(self, *args, **kwargs):
        """Initializes City instance."""
        super().__init__(*args, **kwargs)
        state_id = ""
        name = ""
