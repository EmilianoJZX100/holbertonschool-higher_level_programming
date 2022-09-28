#!/usr/bin/python3
"""checks if the object is an instance of a class directly or no"""


def inherits_from(obj, a_class):
    """returns True if the obj is an instance of a class that inherited"""
    return isinstance(obj, a_class)
