#!/usr/bin/python3
for i in range(00, 100):
    if i < 10:
        print("{:0>2d}".format(i), ",", end="")
    elif i == 99:
        print((i), end="")
    else:
        print("{}".format(i), ",", end="")
