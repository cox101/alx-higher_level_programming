#!/usr/bin/python3
from calculator_1 import add, subtract, multiply, divide
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: ./program.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = subtract(a, b)
    elif operator == '*':
        result = multiply(a, b)
    elif operator == '/':
        result = divide(a, b)
    else:
        print("Unknown operator. Available operators: +, -, *, /")
        sys.exit(1)

    print(f"{a} {operator} {b} = {result}")

if __name__ == "__main__":
    main()
