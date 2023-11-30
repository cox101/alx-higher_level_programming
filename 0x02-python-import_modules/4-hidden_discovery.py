#!/usr/bin/python3
import sys
import types

def print_module_names():
    module = types.ModuleType("hidden_4")
    with open("hidden_4.pyc", "rb") as file:
        magic = file.read(4)
        timestamp = file.read(4)
        code_object = compile(file.read(), "hidden_4.pyc", "exec")
        sys.modules["hidden_4"] = module
        exec(code_object, module.__dict__)

    names = sorted(name for name in dir(module) if not name.startswith("__"))
    for name in names:
        print(name)

if __name__ == "__main__":
    print_module_names()

