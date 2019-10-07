import psycopg2

class Connection():

    def get_connection(self):
        connection = psycopg2.connect(user="postgres",
                                      password="ads",
                                      host="localhost",
                                      port="5432",
                                      database="python_livros")
        return connection
