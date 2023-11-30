#!/usr/bin/python3
import dis

def print_module_names(pyc_file):
    with open(pyc_file, 'rb') as file:
        code = file.read()
        dis.dis(code)

if __name__ == "__main__":
    print_module_names('hidden_4.pyc')
