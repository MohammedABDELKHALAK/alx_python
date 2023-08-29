"""
models.square
~~~~~~~~~~~~~

This module defines the Square class that get Size validation.
"""

class Square:

    """
    This class defines a square.
    
    Private instance attribute:
        size: Size validation.
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
