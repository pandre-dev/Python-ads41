# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 10:13:43 2019

@author: Paulo Andre

Escreva um algoritmo que solicita ao usuário para digitar um número inteiro positivo, e mostre-o por extenso.
Este número deverá variar entre 1 e 5.
Se o usuário introduzir um número que não pertença a este intervalo, mostre a frase “número inválido”.
"""

valido = False

while not valido:
    num = int(input("Digite um inteiro entre 1 e 5: "))
    if num >= 1 and num <= 5:
        valido = True
    else:
        print("Número inválido. Tente novamente.")

if num == 1:
    print("Um")
elif num == 2:
    print("Dois")
elif num == 3:
    print("Tres")
elif num == 4:
    print("Quatro")
elif num == 5:
    print("Cinco")
    