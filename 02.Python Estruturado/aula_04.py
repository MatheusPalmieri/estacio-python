price = 1

discount10 = 0.1
discount20 = 0.2

quantity = eval(input('Digite a quantidade que deseja comprar: '))
value_current = price * quantity

if(quantity <= 10):
    value = value_current
elif(quantity <=20):
    value = value_current *  (1 - discount10)
else:
    value = value_current *  (1 - discount20)

print(f'O valor final da compra é de: {value}')