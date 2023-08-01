# primeiro exemplo
from functools import reduce
import operator


def sum(numbers):
    if not numbers:
        return 0

    first = numbers[0]
    rest = numbers[1:]
    return first + sum(rest)


print(sum([2, 4, 6, 8, 10]))

# segundo exemplo
list = ['Ferrari']
new_list = list + ['Porsche']
print(f'\n{new_list}')

# terceiro exemplo
print(f'\n{operator.add(10, 20)}')

# quarto exemplo
print(f'\n{reduce(operator.add, [5, 20])}')
print(f'\n{reduce(operator.concat, ["Aprendendo reduce!"])}')
