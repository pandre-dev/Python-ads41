'''
20 - Crie um classe Funcionário com os atributos nome, idade e salário.
Deve ter  um método  aumenta_salario. Crie duas subclasses da classe funcionário, programador
 e  analista, implementando o método  nas duas subclasses.
 Para o programador some ao atributo salário mais 20 e ao analista some ao salário mais 30,  mostrando na tela o valor.
 Depois disso, crie uma classe de testes instanciando os objetos programador e analista e
 chame o método  aumenta_salario de cada um.
'''

class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def aumenta_salario(self):
        self.salario += 10
        print(f"\nFuncionário: {self.nome}"
              f"\nNovo salário: RS{self.salario:.2f}")

class Programador(Funcionario):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade, salario)

    def aumenta_salario(self):
        self.salario += 20
        print(f"\nFuncionário: {self.nome}"
              f"\nNovo salário: RS{self.salario:.2f}")

class Analista(Funcionario):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade, salario)

    def aumenta_salario(self):
        self.salario += 30
        print(f"\nFuncionário: {self.nome}"
              f"\nNovo salário: RS{self.salario:.2f}")


if __name__ == "__main__":
    funcionario_1 = Programador('Paulo', 27, 3000)
    funcionario_2 = Analista('Andre', 28, 4000)
    funcionario_1.aumenta_salario()
    funcionario_2.aumenta_salario()
