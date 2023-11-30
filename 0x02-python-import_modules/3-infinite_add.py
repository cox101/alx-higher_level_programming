#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arguments = [int(arg) for arg in argv[1:]]

    result = sum(arguments)

    print(result)
