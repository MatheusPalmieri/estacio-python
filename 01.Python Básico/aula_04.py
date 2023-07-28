a, b = 1, 2 
print('Antes da troca')
print(f'Valor das variáveis: : a={a}, b={b}')
print('')

temp = a
a = b
b = temp
print('Primeira troca')
print(f'Valor das variáveis: : a={a}, b={b}')
print('')

a, b = b, a
print('Segunda troca')
print(f'Valor das variáveis: : a={a}, b={b}')
print('')