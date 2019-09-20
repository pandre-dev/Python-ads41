'''
Faça um programa que crie um arquivo contendo o nome de 5 pessoas.
Se o nome informado for igual ao seu nome crie outro arquivo somente com o seu nome.
'''

maisnomes = open('C:\\Users\\ADS\\Desktop\\PauloAndré\\maisnomes.txt', 'w')

for i in range(1, 6):
    nome = input(f'Digite o {i}º nome: ')
    if nome.lower() == 'paulo':
        meunome = open('C:\\Users\\ADS\\Desktop\\PauloAndré\\meunome.txt', 'w')
        meunome.write(nome + '\n')
        meunome.close()

    maisnomes.write(nome + '\n')

maisnomes.close()
