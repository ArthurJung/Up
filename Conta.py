from Postagem import Postagem
from Conversa import Conversa
from datetime import datetime
from Mensagem import Mensagem
from GerarID import NewId
import json

#Cria a classe Conta_Perfil
class Conta_Perfil:
    #Definindo os atributos da classe: o id do usuário, senha, email, data de nascimento, foto de perfil, publicações, conversas e o status da conta
    def __init__(self, _idUsuario, _nome, _senha, _email, _dataNascimento, _fotoPerfil, _postagens, _conversas, _status):
        self._idUsuario = _idUsuario
        self._nome = _nome
        self._senha = _senha
        self._email = _email
        self._dataNascimento = _dataNascimento
        self._fotoPerfil = _fotoPerfil
        self._postagens = [Postagem(**post) for post in _postagens]
        self._conversas = [Conversa(**conversa) for conversa in _conversas]
        self._status = _status #O status define se a conta está banida ou se continua ativa

    @property
    def idUsuario(self):
        return self._idUsuario

    @property
    def nome(self):
        return self._nome

    @property
    def senha(self):
        return self._senha

    @property
    def email(self):
        return self._email

    @property
    def dataNascimento(self):
        return self._dataNascimento

    @property
    def fotoPerfil(self):
        return self._fotoPerfil

    @property
    def postagens(self):
        return self._postagens

    @property
    def conversas(self):
        return self._conversas

    @property
    def status(self):
        return self._status

    def EditarPerfil(self, nome, senha, email, dataNascimento, fotoPerfil):
        self._nome = nome
        self._senha = senha
        self._email = email
        self._dataNascimento = dataNascimento
        self._fotoPerfil = fotoPerfil

    def RemoverPerfil(self, nome, senha):
        if (nome == self._nome) and (senha == self._senha):
            self._status = False
            # Função do banco de dados, apagar se o status for False por mais de 30 dias

    def RecuperarPerfil(self, nome, senha):
        if (nome == self._nome) and (senha == self._senha):
            self._status = True

    def FazerPostagem(self, descricao, fotos):
        post = Postagem(NewId(), self._idUsuario, descricao, fotos, datetime.today(), [], 0)
        self._postagens.append(post)
        post.ToJSON()

        #abre o arquivo json
        with open('Contas.json', 'r') as file:
            accounts = json.load(file)
            #busca a conta no banco de dados e faz a postagem se for encontrada
            for account in accounts['_accounts']:
                if account['_nome'] == self._nome:
                    account['_postagens'].append(json.loads(json.dumps(post.__dict__)))
        with open('Contas.json', 'w') as file:
            json.dump(accounts, file)
        from Login import Login
        return Login(self._nome, self._senha)

    def RemoverPostagem(self, idPostagem):
        for postagem in self._postagens:
            if postagem.idPostagem == idPostagem:
                self._postagens.remove(postagem)
                return 1 # postagem removida
        else:
            return 0 # Erro ao remover postagem

    def CriarConversa(self, idParticipantes, texto):
        message = Mensagem(NewId(), self._idUsuario, datetime.today(), texto)
        conversation = Conversa(NewId(), self._idUsuario, idParticipantes, [message])
        self._conversas.append(conversation)
        conversation.ToJSON()

        #abre o arquivo json
        with open('Contas.json', 'r') as file:
            accounts = json.load(file)
            #busca a conta no banco de dados e cria a conversa se for encontrada
            for account in accounts['_accounts']:
                if account['_nome'] == self._nome:
                    account['_conversas'].append(json.loads(json.dumps(conversation.__dict__)))
        with open('Contas.json', 'w') as file:
            json.dump(accounts, file)
        from Login import Login
        return Login(self._nome, self._senha)

    def SairConversa(self, idConversa):
        for conversa in self._conversas:
            if conversa.idConversa == idConversa:
                self._conversas.remove(conversa)
                return 1  # conversa removida
        else:
            return 0  # Erro ao remover conversa

    # def DarLike(self, postagem):
    #     postagem.likeUser(self._idUsuario)

    def ToJSON(self):
        for post in self._postagens:
            post.ToJSON()
        for conversa in self._conversas:
            conversa.ToJSON()
