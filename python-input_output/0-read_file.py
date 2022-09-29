#!/usr/bin/python3
"""reads a text file"""


def read_file(filename=""):
    """reads in  utf8"""

    with open('my_file_0', encoding='utf-8') as f:
        read_data = f.read()
    print(f"{read_data}", end="")
