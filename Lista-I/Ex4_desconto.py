'''4. Faça um programa que receba um valor que é o valor pago, um segundo valor que é o preço
do produto e retorne o troco a ser dado'''

def calcula_valor(preco_pago, preco_produto):
    troco=preco_pago-preco_produto
    print(f"\nValor do produto R$: {preco_produto:.2f}"
          f"\nValor pago R$: {preco_pago:.2f}"
          f"\nTroco R$: {troco:.2f}")
    return troco

if __name__ == "__main__":
    calcula_valor(float(input("Digite o valor pago: ")),
                float(input("Digite o valor do produto: ")))
