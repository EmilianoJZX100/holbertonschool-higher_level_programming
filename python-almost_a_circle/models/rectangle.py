#!/usr/bin/python3
"""inherits from base"""
from models.base import Base


class Rectangle(Base):
    """class that inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        self.__width = value
        if value <= 0:
            raise ValueError("width must be > 0")

    @height.setter
    def height(self, value):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        self.__height = value
        if value <= 0:
            raise ValueError("height must be > 0")

    @x.setter
    def x(self, value):
        self.__x = value
        if value <= 0:
            raise ValueError("x must be > 0")

    @y.setter
    def y(self, value):
        self.__y = value
        if value <= 0:
            raise ValueError("y must be > 0")
