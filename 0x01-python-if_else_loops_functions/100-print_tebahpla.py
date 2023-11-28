#!/usr/bin/python3
for char_code in range(ord('z'), ord('a') - 1, -2):
    print("{}".format(chr(char_code)), end="")
    if char_code % 2 == 0:
        print("{}".format(chr(char_code - ord('a') + ord('A'))), end="")
