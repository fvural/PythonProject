import sqlite3
baglanti=sqlite3.connect('a.db', timeout=10)
baglanti.row_factory=sqlite3.Row
veritabani_sec=baglanti.cursor()

import random
from datetime import datetime




#veritabani_sec.execute("INSERT INTO test1 (adi,soyadi,date) VALUES(?,?,?)", (adi,soyadi,date))

import time
starttime=time.time()
while True:
    adi = random.choice(
            ['fatih', 'faruk', 'mehmet', 'serkan', 'ahmet', 'barış', 'yusuf', 'merve', 'eda', 'mustafa', 'gokmen', 'serdar',
             'seckın', 'erhan', 'gülver', 'rasim', 'nazım', 'emre', 'hüseyin', 'ilker', 'sami'
                , 'serkan', 'onur', 'veysel', 'alper', 'hakan', 'harun', 'fikri', 'mesut', 'volkan', 'onur'])
    soyadi = random.choice(
            ['fatih', 'faruk', 'mehmet', 'serkan', 'ahmet', 'barış', 'yusuf', 'merve', 'eda', 'mustafa', 'gokmen', 'serdar',
             'seckın', 'erhan', 'gülver', 'rasim', 'nazım'])
    date = str(datetime.now())
    no = random.randint(1000, 9999)

    print ("tick")
    print(adi)
    print(soyadi)
    print(date)
    veritabani_sec.execute("INSERT INTO test (adi,soyadi,date) VALUES(?,?,?)", (adi, soyadi, date))
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))

baglanti.commit()
baglanti.close()