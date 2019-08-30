'''
6 - Faça um algoritmo que leia um nº inteiro e mostre uma mensagem indicando se este número é par ou ímpar,
e se é positivo ou negativo
'''

def checar_sinal(num):
    if num >= 0:
        print("Positivo")
    else:
        print("Negativo")

def checar_paridade(num):
    if num%2 == 0:
        print("Par")
    else:
        print("Ímpar")

temp=int(input("Digite um numero para verificação: "))

checar_sinal(temp)
checar_paridade(temp)
