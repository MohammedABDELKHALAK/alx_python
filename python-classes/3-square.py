"""
models.square
~~~~~~~~~~~~~

This module defines the Square class that Access and update private attribute .
"""

class Square:
        
    """
    This class defines a square.
    
    Private instance attribute:
        size: Access and update private attribute.
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
