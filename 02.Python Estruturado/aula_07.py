num = 0
num_bigger = 25
isBigger = True

while isBigger:
    print(f'Bigger {num_bigger} é o maior número.')
    num += 1

    if(num >= num_bigger):
        isBigger = False
        print(f'Número {num} é o maior número.')

        
