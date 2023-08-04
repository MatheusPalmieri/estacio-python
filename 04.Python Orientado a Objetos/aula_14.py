class ExcecaoCustomizada(exception):
    pass


x = -1
if x < 0:
    raise Exception('Valor negativo!!!')

x = 'hello'
if not type(x) is int:
    raise TypeError('Use apenas inteiros')
