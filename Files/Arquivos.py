arquivo = open('C:\\Users\\ADS\\Desktop\\PauloAndré\\Teste.txt', 'w')
arquivo.write('Primeira linha escrita no arquivo.\n')
arquivo.write('Segunda linha escrita no arquivo.')
arquivo.write('Um pouco mais da segunda linha.\n')
arquivo.write('Agora é a terceira linha')
arquivo.close()

arquivo = open('C:\\Users\\ADS\\Desktop\\PauloAndré\\Teste.txt', 'r')
for linha in arquivo:
    print(linha)

arquivo.close()
