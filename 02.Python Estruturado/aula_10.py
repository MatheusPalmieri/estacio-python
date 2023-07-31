def sumFactorial(num):
    fac = 1
    for idx in range(1, num + 1):
        fac = fac * idx
    return fac

print(sumFactorial(5))