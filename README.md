# python3
Python basics
First scripts for study:
simple calc:

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def calcular(operation, a, b):
    operations ={
        '+': soma,
        '-': sub,
        '*': mult,
        '/': div
    }
    func = operations.get(operation)
    if func:
        return func(a, b )
    else:
        return 'Invalid'

    
