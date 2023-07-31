import numpy as np
import matplotlib.pyplot as plt

def gerar_pontos_normais(media, desvio_default, tamanho):
    return np.random.normal(media, desvio_default, tamanho)

media = 20
desvio_default = 2
tamanho_amostra = 1000

pontos = gerar_pontos_normais(media, desvio_default, tamanho_amostra)

plt.hist(pontos, bins=30, density=True, alpha=0.6, color='g')

plt.title('Histograma de Pontos com Distribuição Normal')
plt.xlabel('Valores')
plt.ylabel('Frequência Relativa')
plt.grid(True)

plt.show()
