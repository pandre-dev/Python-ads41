'''16 - Faça um algoritmo que leia os valores de COMPRIMENTO, LARGURA e ALTURA e apresente o valor do
volume de uma caixa retangular. Utilize para o cálculo a fórmula VOLUME = COMPRIMENTO * LARGURA * ALTURA.'''


def volume(comprimento, largura, altura):
    volume = comprimento * largura * altura
    return volume

print(volume(float(input("Digite o comprimento: ")),
             float(input("Digite a largura: ")),
             float(input("Digite a altura: "))))
