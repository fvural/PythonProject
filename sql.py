import sqlite3
con=sqlite3.connect('database.db') # Veritabanına Bağlan
con.row_factory=sqlite3.Row
vt=con.cursor() #Veritabanında İşlem yapabilmek için Cursor oluştur


def list(bak):

    print(bak)

    sq = 'select * from ogrenciler'
    #kontrol = vt.execute(sq, (bak,))
    #pw = kontrol.fetchone()
    #kontrol = vt.execute("select * from ogrenciler", (bak))





bak = "ogrenciler"
list(bak)

kontrol = vt.execute('select * from ?', (bak,))
