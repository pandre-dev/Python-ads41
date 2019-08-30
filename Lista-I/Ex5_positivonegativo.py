'''5 - Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo)'''

def checar_sinal(num):
    if num >= 0:
        print("Positivo")
    else:
        print("Negativo")

checar_sinal(int(input("Digite um valor para checar o sinal: ")))
