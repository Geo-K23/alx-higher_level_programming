#!/usr/bin/python3
"""
Contains the 'wrtie_file' function
"""


def write_file(filename="", text=""):
    """Writes a string and returns the number of chars written"""
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
