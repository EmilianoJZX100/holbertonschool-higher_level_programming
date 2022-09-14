#!/usr/bin/python3
import hidden_4
def vdir(hidden_4):
    return [x for x in dir(hidden_4) if not x.startswith('__')]
print(dir(hidden_4))
