#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(0, len(my_list)):
        if i < 0:
            return None
        elif i > len(my_list):
            return None
        else:
            return idx
