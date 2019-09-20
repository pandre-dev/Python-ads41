'''8 - faça um método que mostre 10 vezes na tela a palavra python (for i in range(10))'''

def lista_python():
    lista = ["python" for x in range(10)]
    return lista

def checar_palavra(lista, palavra):
    for i in range(len(lista)):
        if(lista[i] != palavra):
            return False
    return True
