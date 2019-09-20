'''
Crie um arquivo chamado nomes.txt que permita que o usuário faça a inserção de 10 nomes.
Procure no arquivo o arquivo o nome ‘gisele’
'''

nomes = open('C:\\Users\\ADS\\Desktop\\PauloAndré\\nomes.txt', 'w')

for i in range(1, 11):
    nomes.write(input(f'Digite o {i}º nome: ') + '\n')

nomes.close()

nomes = open('C:\\Users\\ADS\\Desktop\\PauloAndré\\nomes.txt', 'r')
for linha in nomes:
    if 'gisele' in linha.lower():
        print("Nome 'Gisele' encontrado")

nomes.close()
