'''11 -  Escreva um algoritmo para ler um valor (do teclado) e escrever (na tela) o seu antecessor.'''

def antecessor(num):
    return num - 1
    
if __name__ == "__main__":
    temp=int(input("Digite um valor: "))
    print(f"Antecessor: {temp-1}")
