'''
6 - Faça um algoritmo que leia um nº inteiro e mostre uma mensagem indicando se este número é par ou ímpar,
e se é positivo ou negativo
'''

#retorna true se num for positivo
def checar_sinal(num):
    pos = False
    if num >= 0:
       pos = True
    return pos

#retorna true se num for par
def checar_paridade(num):
    par = False
    if num%2 == 0:
       par = True
    return par

if __name__ == "__main__":
    temp=int(input("Digite um numero para verificação: "))

    checar_sinal(temp)
    checar_paridade(temp)
