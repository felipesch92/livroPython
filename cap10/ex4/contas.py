class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print('-'*40)
        for c in self.clientes:
            print(f'Cliente {c.nome} Telefone {c.telefone}')
        print(f'CC Número: {self.numero} Saldo: {self.saldo:10.2f}')
        print('-'*40)
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
        else:
            print('Saldo insuficiente para saque!')

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['DEPÓSITO', valor])

    def extrato(self):
        print(f'Extrato CC No {self.numero}\n')
        for o in self.operacoes:
            print(f'{o[0]:10s} {o[1]:10.2f}')
        print(f'\n    Saldo: {self.saldo:10.2f}\n')
