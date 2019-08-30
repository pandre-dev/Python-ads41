'''19 - Crie uma classe chamada Bicicleta. Ela terá os seguintes métodos:
quantidadeMarchas(); tipoFreio() e marca(); Crie também duas classes que estendem esta classe,
uma se chamará BicicletaPasseio e a outra BicicletaProfissional.
Para ﬁnalizar crie uma classe onde deverá estar o método main
e crie uma instancia de cada tipo de bicicleta e mostre o resultado dos métodos.'''

class Bicicleta:
    def __init__(self, marchas, freio, marca):
        self.marchas = marchas
        self.freio = freio
        self.marca = marca

    def quantidade_marchas(self):
        print(self.marchas)

    def tipo_freio(self):
        print(self.freio)

    def nome_marca(self):
        print(self.marca)

class BicicletaPasseio(Bicicleta):
    def __init__(self, marchas, freio, marca):
        super().__init__(marchas, freio, marca)

class BicicletaProfissional(Bicicleta):
    def __init__(self, marchas, freio, marca):
        super().__init__(marchas, freio, marca)

if __name__=="__main__":
    bike=Bicicleta(21, 'disco', 'Caloi')
    bike_2=BicicletaPasseio(18, 'disco', 'Caloi')
    bike_3=BicicletaProfissional(24, 'disco', 'Caloi')
    bike.quantidade_marchas()
    bike_2.tipo_freio()
    bike_3.nome_marca()
