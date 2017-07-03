'''
import sqlite3
con=sqlite3.connect('database.db') # Veritabanına Bağlan
con.row_factory=sqlite3.Row
vt=con.cursor() #Veritabanında İşlem yapabilmek için Cursor oluştur
'''
import pymysql
con = pymysql.connect(host = '127.0.0.1', port = 3388, user = 'root', passwd = '159753', db = 'python', charset='utf8')
vt = con.cursor(pymysql.cursors.DictCursor)


import fonk
#


################################################################################################################
def tablo():
    #global m
    #sum=vt.execute("SELECT COUNT(*) FROM ogrenciler").fetchone()[0]


    sql_total = "SELECT COUNT(*) FROM aktas_envanter_liste"
    vt.execute(sql_total)
    total = vt.fetchone()
    sum = total['COUNT(*)']




    print("\n")
    print("==================================")
    print("|           |MENU|               |")
    print("==================================")
    print("| [1]Listele  ","(",sum,")","            |")
    print("| [2]VeriEkle                    |")
    print("| [3]Güncelleme                  |")
    print("| [4]Silme                       |")
    print("| [5]Arama                       |")
    print("| [6]Çıkış                       |")
    print("| [7]Detay                       |")#detay+silmeopsiyonu+güncellemeopsiyonu...
    print("==================================")
    m=float(input("Hangi Islemi Yapmak Istıyorsun?="))
    #m=input("Hangi Islemi Yapmak Istıyorsun?=")
    return m



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
    #sql = "Select * from aktas_envanter_liste where location in ('DOSB','KOSB','OSB')"
    #oku=vt.execute(sql)

    durumu=['Boşta','Kontrol']
    durumu = ",".join(map(lambda x: str.format("'{}'", x), durumu))


    liste=['KOSB','DOSB']
    #liste=str(liste)
    liste_yeni=str(liste)[:-1]
    l=liste_yeni[1:]


    table_name = "aktas_envanter_liste"
    oku=vt.execute("select * from aktas_envanter_liste where  status in ({d})". \
               format(tn=table_name,l1=l,d=durumu))

    sari="\033[1;33;40m "
    kirmizi="\033[1;31;40m "
    mavi="\033[1;34;40m "
    yesil="\033[1;32;40m "
    magenta="\033[1;35;40m "
    normal = "\033[1;37;40m "

    d1 = sari + "aktas" + "\33"+normal
    d2 = kirmizi + "fatih" + "\33"+normal
    d3 = mavi + "vural" + "\33"+normal
    d4 = yesil + "it" + "\33"+normal
    d5 = magenta + "helpdesk" + "\33"+normal





    name1="AD"
    name1 = name1 + (10 - len(name1)) * ' '
    name1 = name1[:10]

    x = 1
    print("====================================================================================================================================================================")
    print("000  |",name1,"s")
    results=vt.fetchall()
    for row in results:

        date = row['location']
        date = date[:19]
        a = (" | ")

        if x<10:
            y="00"+str(x)
        elif x<100:
            y="0"+str(x)
        else:
            y=x




        status=row['status']
        status = status + (10 - len(status)) * ' '
        if (row['status'] == "Kullanımda"):
            status = yesil + status +normal
        elif (row['status'] == "Boşta"):
            status = sari + status +normal


        barkod=row['barkod']
        barkod = barkod + (16 - len(barkod)) * ' '
        barkod1 = sari + barkod + "\33" + normal


        officer=row['officer']
        if officer != "X":
            officer="-"
        officer = officer + (1 - len(officer)) * ' '
        #officer = (officer + " ")[:3]


        name=row['name']
        name = name + (30 - len(name)) * ' '
        name1 = kirmizi + name + "\33" + normal
        name=name[:40]


        before_user=row['before_user']
        before_user="{:<20}".format(before_user)
        before_user = before_user[:20]


        computer_name=row['computer_name']
        computer_name = computer_name + (15 - len(computer_name)) * ' '
        computer_name1 = mavi + computer_name + "\33" + normal


        location=row['location']
        location = location + (5 - len(location)) * ' '
        if (row['location'] == "BOSB"):
            location = yesil + location +normal
        elif(row['location'] == "OSB"):
            location = kirmizi + location +normal
        elif (row['location'] == "DOSB"):
            location = mavi + location +normal


        location1 = sari + location + "\33" + normal

        operation_date=row['operation_date']
        operation_date = operation_date + (15 - len(operation_date)) * ' '
        operation_date1 = yesil + operation_date + "\33" + normal


        model=row['model']
        serial=row['serial']
        cpu=row['cpu']
        ram=row['ram']
        hdd=row['hdd']
        ssd=row['ssd']
        os=row['os']
        whodid=row['whodid']
        note=row['note']

        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        '''
        if x%2==0:
            print(sari)
            print(y, a, status, a, barkod, a, officer, a, name, a, before_user, a, computer_name, a, location, a,
                  operation_date)

        else:
            print(normal)
            print(y, a, status, a, barkod, a, officer, a, name, a, before_user, a, computer_name, a, location, a,
                  operation_date)

        '''
        print(y, a, status, a, barkod, a, officer, a, name, a, before_user, a, computer_name, a, location, a,
              operation_date)

        x = x + 1



    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    sql_total = "SELECT COUNT(*) FROM aktas_envanter_liste"
    vt.execute(sql_total)
    total = vt.fetchone()
    sum = total['COUNT(*)']

    # print("\n")
    print('\033[1;31;40mToplam =', sum, 'kayıt var.\033')


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