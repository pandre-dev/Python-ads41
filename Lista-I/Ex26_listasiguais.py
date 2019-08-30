'''
26 - Faça um programa que receba duas listas e retorne True se são iguais ou False caso contrário,
 além do número de ocorrências do primeiro elemento da lista.
'''

lista_um = []
lista_dois = []

def preencher_lista(lista, tamanho):
    for i in range(tamanho):
        temp = int(input(f"Digite o {i+1}º elemento: "))
        lista.append(temp)


print("Primeira lista")
preencher_lista(lista_um, 5)
print("\nSegunda lista")
preencher_lista(lista_dois, 5)

print(lista_um == lista_dois)
print(f"O 1º elemento da lista 1 ocorre {lista_um.count(lista_um[0])} vezes.")
print(f"O 1º elemento da lista 2 ocorre {lista_dois.count(lista_dois[0])} vezes.")
