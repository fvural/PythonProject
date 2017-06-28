import sqlite3
con=sqlite3.connect('database.db') # Veritabanına Bağlan
con.row_factory=sqlite3.Row
vt=con.cursor() #Veritabanında İşlem yapabilmek için Cursor oluştur

sql = "Select * from ogrenciler order by id asc"
oku= vt.execute(sql)

x = 1
vt = vt.fetchall()
for row in vt:
    date = row['date']
    date = date[:19]

    print(x,row['id'],date,row['adi'],row['soyadi'],row['no'])
    x = x + 1