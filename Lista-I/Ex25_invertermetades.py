'''
25 - Faça uma função que receba uma lista e exiba os elementos da última metade na frente
 dos elementos da primeira metade.
'''

import math

lista_teste=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def inverter_metades(lista):
    print(lista[int(len(lista)/2):len(lista)] + lista[0:int(len(lista)/2)])


print(f"Lista invertida: ")
inverter_metades(lista_teste)
