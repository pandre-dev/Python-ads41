'''
Escreva um programa que receba do usuário 5 números inteiros e o nome do arquivo no qual eles devem ser armazenados.
Em seguida, ler do arquivo estes valores armazenados copiando-os para um vetor de inteiros e imprimindo na tela.
'''

arq = input(f'Digite o nome do arquivo para armazenamento ds valores: ')
arquivo = open('C:\\Users\\ADS\\Desktop\\PauloAndré\\' + arq, 'w')

for i in range(5):
    numero = int(input('Digite um numero inteiro: '))
    arquivo.write(str(numero) + '\n')

arquivo.close()

numeros = []
arquivo = open('C:\\Users\\ADS\\Desktop\\PauloAndré\\' + arq, 'r')

for linha in arquivo:
    numeros.append(str(linha)[0])

print(numeros)