import threading
import time


def func():
    for i in range(3):
        print(f'Executando a thread {i}')
        time.sleep(1)


print('Iniciando o programa!')
threading.Thread(target=func).start()
print('\nFinalizando o programa!')
