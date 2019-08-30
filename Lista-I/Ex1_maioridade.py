# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 10:01:33 2019

@author: Paulo Andre

1- Escreva uma classe que contém um método que calcule
 se a pessoa é maior de 18 anos ou não.
 Receba os dados pela console e chame este método
"""

class Pessoa:
    def __init__(self, idade):
        self.idade = idade
    
    def maioridade(self):
        if self.idade >= 18:
            print("Maior de 18 anos.")
        else:
            print("Menos de 18 anos.")

nova_pessoa = Pessoa(int(input("Digite a idade: ")))
nova_pessoa.maioridade()
