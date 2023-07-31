while True:
    try:
        age = int(input("Digite sua idade: "))

        print(f'Você tem {age} anos.')

        break
    except ValueError:
        print("Digite um número válido!")