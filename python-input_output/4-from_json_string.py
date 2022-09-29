#!/usr/bin/python3
"""from json to string"""


def from_json_string(my_str):
    """returns an object represented by a json string"""

    import json
    return json.load(my_str)
