#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):             #goes thru every sub-list in matrix
        for j in matrix[i]:                  #j goes thru every element in that matrix sub-list
            print("{:d} ".format(j), end='') #prints every element of the sub-list without going to a new line
        print()                              #creates a new line after each sub-list prints over
