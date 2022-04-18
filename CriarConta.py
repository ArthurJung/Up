import json

# Verifica se já existe uma conta com o mesmo nome de usuário ou email
def AlredyExistName_Email(nomeUsuario, email):

    #busca no banco de dados Json
    with open('Contas.json', 'r') as file:
        accounts = json.load(file)

        #Se a conta já existir retorna True, do contrario , retorna False
        for account in accounts['_accounts']:
            if account['_nome'] == nomeUsuario:
                return True
            if account['_email'] == email:
                return True
        else:
            return False

#Cria a conta inserindo as informações e as atualiza no banco de dados
def CriarConta(account):
    account.ToJSON()
    account = json.loads(json.dumps(account.__dict__))
    with open('Contas.json', 'r') as file:
        data = json.load(file)
        data['_accounts'].append(account)
    with open('Contas.json', 'w') as file:
        json.dump(data, file)
