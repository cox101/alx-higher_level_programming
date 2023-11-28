#!/usr/bin/python3
for number in range(0, 9):
    for integer in range(number + 1, 10):
        if number == 8:
            print("{}{}".format(number, integer))
        else:
            print("{}{}".format(number, integer), end=", ")
