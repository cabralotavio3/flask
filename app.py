#pip install flask
#pip install Flask-SQLAlchemy
#pip install Flask-Migrate
#pip install Flask-Script
#pip install pymysql
#flask db init
#flask db migrate -m "Migracao inicial"
#flask db upgrade
from flask import Flask, render_template, request, flash, redirect
from database import db
from flask_migrate import Migrate
from models import Usuario

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

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

@app.route('/usuario/add')
def usuario_add():
    u = Usuario.query.all()
    return render_template('usuario_add.html', dados_html = u)

@app.route('/usuario/save', methods=['POST'])
def usuario_save():
    nome = request.form.get('nome')
    email = request.form.get('email')
    idade = request.form.get('idade')
    if nome and email and idade:
        usuario = Usuario(nome, email, idade)
        db.session.add(usuario)
        db.session.commit()
        flash('usuario cadastrado com sucesso fera!!')
        return redirect('/usuario')
    else:
        flash('preencha todos os campos zeca')
        return redirect('/usuario/add')

@app.route('/usuario/remove/<int:id>')
def usuario_remove(id):
    if id > 0:
        usuario = Usuario.query.get(id)
        db.session.delete(usuario)
        db.session.commit()
        flash('Foi Jubilado Com sucesso!!!!!!!')
        return redirect('/usuario')
    else:
        flash('Deu certo nao irmao faz o L')
        return redirect('/usuario')
    
@app.route('/usuario/edita/<int:id>')
def usuario_edita(id):
        usuario = Usuario.query.get(id)
        return render_template('usuario_edita.html', dados_html=usuario)

@app.route('/usuario/editasave', methods = ['POST'])
def usuario_editasave():
    id = request.form.get('id')
    nome = request.form.get('nome')
    email = request.form.get('email')
    idade = request.form.get('idade')
    if id and nome and email and idade:
        usuario = Usuario.query.get(id)
        usuario.nome = nome
        usuario.email = email
        usuario.idade = idade
        db.session.commit()
        flash('Dados atualizados com sucesso!!')
        return redirect('/usuario')
    else:
        flash('Está faltando dados!')
        return redirect('/usuario')
@app.route
def base():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()