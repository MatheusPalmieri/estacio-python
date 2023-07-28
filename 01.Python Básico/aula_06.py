def multiplicador(numero):
        a = 2
        print(f"Dentro da função, a variável vale: {a}")
        return a * numero

a = 3
b = multiplicador(5)

print(f"Fora da função, a variável a vale: {a}")
print(f"Fora da função, a variável b vale: {b}")