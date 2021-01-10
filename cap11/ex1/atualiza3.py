import sqlite3
from contextlib import closing
prod = input('Produto: ')
prec = input('Novo preço: ')
with sqlite3.connect('precos.db') as con:
    with closing(con.cursor()) as cursor:
        cursor.execute('''
            update precos 
            set valor = ?
            where nome = ?
        ''', (prec, prod))
        if cursor.rowcount == 1:
            con.commit()
            print('Preço atualizado com sucesso!')
        else:
            con.rollback()
            print('Alterações abordadas!')
