#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 and idx >= len(my_list):
        return my_list
    else:
        new_list = my_list.replace(idx + 1, element)
        return new_list
