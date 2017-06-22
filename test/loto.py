"""
Sayısal Loto
"""

#!/usr/bin/env python
#-*- coding:utf-8-*-
from tkinter import* #python 3,5 ve üzeri V kullanıyorsan Tkinter'i Küçük harfle yaz tkinter olarak
import random
pencere=Tk()
pencere.title("Sayısal Loto...") #pencere başlığı
pencere.geometry("400x100+60+200")#pencerenin boyutu
pencere.resizable(width=FALSE,height=FALSE)#pencer enin boyutlanmasını engeller

class Cekilis(object):
    def __init__(self):
        self.araclar()

    def araclar(self):
        self.buton=Button(text="Çekiliş",command=self.kodlar)
        self.buton.pack()
        self.etiket=Label(text="RastGele...",fg="blue",font="Comic 15 bold")
        self.etiket.pack()
    def kodlar(self):
        liste=[]
while len(liste)!=6: #kaçtane sayı yazmasını istiyorsan
    a=random.randint(1,49) #hangi sayılar arasında olmasını istiyorsan
    if a not in liste:
        liste.append(a)
        self.etiket["text"]=liste


uyg=Cekilis()
mainloop()#döngü yapak pencerenin
#devamlı olarak ekranda kalmasını sağlıyor
"""
mainloop() komutu yazılmaz ise
program yine calısır ama pencereyi ekranda göremeyiz.
"""