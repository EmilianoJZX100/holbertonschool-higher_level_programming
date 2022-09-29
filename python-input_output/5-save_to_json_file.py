#!/usr/bin/python3
"""writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """uses json representation"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
