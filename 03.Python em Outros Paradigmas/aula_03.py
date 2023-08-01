# primeiro exemplo
def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(sum([2, 4, 6, 8, 10]))

# segundo exemplo
list = ['Ferrari']
list.append('Porsche')
print(f'\n{list}')
