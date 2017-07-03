liste = ['bursa','ankara','istanbul','izmir']

liste_yeni = str(liste)[:-1]
liste_son = liste_yeni[1:100]

print(liste_son)


birlikte_liste = ",".join(map(lambda x: str.format("'{}'",x), liste))

print(birlikte_liste)

Liste = ['Ali']
input("gir:")
Liste.append('Mehmet') #Mehmet verisin ekliyoruz.
print(Liste)