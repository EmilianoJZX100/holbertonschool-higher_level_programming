#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx <= 0 and idx >= range(0, len(my_list)) and idx == len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
