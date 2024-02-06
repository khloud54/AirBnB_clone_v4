#!/usr/bin/python3

"""
Module base_model
Contains a class that defines all common attributes or
methods for other classes

"""

import uuid
import json
from datetime import datetime
from models import storage
import os.path

class BaseModel():
    ''' Base class for other classes '''

    def __init__(self, *args, **kwargs):
        ''' Initializes the values '''

        if kwargs:
            dt_format ='%Y-%m-%dT%H:%M:%S.%f'
            kwargs_copy = kwargs.copy()
            del kwargs_copy["__class__"]
            for key, value in kwargs_copy.items():
                if key in ["created_at", "updated_at"]:
                    kwargs_copy[key] = datetime.strptime(value, dt_format)
            self.__dict__= kwargs_copy
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        ''' String representation of the instance '''
        return ('[{}] ({}) {}'.format(
            self.__class__.__name__,
            self.id,
            self.__dict__))

    def save(self):
        ''' Updated the public instance attribute updated_at with the
        current datetime '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        ''' Returns a dictionary containing all keys/values of __dict__
        of the instance '''
        obj_dict = {}
        obj_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, (datetime, )):
                obj_dict[key] = value.isoformat()
            else:
                obj_dict[key] = value
        return obj_dict

    def to_json(self):
        ''' Returns a JSON containing all keys/value of __dict__
        of the instance '''
        json_dict = self.__dict__.copy()
        json_dict.update({'created_at': self.created_at.strftime(self.dt_format)})
        json_dict.update({'__class__': str(self.__class__.__name__)})
        if hasattr(self, 'upsated_at'):
            json_dict.update({'updated_at': self.updated_at.strftime(self.dt_format)})
            return json_dict

