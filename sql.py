
################################################################33
#mysql listele-silme kodları
################################################################33
#sütun numarasına göre listeleme

def mysqlist2():

    import pymysql
    con = pymysql.connect(host = '127.0.0.1', port = 3388, user = 'root', passwd = '159753', db = 'python')
    vt = con.cursor()

    '''
    #sql diğer sorgu tipi
    sql = "SELECT * FROM ogrenciler"
    vt.execute(sql)
    '''
    table_name="ogrenciler"
    vt.execute('select * from {tn}'. \
               format(tn=table_name))

    results = vt.fetchall()
    for row in results:
        id = row[0]
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

    '''
    sql = "Select * from ogrenciler order by id asc"
    oku=vt.execute(sql)
    '''
    table_name="ogrenciler"
    vt.execute('select * from {tn} order by id asc'. \
               format(tn=table_name))

    x=1
    for row in vt:
        id = row['id']
        no = row['no']
        adi=row['adi']
        soyadi=row['soyadi']
        date=row['date']
        print(x,id,no,date,adi,soyadi)
        x = x + 1

    sql_total = "SELECT COUNT(*) FROM ogrenciler"
    vt.execute(sql_total)
    total = vt.fetchone()
    count = total['COUNT(*)']
    print(count)


    con.commit()

################################################################33

import pymysql
con = pymysql.connect(host = '127.0.0.1', port = 3388, user = 'root', passwd = '159753', db = 'python')
vt = con.cursor(pymysql.cursors.DictCursor)

def dele(id):

    '''
    sql = "delete from ogrenciler where id='%s'" % (id)
    vt.execute(sql)
    '''
    table_name="ogrenciler"
    vt.execute('delete from {tn} where id={did} '. \
               format(did=id, tn=table_name))

################################################################33

def goster(id):

    import pymysql
    con = pymysql.connect(host = '127.0.0.1', port = 3388, user = 'root', passwd = '159753', db = 'python')
    vt = con.cursor(pymysql.cursors.DictCursor)

    '''
    sql = "select * from ogrenciler where id='%s'" % (id)
    vt.execute(sql)
    '''
    table_name = "ogrenciler"
    vt.execute('select * from {tn} where id={did}'. \
               format(tn=table_name,did=id))

    row = vt.fetchone()
    print(row)
    id = row['id']
    no = row['no']
    adi = row['adi']
    soyadi = row['soyadi']
    date = row['date']
    print(id, no, date, adi, soyadi)
    print("\n")

################################################################33
dele(7)
goster(45)
mysqlist1()