#!/usr/bin/python3
"""Defines a base model class."""
import json


class Base:
    """
    Base class for creating and manipulating instances
    with common functionality.

    Attributes:
        __nb_objects (int): A private class attribute to
        keep track of the number of objects created.

    Methods:
        __init__(self, id=None):
            Initializes a new instance of the Base class.
        to_json_string(list_dictionaries):
                Converts a list of dictionaries to a JSON-formatted string.
        save_to_file(cls, list_objs):
                Saves a list of objects to a JSON file named after the class.
        from_json_string(json_string):
                Converts a JSON-formatted string to a list of dictionaries.
        create(cls, **dictionary):
                Creates a new instance based on a dictionary of attributes.
        load_from_file(cls):
                Loads instances from a JSON file and returns them as a list.
        """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list): A list of dictionaries to
            be converted to JSON.
        Returns:
            str: The JSON-formatted string representing the input
            list of dictionaries.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file named after the class.

        Args:
            cls (class): The class itself (class method).
            list_objs (list): A list of instances to be serialized
            and saved to the JSON file.
        """
        with open(cls.__name__ + ".json", "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                jsonfile.write(Base.to_json_string([o.to_dictionary()
                                                    for o in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON-formatted string to a list of dictionaries.

        Args:
            json_string (str): A JSON-formatted string.
        Returns:
            list: A list of dictionaries parsed from the JSON string.
        """

        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance based on a dictionary of attributes.

        Args:
            cls (class): The class itself (class method).
            **dictionary: Arbitrary keyword arguments representing
            the attributes of the instance.
        Returns:
            instance: An instance of the class with attributes
            based on the input dictionary.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                d = cls(1)
            else:
                d = cls(1, 1)
            d.update(**dictionary)
            return d

    @classmethod
    def load_from_file(cls):
        """
        Loads instances from a JSON file and returns them as a list.

        Args:
            cls (class): The class itself (class method).

        Returns:
            list: A list of instances loaded from the corresponding JSON file
                or an empty list if the file doesn't exist.
        """

        try:
            with open(cls.__name__ + ".json") as jsonfile:
                obj_arr = Base.from_json_string(jsonfile.read())
                return [cls.create(**_) for _ in obj_arr]
        except IOError:
            return []
