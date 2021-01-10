import sqlite3
from contextlib import closing
p1 = input('Valor 1: ')
p2 = input('Valor 2: ')
with sqlite3.connect('precos.db') as con:
    with closing(con.cursor()) as cursor:
        cursor.execute('select * from precos where valor between ? and ?', (p1, p2))
        x = 0
        while True:
            res = cursor.fetchone()
            if res is None:
                if x == 0:
                    print('Nada encontrado.')
                break
            else:
                print(f'Nome: {res[0]} Preço: {res[1]}')
                x += 1
