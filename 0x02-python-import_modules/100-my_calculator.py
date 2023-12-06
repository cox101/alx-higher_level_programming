#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)

    result = {"+": add, "-": sub, "*": mul, "/": div}[argv[2]](int(argv[1]), int(argv[3]))
    print("{:d} {:s} {:d} = {:d}".format(int(argv[1]), argv[2], int(argv[3]), result))

