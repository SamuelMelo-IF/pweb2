from flask import Flask, render_template, request
from dao.db_config import get_connection
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO
from dao.turma_dao import CursoDAO

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('dashboard/index.html')

@app.route('/sobre')
def sobre():
    return render_template('dashboard/sobre.html')

@app.route('/aluno')

def listar_aluno():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista.html', lista=lista)

@app.route('/professor')
def lista_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html',lista=lista)

@app.route('/turma')
def listar_turma():
    dao = TurmaDAO()
    lista = dao.listar()
    return render_template('turma/lista.html', lista=lista)

@app.route('/curso')
def listar_curso():
    dao = CursoDAO()
    lista = dao.listar()
    return render_template('curso/lista.html', lista=lista)

@app.route('/ajuda')
def ajuda():
    return render_template('ajuda.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/saudacao1/<nome>')
def saudacao1(nome):
    print(nome)
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

@app.route('/saudacao2/')
def saudacao2():
    nome = request.args.get('nome')
    print(nome)
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    email = request.form['email']
    dados = f"Usuário: {usuario}, Senha: {senha}, E-mail: {email}"
    return render_template('saudacao/saudacao.html', valor_recebido=dados)


@app.route('/formulario', methods=['POST'])
def enviar_formulario():
    nome = request.form['nome']
    data_nascimento = request.form['data_nascimento']
    cpf = request.form['cpf']
    nome_mae = request.form['nome_mae']
    
    return render_template('desafios/resultado.html', nome=nome, data_nascimento=data_nascimento, cpf=cpf, nome_mae=nome_mae)


@app.route('/formulario')
def formulario():
    return render_template('desafios/formulario.html')

if __name__ == '__main__':
    app.run(debug=True)