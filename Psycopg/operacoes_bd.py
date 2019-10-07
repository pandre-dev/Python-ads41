import psycopg2
from conexao import Connection

class Operacoes():

    def salvar_livros(self, autor, assunto, editora):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            insert = f"""insert into livros (autor, assunto_id, editora_id) values ('{autor}', {assunto}, {editora});"""
            cursor.execute(insert)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as er:
            print('Error: ', er)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def buscar_livros(self):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            select = "select * from livros"
            cursor.execute(select)
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
