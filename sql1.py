#v3
'''
conn = MySQLdb.connect (host = "sql302.byethost6.com",
                        user = "b6_20276654",
                        passwd = "159753",
                        db = "b6_20276654_1")
'''

# db yada *database diye kullanılsın...

import sqlite3
baglanti=sqlite3.connect('veriler.db')
#baglanti=sqlite3.connect('\\aktdesktop008\Programlar\veritabani\veriler.db')
baglanti.row_factory=sqlite3.Row
veritabani_sec=baglanti.cursor()
#baglantikapatmavekaydetme.

import random
from datetime import datetime

def cls():
    import os
    os.system('cls')
    return

def menu():
    sum=veritabani_sec.execute("SELECT COUNT(*) FROM ogrenciler").fetchone()[0]
    print("\n")
    print('Toplam  = ',sum,'kayıt var.')

    cls()
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
    return m

m=menu()



if m==1:

    oku=veritabani_sec.execute('Select * from ogrenciler order by id asc')

    x=1
    print("----------------------------------------------------------------------------------")
    print("| NO | ID | ADI | SOYADI | DETAY  ")
    for verileri_cek in oku.fetchall():
        a=("|")
        print("----------------------------------------------------------------------------------")

        print(a,x,a,verileri_cek['id'],a,verileri_cek['adi'],"",a,verileri_cek['soyadi'],"",a,verileri_cek['no'],a,verileri_cek['date'])
        x=x+1
    print("----------------------------------------------------------------------------------")
    sum=veritabani_sec.execute("SELECT COUNT(*) FROM ogrenciler").fetchone()[0]
    #print("\n")
    print('Toplam =',sum,'kayıt var.')


elif(m==2):
    '''
    veriekleme
    '''

    adi=input("Ad=")
    soyadi=input("Soyadı=")
    no=random.randint(1,99)

    #ekle=veritabani_sec.execute("insertintoogrenciler(ogrenci_no,adi,soyadi)VALUES('1234',?,?)",(adi,soyadi))
    #ekle=veritabani_sec.execute("insertintoogrenciler(ogrenci_no,adi,soyadi)VALUES('1234','fatih','vural')")
    veritabani_sec.execute("INSERT INTO ogrenciler (ogrenci_no,adi,soyadi) VALUES(?,?,?)",(no,adi,soyadi))
    '''
    if(adi!=''):
    print("AdıAlanıBoşBırakılamaz")#sanırımbununiçinfonktanımlanacak
    exit()
    #adi=input("Ad=")
    '''
elif(m==3):
    print(m)

elif(m==4):

    #bak=str(input('[SILME] Silinecek Kayıt Numarasını Giriniz:'))
    bak=input('[SILME] Silinecek Kayıt Numarasını Giriniz:')

    #kayıtyoksahatamesajı
    #kayıtvarsaeminmisinizdiyesorsun
    sq='select * from ogrenciler where id=?'
    kontrol=veritabani_sec.execute(sq,(bak,))
    pw = kontrol.fetchone()

    if (not pw):  #Kayıt Yoksa Burası
        print("Böyle Bir Kayıt YOK !!!")
    else: # Kayıt varsa burası
        print("\n")
        print("UYARI=",bak," Nolu Kayıt silinecek !!!")
        answer = input('[e(vet)/h(ayır)]:')
        if answer.lower().startswith("e"):  # EVET Durumunda Yapılacak
            cls()
            print(bak," nolu Kayıt silindi...")
            sql = 'delete from ogrenciler where id=?'
            sil = veritabani_sec.execute(sql, (bak,))


        elif answer.lower().startswith("h"):  # HAYIR Durumunda Yapılacak
            print("silme işlemi iptal edildi...")
            exit()
        elif answer.lower().startswith(""):  # (answer=""): # BOŞ Bırakılırsa Yapılacak #
            print("Boş Bırakılamaz...!")

        else:
            print("Soruya e(vet) yada h(ayır) seklinde cevap veriniz...")


