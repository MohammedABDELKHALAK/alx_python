"""
models.base
~~~~~~~~~~~

This module defines the Base class that manages the id attribute for all other classes.
"""

class Base:
    """
    This is the base class that manages the id attribute for all other classes.
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        Initializes the Base instance.

        Args:
            id (int, optional): The id attribute value. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
