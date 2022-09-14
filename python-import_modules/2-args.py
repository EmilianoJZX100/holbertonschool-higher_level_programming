#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    quantity =  len(sys.argv)

    if quantity == 1:
        print(f"{quantity - 1} arguments.")
    elif quantity == 2:
        print(f"{quantity - 1} argument:")
    else:
        print(f"{quantity - 1} arguments:")

    for i in range(1, quantity):
        print("{}: {}".format(i, sys.argv[i]))

