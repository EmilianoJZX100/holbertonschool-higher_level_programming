#!/usr/bin/python3
"""defines a student"""


class Student:
    """new student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        student_dictionary = self.__dict__
        students = {}

        if attr is None:
            return student_dictionary
        if type(attrs) is list:
            for elements in attrs:
                if hasattr(self, elements):
                    students{elements} = getattr(self, elements)
            return students
