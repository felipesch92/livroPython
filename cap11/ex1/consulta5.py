import sqlite3
with sqlite3.connect('precos.db') as con:
    for reg in con.execute('select * from precos'):
        print(f'Produto: {reg[0]} Valor: {float(reg[1]):.2f}')
