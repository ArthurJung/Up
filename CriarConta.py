import json


def AlredyExistName_Email(nomeUsuario, email):
    with open('Contas.json', 'r') as file:
        accounts = json.load(file)
        for account in accounts['_accounts']:
            if account['_nome'] == nomeUsuario:
                return True
            if account['_email'] == email:
                return True
        else:
            return False


def CriarConta(account):
    account.ToJSON()
    account = json.loads(json.dumps(account.__dict__))
    with open('Contas.json', 'r') as file:
        data = json.load(file)
        data['_accounts'].append(account)
    with open('Contas.json', 'w') as file:
        json.dump(data, file)
