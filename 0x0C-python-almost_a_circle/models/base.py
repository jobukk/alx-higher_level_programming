#!/usr/bin/python3
"""Base Class Module"""
import json


class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:        
            Base.__nb_objects += 1
            self.id =  Base.__nb_objects

    @staticmethod        
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dump(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            file.write(cls.to_json_string(list_objs))
    @staticmethod
    def from_json_string(json_string):
        if json_string  is None or json_string == "[]":
            return []
        return json.loads(json_string) 
    @classmethod
    def create(cls, **dictionary):
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1,1)
            elif cls.__name__ == "Square":
                new = cls(1)
            new.update(**dictionary)
            returnnew  
    @classmethod
    def load_from_file(cls):
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []




