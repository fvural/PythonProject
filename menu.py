
import vt
con=vt.con
vt=vt.vt


def cls():
    import os
    os.system('cls')
    return



def menu():
    global m
    sum=vt.execute("SELECT COUNT(*) FROM ogrenciler").fetchone()[0]
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
    return  m

m=menu()

