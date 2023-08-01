# exercício 03
from functools import reduce

list_numbers = [1, 2, 3, 4, 5, 6, 7, 23, 4, 52, 3, 5, 1, 6]
print(f'A soma dos números é {sum(list_numbers)}')


def f_soma(x, y): return x + y


result = reduce(f_soma, list_numbers)
print(f'A soma dos números é {result}')
