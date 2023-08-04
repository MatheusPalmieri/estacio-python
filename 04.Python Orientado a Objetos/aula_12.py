from datetime import date


class Extrato:
    def __init__(self):
        self.transacoes = []

    def imprimir(self):
        for p in self.transacoes:
            print(p[0], p[1])


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(
            ['DEPOSITO', valor]
        )

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(
                ['SAQUE', valor]
            )

            return True


class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo, limite):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append([
                'SAQUE', valor
            ])
            return True


c1 = Cliente('123123123-12', 'Ana', 'Rua vava')
c2 = Cliente('939939393-12', 'Gigante', 'Rua vovo')

conta = Conta([c1, c2], 1000, 5000)

conta.depositar(1000)
conta.sacar(500)

# Herança


class Poupanca:
    def __init__(self, taxaremunaracao):
        self.taxaremunaracao = taxaremunaracao
        self.data_abertura = date.today()

    def remuneraConta(self):
        self.saldo += self.saldo * self.taxaremunaracao


class ContaRemuneradaPoupanca(Conta, Poupanca):
    def __init__(self, clientes, numero, saldo, taxaremunaracao):
        Conta.__init__(self, clientes, numero, saldo)
        Poupanca.__init__(self, taxaremunaracao)
        self.taxaremunaracao = taxaremunaracao

    def remuneraConta(self):
        self.saldo += self.saldo * (self.taxaremunaracao/30)


cx = ContaRemuneradaPoupanca([c1, c2], 98989412, 1500.00, 0.03)
cx.remuneraConta()
print(cx.saldo)
