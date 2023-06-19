#!/usr/bin/python3
"""
class Module
"""
import json


class Base:
    """A class representing a Base object."""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): An optional integer representing the object's ID.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator_1(self, name, value):
        """checks if value is an integer"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(name))

    def integer_validator_2(self, name, value):
        """checks if value is an integer"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(name))

    @staticmethod
    def from_json_string(json_string):
        """json to string static method
        args:
            json_string: A JSON str representation of a list of dicts.
        return:
            list of json strings
        """
        if json_string:
            return json.loads(json_string)
        return []

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string
        args:
            list_dictionaries (list): list of dictionaries
        return:
            returns a serialized list or empty list
        """
        return json.dumps(list_dictionaries or [])

    @classmethod
    def create(cls, **dictionary):
        """returns a class instance with all attributes set
        args:
            dictionary: Key/value pairs of attributes to initialize.
        return:
            instance with set attribute
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        if cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON serialization of a list of objects to a file.
        args:
            list_objs: list of objects
        """
        if list_objs:
            k = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        else:
            k = '[]'
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(k)

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances
        return:
            list of instance json string
        '''
        try:
            filename = cls.__name__ + '.json'
            with open(filename, mode='r') as f:
                d = cls.from_json_string(f.read())
            return [cls.create(**x) for x in d]
        except FileNotFoundError:
            return []
