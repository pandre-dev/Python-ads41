'''15 - Ler 10 valores (considere que não serão lidos valores iguais) e escrever o maior deles.'''

valores=[]
cont=0

while cont < 10:
    temp = int(input("Digite um valor: "))
    if temp in valores:
        print("Número repetido. Tente novamente.")
    else:
        valores.append(temp)
        cont += 1

print(max(valores))
