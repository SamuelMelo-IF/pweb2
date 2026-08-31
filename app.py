from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('dashboard/index.html')

@app.route('/sobre')
def sobre():
    return render_template('dashboard/sobre.html')

@app.route('/aluno')
def lista_aluno():
    lista = [
    (1, "Ana Beatriz Silva", 20, "Teresina"),
    (2, "Carlos Eduardo Lima", 22, "Parnaíba"),
    (3, "Mariana Souza", 19, "Picos"),
    (4, "Rafael Oliveira", 23, "Floriano"),
    (5, "Juliana Costa", 21, "Campo Maior"),
    (6, "Pedro Henrique", 20, "Oeiras"),
    (7, "Fernanda Gomes", 18, "Piripiri"),
    (8, "Lucas Almeida", 22, "Altos"),
    (9, "Bianca Rocha", 24, "Esperantina"),
    (10, "Matheus Ribeiro", 19, "Barras"),
    ]
    return render_template('aluno/lista.html', lista = lista)

@app.route('/professor')
def lista_professor():
    return render_template('professor/lista.html')


if __name__ == '__main__':
    app.run(debug=True)