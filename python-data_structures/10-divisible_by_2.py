#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for n in range(len(my_list)):
        if n % 2 == 0:
            new_list.append(True)
        elif 1 % 2 == 0:
            new_list.append(False)
        else:
            new_list.append(False)
        return new_list
