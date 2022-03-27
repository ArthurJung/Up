from Perfil import Perfil
from Postagem import Postagem
from Conversa import Conversa
from GerarID import NewId
import json


class Conta:
    def __init__(self, _nomeUsuario, _senha, _perfil=None, _email='', _dataNascimento='', _postagens=[], _conversas=[], _dateRemove=0):
        self._nomeUsuario = _nomeUsuario
        self._senha = _senha
        if _perfil is None:
            self._perfil = Perfil(NewId(), _nomeUsuario, _email, _dataNascimento)
            self._postagens = []
        else:
            self._perfil = Perfil(**_perfil)
            self._postagens = []
            for post in _postagens:
                self._postagens.append(Postagem(**post))
        self._conversas = _conversas
        self._dateRemove = _dateRemove

    @property
    def perfil(self):
        return self._perfil

    @property
    def postagens(self):
        return self._postagens

    def EditarPerfil(self, nome=None, email=None, dataNascimento=None, fotoURL=None):
        if nome is not None:
            self._perfil.nome = nome
        if email is not None:
            self._perfil.email = email
        if dataNascimento is not None:
            self._perfil.dataNascimento = dataNascimento
        if nome is not None:
            self._perfil.fotoURL = fotoURL

    def RemoverPerfil(self, nomeUsuario, senha):
        from datetime import datetime
        if (nomeUsuario == self._nomeUsuario) and (senha == self._senha):
            self._perfil.showStatus = False
            self._dateRemove = datetime.today()
            # Função do banco de dados, apagar depois do dateRemove ultrapassar 30 dias

    def RecuperarPerfil(self, nomeUsuario, senha):
        if (nomeUsuario == self._nomeUsuario) and (senha == self._senha):
            self._perfil.showStatus = True
            self._dateRemove = 0

    def FazerPostagem(self, descricao, fotoURL=[]):
        post = Postagem(NewId(), self._perfil.idUsuario, descricao, 0, fotoURL)
        self._postagens.append(post)

        post.FotoToJSON()
        post = json.loads(json.dumps(post.__dict__))

        with open('Contas.json', 'r') as file:
            data = json.load(file)
            for account in data['_accounts']:
                if account['_nomeUsuario'] == self._nomeUsuario:
                    account['_postagens'].append(post)
        with open('Contas.json', 'w') as file:
            json.dump(data, file)

    def RemoverPostagem(self, idPostagem):
        for postagem in self._postagens:
            if postagem.idPostagem == idPostagem:
                self._postagens.remove(postagem)
                break

    def CriarConversa(self, idParticipante, texto, fotoURL=None):
        self._conversas.append(Conversa(self._perfil.idUsuario, idParticipante, texto, fotoURL))

    def SairConversa(self, idConversa):
        for conversa in self._conversas:
            if conversa.idConversa == idConversa:
                conversa.SelfRemoveConversa(self._perfil.idUsuario)
                self._conversas.remove(conversa)

    def DarLike(self, postagem):
        postagem.likeUser(self.perfil.idUsuario)

    def PerfilToJSON(self):
        self._perfil.FotoToJSON()
        self._perfil = json.loads(json.dumps(self._perfil.__dict__))

    # def PostagemToJSON(self):
    #     if self._postagens is not None:
    #         for post in self._postagens:
    #             post.FotoToJSON()
    #         self._postagens = json.loads(json.dumps(self._postagens.__dict__))
