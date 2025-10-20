# classe veiculo
aula veiculo:
    def __iniciar__(auto,rodas,marcas):
        auto.rodas = rodas
        auto.marca = marca

    def ligar(auto):
      imprimir("Vruum")

class carro(veiculos):
    def __init__(self, marca, modelo):
        super().__init__()
        self.marca = marca
        self.modelo = modelo