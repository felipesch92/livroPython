import sqlite3
from contextlib import closing

def criar_tabela():
    with sqlite3.connect('estados.db') as con:
        with closing(con.cursor()) as cursor:
            cursor.execute('''create table estados(
                            id integer primary key autoincrement,
                            nome text, populacao integer)''')
            con.commit()


def inserir(nome, populacao):
    with sqlite3.connect('estados.db') as con:
        with closing(con.cursor()) as cursor:
            cursor.execute('''insert into estados
                            (nome, populacao) values
                            (?, ?)''', (nome, populacao))
        con.commit()

def busca():
    with sqlite3.connect('estados.db') as con:
        con.row_factory = sqlite3.Row
        print(f'{"ID":<3} {"Estado":<20} {"UF":<3} {"População"}')
        for estado in con.execute('select * from estados order by nome'):
            print(f'{estado["id"]:<3} {estado["nome"]:<20} {estado["uf"]:<3} {estado["populacao"]}')

def alterar_tabela():
    with sqlite3.connect('estados.db') as con:
        con.execute('alter table estados add uf text')
