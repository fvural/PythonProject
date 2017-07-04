'''
import vt
con=vt.con
vt=vt.vt
'''
#
'''
import sqlite3
con=sqlite3.connect('database.db') # Veritabanına Bağlan
con.row_factory=sqlite3.Row
vt=con.cursor() #Veritabanında İşlem yapabilmek için Cursor oluştur
'''
import pymysql
con = pymysql.connect(host = '127.0.0.1', port = 3388, user = 'root', passwd = '159753', db = 'python')
vt = con.cursor(pymysql.cursors.DictCursor)

########################################################################################################################
import random
from datetime import datetime
import sorgu1


z=Liste = []
z = ",".join(map(lambda x: str.format("'{}'", x), z))
print(z)

def menu():
    #sum=vt.execute("SELECT COUNT(*) FROM ogrenciler").fetchone()[0]

    m=sorgu1.tablo()

    if (m == 1):

        print("\033[1;36;40m3 \033 ")

        sorgu1.liste()

        print("\033[0;37;40m \n")

        print(Liste)

        menu()


    elif (m == 2):

        sorgu1.insert()
        menu()
    elif (m == 3):
        print(m)
    elif (m == 4):

        bak = input('[SILME] Silinecek Kayıt Numarasını Giriniz:')
        sorgu1.delete("ogrenciler", bak)

    elif (m == 5):
        
        sorgu1.ara()
        menu()

    elif (m == 6):
        
        sorgu1.cikis()
        menu()

    elif (m == 9):
        cls()

    elif (m == 99):
        
        sorgu1.delall()
        menu()

    elif (m == 100):  # TEK Otomatik Kayıt Girer
        
        sorgu1.tekkayit()
        menu()

    elif (m == 101):
        
        sorgu1.insertall()
        menu()
    elif (m == 999):
        def liste_filtre():

            a = input("gir:")
            Liste.append(a)  # Mehmet verisin ekliyoruz.

        liste_filtre()
        liste_filtre()
        liste_filtre()
        print(Liste)
    elif m.lower().startswith(""):  # (answer=""):

        print("Boş Bırakılamaz...!")

    else:

        cls()

        print("Lütfen Menudeki Seceneklerden Seciniz")

    menu()


def altmenu():
    menu()
    '''
    alt_menu_secim = input("Ana menüye dönmek için 0 - Çıkış için 1 \n"
                           "İşlem kodu:")
    if alt_menu_secim == "0":

        menu()
    elif alt_menu_secim == "1":
        exit()
    else:
        print("Lütfen geçerli bir işlem kodu giriniz.")
    '''

menu()
########################################################
con.commit()
con.close()
########################################################

#programdançıkış

