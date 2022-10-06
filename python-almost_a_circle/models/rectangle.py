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
        self.__width = width
        return self.__width

    @property
    def height(self):
        """height"""
        self.__height = height
        return self.__height

    @property
    def x(self):
        """x"""
        self.__x = x
        return self.__x

    @property
    def y(self):
        """y"""
        self.__y = y
        return self.__y

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

    @height.getter
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, i, height):
        """height setter"""
        if type(i) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

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
