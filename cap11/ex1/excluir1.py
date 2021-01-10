import sqlite3
from contextlib import closing
prod = input('Informe o produto a ser deletado: ')
with sqlite3.connect('precos.db') as con:
    with closing(con.cursor()) as cursor:
        cursor.execute('''
            delete from precos
            where nome = ?
        ''', (prod,))
        if cursor.rowcount == 1:
            con.commit()
            print(f'Produto {prod} apagado com sucesso!')
        else:
            con.rollback()
            print('Alterações abordadas!')
