#!/usr/bin/python3
"""creates an object"""
import json


def load_from_json_file(filename):
    """creates an obj from a json file"""

    with open(filename, 'r') as f:
        return json.load(f)
