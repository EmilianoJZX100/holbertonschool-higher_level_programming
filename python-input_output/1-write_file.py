#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """writes the string and return num of characters written"""
    with open(filename, 'w') as f:
        return f.write(text)
