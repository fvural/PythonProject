'''
import vt
con=vt.con
vt=vt.vt
'''


import sqlite3
con=sqlite3.connect('database.db') # Veritabanına Bağlan
con.row_factory=sqlite3.Row
vt=con.cursor() #Veritabanında İşlem yapabilmek için Cursor oluştur
'''
import pymysql
db = pymysql.connect(host = '127.0.0.1', port = 3388, user = 'root', passwd = '159753', db = 'python')
vt = db.cursor(pymysql.cursors.DictCursor)
'''

########################################################################################################################
import random
from datetime import datetime
import sorgu

def menu():
    global m
    #sum=vt.execute("SELECT COUNT(*) FROM ogrenciler").fetchone()[0]

    '''
    sorgu1=vt.execute("SELECT COUNT(*) FROM ogrenciler")
    count=sorgu1.fetchone()
    sum=count[0]
    '''
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

    if (m == 1):

        sorgu.liste()
        menu()
    elif (m == 2):

        sorgu.insert()
        menu()
    elif (m == 3):
        print(m)
    elif (m == 4):

        bak = input('[SILME] Silinecek Kayıt Numarasını Giriniz:')
        sorgu.delete("ogrenciler", bak)

    elif (m == 5):
        
        sorgu.ara()
        menu()

    elif (m == 6):
        
        sorgu.cikis()
        menu()

    elif (m == 9):
        cls()

    elif (m == 99):
        
        sorgu.delall()
        menu()

    elif (m == 100):  # TEK Otomatik Kayıt Girer
        
        sorgu.tekkayit()
        menu()

    elif (m == 101):
        
        sorgu.insertall()
        menu()

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

