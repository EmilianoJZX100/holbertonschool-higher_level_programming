#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(0, len(my_list)):
        if idx < 0:
            return None
        elif idx > i:
            return None
        else:
            return idx
