'''
13 - Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres
(considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres).
Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova,
 e o produto das idades do homem mais novo com a mulher mais velha.
'''

homens=[]
mulheres=[]

def preencher_idades(lista):
    for i in range(2):
        temp = int(input(f"Digite a idade da {i+1}ª pessoa: "))
        lista.append(temp)
    if lista[0] == lista[1]:
        print("Idades iguais. Tente novamente.")
        lista.pop()
        lista.pop()
        preencher_idades(lista)


print("\nPreenchendo idade dos homens.")
preencher_idades(homens)
print("\nPreenchendo idade das mulheres.")
preencher_idades(mulheres)

print(f"\nSoma homem mais velho com mulher mais nova: {max(homens)+min(mulheres)}")
print(f"\nProduto homem mais novo com mulher mais velha: {min(homens)*max(mulheres)}")
