from flask import Flask, render_template
from dao.db_config import get_connection

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('dashboard/index.html')

@app.route('/sobre')
def sobre():
    return render_template('dashboard/sobre.html')

@app.route('/aluno')

def listar_aluno():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, idade, cidade FROM aluno')
    lista = cursor.fetchall()
    return render_template('aluno/lista.html', lista=lista)

@app.route('/professor')
def lista_professor():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, disciplina FROM professor')
    lista = cursor.fetchall()
    return render_template('professor/lista.html',lista=lista)

@app.route('/turma')
def listar_turma():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT turma.id, semestre, nome_curso, professor.nome FROM turma JOIN curso ON curso.id = turma.curso_id JOIN professor ON professor.id = turma.professor_id')
    lista = cursor.fetchall()
    return render_template('turma/lista.html', lista=lista)


@app.route('/ajuda')
def ajuda():
    return render_template('ajuda.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')


if __name__ == '__main__':
    app.run(debug=True)