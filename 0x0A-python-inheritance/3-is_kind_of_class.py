#!/usr/python3
"""
This contains the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """True if obj is an instance or inherited the class, else False"""
    return isinstance(obj, a_class)
