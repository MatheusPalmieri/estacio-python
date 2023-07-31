def isCousin(num):
    if(num < 2):
        return False

    i = num // 2

    while(i > 1):
        if(num % i == 0):
            return False
        i -= 1
    return True
    

def printResult(number, result):
    message = f'O número {number} NÃO é primo.'

    if(result):
        message = f'O número {number} é primo.'

    return message

number = 11

result = isCousin(number)
message = printResult(number, result)

print(message)