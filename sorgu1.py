'''
import sqlite3
con=sqlite3.connect('database.db') # Veritabanına Bağlan
con.row_factory=sqlite3.Row
vt=con.cursor() #Veritabanında İşlem yapabilmek için Cursor oluştur
'''
import pymysql
con = pymysql.connect(host = '127.0.0.1', port = 3388, user = 'root', passwd = '159753', db = 'python')
vt = con.cursor(pymysql.cursors.DictCursor)


import fonk
#
################################################################################################################

def delete(table_name, id):
    #print(table_name) # GELEN DEĞERİ GÖRMEK İÇİN
    #print(id) # GELEN DEĞERİ GÖRMEK İÇİN

    '''
    sq = 'select * from ogrenciler where id=?'
    kontrol = vt.execute(sq, (id,))
    pw = kontrol.fetchone()
    '''

    sql = "select * from ogrenciler where id='%s'" % (id)
    vt.execute(sql)
    pw = vt.fetchone()

    if (not pw):  # Kayıt Yoksa Burası
        print("Böyle Bir Kayıt YOK !!!")
    else:  # Kayıt varsa burası

################################################
# silinecek olan kayıdı göstermek için ...
        sql = "select * from ogrenciler where id='%s'" % (id)
        oku = vt.execute(sql)


        x = 1
        print("----------------------------------------------------------------------------------")
        print("| NO | ID  | TARIH               | ADI     | SOYADI  |  ")
        results=vt.fetchall()
        for verileri_cek in results:
            a = ("|")
            print("----------------------------------------------------------------------------------")
            date = verileri_cek['date']
            date = date[:19]

            print(a, x, a, verileri_cek['id'], a, date, a, verileri_cek['adi'], "", a, verileri_cek['soyadi'], "", a,
                  verileri_cek['no'], a)
            x = x + 1
        print("----------------------------------------------------------------------------------")

################################################

        print("\n")
        print("UYARI=", id, " Nolu Kayıt silinecek !!!")
        answer = input('[e(vet)/h(ayır)]:')
        if answer.lower().startswith("e"):  # EVET Durumunda Yapılacak
            fonk.cls()
            print(id, " nolu Kayıt silindi...")

            vt.execute('delete from {tn} where id={did} '. \
                                format(did=id, tn=table_name))

            con.commit()
        elif answer.lower().startswith("h"):  # HAYIR Durumunda Yapılacak
            print("silme işlemi iptal edildi...")
            exit()
        elif answer.lower().startswith(""):  # (answer=""): # BOŞ Bırakılırsa Yapılacak #
            print("Boş Bırakılamaz...!")
        else:
            print("Soruya e(vet) yada h(ayır) seklinde cevap veriniz...")


################################################################################################################

def insert():
    import random
    from datetime import datetime
    adi = input("Ad=")

    soyadi = input("Soyadı=")

    no = random.randint(1, 99)
    date = str(datetime.now())

    print(adi)
    print(soyadi)
    print(no)
    print(date)

    query = "INSERT INTO ogrenciler(adi,soyadi,date,no) " \
                "VALUES(%s,%s,%s,%s)"
    args = (adi, soyadi, date, no)
    vt.execute(query, args)
    #vt.execute("INSERT INTO ogrenciler (no,adi,soyadi,date) VALUES(?,?,?,?)", (no, adi, soyadi, date))
    con.commit()

################################################################################################################
def ara():
    like = input('Aranacak Kelime:')

    # like='fat'

    print(like)

    oku = vt.execute("Select * from ogrenciler where adi like ?", ('%' + like + '%',))

    x = 1

    print("----------------------------------------------------------------------------------")

    print("| NO | ID | ADI | SOYADI | DETAY  ")

    for verileri_cek in oku.fetchall():
        a = ("|")

        print("----------------------------------------------------------------------------------")

        print(a, x, a, verileri_cek['id'], a, verileri_cek['adi'], "", a, verileri_cek['soyadi'], "", a,
              verileri_cek['no'], a, verileri_cek['date'])

        x = x + 1

    sum = vt.execute("SELECT COUNT(*) FROM ogrenciler").fetchone()[0]

    print("\n")

    print('Toplam  = ', sum, 'kayıt var.')

