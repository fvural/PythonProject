
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

  baglanti = sqlite3.connect('aktpi.db')
  baglanti.row_factory = sqlite3.Row
  veritabani_sec = baglanti.cursor()
  # baglantikapatmavekaydetme.
  import random
  from datetime import datetime

  cihaz = random.choice(['aktpi001', 'aktpi001', 'aktpi002', 'aktpi003', 'aktpi004', 'aktpi005'])
  lokasyon = random.choice(['Vulkanizasyon-1', 'Vulkanizasyon-2', 'Vulkanizasyon-3', 'Vulkanizasyon-4', 'Vulkanizasyon-5', 'Mikser-1','Mikser-2','Kalender-1'])
  sicaklik = random.randint(1, 99)
  nem = random.randint(1, 99)
  date = str(datetime.now())
  sql = veritabani_sec.execute("INSERT INTO aktas (cihaz,lokasyon,sicaklik,nem,date) VALUES(?,?,?,?,?)", (cihaz, lokasyon, sicaklik, nem, date))
  x=x+1
  print( x,cihaz,lokasyon,sicaklik,nem,date)
  baglanti.commit()
  baglanti.close()

  time.sleep(10.0 - ((time.time() - starttime) % 10.0))