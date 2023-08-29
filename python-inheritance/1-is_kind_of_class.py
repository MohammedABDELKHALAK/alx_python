
"""
models.is_kind_of_class
~~~~~~~~~~~~~

This module defines def is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance of a class that
    inherited from, the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass, False otherwise.
    """
    return isinstance(obj, a_class)
