from Conta import Conta_Perfil
from Login import Login
from GerarID import NewId
from CriarConta import CriarConta, AlredyExistName_Email
import json
import os
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for
)

UPLOAD_FOLDER = 'static/images/uploads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
account = Conta_Perfil(0000000000000000, '', '', '', '', None, [], [], False)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global account
    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']
        verify, account = Login(nome, senha)
        if verify:
            return redirect(url_for('profile'))

        return render_template('/login.html', errou_senha="Usuário ou senha incorretos !")

    return render_template('/login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    import datetime
    global account

    if request.method == 'POST':
        nome = request.form['username']
        email = request.form['email']
        senha = request.form['password']
        datanascimento = datetime.datetime.strptime(request.form['data'], '%Y-%m-%d').strftime('%d/%m/%Y')
        if AlredyExistName_Email(nome, email):
            return redirect(url_for('register'))
        nAccount = Conta_Perfil(NewId(), nome, senha, email, datanascimento, None, [], [], True)
        CriarConta(nAccount)
        verify, account = Login(nome, senha)
        if verify:
            return redirect(url_for('profile'))

    return render_template('/register.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    global account
    # Se não existir conta logada o python retorna a página de login
    if account.idUsuario == 0000000000000000:
        return redirect(url_for('login'))
    if request.method == 'POST':
        descricao = request.form['descricao']
        files = request.files['files']
        _, file_extension = os.path.splitext(files.filename)
        files.filename = str(NewId()) + file_extension
        path = f'{UPLOAD_FOLDER}{files.filename}'
        files.save(path)
        _, account = account.FazerPostagem(descricao, [path])

    return render_template('/profile.html', user=account.nome)


@app.route('/feed')
def feed():
    global account
    if account.idUsuario != 0000000000000000:
        return render_template('/feed.html', posts=account.postagens)
    return redirect(url_for('login'))


@app.route('/message', methods=['GET', 'POST'])
def message():
    global account
    users = []
    if account.idUsuario == 0000000000000000:
        return redirect(url_for('login'))
    with open('Contas.json', 'r') as file:
        data = json.load(file)
        for data_user in data['_accounts']:
            if data_user['_nome'] != account.nome:
                users.append(data_user)
    if request.method == 'POST':
        nomepp = request.form['users']
        texto = request.form['message']
        with open('Contas.json', 'r') as file:
            data = json.load(file)
            for data_user in data['_accounts']:
                if data_user['_nome'] == nomepp:
                    participante = Conta_Perfil(**data_user)
        _, account = account.CriarConversa(participante.idUsuario, texto)

    return render_template('/message.html', users=users)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()
