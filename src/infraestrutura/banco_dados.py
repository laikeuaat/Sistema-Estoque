import mysql.connector

def conectar_bd():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="Batata!@#526",  
            database="sistema_estoque"  
        )
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro ao conectar no banco de dados: {err}")
        return None
