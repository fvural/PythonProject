################################################################
#mysql kayit ekleme kodu

import pymysql
import random
from datetime import datetime

db = pymysql.connect(host = '127.0.0.1', port = 3388, user = 'root', passwd = '159753', db = 'python')
cursor = db.cursor(pymysql.cursors.DictCursor)

count = 0
while count < 5:
    no = random.randint(1, 99)
    date = str(datetime.now())
    adi = random.choice(['fatih', 'faruk', 'mehmet', 'serkan', 'ahmet'])
    soyadi = random.choice(['fatih', 'faruk', 'mehmet', 'serkan', 'ahmet'])
    '''
    query = "INSERT INTO ogrenciler(adi,soyadi,date,no) " \
                "VALUES(%s,%s,%s,%s)"
    args = (adi, soyadi, date, no)
    cursor.execute(query, args)
    '''
    table_name="ogrenciler"
    cursor.execute("INSERT INTO ogrenciler(adi,soyadi,date,no) VALUES('{a}','{b}','{c}','{d}') ". \
               format(tn=table_name, a=adi, b=soyadi, c=date, d=no))


    count += 1

db.commit()
db.close()
################################################################
