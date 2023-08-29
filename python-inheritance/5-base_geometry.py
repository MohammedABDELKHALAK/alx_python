
"""
models.5-base_geometry.py
~~~~~~~~~~~~~

This module defines class BaseGeometry.
"""

class BaseGeometry:
    """
    This class defines the base geometry with an area method and an integer validator.
    """
    def area(self):
        """
        Calculates the area.

        Raises:
            Exception: Always raises an exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates the value as an integer.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
