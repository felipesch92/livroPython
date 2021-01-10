import sqlite3
con = sqlite3.connect('precos.db')
cursor = con.cursor()
cursor.execute('select * from precos where nome = "Feijão"')
while True:
    res = cursor.fetchone()
    if res is None:
        break
    print(f'Produto: {res[0]}')
    print(f'Valor: {res[1]}')
