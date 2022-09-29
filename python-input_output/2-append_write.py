#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends and return the num of characters"""

    with open(filename, 'a') as f:
        return f.write(text)
