def multiplicador(numero):
        global a 
        a = 2
        print(f"Dentro da função,  variável  vale: {a}")
        return a * numero


a = 3
b = multiplicador(5)

print(f"A variável b vale: {b}")
print(f"Fora da função, a variável a vale: {a}")