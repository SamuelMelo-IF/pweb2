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

        (11, "Gabriel Santos", 21, "Teresina"),
    (12, "Larissa Martins", 20, "Parnaíba"),
    (13, "João Victor Alves", 23, "Picos"),
    (14, "Camila Ferreira", 19, "Floriano"),
    (15, "Bruno Henrique Costa", 22, "Campo Maior"),
    (16, "Letícia Almeida", 21, "Oeiras"),
    (17, "Gustavo Rocha", 20, "Piripiri"),
    (18, "Amanda Souza", 18, "Altos"),
    (19, "Thiago Oliveira", 24, "Esperantina"),
    (20, "Beatriz Lima", 19, "Barras"),

    (21, "Daniel Pereira", 22, "Teresina"),
    (22, "Isabela Martins", 20, "Parnaíba"),
    (23, "Marcos Vinícius Silva", 21, "Picos"),
    (24, "Carolina Alves", 23, "Floriano"),
    (25, "André Luiz Costa", 19, "Campo Maior"),
    (26, "Natália Gomes", 22, "Oeiras"),
    (27, "Felipe Rodrigues", 20, "Piripiri"),
    (28, "Júlia Santos", 18, "Altos"),
    (29, "Ricardo Almeida", 24, "Esperantina"),
    (30, "Vitória Rocha", 21, "Barras"),

    (31, "Eduardo Lima", 20, "Teresina"),
    (32, "Sofia Oliveira", 19, "Parnaíba"),
    (33, "Henrique Costa", 23, "Picos"),
    (34, "Raquel Ferreira", 21, "Floriano"),
    (35, "Caio Henrique Silva", 22, "Campo Maior"),
    (36, "Aline Souza", 20, "Oeiras"),
    (37, "Rodrigo Gomes", 24, "Piripiri"),
    (38, "Manuela Alves", 19, "Altos"),
    (39, "Leonardo Martins", 21, "Esperantina"),
    (40, "Clara Vitória Lima", 18, "Barras"),

    (41, "Samuel Pereira", 23, "Teresina"),
    (42, "Marina Costa", 20, "Parnaíba"),
    (43, "Arthur Oliveira", 22, "Picos"),
    (44, "Débora Santos", 19, "Floriano"),
    (45, "Vinícius Almeida", 21, "Campo Maior"),
    (46, "Elisa Rocha", 20, "Oeiras"),
    (47, "Murilo Ferreira", 24, "Piripiri"),
    (48, "Luana Gomes", 18, "Altos"),
    (49, "Diego Martins", 22, "Esperantina"),
    (50, "Renata Silva", 21, "Barras"),

    (51, "Alexandre Costa", 23, "Teresina"),
    (52, "Helena Pereira", 20, "Parnaíba"),
    (53, "Igor Santos", 19, "Picos"),
    (54, "Melissa Oliveira", 22, "Floriano"),
    (55, "Fábio Lima", 21, "Campo Maior"),
    (56, "Caroline Alves", 20, "Oeiras"),
    (57, "Wesley Rocha", 23, "Piripiri"),
    (58, "Yasmin Ferreira", 19, "Altos"),
    (59, "Ruan Gomes", 22, "Esperantina"),
    (60, "Patrícia Martins", 24, "Barras"),

    (61, "Anderson Silva", 21, "Teresina"),
    (62, "Gabriela Costa", 20, "Parnaíba"),
    (63, "Lucas Pereira", 23, "Picos"),
    (64, "Sara Oliveira", 18, "Floriano"),
    (65, "Matheus Santos", 22, "Campo Maior"),
    (66, "Ana Paula Lima", 21, "Oeiras"),
    (67, "João Gabriel Rocha", 20, "Piripiri"),
    (68, "Beatriz Ferreira", 19, "Altos"),
    (69, "Renato Almeida", 24, "Esperantina"),
    (70, "Alice Gomes", 22, "Barras"),

    (71, "Cristiano Alves", 23, "Teresina"),
    (72, "Lívia Martins", 20, "Parnaíba"),
    (73, "Eduardo Costa", 21, "Picos"),
    (74, "Isadora Silva", 19, "Floriano"),
    (75, "Rafael Pereira", 22, "Campo Maior"),
    (76, "Mirella Santos", 20, "Oeiras"),
    (77, "Paulo Henrique Oliveira", 24, "Piripiri"),
    (78, "Laura Rocha", 18, "Altos"),
    (79, "Gabriel Ferreira", 21, "Esperantina"),
    (80, "Amanda Martins", 23, "Barras"),

    (81, "José Carlos Lima", 22, "Teresina"),
    (82, "Maria Eduarda Costa", 20, "Parnaíba"),
    (83, "Felipe Alves", 19, "Picos"),
    (84, "Luiza Pereira", 21, "Floriano"),
    (85, "Carlos Henrique Gomes", 23, "Campo Maior"),
    (86, "Mariana Oliveira", 20, "Oeiras"),
    (87, "Victor Santos", 22, "Piripiri"),
    (88, "Nicole Almeida", 19, "Altos"),
    (89, "João Pedro Rocha", 24, "Esperantina"),
    (90, "Brenda Ferreira", 21, "Barras"),

    (91, "Fernando Martins", 20, "Teresina"),
    (92, "Cecília Silva", 22, "Parnaíba"),
    (93, "Guilherme Costa", 21, "Picos"),
    (94, "Manuela Pereira", 19, "Floriano"),
    (95, "Lucas Henrique Santos", 23, "Campo Maior"),
    (96, "Rebeca Oliveira", 20, "Oeiras"),
    (97, "Marcelo Rocha", 24, "Piripiri"),
    (98, "Sophia Alves", 18, "Altos"),
    (99, "Antônio Gomes", 22, "Esperantina"),
    (100, "Laura Beatriz Martins", 21, "Barras"),
    ]
    return render_template('aluno/lista.html', lista = lista)

@app.route('/professor')
def lista_professor():
    return render_template('professor/lista.html')

@app.route('/ajuda')
def ajuda():
    return render_template('ajuda.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')


if __name__ == '__main__':
    app.run(debug=True)