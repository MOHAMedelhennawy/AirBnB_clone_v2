#!/usr/bin/python3
"""
Module that contain FileStorage class
"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class that serializes instances to a JSON file
    and deserializes JSON file to instances

    Attributes:
    __file_path(string): a path to json file
    __objests(dictionary): dictionary of objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id

        Args:
        obj: object to be added to the dictionary
        """
        if obj and hasattr(obj, 'id'):
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dict = {}
        for key, obj in FileStorage.__objects.items():
            dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(dict))

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        cls = {
                "BaseModel": BaseModel, "User": User, "City": City,
                "Place": Place, "Review": Review, "Amenity": Amenity,
                "State": State
                    }
        try:
            with open(self.__file_path, 'r') as file_obj:
                data_dict = json.load(file_obj)
            for obj_dict in data_dict.values():
                cls_name = obj_dict['__class__']
                cls_name = cls[cls_name]
                self.new(cls_name(**obj_dict))
        except FileNotFoundError:
            pass
