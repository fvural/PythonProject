'''
import sqlite3
con=sqlite3.conect('database.db') # Veritabanına Bağlan
con.row_factory=sqlite3.Row
vt=con.cursor() #Veritabanında İşlem yapabilmek için Cursor oluştur

def list():
    t = "ogrenciler"
    print(t)

    sq = 'select * from ?'
    #vt.execute(sq, (tablo,))
    vt.execute('select * from ogrenciler')


list()
'''




import sqlite3

sqlite_file = 'database.db'    # name of the sqlite database file
table_name = 'ogrenciler'   # name of the table to be queried
id_column = 'no'
some_id = 123456
column_2 = 'adi'
column_3 = 'soyadi'

# conecting to the database file
con = sqlite3.connect(sqlite_file)
#con.row_factory=sqlite3.Row

c = con.cursor()


c.execute('SELECT {coi1},{coi2} FROM {tn} '.\
        format(coi1=column_2, coi2=column_3, tn=table_name, cn=column_2))
oku = c.fetchall()
print(oku)



con.commit()
con.close()