from meyve import Meyve

elma=Meyve("elma starking","kırmızı",10,"yaz")
armut=Meyve("Armut","yeşil","dört mevsim",8)
seftali=Meyve("seftali","turuncu",10,"yaz")

elma.adiEkranaYaz()
armut.adiEkranaYaz()
print(seftali.fiyatHesapla(3))
print(elma.cins)