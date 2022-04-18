from datetime import datetime
from Mensagem import Mensagem
from GerarID import NewId

#Cria a classe conversa com os atributos: id da conversa, id do administrador da conversa, id dos participantes e as mensagens
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

    #Método que permite incluir um participante como administrador na conversa
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

    #Método que remove a permissão de um participante ser administrador na conversa
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

    #Método para adicionar um novo participante na conversa
    def AdicionarParticipante(self, idAdmin, idParticipante):
        for admin in self._idAdmin:
            if admin == idAdmin:
                self._idParticipantes.append(idParticipante)
                return 1 # Sucesso
        else:
            return 0 # Você não é admin

    #Método para remover um participante da conversa
    def RemoverParticipante(self, idAdmin, idParticipante):
        for admin in self._idAdmin:
            if admin == idAdmin:
                self._idParticipantes.remove(idParticipante)
                return 1 # Sucesso
        else:
            return 0 # Você não é admin

    #Método que envia as mensagens com base na identificação do usuário e data e hora
    def EnviarMensagem(self, idParticipante, texto):
        self._mensagens.append(Mensagem(NewId(), idParticipante, datetime.today(), texto))

    #Método que exclui uma mensagem existente, buscando conforme o id do usuário e o id da mensagem a ser excluída
    def ExcluirMensagem(self, idParticipante, idMensagem):
        for mensagem in self._mensagens:
            if mensagem.idMensagem == idMensagem:
                if idParticipante == mensagem.idOrigem:
                    self._mensagens.remove(mensagem)
                    return 1 # Mensagem excluida
                else:
                    return 0 # Mensagem não pode ser excluida

    #Arquivo JSON
    def ToJSON(self):
        import json
        if self._mensagens is not None:
            for mensagem in range(len(self._mensagens)):
                self._mensagens[mensagem].ToJson()
                self._mensagens[mensagem] = json.loads(json.dumps(self._mensagens[mensagem].__dict__))
