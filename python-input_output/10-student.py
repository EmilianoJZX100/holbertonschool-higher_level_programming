#!/usr/bin/python3
"""defines a student"""


class Student:
    """new student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        self_dictionary = self.__dict__
        stds = {}

        if attrs is None:
            return self_dictionary

        if type(attrs) is list:
            for elements in attrs:
                if hasattr(self, elements):
                    stds{elements} = getattr(self, elements)
            return stds
