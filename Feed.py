class Feed:
    def __init__(self, contas):
        # self._postagens = []# Banco de Dados de postagens
        self.showFeed(contas)

    def showFeed(self, contas):
        for conta in contas:
            for post in conta.postagens:
                print(f'\n{post.descricao}')
