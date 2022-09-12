#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        opposite = number * -1
        print(f"{opposite % 10}", end="")
        return opposite % 10
    elif number > 0:
        print(f"{number % 10}", end="")
        return number % 10
    else:
        print(f"{number}",  end="")
        return number
