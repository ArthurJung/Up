from GerarID import NewId
from Mensagem import Mensagem


class Conversa:
    def __init__(self, idOrigem, idParticipante, texto, fotoURL=None):
        self._idConversa = NewId()
        self._idAdmin = [idOrigem]
        self._idParticipantes = [idOrigem, idParticipante] # ids dos Usuarios participantes
        self._mensagem = []
        self.AdicionarMensagem(idOrigem, texto, fotoURL)

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
    def mensagem(self):
        return self._mensagem

    def AdicionarAdmin(self, idOrigem, idParticipante):
        for admin in self._idAdmin:
            if idOrigem == admin:
                for participante in self._idParticipantes:
                    if participante == idParticipante:
                        self._idAdmin.append(idParticipante)
                        break
                else:
                    print("Esse participante não existe!")
                    break
        else:
            print("Você não é admin")

    def RemoverAdmin(self, idOrigem, idParticipante):
        for admin in self._idAdmin:
            if idOrigem == admin:
                for adm in self._idAdmin:
                    if adm == idParticipante:
                        if adm is not(self._idAdmin[0]):
                            self._idAdmin.remove(idParticipante)
                            break
                        else:
                            print("Você não pode remover o main admin!")
                else:
                    print("Esse admin não existe!")
                    break
        else:
            print("Você não é admin")

    def AdicionarParticipante(self, idOrigem, idParticipante):
        for admin in self._idAdmin:
            if admin == idOrigem:
                self._idParticipantes.append(idParticipante)
                break
        else:
            print("Você não é admin!")

    def RemoverParticipante(self, idOrigem, idParticipante):
        for admin in self._idAdmin:
            if admin == idOrigem:
                self._idParticipantes.remove(idParticipante)
                break
        else:
            print("Você não é admin!")

    def SelfRemoveConversa(self, idOrigem):
        for participante in self._idParticipantes:
            if participante == idOrigem:
                if participante in self._idAdmin:
                    if len(self._idAdmin) == 1:
                        self._idAdmin.remove(idOrigem)
                        self._idParticipantes.remove(idOrigem)
                        for member in self._idParticipantes:
                            self._idAdmin.append(member)
                            break
                    else:
                        self._idAdmin.remove(idOrigem)
                        self._idParticipantes.remove(idOrigem)
                        break
                else:
                    self._idParticipantes.remove(idOrigem)
                    break

    def AdicionarMensagem(self, idOrigem, texto, fotoURL=None):
        self._mensagem.append(Mensagem(random(), idOrigem, texto, fotoURL))

    def ExcluirMensagem(self, idOrigem, idMensagem):
        for mensagem in self._mensagem:
            if mensagem.idMensagem == idMensagem:
                if idOrigem == mensagem.idOrigem:
                    self._mensagem.remove(mensagem)
                else:
                    print("Você não pode exluir a mensagem de outrem!")
