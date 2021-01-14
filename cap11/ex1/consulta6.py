import sqlite3
from contextlib import closing
with sqlite3.connect('precos.db') as con:
    con.row_factory = sqlite3.Row
    with closing(con.cursor()) as cursor:
        for reg in cursor.execute('select * from precos'):
            print(f'Produto: {reg["nome"]:<10} Valor R$: {float(reg["valor"]):.2f}')