################################################################################################################
def delall():
    print("\n")

    print("UYARI= Tüm kayıtlar silinecek !!!")

    answer = input('[e(vet)/h(ayır)]:')

    if answer.lower().startswith("e"):  # EVET Durumunda Yapılacak

        # cls()

        print("Tüm Kayıtlar temizlendi...")

        sql = 'delete from ogrenciler'

        sil = vt.execute(sql)


    elif answer.lower().startswith("h"):  # HAYIR Durumunda Yapılacak

        print("Tümünü silme işlemi iptal edildi...")

        exit()

    elif answer.lower().startswith(""):  # (answer=""): # BOŞ Bırakılırsa Yapılacak #

        print("Boş Bırakılamaz...!")


    else:

        print("Soruya e(vet) yada h(ayır) seklinde cevap veriniz...")

    con.commit()


################################################################################################################
def insertall():
    count = 0

    while count < 10:
        # print(count)

        # count+=1
        import random
        from datetime import datetime
        no = random.randint(1, 99)
        date = str(datetime.now())

        adi = random.choice(['fatih', 'faruk', 'mehmet', 'serkan', 'ahmet'])
        soyadi = random.choice(['fatih', 'faruk', 'mehmet', 'serkan', 'ahmet'])

        date = str(datetime.now())

        no = random.randint(1000, 9999)


        vt.execute("INSERT INTO ogrenciler(adi,soyadi,date,no) VALUES('{a}','{b}','{c}','{d}') ". \
                       format(a=adi, b=soyadi, c=date, d=no))

        #vt.execute("INSERT INTO ogrenciler (no,adi,soyadi,date) VALUES(?,?,?,?)", (no, adi, soyadi, date))

        count += 1

        con.commit()

################################################################################################################
def liste():
    import fonk
    fonk.cls()

    #sql = "Select * from ogrenciler order by id asc"
    sql = "Select * from aktas_envanter_liste "
    oku=vt.execute(sql)

    x = 1
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("| NO | ID | ADI | SOYADI | DETAY  ")
    results=vt.fetchall()
    for row in results:

        date = row['location']
        date = date[:19]
        a = ("|")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        #print(a, x, a, row['barkod'], a, date, a, row['adi'], "", a, row['bilgisayar_adi'], "", a,row['serial'], a)
        print(x,a,row['status'],a,row['barkod'],a,row['officer'],a,row['name'],a,row['before_user'],a,row['computer_name'],a,row['type'],a,row['brand'],a,row['model'],a,row['serial'],a,row['cpu'],a,row['ram'],a,row['hdd'],a,row['ssd'],a,row['location'],a,row['os'],a,row['operation_date'],a,row['whodid'],a,row['note'])
        x = x + 1



    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    sql_total = "SELECT COUNT(*) FROM ogrenciler"
    vt.execute(sql_total)
    total = vt.fetchone()
    sum = total['COUNT(*)']

    # print("\n")
    print('Toplam =', sum, 'kayıt var.')

   ################################################################################################################
def cikis():
    print("\n")
    print("Programdan Çıkış yapılacak !")
    answer = input('Devam Etmek Istiyormusun ?[e(vet)/h(ayır)]:')

    if answer.lower().startswith("e"):

        import fonk
        fonk.cls()
        print("ok,Güle güle yine gel...Seviyoz seni !")

        exit()

    elif answer.lower().startswith("h"):

        print("ok,Takıl Bakalım...")

################################################################################################################
def tekkayit():
    import random
    from datetime import datetime
    adi = random.choice(['fatih', 'faruk', 'mehmet', 'serkan', 'ahmet'])
    soyadi = random.choice(['fatih', 'faruk', 'mehmet', 'serkan', 'ahmet'])

    no = random.randint(1, 99)
    date = str(datetime.now())
    vt.execute("INSERT INTO ogrenciler(adi,soyadi,date,no) VALUES('{a}','{b}','{c}','{d}') ". \
               format(a=adi, b=soyadi, c=date, d=no))
    #vt.execute("INSERT INTO ogrenciler (no,adi,soyadi,date) VALUES(?,?,?,?)", (no, adi, soyadi, date))
    con.commit()


###############################################################################################################




###############################################################################################################