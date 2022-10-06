#!/usr/bin/python3
"""inherits from base"""
from models.base import Base


class Rectangle(Base):
    """class that inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        self.__width = width
        return self.__width

    @property
    def height(self):
        self.__height = height
        return self.__height

    @property
    def x(self):
        self.__x = x
        return self.__x

    @property
    def y(self):
        self.__y = y
        return self.__y

    @width.setter
    def width(self, value):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value