#menu()

elif(m==5):

    like=input('Aranacak Kelime:')

    #like='fat'
    print(like)
    oku=veritabani_sec.execute("Select * from ogrenciler where adi like ?",('%'+like+'%',))

    x=1
    print("----------------------------------------------------------------------------------")
    print("| NO | ID | ADI | SOYADI | DETAY  ")
    for verileri_cek in oku.fetchall():
        a=("|")
        print("----------------------------------------------------------------------------------")

        print(a,x,a,verileri_cek['id'],a,verileri_cek['adi'],"",a,verileri_cek['soyadi'],"",a,verileri_cek['no'],a,verileri_cek['date'])
        x=x+1


    sum=veritabani_sec.execute("SELECT COUNT(*) FROM ogrenciler").fetchone()[0]
    print("\n")
    print('Toplam  = ',sum,'kayıt var.')


elif(m==6):
#print(m)

    answer=input('Devam Etmek Istiyormusun ?[e(vet)/h(ayır)]:')
    if answer.lower().startswith("e"):
        cls()
        print("ok,TakılBakalım..")
        menu()
    elif answer.lower().startswith("h"):
        print("ok,GüleGüle...TekrarGel...")
        exit()
elif(m==9):
    cls()
elif(m==99):
    print("\n")
    print("UYARI= Tüm kayıtlar silinecek !!!")
    answer=input('[e(vet)/h(ayır)]:')
    if answer.lower().startswith("e"): # EVET Durumunda Yapılacak
        cls()
        print("Tüm Kayıtlar temizlendi...")
        sql='delete from ogrenciler'
        sil=veritabani_sec.execute(sql)

    elif answer.lower().startswith("h"): # HAYIR Durumunda Yapılacak
        print("Tümünü silme işlemi iptal edildi...")
        exit()
    elif answer.lower().startswith(""): #(answer=""): # BOŞ Bırakılırsa Yapılacak #
        print("Boş Bırakılamaz...!")

    else:
        print("Soruya e(vet) yada h(ayır) seklinde cevap veriniz...")

elif(m==100): # TEK Otomatik Kayıt Girer
    adi=random.choice(['fatih','faruk','mehmet','serkan','ahmet'])
    soyadi=random.choice(['fatih','faruk','mehmet','serkan','ahmet'])
    no=random.randint(1,99)
    date = str(datetime.now())
    veritabani_sec.execute("INSERT INTO ogrenciler (no,adi,soyadi,date) VALUES(?,?,?,?)",(no,adi,soyadi,date))

elif(m==101):
    count=0
    while count < 20 :
        #print(count)
        #count+=1
        adi=random.choice(['fatih','faruk','mehmet','serkan','ahmet','barış','yusuf','merve','eda','mustafa','gokmen','serdar','seckın','erhan','gülver','rasim','nazım','emre','hüseyin','ilker','sami'
                              , 'serkan','onur','veysel','alper','hakan','harun','fikri','mesut','volkan','onur'])
        soyadi=random.choice(['fatih','faruk','mehmet','serkan','ahmet','barış','yusuf','merve','eda','mustafa','gokmen','serdar','seckın','erhan','gülver','rasim','nazım'])


        date = str(datetime.now())
        no=random.randint(1000,9999)
        veritabani_sec.execute("INSERT INTO ogrenciler (no,adi,soyadi,date) VALUES(?,?,?,?)", (no,adi,soyadi,date))
        count+=1
elif m.lower().startswith(""): #(answer=""):
        print("Boş Bırakılamaz...!")
else:
    cls()
    print("Lütfen Menudeki Seceneklerden Seciniz")
    menu()


########################################################
baglanti.commit()
baglanti.close()
########################################################
#ekrantemizlemek
#programdançıkış

#ifilegelenmenütespiti


#nem.ısıvsprogramı
#sqliuzakolanabağlanma
