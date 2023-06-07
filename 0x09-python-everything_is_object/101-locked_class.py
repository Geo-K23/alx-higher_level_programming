#!/usr/bin/python3
"""
101-locked_class Module
"""


class LockedClass:
    """
    A class that prevents the user from creating new instance attributes
    """
    __slots__ = ["first_name"]
