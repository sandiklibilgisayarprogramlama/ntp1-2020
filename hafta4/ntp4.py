"""
import webbrowser as wb
from os import listdir
import ornek
import os

wb.open("www.google.com")

print(listdir())

import os
os.listdir()

import os as dosya
dosya.listdir()

from os import listdir,mkdir
listdir()



print(dir(os))


harddisk1isim="Wd"
harddisk1renk="siyah"
hardisk1boyut=500
harddisk1agirlik=300

harddisk2isim="seagate"
harddisk2renk="siyah"
hardisk2boyut=1024
harddisk2agirlik=240

harddisk3isim="samsung"
harddisk3renk="mavi"
hardisk3boyut=1024
harddisk3agirlik=240

harddisk4isim="beko"
harddisk4renk="mavi"
hardisk4boyut=1024
harddisk4agirlik=240

class Harddisk:
    isim=""
    renk="siyah"
    boyut=0
    agirlik=0

harddisk1=Harddisk()
harddisk2=Harddisk()
harddisk3=Harddisk()
harddisk4=Harddisk()
harddisk5=Harddisk()
harddisk6=Harddisk()
harddisk7=Harddisk()

harddisk3.renk="mavi"
print(harddisk3.renk)
"""



from ogrenci import Ogrenci

omer = Ogrenci()

omer.ad="Ömer"
omer.soyad="Gök"
omer.boy=1.75
omer.yas=20
omer.no="13809813761"


suleyman = Ogrenci()
suleyman.ad="Süleyman"
suleyman.boy="185"
suleyman.sacRengi="siyah"

suleyman.boy = "190"

print(suleyman.ad)