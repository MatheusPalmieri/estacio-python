# exercício 02
list_numbers = [9.523, 2.643, 9.5892, 0.742]
list_precision = [2, 2, 3, 3]


def rounding(x, y): return round(x, y)


result = list(map(rounding, list_numbers, list_precision))

print(result)
