#!/usr/bin/python3
"""instance of a class or of a subclass"""


def is_kind_of_class(obj, a_class):
    """true if its an instance of class or subclass, otherwise false"""
    return isinstance(obj, a_class)
