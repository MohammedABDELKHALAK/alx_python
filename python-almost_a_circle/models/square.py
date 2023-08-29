"""
models.square
~~~~~~~~~~~~~

This module defines the Square class that inherits from the Rectangle class.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    This class defines a Square that inherits from the Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): x-coordinate of the square's position. Defaults to 0.
            y (int, optional): y-coordinate of the square's position. Defaults to 0.
            id (int, optional): The id attribute value. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size value.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: The string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
