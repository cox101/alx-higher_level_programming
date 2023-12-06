#!/usr/bin/python3
from calculator_1 import add, subtract, multiply, divide
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./your_program.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    result = None

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = subtract(a, b)
    elif operator == '*':
        result = multiply(a, b)
    elif operator == '/':
        result = divide(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))

