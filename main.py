from Conta import Conta
from Login import Login
from GerarID import NewId
from CriarConta import CriarConta, AlredyExistName_Email
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
account = None


@app.route('/login', methods=['GET', 'POST'])
def login():
    global account
    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']
        verify, account = Login(nome, senha)
        if verify:
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

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
        create_account = Conta(nome, senha, _email=email, _dataNascimento=datanascimento)
        CriarConta(create_account)
        verify, account = Login(nome, senha)
        if verify:
            return redirect(url_for('profile'))

    return render_template('/register.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    global account
    if account is None:
        return redirect(url_for('login'))
    if request.method == 'POST':
        descricao = request.form['descricao']
        files = request.files['files']
        _, file_extension = os.path.splitext(files.filename)
        files.filename = str(NewId()) + file_extension
        path = f'{UPLOAD_FOLDER}{files.filename}'
        files.save(path)
        account.FazerPostagem(descricao, [path])

    return render_template('/profile.html')


@app.route('/feed', methods=['GET', 'POST'])
def feed():
    global account
    if account is not None:
        return render_template('/feed.html', posts=account.postagens)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()
