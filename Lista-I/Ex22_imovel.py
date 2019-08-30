'''
22 - Crie a classe Imóvel, que possui um endereço e um preço.
a. crie uma classe Novo, que herda Imóvel e possui um adicional no preço. Crie
métodos de acesso e impressão deste valor adicional.
b. crie uma classe Velho, que herda Imóvel e possui um desconto no preço. Crie
métodos de acesso e impressão para este desconto.
'''

class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

class ImovelNovo(Imovel):
    def __init__(self, endereco, preco):
        super().__init__(endereco, preco)

    def mostrar_valor(self):
        print(f"Preço imóvel novo: R${self.preco+1000}")

class ImovelAntigo(Imovel):
    def __init__(self, endereco, preco):
        super().__init__(endereco, preco)

    def mostrar_valor(self):
        print(f"Preço imóvel antigo: R${self.preco-500}")


novo_imovel = ImovelNovo('Rua 1', 20000)
antigo_imovel = ImovelAntigo('Rua 3', 15000)
novo_imovel.mostrar_valor()
antigo_imovel.mostrar_valor()
