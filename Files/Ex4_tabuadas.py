'''
Faça a tabuada de 1 até 10 e salve cada uma em um arquivo, depois leia e mostre na tela.
'''

caminho = 'C:\\Users\\ADS\\Desktop\\PauloAndré\\Files\\'

def tabuada_em_arquivo(num):
    arquivo = open(caminho + 'Tabuada' + str(num) + '.txt', 'w')
    arquivo.write('Tabuada de ' + str(num) + '\n')
    for i in range(1, 11):
        arquivo.write(f'{num} * {i} = {num*i}\n')
    arquivo.close()


for k in range(1, 11):
    tabuada_em_arquivo(k)

for l in range(1, 11):
    leitura = open(caminho + 'Tabuada' + str(l) + '.txt', 'r')
    print(leitura.read())
    print('\n')
    leitura.close()
