a = 0
for i in range(30):
    print('a = {}'.format(a))
    if a % 2 == 0:
        a += 1
        continue
    else:
        if a % 5 == 0:
            break
        else:
            a += 3
print ('final = ', a)