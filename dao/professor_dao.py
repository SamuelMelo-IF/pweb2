from dao.db_config import get_connection

class ProfessorDAO:
    
    sqlSelect = 'SELECT id, nome, disciplina FROM professor'

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        return lista

    def salvar(self, id, nome, idade, cidade):
            conn = get_connection()
            cursor = conn.cursor()
            try:
                cursor.execute('INSERT INTO professor (nome, idade, cidade) VALUES (%s, %s, %s)', (nome, idade, cidade))
                conn.commit()
                return {"status": "ok"}
            except Exception as e:
                return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
            finally:
                conn.close()