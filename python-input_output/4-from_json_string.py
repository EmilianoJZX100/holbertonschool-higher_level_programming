#!/usr/bin/python3
"""from json to string"""
import json


def from_json_string(my_str):
    """returns an object represented by a json string"""

    return json.loads(my_str)
