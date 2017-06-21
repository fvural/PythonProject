oku = veritabani_sec.execute('Select * from ogrenciler order by id asc')
x = 1
for verileri_cek in oku.fetchall():
    print(verileri_cek['id'], verileri_cek['adi'])
    x = x + 1