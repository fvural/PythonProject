
####################
def cls():
    import os
    os.system('cls')
    return
cls()
import time
starttime=time.time()

#sıcaklık,nem,lokasyon,tarih+saat,cihazno
x=0
while True:
  import sqlite3

  baglanti = sqlite3.connect('database.db')
  baglanti.row_factory = sqlite3.Row
  veritabani_sec = baglanti.cursor()
  # baglantikapatmavekaydetme.
  import random
  from datetime import datetime

  adi = random.choice(['fatih', 'faruk', 'mehmet', 'serkan', 'ahmet'])
  soyadi = random.choice(['fatih', 'faruk', 'mehmet', 'serkan', 'ahmet'])
  no = random.randint(1, 99)
  date = str(datetime.now())
  sql = veritabani_sec.execute("INSERT INTO ogrenciler (no,adi,soyadi,date) VALUES(?,?,?,?)", (no, adi, soyadi, date))
  x=x+1
  print( x,no,adi, soyadi,date)
  baglanti.commit()
  baglanti.close()

  time.sleep(10.0 - ((time.time() - starttime) % 10.0))

