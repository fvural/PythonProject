import pymysql

db = pymysql.connect(host = '127.0.0.1', port = 3388, user = 'root', passwd = '159753', db = 'python')
if(db):
    print('Baglanti Başarılı!')
else:
    print('Bağlantı Başarısız!')

cursor = db.cursor()

sql = "SELECT * FROM ogrenciler"
cursor.execute(sql)

results = cursor.fetchall()
for row in results:

    lname = row[1]
    adi = row[2]
    soyadi = row[3]
    date = row[4]
    no = row[4]

    # Now print fetched result
    print("%s,%s,%s,%s" % \
          (adi, soyadi, date, no))

db.commit()

################################################################33

