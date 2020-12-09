from mevyesebze import MeyveSebze
from cerez import Cerez


urunListe=[]
with open("ornek2/urunler.txt","r") as dosya:
    urunListe=dosya.readlines()
    dosya.close()

for urun in urunListe:
    urun=urun.replace("\n","")
    urunL=urun.split(",")
    if (urunL[0]=="meyve" or urunL[0]=="sebze"):
        meyvesebze=MeyveSebze(urunL[0],urunL[1],urunL[3],urunL[2])
        meyvesebze.adrenkfiyatyaz(1)
    else:
        cerez=Cerez(urunL[1],urunL[2])
        cerez.adfiyatyaz(1)