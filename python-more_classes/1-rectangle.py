#!/usr/bin/python3
"""class that defines a rectangle"""


class: Rectangle:
"""defines a Rectangle"""


def __init__(self, width=0, height=0):
    self.width = value
    self.height = value

    @property
    def width(self):
        return self.__width = value

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__heigth = value

    @property
    def height(self):
        return self.__height = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

