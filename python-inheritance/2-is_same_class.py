#!/usr/bin/python3
"""check object of the same class"""


def is_same_class(obj, a_class):
    """returns True if the object its of that instance"""

    return type(obj) is a_class
