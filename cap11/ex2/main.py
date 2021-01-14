from uteis import *
import datetime
while True:
    op = int(input('1 - Inserir 2 - Listar 3 - Buscar 4 - Atualizar 5 - Excluir 6 - Sair '))
    if op == 1:
        nome = input('Estado: ')
        populacao = input('População: ')
        inserir(nome, populacao)
    if op == 2:
        busca()
    if op == 3:
        daqui60dias = datetime.date.today() + datetime.timedelta(days=90)
        print(daqui60dias)
    else:
        print('Opção inválida.')
