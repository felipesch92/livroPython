import sqlite3
from contextlib import closing
nome = input('Produto a pesquisar: ')
with sqlite3.connect('precos.db') as con:
    with closing(con.cursor()) as cursor:
        cursor.execute(f'select * from precos where nome = "{nome}"')
        while True:
            res = cursor.fetchone()
            if res is None:
                break
            else:
                print(f'Nome: {res[0]} Preço: {res[1]}')
