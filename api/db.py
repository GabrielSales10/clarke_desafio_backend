import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="fornecedores_db",
        user="gabriel",
        password="#800VSea1000@",
        host="localhost",  # Alterar se necessário
        port="5432"
    )
    return conn
