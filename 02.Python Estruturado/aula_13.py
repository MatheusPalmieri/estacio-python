import numpy as np

def entry_date():
    coefficient = quantity = eval(input('Digite o valor do coeficiente: '))
    return coefficient

def calc_delta(a, b, c):
    delta = b * b - 4 * a * c
    return delta

def calc_root(a, b, c, delta):
    if(delta < 0):
        result = 'A equação não possui raízes nos números reais.'
    elif(delta == 0):
        x = -b / (2 * a)
        result = f'A equação possui apenas a raiz: {x}'
    else:
        x1 = (-b - np.sqrt(delta)) / (2 * a)
        x2 = (-b + np.sqrt(delta)) / (2 * a)
        result = f'A equação possui as raízes: {x1}, {x2}'

    return result

a = entry_date()
b = entry_date()
c = entry_date()

delta = calc_delta(a, b, c)

result = calc_root(a, b, c, delta)

print(result)