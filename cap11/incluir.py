import sqlite3
con = sqlite3.connect('agenda.db')
cursor = con.cursor()
dados = [('João', '93182-3213'),
         ('Maria', '93823-5422'),
         ('Pedro', '98434-3213')]
cursor.executemany('''
    insert into agenda (nome, telefone)
    values (?, ?)
''', dados)
con.commit()
cursor.close()
con.close()
