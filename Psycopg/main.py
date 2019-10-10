from operacoes_bd import Operacoes

if __name__ == "__main__":
    operacoes = Operacoes()
    continuando = True

    print(f"\nCadastro de livros")
    while continuando:
        print(f"\n1 - Registrar livro"
              f"\n2 - Mostrar todos"
              f"\n3 - Buscar livro pelo ID"
              f"\n4 - Editar livro"
              f"\n5 - Excluir livro pelo ID"
              f"\n\n0 - Sair")
        op = int(input("\nDigite a opção desejada: "))

        if op == 1:
            autor = input("Digite o autor do livro: ")
            assunto = int(input("Digite o ID do assunto: "))
            editora = int(input("Digite o ID da editora: "))
            operacoes.salvar_livros(autor, assunto, editora)
        elif op == 2:
            operacoes.mostrar_todos()
        elif op == 3:
            livro_id = int(input("Digite o ID do livro para a pesquisa: "))
            operacoes.buscar_livro(livro_id)
        elif op == 4:
            livro_id = int(input("Digite o ID do livro a ser editado: "))
            operacoes.buscar_livro(livro_id)
            autor = input("Digite o novo autor do livro: ")
            assunto = int(input("Digite o novo ID do assunto: "))
            editora = int(input("Digite o novo ID da editora: "))
            operacoes.editar_livros(autor, assunto, editora, livro_id)
        elif op == 5:
            livro_id = int(input("Digite o ID do livro a ser excluído: "))
            operacoes.excluir_livro(livro_id)
        elif op == 0:
            continuando = False
        else:
            print("\nOpção indesejada. Tente novamente")
