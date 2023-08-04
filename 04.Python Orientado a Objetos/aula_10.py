class Veiculo:
    def rodar(self):
        print('Reduz o consumo de combustivel.')


class VeiculoEletrico(Veiculo):
    def rodar(self):
        # chama a função rodar() do Veiculo
        super().rodar()
        print('Esse veiculo utiliza eletrecidade.')


veiculo_eletrico = VeiculoEletrico()
# chama a função rodar() do VeiculoEletrico()
veiculo_eletrico.rodar()
