import threading
import time


def func(message):
    for i in range(3):
        print(f'{message} {i}')
        time.sleep(1)


print('Iniciando o programa!')

x = threading.Thread(target=func, args=('Executando',))
x.start()

print('\nFinalizando o programa!')
