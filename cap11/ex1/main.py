import sqlite3
con = sqlite3.connect('precos.db')
cursor = con.cursor()
cursor.execute('''
    create table if not exists precos(
    nome text,
    valor text)
''')
cursor.execute('''
        insert into precos(nome, valor)
            values(?, ?)
''', ("Feijão", "1.35"))
cursor.execute('''
        insert into precos(nome, valor)
            values(?, ?)
''', ("Batata", "2.65"))
cursor.execute('''
        insert into precos(nome, valor)
            values(?, ?)
''', ("Uva", "5.56"))
cursor.execute('''
        insert into precos(nome, valor)
            values(?, ?)
''', ("Maracujá", "7.32"))
con.commit()
cursor.close()
con.close()
