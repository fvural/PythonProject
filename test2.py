import sqlite3
baglanti = sqlite3.connect('database.db')
if(baglanti):
    print('Baglanti Başarılı!')
else:
    print('Bağlantı Başarısız!')
#baglanti kurulan veriyi seç.
veritabani_sec = baglanti.cursor()
#seçili olan veritabanın verileri okuyalım
oku = veritabani_sec.execute('SELECT adi,soyadi,id from ogrenciler')
print(oku.fetchall())


for verileri_cek in oku.fetchall():
    print('  %s : %s  : %s'%verileri_cek)


baglanti.commit()
baglanti.close()