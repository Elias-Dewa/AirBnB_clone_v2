#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns the list of objects of one type of class"""
        if not cls:
            return self.__objects
        elif type(cls) == str:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        else:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__:
                    new_dict[key] = value
            return new_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """objects to dictionary to Json file"""
        objs = {}
        for key in self.__objects:
            objs[key] = self.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(objs, file)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
            for key in temp:
                self.__objects[key] = classes[temp[key]
                                              ['__class__']](**temp[key])
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """a public instance method to delete obj from __objects
        if it’s inside, if obj is equal to None,
        the method should not do anything"""
        if obj is None:
            return
        key = "{}.{}".format(type(obj).__name__, obj.id)
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]
            self.save()

    def close(self):
        """Deserialize JSON file to objects"""
        self.reload()
