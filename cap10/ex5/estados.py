from cidades import Cidade
class Estado():
    def __init__(self, nome, sigla, cidades):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades

    def resumo(self):
        print('-'*40)
        print(f'Estado: {self.nome} UF: {self.sigla}')
        total_populacao = 0
        for c in self.cidades:
            c.resumo()
            total_populacao += c.populacao
        print(f'População total: {total_populacao:}')
        print('-'*40)
