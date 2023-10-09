import os
def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y
    
def calculadora():
    while True:
        x, operacao, y = map(input().split())
        x = int(x)
        y = int(y)
        if operacao == '=':
            break
        elif operacao == '+':
            print(f'{x} + {y} = {x+y}')
        elif operacao == '-':
            print(f'{x} - {y} = {x-y}')
        elif operacao == '*':
            print(f'{x} * {y} = {x*y}')
        elif operacao == '/':
            print(f'{x} / {y} = {x/y}')
        else:
            print('Operação inválida')
    os.system('cls')
calculadora()