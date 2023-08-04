class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True


c1 = Cliente('123123123-12', 'Ana', 'Rua vava')
c2 = Cliente('939939393-12', 'Gigante', 'Rua vovo')

conta = Conta([c1, c2], 1000, 5000)
