#!/usr/bin/python3
"""inherits from base"""
from models.base import Base


class Rectangle(Base):
    """class that inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """type error message"""
    def error_type(name, newvalue):
        if type(newvalue)is not int:
            raise TypeError(f"{name} must be an integer")

    """value error messages"""
    def error_value(name, newvalue2):
        if newvalue2 < 0:
            raise ValueError(f"{name} must be >= 0")

    def error_value2(name, newvalue3):
        if newvalue3 <= 0:
            raise ValueError(f"{name} must be > 0")

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.error_type("width", value)
        self.error_value2("width", value)
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.error_type("height", value)
        self.error_value2("height", value)
        self.__height = value

    @property
    def x(self):
        """x"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of rectangle"""
        return self.height * self.width

    def display(self):
        """ print rectangle """
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            for j in range(self.__y):
                print()
            for row in range(self.__height):
                for j in range(self.__x):
                    print(' ', end='')
                for column in range(self.__width):
                    print('#', end='')
                print()

    def __str__(self):
        """rectangle"""
        string = '[Rectangle]' + f' ({self.id}) '
        string += f'{self.__x}/{self.__y} - {self.__width}/{self.__height}'
        return string        
