#!/usr/bin/python3
"""base class"""


class Base:
    """new class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if type(id) != int:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
