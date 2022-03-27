import json


def AlredyExistName_Email(nomeUsuario, email):
    with open('Contas.json', 'r') as file:
        _accounts = json.load(file)
        for account in _accounts['_accounts']:
            if account['_nomeUsuario'] == nomeUsuario:
                return True
            if account['_perfil']['_email'] == email:
                return True
        else:
            return False


def CriarConta(account):
    account.PerfilToJSON()
    account = json.loads(json.dumps(account.__dict__))
    with open('Contas.json', 'r') as file:
        data = json.load(file)
        data['_accounts'].append(account)
    with open('Contas.json', 'w') as file:
        json.dump(data, file)
