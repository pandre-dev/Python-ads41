'''
28 - Faça um programa que percorre uma lista e exiba na tela o valor mais próximo da média dos valores da lista.
Exemplo: lista = [2.5, 7.5, 10.0, 4.0] (média = 6.0). Valor mais próximo da média = 7.5
'''

valores = []

for i in range(5):
    valores.append(float(input(f"Digite o {i+1}º valor: ")))

mediaprox = sum(valores)/len(valores)
maisprox = 0

for i in range(len(valores)):
    if abs(valores[i] - mediaprox) <= abs(maisprox - mediaprox):
        maisprox = valores[i]

print(f"\nO valor mais próximo da média ({mediaprox}) é: {maisprox}")
