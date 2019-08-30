'''
21 - Crie uma classe chamada Ingresso que possui um valor em reais e um método
imprimeValor().
a. crie uma classe VIP, que herda Ingresso e possui um valor adicional. Crie um
método que retorne o valor do ingresso VIP (com o adicional incluído).
b. crie uma classe Normal, que herda Ingresso e possui um método que imprime:
"Ingresso Normal".
c. crie uma classe CamaroteInferior (que possui a localização do ingresso e métodos
para acessar e imprimir esta localização) e uma classe CamaroteSuperior, que é
mais cara (possui valor adicional). Esta última possui um método para retornar o
valor do ingresso. Ambas as classes herdam a classe VIPame o método  aumentaSalario de cada um.
'''

class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprime_valor(self):
        print(f"Ingresso: R${self.valor:.2f}")

class VIP(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def imprime_valor(self):
        self.valor += 20
        print(f"Ingresso VIP: R${self.valor:.2f}")

class CamaroteInferior(VIP):
    def __init__(self, valor, localizacao):
        super().__init__(valor)
        self.localizacao = localizacao

    def imprime_local(self):
        print(f"Localização: {self.localizacao}")

class CamaroteSuperior(VIP):
    def __init__(self, valor, localizacao):
        super().__init__(valor)
        self.localizacao = localizacao

    def imprime_local(self):
        print(f"Localização: {self.localizacao}")

    def aumenta_valor(self):
        self.valor += 15

if __name__ == "__main__":
    ingresso_sup = CamaroteSuperior(40, 'Fundo')
    ingresso_inf = CamaroteInferior(40, 'Frente')
    ingresso_sup.aumenta_valor()
    ingresso_sup.imprime_local()
    ingresso_sup.imprime_valor()
    ingresso_inf.imprime_local()
    ingresso_inf.imprime_valor()
