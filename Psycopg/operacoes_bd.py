import psycopg2
from conexao import Connection

class Operacoes():

    def salvar_livros(self, autor, assunto, editora):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            query_insert = f"""insert into livros (autor, assunto_id, editora_id) values ('{autor}', {assunto}, {editora});"""
            cursor.execute(query_insert)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as er:
            print('Error: ', er)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def mostrar_todos(self):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            query_selectall = "select * from livros"
            cursor.execute(query_selectall)
            livros = cursor.fetchall()

            print("\nTabela livros: ")
            for row in livros:
                print("\nId = ", row[0])
                print("autor = ", row[1])
                print("assunto_id = ", row[2])
                print("editora_id = ", row[3])

        except (Exception, psycopg2.DatabaseError) as er:
            print('Error: ', er)

        finally:
            if connection:
                cursor.close()
                connection.close()

    def buscar_livro(self, livro_id):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            query_select1 = f'select * from livros where id = {livro_id}'
            cursor.execute(query_select1)
            livro = cursor.fetchall()

            for row in livro:
                print("\nId = ", row[0])
                print("autor = ", row[1])
                print("assunto_id = ", row[2])
                print("editora_id = ", row[3])

        except (Exception, psycopg2.DatabaseError) as er:
            print('Error: ', er)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def editar_livros(self, novo_autor, novo_assuntoid, nova_editoraid, livro_id):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            query_update = f"""update livros set autor = '{novo_autor}', assunto_id = {novo_assuntoid}, editora_id = {nova_editoraid}
                    where id = {livro_id}"""
            cursor.execute(query_update)
            connection.commit()
            print('Registro alterado com sucesso!\n')
        except (Exception, psycopg2.DatabaseError) as er:
            print('Error: ', er)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def excluir_livro(self, livro_id):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            query_delete = f"""delete from livros where id = {livro_id}"""
            cursor.execute(query_delete)
            connection.commit()
            print('Registro excluído com sucesso!\n')
        except (Exception, psycopg2.DatabaseError) as er:
            print('Error: ', er)
        finally:
            if connection:
                cursor.close()
                connection.close()
