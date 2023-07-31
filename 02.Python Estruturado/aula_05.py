list = [10, 15, 1, 52, 14, 7, 2, 8, 3, 25]
length_list = len(list)
sum = 0

for i in range (length_list):
    if(list[i] % 2 == 0):
        sum += list[i]

print(f'O somatório dos elementos pares é {sum}')

sum = 0

for num in range (length_list):
    if(num % 2 != 0):
        sum += num

print(f'O somatório dos elementos impares é {sum}')