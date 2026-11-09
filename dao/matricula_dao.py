
from dao.db_config import get_connection

class MatriculaDAO:

    
    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT matricula.id, aluno.nome, curso.nome_curso,
                turma.semestre, professor.nome
            FROM matricula
            JOIN aluno ON matricula.aluno_id = aluno.id
            JOIN curso ON matricula.curso_id = curso.id
            JOIN turma ON matricula.turma_id = turma.id
            JOIN professor ON turma.professor_id = professor.id
            ORDER BY matricula.id DESC
        ''')

        lista = cursor.fetchall()
        cursor.close()
        conn.close()

        return lista

    def salvar(self, id, aluno_id, curso_id):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            if id:
                cursor.execute('''
                    UPDATE matricula
                    SET aluno_id = %s, curso_id = %s
                    WHERE id = %s
                ''', (aluno_id, curso_id, id))
            else:
                cursor.execute('''
                    INSERT INTO matricula (aluno_id, curso_id)
                    VALUES (%s, %s)
                ''', (aluno_id, curso_id))

            conn.commit()
            return {"status": "ok"}

        except Exception as e:
            return {"status": "erro", "mensagem": str(e)}

        finally:
            cursor.close()
            conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT id, aluno_id, curso_id
            FROM matricula
            WHERE id = %s
        ''', (id,))

        registro = cursor.fetchone()
        cursor.close()
        conn.close()

        return registro

    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                'DELETE FROM matricula WHERE id = %s',
                (id,)
            )

            conn.commit()
            return {"status": "ok"}

        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}

        finally:
            cursor.close()
            conn.close()
