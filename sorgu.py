import sqlite3
con=sqlite3.connect('database.db') # Veritabanına Bağlan
con.row_factory=sqlite3.Row
vt=con.cursor() #Veritabanında İşlem yapabilmek için Cursor oluştur

import fonk

################################################################################################################

def delete(table_name, id):
    #print(table_name) # GELEN DEĞERİ GÖRMEK İÇİN
    #print(id) # GELEN DEĞERİ GÖRMEK İÇİN

    sq = 'select * from ogrenciler where id=?'
    kontrol = vt.execute(sq, (id,))
    pw = kontrol.fetchone()

    if (not pw):  # Kayıt Yoksa Burası
        print("Böyle Bir Kayıt YOK !!!")
    else:  # Kayıt varsa burası

################################################
# silinecek olan kayıdı göstermek için ...
        oku =vt.execute('select * from {tn} where id={did} '. \
                   format(did=id, tn=table_name))


        x = 1
        print("----------------------------------------------------------------------------------")
        print("| NO | ID  | TARIH               | ADI     | SOYADI  |  ")
        for verileri_cek in oku.fetchall():
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
    vt.execute("INSERT INTO ogrenciler (no,adi,soyadi,date) VALUES(?,?,?,?)", (no, adi, soyadi, date))
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

        adi = random.choice(
            ['fatih', 'faruk', 'mehmet', 'serkan', 'ahmet', 'barış', 'yusuf', 'merve', 'eda', 'mustafa', 'gokmen',
             'serdar', 'seckın', 'erhan', 'gülver', 'rasim', 'nazım', 'emre', 'hüseyin', 'ilker', 'sami'

                , 'serkan', 'onur', 'veysel', 'alper', 'hakan', 'harun', 'fikri', 'mesut', 'volkan', 'onur'])

        soyadi = random.choice(
            ['fatih', 'faruk', 'mehmet', 'serkan', 'ahmet', 'barış', 'yusuf', 'merve', 'eda', 'mustafa', 'gokmen',
             'serdar', 'seckın', 'erhan', 'gülver', 'rasim', 'nazım'])

        date = str(datetime.now())

        no = random.randint(1000, 9999)

        vt.execute("INSERT INTO ogrenciler (no,adi,soyadi,date) VALUES(?,?,?,?)", (no, adi, soyadi, date))

        count += 1

        con.commit()

################################################################################################################
def liste():
    import fonk
    fonk.cls()
    oku = vt.execute('Select * from ogrenciler order by id asc')

    x = 1
    print("----------------------------------------------------------------------------------")
    print("| NO | ID | ADI | SOYADI | DETAY  ")
    for verileri_cek in oku.fetchall():
        date = verileri_cek['date']
        date = date[:19]
        a = ("|")
        print("----------------------------------------------------------------------------------")

        print(a, x, a, verileri_cek['id'], a, date, a, verileri_cek['adi'], "", a, verileri_cek['soyadi'], "", a,
              verileri_cek['no'], a)
        x = x + 1
    print("----------------------------------------------------------------------------------")
    sum = vt.execute("SELECT COUNT(*) FROM ogrenciler").fetchone()[0]
    # print("\n")
    print('Toplam =', sum, 'kayıt var.')

    # import menu
    # import os
    # os.system('python menu.py') # go to gibi menüye gönmeyi sağlıyor #
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
    vt.execute("INSERT INTO ogrenciler (no,adi,soyadi,date) VALUES(?,?,?,?)", (no, adi, soyadi, date))
    con.commit()


###############################################################################################################




###############################################################################################################