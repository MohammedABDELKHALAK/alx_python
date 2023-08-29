
"""
models.inherits_from
~~~~~~~~~~~~~

This module defines def inherits_from
"""

def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a class that inherits from a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class 
