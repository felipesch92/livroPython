import sqlite3
con = sqlite3.connect('agenda.db')
cursor = con.cursor()
cursor.execute('''
        create table if not exists agenda(
            nome text,
            telefone text)
        ''')
cursor.execute('''
        insert into agenda(nome, telefone)
            values(?, ?)
        ''', ("Tamara", "51-98175-0510"))
con.commit()
cursor.close()
con.close()
