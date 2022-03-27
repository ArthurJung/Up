class Foto:
    def __init__(self, _idFoto, _idOrigem, _fotoURL):
        self._idFoto = _idFoto
        self._idOrigem = _idOrigem  # idUsuario ou idPostagem ou idMensagem
        self._fotoURL = _fotoURL

    @property
    def idFoto(self):
        return self._idFoto

    @property
    def idOrigem(self):
        return self._idOrigem

    @property
    def fotoURL(self):
        return self._fotoURL
