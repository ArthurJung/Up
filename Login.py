import json
from Conta import Conta_Perfil


def Login(nomeUsuario, senha):
    with open('Contas.json', 'r') as file:
        accounts = json.load(file)
        for account in accounts['_accounts']:
            if (account['_nome'] == nomeUsuario) and (account['_senha'] == senha):
                account = Conta_Perfil(**account)
                return True, account
        else:
            account = Conta_Perfil(0000000000000000, '', '', '', '', None, [], [], False)
            return False, account
