liste = ['bursa','ankara','istanbul','izmir']

liste_yeni = str(liste)[:-1]
liste_son = liste_yeni[1:100]

print(liste_son)


birlikte_liste = ",".join(map(lambda x: str.format("'{}'",x), liste))

print(birlikte_liste)

global Liste = []
def liste_filtre():

    a=input("gir:")
    Liste.append(a) #Mehmet verisin ekliyoruz.
    print(Liste)

liste_filtre()
liste_filtre()
liste_filtre()
print(Liste)