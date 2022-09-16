#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            print(j, end= ' ')
        print("{:d}''".format(i), sep='\n')
