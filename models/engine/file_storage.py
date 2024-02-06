#!/usr/bin/python3
import os
import json
import models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """

    A class serializing instances to a JSON file and deserializing JSON file
    to instances

    """

    def __init__(self):
        """ Initializes FileStorage """
        self._file_path = "file.json"
        self._objects = {}

    def all(self):
        """ Returns the directory containing all sorted objects """
        return self._objects

    def new(self, obj):
        """ Sets the given object in the dictionary with
        a key of <object class name>.id"""

        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self._objects[key] = obj

    def save(self):
        """ serializes objects to JSON and saves to the specified file path """
        serialized_objs = {}

        for key, val in self._objects.items():
            serialized_objs[key] = val.to_dict()

        with open(self._file_path, "W") as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """ Deserializes JSON file to objects """
        class_map = {
            "BaseModel" : BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        if not os.path.isfile(self._file_path):
            return

        with open(self._file_path, "r") as file:
            data = json.load(file)
            self._objects = {}
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                cls = class_map[class_name]
                self._objects[key] = cls(**value)
