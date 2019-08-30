'''
10 - receba três notas de um aluno e informe se ele passou ou reprovou
'''

def aprovacao(n1, n2, n3):
    media = (n1+n2+n3)/3
    if media >= 7:
        print("\nAluno aprovado!")
    else:
        print("\nAluno rerovado!")
    print(f"Média: {media}")

aprovacao(float(input("Digite a primeira nota: ")),
          float(input("Digite a segunda nota: ")),
          float(input("Digite a terceira nota: ")))
