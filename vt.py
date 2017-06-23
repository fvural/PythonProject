import sqlite3
con=sqlite3.connect('database.db') # Veritabanına Bağlan
con.row_factory=sqlite3.Row
vt=con.cursor() #Veritabanında İşlem yapabilmek için Cursor oluştur