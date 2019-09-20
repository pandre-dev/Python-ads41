'''12 - Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles'''


def maior_valor(v1, v2):
    #print(f"Maior valor = {v1}") if v1 >= v2 else print(f"Maior valor = {v2}")
    if(v1 != v2):
        return v1 >= v2 and v1 or v2
    return 0


if __name__ == "__main__":
    maior_valor(int(input("Digite o primeiro valor para verificar: ")),
                int(input("Digite o segundo valor para verificar: ")))
