#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    #goes thru every sub-list in matrix
    for i in range(len(matrix)):
        #j goes thru every element in that matrix sub-list i
        for idx, j in matrix[i]:
            if idx + 1 != len(matrix[i]):
                print("{:d} ".format(j), end='')
            else:
                #prints every element of the sub-list without going to a new line
                print("{:d}".format(j))
