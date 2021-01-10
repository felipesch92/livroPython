import sqlite3
from contextlib import closing
with sqlite3.connect('precos.db') as con:
    with closing(con.cursor()) as cursor:
        cursor.execute('''
            update precos
            set valor = "2.75"
            where nome = "Tubaina"
        ''')
        print('Registros alterados:', cursor.rowcount)
        if cursor.rowcount == 1:
            con.commit()
            print('Alterações gravadas')
        else:
            con.rollback()
            print('Alterações abordadas!')
