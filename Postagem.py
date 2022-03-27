from GerarID import NewId
from datetime import datetime
from Foto import Foto
from Mensagem import Mensagem
import json


class Postagem:
    def __init__(self, _idPostagem, _idOrigem, _descricao, _data, _fotoPostagem=[], _comentario=[], _like=[]):
        self._idPostagem = _idPostagem
        self._idOrigem = _idOrigem
        self._descricao = _descricao
        self._fotoPostagem = []
        with open('Contas.json', 'r') as file:
            data = json.load(file)
            for account in data['_accounts']:
                if account['_perfil']['_idUsuario'] == _idOrigem:
                    for post in account['_postagens']:
                        if post['_idPostagem'] == _idPostagem:
                            self._data = _data
                            if _fotoPostagem is not None:
                                for foto in _fotoPostagem:
                                    self._fotoPostagem.append(Foto(**foto))
                            break
            else:
                self._data = str(datetime.today())
                if _fotoPostagem is not None:
                    for foto in _fotoPostagem:
                        self._fotoPostagem.append(Foto(NewId(), _idOrigem, foto))
                else:
                    self._fotoPostagem = []
            self._comentario = _comentario
            self._like = _like

    @property
    def descricao(self):
        return self._descricao

    @property
    def data(self):
        return self._data

    @property
    def like(self):
        return len(self._like)

    def likeUser(self, idOrigem):
        for like in self._like:
            if like == idOrigem:
                print("Você já deu like!")
                break
        else:
            self._like.append(idOrigem)

    @property
    def idPostagem(self):
        return self._idPostagem

    @property
    def idOrigem(self):
        return self._idOrigem

    @property
    def comentario(self):
        return self._comentario

    @property
    def fotoPostagem(self):
        return self._fotoPostagem

    def AdicionarComentario(self, idOrigem, texto):
        self._comentario.append(Mensagem(NewId(), idOrigem, texto))

    def RemoverComentario(self, idOrigem, idMensagem):
        for comentario in self._comentario:
            if comentario.idMensagem == idMensagem:
                if comentario.idOrigem == idOrigem:
                    self._comentario.remove(comentario)
                else:
                    print("Você não pode remover o comentario de outrem!")

    def ApagarComentario(self, idOrigem, idMensagem):
        for comentario in self._comentario:
            if comentario.idMensagem == idMensagem:
                if self._idOrigem == idOrigem:
                    self._comentario.remove(comentario)
                else:
                    print("Você não pode apagar o comentario na postagem de outrem!")

    def FotoToJSON(self):
        import json
        if self._fotoPostagem is not None:
            for foto in range(len(self._fotoPostagem)):
                self._fotoPostagem[foto] = json.loads(json.dumps(self._fotoPostagem[foto].__dict__))
