'''
27 - Duas amigas estabeleceram o código abaixo para que suas mensagens não fossem lidas pelas demais pessoas.
 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
' ' a b  c d e f  g h  i   j    k   l    m  n    o  p   q   r    s   t   u   v    w  x   y   z
Observe que cada letra equivale a um número entre 1 e 26 e o espaço ao 0.
Faça um método para "traduzir", que recebe uma lista com uma mensagem (secreta)
e "traduz" a sequência armazenada em uma lista.
'''

codigo_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
codigo_letras = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def decode_numtoletter(entrada):
    saida = ''
    for i in range(len(entrada)):
        saida += codigo_letras[codigo_numeros.index(entrada[i])]
    print(saida)


def decode_lettertonum(entrada):
    saida = []
    for i in range(len(entrada)):
        temp = codigo_numeros[codigo_letras.index(entrada[i])]
        saida.append(temp)
    for num in saida:
        print(num)


decode_numtoletter([16, 1, 21, 12, 15, 0, 1, 14, 4, 18, 5])
decode_lettertonum('alo')
