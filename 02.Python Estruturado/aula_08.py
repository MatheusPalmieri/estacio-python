def findBySmall(list):
    minimum = list[0]

    for num in list:
        if(num < minimum):
            minimum = num
    
    return minimum

list_numbers = [5, 10, 6, 2]

small = findBySmall(list_numbers)
print(f'O menor número da lista é: [{small}]')