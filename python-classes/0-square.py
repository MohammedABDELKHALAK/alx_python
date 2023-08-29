"""
models.square
~~~~~~~~~~~~~

This module defines the Square class that get info of Square with size.
"""

class Square:
    """
    This class defines a square.
    
    Private instance attribute:
        size: The size of the square.
    """
    
    def __init__(self, size):
        """
        Initializes a Square instance with the given size.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size
    
    @property
    def _dict_(self):
        """
        Returns a dictionary containing the size of the square.
        
        Returns:
            dict: A dictionary with the size of the square.
        """
        return {'size': self.__size}