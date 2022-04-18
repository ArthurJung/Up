from datetime import datetime
from Mensagem import Mensagem
from GerarID import NewId


class Conversa:
    def __init__(self, _idConversa, _idAdmin, _idParticipantes, _mensagens):
        self._idConversa = _idConversa
        self._idAdmin = [_idAdmin]
        if type(_idParticipantes) is not list:
            self._idParticipantes = [_idParticipantes]
        else:
            self._idParticipantes = [participante for participante in _idParticipantes]
        self._mensagens = [message for message in _mensagens]

    @property
    def idConversa(self):
        return self._idConversa

    @property
    def idAdmin(self):
        return self._idAdmin

    @property
    def idParticipantes(self):
        return self._idParticipantes

    @property
    def mensagens(self):
        return self._mensagens

    def AdicionarAdmin(self, idAdmin, idParticipante):
        for admin in self._idAdmin:
            if idAdmin == admin:
                for participante in self._idParticipantes:
                    if participante == idParticipante:
                        self._idAdmin.append(idParticipante)
                        return 1 # Sucesso
                else:
                    return -1 # Participante não existe
        else:
            return 0 # Você não é adimin

    def RemoverAdmin(self, idAdmin, idParticipante):
        for admin in self._idAdmin:
            if idAdmin == admin:
                for adm in self._idAdmin:
                    if adm == idParticipante:
                        if adm is not(self._idAdmin[0]):
                            self._idAdmin.remove(idParticipante)
                            return 1 # Sucesso
                        else:
                            return 2 # main admin
                else:
                    return -1 # Participante não existe
        else:
            return 0 # Você não é admin

    def AdicionarParticipante(self, idAdmin, idParticipante):
        for admin in self._idAdmin:
            if admin == idAdmin:
                self._idParticipantes.append(idParticipante)
                return 1 # Sucesso
        else:
            return 0 # Você não é admin

    def RemoverParticipante(self, idAdmin, idParticipante):
        for admin in self._idAdmin:
            if admin == idAdmin:
                self._idParticipantes.remove(idParticipante)
                return 1 # Sucesso
        else:
            return 0 # Você não é admin

    def EnviarMensagem(self, idParticipante, texto):
        self._mensagens.append(Mensagem(NewId(), idParticipante, datetime.today(), texto))

    def ExcluirMensagem(self, idParticipante, idMensagem):
        for mensagem in self._mensagens:
            if mensagem.idMensagem == idMensagem:
                if idParticipante == mensagem.idOrigem:
                    self._mensagens.remove(mensagem)
                    return 1 # Mensagem excluida com sucesso
                else:
                    return 0 # Mensagem não pode ser excluida

    def ToJSON(self):
        import json
        if self._mensagens is not None:
            for mensagem in range(len(self._mensagens)):
                self._mensagens[mensagem].ToJson()
                self._mensagens[mensagem] = json.loads(json.dumps(self._mensagens[mensagem].__dict__))
