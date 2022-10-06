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
        type_error("width", value)
        wh("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        type_error("height", value)
        wh("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        type_error("x", value)
        wh("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        type_error("y", value)
        wh("y", value)
        self.__y = value
