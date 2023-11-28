#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - ord('a') + ord('A'))
        print(char, end="")
    print()

uppercase("Hello, World!")

