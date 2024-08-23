from flask import Flask, render_template, request
from database import db
from flask_migrate import Migrate
from models import Usuario

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

#drive://usuario:senha@servidor/banco_dados
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/flasko"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

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

@app.route('/usuario')
def usuario():
    u = Usuario.query.all()
    return render_template('usuario_lista.html', dados_html = u)

@app.route
def base():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()