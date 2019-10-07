from operacoes_bd import Operacoes

if __name__ == "__main__":
    operacoes = Operacoes()
    autor_livro = str(input("Digite o autor do livro: "))
    assunto_livro = int(input("Digite o ID referente ao assunto: "))
    editora_livro = int(input("Digite o ID referente à editora: "))

    operacoes.salvar_livros(autor_livro, assunto_livro, editora_livro)
    operacoes.buscar_livros()
