from infraestrutura.banco_dados import conectar_bd


class RepositorioUsuario:
    def __init__(self):
        self.conexao = conectar_bd()

    def inserir_usuario(self, email, senha):
        if self.conexao is None:
            raise Exception("Falha na conexão com o banco de dados.")

        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "INSERT INTO usuarios (email, senha) VALUES (%s, %s)", (email, senha)
            )
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            raise Exception(f"Erro ao inserir usuário: {e}")


    def buscar_usuario(self, email, senha):
        if self.conexao is None:
            raise Exception("Falha na conexão com o banco de dados.")

        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "SELECT * FROM usuarios WHERE email = %s AND senha = %s", (email, senha)
            )
            usuario = cursor.fetchone()
            cursor.close()
            return usuario
        except Exception as e:
            raise Exception(f"Erro ao buscar usuário: {e}")
