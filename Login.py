import json
from Conta import Conta


def Login(nomeUsuario, senha):
    with open('Contas.json', 'r') as file:
        accounts = json.load(file)
        for account in accounts['_accounts']:
            if (account['_nomeUsuario'] == nomeUsuario) and (account['_senha'] == senha):
                account = Conta(**account)
                return True, account
        else:
            return False, None
