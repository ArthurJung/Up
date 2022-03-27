from Foto import Foto
from GerarID import NewId


class Perfil:
    def __init__(self, _idUsuario, _nome, _email, _dataNascimento, _showStatus=True, _fotoPerfil=None):
        self._idUsuario = _idUsuario
        self._nome = _nome
        self._email = _email
        self._dataNascimento = _dataNascimento
        self._showStatus = _showStatus
        if _fotoPerfil is None:
            self._fotoPerfil = _fotoPerfil
        else:
            self._fotoPerfil = Foto(**_fotoPerfil)

    @property
    def idUsuario(self):
        return self._idUsuario

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def dataNascimento(self):
        return self._dataNascimento

    @dataNascimento.setter
    def dataNascimento(self, dataNascimento):
        self._dataNascimento = dataNascimento

    @property
    def fotoPerfil(self):
        return self._fotoPerfil

    @fotoPerfil.setter
    def fotoPerfil(self, fotoPerfil):
        self._fotoPerfil = Foto(NewId(), self._idUsuario, fotoPerfil)

    def RemoverFotoPerfil(self):
        self._fotoPerfil = None

    @property
    def showStatus(self):
        return self._showStatus

    @showStatus.setter
    def showStatus(self, showStatus):
        self._showStatus = showStatus

    def FotoToJSON(self):
        import json
        if self._fotoPerfil is not None:
            self._fotoPerfil = json.loads(json.dumps(self._fotoPerfil.__dict__))
