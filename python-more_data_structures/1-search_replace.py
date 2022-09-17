#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for idx, item in enumerate(my_list):
        if item == search:
            my_list[idx] = replace
    return new_list
