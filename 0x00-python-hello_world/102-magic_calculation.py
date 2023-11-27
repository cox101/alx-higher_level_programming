import dis

def magic_calculation(a, b):
    result = a ** b
    result += 98
    return result

/*Compare bytecode*/
dis.dis(magic_calculation)

