import sql_list

#sql_list.list("test")
#sql_list.list("ogrenciler")

colums = ["no","adi","soyadi","date"]
#print(colums)
liste_say = len(colums)
a = 0
b = []
while (a < liste_say):

    if a==0:
        x1 = ""
    else :
        x1 = ","

    x2 = colums[a]

    y=x1+x2
    b.append(colums[a])

    colums[a] = colums[a]
    a = a + 1
print(b)

liste_say = len(colums)
a=0
while(a<liste_say):
    x1 = "veri['"
    x2 = colums[a]
    x3 = "']"
    x=x1+x2+x3
    print(x)

    a = a + 1