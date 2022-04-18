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

#local da pasta de Uploads
UPLOAD_FOLDER = 'static/images/uploads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
account = Conta_Perfil(0000000000000000, '', '', '', '', None, [], [], False)

#Realiza o login e autentica o usuário
@app.route('/login', methods=['GET', 'POST'])
def login():
    global account
    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']
        verify, account = Login(nome, senha)
        if verify:
            return redirect(url_for('profile'))
        #Se a autenticação falhar informa que o usuário ou senha não correspondem com o banco de dados
        return render_template('/login.html', errou_senha="Usuário ou senha incorretos !")

    return render_template('/login.html')

#Realiza o cadastro
@app.route('/cadastro', methods=['GET', 'POST'])

def cadastro():
    import datetime
    global account
    #colhe os dados do cadastro
    if request.method == 'POST':
        nome = request.form['username']
        email = request.form['email']
        senha = request.form['password']
        c_senha = request.form['repassword']

        #confere se a primeira e a segunda senha correspondem
        if senha != c_senha:
            return render_template('/cadastro.html', errou_senha="As senhas são diferentes !")

        #colhe a data de nascimento do usuário
        datanascimento = datetime.datetime.strptime(request.form['data'], '%Y-%m-%d').strftime('%d/%m/%Y')

        #verifica se o nome de usuário ou email já existem
        if AlredyExistName_Email(nome, email):
            return render_template('/cadastro.html', errou_senha="Nome de usuário ou email já existem !")

        #Cria a conta
        nAccount = Conta_Perfil(NewId(), nome, senha, email, datanascimento, None, [], [], True)
        CriarConta(nAccount)
        verify, account = Login(nome, senha)
        if verify:
            return redirect(url_for('profile'))

    return render_template('/cadastro.html')

#Página perfil do usuário com todas as publicações já realizadas
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    global account
    # Se não existir conta logada o python retorna a página de login
    if account.idUsuario == 0000000000000000:
        return redirect(url_for('login'))
    return render_template('/profile.html', user=account.nome)

#Página criar uma nova publicação
@app.route('/publicacao', methods=['GET', 'POST'])

def publicacao():
    global account

    if account.idUsuario == 0000000000000000:
        return redirect(url_for('login'))

    #insere a descrição e os arquivos na publicação
    if request.method == 'POST':
        descricao = request.form['descricao']
        files = request.files['files']
        _, file_extension = os.path.splitext(files.filename)
        files.filename = str(NewId()) + file_extension
        path = f'{UPLOAD_FOLDER}{files.filename}'
        files.save(path)
        _, account = account.FazerPostagem(descricao, [path])
    return render_template('/publicacao.html')

#Verifica o feed principal com as publicações de todos os usuários
@app.route('/feed')
def feed():
    global account
    if account.idUsuario == 0000000000000000:
        return redirect(url_for('login'))
    return render_template('/feed.html', posts=account.postagens)

#Página de mensagens
@app.route('/message', methods=['GET', 'POST'])
def message():
    global account
    users = []

    if account.idUsuario == 0000000000000000:
        return redirect(url_for('login'))

    #abre o banco de dados
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

#Página de notificações
@app.route('/notificacao')
def notificacao():
    global account
    if account.idUsuario == 0000000000000000:
        return redirect(url_for('login'))
    return render_template('/notificacao.html')

#Página de comentários
@app.route('/comentarios')
def comentarios():
    global account
    if account.idUsuario == 0000000000000000:
        return redirect(url_for('login'))
    return render_template('/comentarios.html')


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()
