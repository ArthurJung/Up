class Postagem:
    def __init__(self, _idPostagem, _idUsuario, _descricao, _fotos, _data, _comentarios, _likes):
        self._idPostagem = _idPostagem
        self._idUsuario = _idUsuario
        self._descricao = _descricao
        if type(_fotos) is not list:
            self._fotos = [_fotos]
        else:
            self._fotos = [foto for foto in _fotos]
        self._data = _data
        self._comentarios = _comentarios
        self._likes = _likes

    @property
    def idPostagem(self):
        return self._idPostagem

    @property
    def idUsuario(self):
        return self._idUsuario

    @property
    def descricao(self):
        return self._descricao

    @property
    def fotos(self):
        return self._fotos

    @property
    def data(self):
        return self._data

    @property
    def comentarios(self):
        return self._comentarios

    @property
    def likes(self):
        return self._likes

    def ToJSON(self):
        import json
        self._data = json.loads(json.dumps(self._data, indent=4, sort_keys=True, default=str))
        if self._comentarios is not None:
            for comentario in range(len(self._comentarios)):
                self._comentarios[comentario].ToJson()
                self._comentarios[comentario] = json.loads(json.dumps(self._comentarios[comentario].__dict__))
