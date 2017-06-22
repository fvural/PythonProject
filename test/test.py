import sqlite3
vt=sqlite3.connect('fv.db')
vt_sec=vt.cursor()
oku = vt_sec.execute('SELECT * FROM ogrenciler')
print(oku.fetchall())