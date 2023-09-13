#!/usr/bin/python3
"""This module defines a Student class for representing student information."""


class Student:
    """
    A class representing a student.

    This class stores information about a student, including their first name,
    last name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    Methods:
         to_json(self, attrs=None): Converts the student object to a
         JSON-serializable dictionary.
         reload_from_json(self, json): Updates the student object's
         attributes from a JSON dictionary.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the provided information.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Converts the student object to a JSON-serializable dictionary.

        Args:
            attrs (list, optional): A list of attribute names to include in
            the JSON representation. Defaults to None.
        Returns:
            dict: A dictionary containing the student's information.
        """
        if (isinstance(attrs, list) and
                all(isinstance(ele, str) for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Updates the student object's attributes from a JSON dictionary.

        Args:
            json (dict): A dictionary containing attribute-value pairs.
        """
        for key, value in json.items():
            setattr(self, key, value)
