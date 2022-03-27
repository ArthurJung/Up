from datetime import datetime
from GerarID import NewId
from Foto import Foto


class Mensagem:
    def __init__(self, idMensagem, idOrigem, texto, fotoURL=None):
        self._idMensagem = idMensagem
        self._idOrigem = idOrigem  # idConversa ou idPostagem
        self._data = datetime.today() # Retorna o dia
        self._like = 0
        self._texto = texto
        if fotoURL is not None:
            self._foto = Foto(NewId(), idOrigem, fotoURL)
        else:
            self._foto = None

    @property
    def idMensagem(self):
        return self._idMensagem

    @property
    def idOrigem(self):
        return self._idOrigem

    @property
    def data(self):
        return self._data

    @property
    def like(self):
        return self._like

    @property
    def texto(self):
        return self._texto

    @property
    def foto(self):
        return self._foto
