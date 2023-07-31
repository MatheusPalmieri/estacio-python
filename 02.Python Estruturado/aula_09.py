def isPars(num):
    res = (num % 2 == 0)
    return res

def sumPars(list):
    sum = 0
    for num in list:
        if(isPars(num)):
            sum += num
    
    return sum

list_numbers = [5, 10, 6, 2, 7, 4, 8, 3]

sum = sumPars(list_numbers)
print(f'O valor total de números pares da lista é: [{sum}]')