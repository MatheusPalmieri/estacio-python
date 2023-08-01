vehicles = ['avião', 'carro', 'navio', 'ônibus']


def f_capital(x): return str.upper(x)


names_capital = list(map(f_capital, vehicles))

print(f'Nomes maiúsculos = {names_capital}')
