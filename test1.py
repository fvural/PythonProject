import sqlite3
baglanti = sqlite3.connect('veriler.db')
baglanti.row_factory = sqlite3.Row
veritabani_sec = baglanti.cursor()
#baglanti kapatma ve kaydetme.


adi=input("Ad=")
soyadi=input("Soyadı=")

veritabani_sec.execute("INSERT INTO ogrenciler (ogrenci_no,adi,soyadi) VALUES ('1234',?,?)", (adi, soyadi))
oku = veritabani_sec.execute('Select adi,soyadi,ogrenci_no from ogrenciler order by kayit_no desc')

x=1
for verileri_cek in oku.fetchall():
    a=("|")
    print(a,x,a,verileri_cek['adi'],verileri_cek['soyadi'],verileri_cek['ogrenci_no'],a)
    x=x+1


baglanti.commit()
baglanti.close()

#silme
#güncelleme