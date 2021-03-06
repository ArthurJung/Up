#Cria a classe mensagem com os atributos id da mensage, id da origem, data e o texto
class Mensagem:
    def __init__(self, _idMensagem, _idOrigem, _data, _texto):
        self._idMensagem = _idMensagem
        self._idOrigem = _idOrigem
        self._data = _data
        self._texto = _texto

    @property
    def idMensagem(self):           #privado
        return self._idMensagem

    @property
    def idOrigem(self):
        return self._idOrigem

    @property
    def data(self):
        return self._data

    @property
    def texto(self):
        return self._texto

    #Arquivo JSON
    def ToJson(self):
        import json
        self._data = json.loads(json.dumps(self._data, indent=4, sort_keys=True, default=str))
