#!/usr/bin/python3
def read_file(filename=""):
    with open('my_file_0', encoding='utf-8') as f:
        read_data = f.read()
    print(f"{read_data}", end="")
