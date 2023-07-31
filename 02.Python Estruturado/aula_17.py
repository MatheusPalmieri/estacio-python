def division(x, y):
    try:
        result = x / y
        print(f'{x} divido por {y} é igual a {result}')
    except ZeroDivisionError:
        print('Divisão por zero!')

division(25, 5)
division(25, 0)
