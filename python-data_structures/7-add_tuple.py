#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple(map(sum, zip(tuple_a, tuple_b)))
    return new_tuple
