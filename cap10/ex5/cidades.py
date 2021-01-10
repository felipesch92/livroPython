class Cidade():
    def __init__(self, nome, populacao=0):
        self.nome = nome
        self.populacao = populacao

    def resumo(self):
        print(f'Cidade: {self.nome:<30} População: {self.populacao}')
