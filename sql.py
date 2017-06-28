################################################################33
#sütun numarasına göre listeleme

def mysqlist2():

    import pymysql
    con = pymysql.connect(host = '127.0.0.1', port = 3388, user = 'root', passwd = '159753', db = 'python')
    vt = con.cursor()

    sql = "SELECT * FROM ogrenciler"
    vt.execute(sql)

    results = vt.fetchall()
    for row in results:
        adi = row[1]
        soyadi = row[2]
        date = row[3]
        no = row[4]
        print("%s : %s,%s,%s" % \
              (no, date, adi, soyadi))

    con.commit()

################################################################33
#sütun ismine göre listeleme

def mysqlist1():

    import pymysql
    con = pymysql.connect(host = '127.0.0.1', port = 3388, user = 'root', passwd = '159753', db = 'python')
    vt = con.cursor(pymysql.cursors.DictCursor)

    sql = "Select * from ogrenciler order by id asc"
    oku=vt.execute(sql)

    x=1
    for row in vt:
        no = row['no']
        adi=row['adi']
        soyadi=row['soyadi']
        date=row['date']
        print(x,no,date,adi,soyadi)
        x = x + 1
    con.commit()

################################################################33

mysqlist1()