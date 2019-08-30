'''
18 - Crie uma classe animal com o método comer, este método deve  escrever na tela "o animal esta comendo".
Depois disso crie as classes cachorro, cavalo e gato e implemente o método comer de acordo com o que cada animal come.
Crie uma classe AnimalTeste e coloque os três animais dentro de uma lista de animais e chame o método comer
polimorficamente (com um for)
'''

class Animal:
    def comendo(self):
        print("O animal está comendo.")

class Cachorro(Animal):
    def comendo(self):
        print("O cachorro está comendo ração.")

class Cavalo(Animal):
    def comendo(self):
        print("O cavalo está comendo pasto.")

class Gato(Animal):
    def comendo(self):
        print("O gato está tomando leite.")

meu_cachorro=Cachorro()
meu_cavalo=Cavalo()
meu_gato=Gato()

animais=[]
animais.append(meu_cachorro)
animais.append(meu_cavalo)
animais.append(meu_gato)

for i in range(len(animais)):
    animais[i].comendo()
