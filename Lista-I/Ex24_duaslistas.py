'''
24 - Receba duas listas e exiba a união destas listas e a intercalação destas listas,
isto é, 1º da 1ª lista, 1º da 2ª lista, 2º da 1ª lista, 2º da 2ª lista.
'''

lista_um = [1, 2, 3, 4, 5]
lista_dois = ['A', 'B', 'C', 'D', 'E']
lista_final = []
cont_um = 0
cont_dois = 0

for i in range(len(lista_um + lista_dois)):
    if i%2 == 0:
        lista_final.append(lista_um[cont_um])
        cont_um += 1
    else:
        lista_final.append(lista_dois[cont_dois])
        cont_dois += 1

print(lista_final)
