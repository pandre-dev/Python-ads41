'''5 - Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo)'''

def checar_sinal(num):
    return num >= 0

if __name__ == "__main__":
    result = checar_sinal(int(input("Digite um valor para checar o sinal: ")))
    if(result == True):
        print('Positivo!')
    else:
        print('Negativo')
