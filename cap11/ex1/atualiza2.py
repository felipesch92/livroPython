import sqlite3
from contextlib import closing
with sqlite3.connect('precos.db') as con:
    with closing(con.cursor()) as cursor:
        cursor.execute('''
                update precos
                set valor = valor * 1.1
        ''')
        if cursor.rowcount > 0:
            con.commit()
            print('Alterações gravadas')
        else:
            con.rollback()
            print('Alterações abordadas!')
