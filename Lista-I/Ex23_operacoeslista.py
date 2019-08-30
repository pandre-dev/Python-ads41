'''
23 - Crie uma programa que recebe uma lista qualquer e:
a. retorne o maior elemento
b. retorne a soma dos elementos
c. retorne o número de ocorrências do primeiro elemento da lista
d. retorne a média dos elementos
'''

tamanho = int(input("Digite a quantidade de elementos da lista: "))
lista_qualquer = []

for i in range(tamanho):
    temp = float(input(f"Digite o {i+1}º elemento da lista: "))
    lista_qualquer.append(temp)

print(f"\nO maior elemento é: {max(lista_qualquer)}")
print(f"\nA soma dos elementos é: {sum(lista_qualquer)}")
print(f"\nO primeiro valor ocorre {lista_qualquer.count(lista_qualquer[0])} vezes.")
print(f"\nA média dos elementos é: {sum(lista_qualquer)/len(lista_qualquer)}")
