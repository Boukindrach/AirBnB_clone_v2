#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retrieve all stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize objects to a JSON file."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(serialized_objects, f)
    
    def delete(self, obj=None):
        """Deletes obj from __objecs if its inside
        Not sure if it should also delete from json file
        """

        dict_key = ""
        for key, value in self.__objects.items():
            if obj == value:
                dict_key = key
        if dict_key is not "":
            del self.__objects[dict_key]

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if cls is None:
            return self.__objects
        else:
            new_dict = {}
            if len(self.__objects) > 0:
                for key, value in self.__objects.items():
                    if type(cls) is str:
                        if cls == key.split('.')[0]:
                            new_dict[key] = value
                    else:
                        if cls is type(value):
                            new_dict[key] = value
            return new_dict

    def reload(self):
        """Deserialize the JSON file to objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for value in obj_dict.values():
                    cls_n = value["__class__"]
                    del value["__class__"]
                    self.new(eval(cls_n)(**value))
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    class_ = self.__objects.get(class_name)
                    if class_:
                        self.__objects[key] = class_(**value)
        except FileNotFoundError:
            return
