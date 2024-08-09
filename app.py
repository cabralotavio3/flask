from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aula/')
@app.route('/aula/<nome>')
@app.route('/aula/<nome>/<curso>/<int:ano_nasc>')
def aula(nome = 'Otávio Cabral', curso = '2°informatica', ano_nasc = 2007):
    dados = {'nome' : nome, 'curso' : curso, 'ano_nasc' : ano_nasc }
    return render_template('aula.html',dados_html =dados)

if __name__ == '__main__':
    app.run()