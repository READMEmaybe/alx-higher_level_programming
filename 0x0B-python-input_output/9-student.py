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
        to_json(self): Converts the student object to a
        JSON-serializable dictionary.
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

    def to_json(self):
        """
        Converts the student object to a JSON-serializable dictionary.

        Returns:
            dict: A dictionary containing the student's information.
        """
        return self.__dict__
