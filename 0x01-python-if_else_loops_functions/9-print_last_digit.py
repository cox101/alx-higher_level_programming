#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit)
    return last_digit

print_last_digit(123)  
print_last_digit(-456) 
