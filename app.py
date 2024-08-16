from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/banda/')
@app.route('/banda/<banda>')
@app.route('/banda/<banda>/<cantor>/<int:nmr_albuns>')
def aula(banda = 'Alice in chains', cantor = 'Layne staley', nmr_albuns = 4):
    dados = {'banda' : banda, 'cantor' : cantor, 'nmr_albuns' : nmr_albuns }
    return render_template('banda.html',dados_html =dados)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/dados', methods=['POST'])
def dados():
    dados = request.form
    return render_template('dados.html', dados_html = dados)

@app.route
def base():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()