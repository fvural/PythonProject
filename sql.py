import sqlite3
con=sqlite3.connect('database.db') # Veritabanına Bağlan
con.row_factory=sqlite3.Row
vt=con.cursor() #Veritabanında İşlem yapabilmek için Cursor oluştur


def list(tablo):

    print(tablo)

    sq = 'select * from ?'
    kontrol = vt.execute(sq, (tablo,))






bak = "tablo"
list(ogrenciler)

