'''
7 - Escreva um algoritmo que leia 10 números informados pelo usuário e, depois, informe o menor, número,
o maior número, a soma dos números informados e a média aritmética dos números informados.
'''

def achar_maior(list):
    return max(list)

def achar_menor(list):
    return min(list)

def soma(list):
    return sum(list)

def media(list):
    return sum(list)/len(list)

if __name__ == "__main__":
    numeros=[]
    for i in range(10):
        numeros.append(int(input(f"Adicione o {i+1}º numero: ")))

    print(f'Menor numero: {min(numeros)}')
    print(f"Maior numero: {max(numeros)}")
    print(f"Soma: {sum(numeros)}")
    print(f"Média aritmética: {(sum(numeros))/len(numeros)}")
