# exercício 01
listNumber = [0, 11, 2, 3, 5, 8, 13, 21, 34]


def fTesteParidade(x): return x % 2 == 0


print(f'Teste de fTesteParidade(5) = {fTesteParidade(5)}')

pares = list(filter(fTesteParidade, listNumber))
print(f'Lista de números pares = {pares}')
