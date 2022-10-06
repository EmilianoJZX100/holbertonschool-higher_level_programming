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
        """width"""
        return self.__width

    @width.getter
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height"""
        return self.__height

    @height.getter
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x"""
        return self.__x

    @x.getter
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y"""
        return self.__y

    @y.getter
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value
