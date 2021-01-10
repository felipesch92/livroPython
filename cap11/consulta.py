import sqlite3
con = sqlite3.connect('agenda.db')
cursor = con.cursor()
cursor.execute('select * from agenda')
'''res = cursor.fetchall()
for l in res:
    print(f'Nome: {l[0]}')
    print(f'Telefone: {l[1]}')
    print('-'*40)'''
while True:
    res = cursor.fetchone()
    if res is None:
        break
    print(f'Nome: {res[0]}')
    print(f'Telefone: {res[1]}')
cursor.close()
con.close()
