#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, subtract, multiple, division

    a = 10
    b = 5

    result_add = add(a, b)
    result_sub = subtract(a, b)
    result_mul = multiple(a, b)
    result_div = division(a, b)

    print("{} + {} = {}".format(a, b, result_add))
    print("{} - {} = {}".format(a, b, result_subtract))
    print("{} * {} = {}".format(a, b, result_multiple))
    print("{} / {} = {}".format(a, b, result_division))
