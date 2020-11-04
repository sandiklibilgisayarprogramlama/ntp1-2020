from ogrenci import Ogrenci
from ders import Ders


if __name__ == "__main__":
    ogrenci1 = Ogrenci()
    ogrenci1.ad="Ahmet"
    ogrenci1.yas=19
    ogrenci1.soyad="Uzun"
    ogrenci1.dogumyeri="Afyonkarahisar"
    ogrenci1.dogumtarihi = "31.01.2003"
    ogrenci1.bolum="Bilgisayar Programcılığı"

    print("ad:", ogrenci1.ad)
    print("soyad:", ogrenci1.soyad)
    print("yas:",ogrenci1.yas)

    ogrenci2=Ogrenci()
    ogrenci2.ad="Veli"
    ogrenci2.yas=20
    ogrenci3=Ogrenci()
    ogrenci100=Ogrenci()

    if ogrenci2.yas>ogrenci1.yas:
        print(ogrenci2.ad," büyük ",ogrenci1.ad)
    else:
        print(ogrenci1.ad," büyük ",ogrenci2.ad)
    
    mat = Ders()
    mat.dersadi="Matematik 1"
    mat.dersbolumu="Bilgisayar Prog"
    mat.dershocaadi="Hasan"
    mat.dersicerik="Genel matematik bilgisinin öğretildiği derstir."
    mat.derskredi=3.5
    mat.derslabadi="Lab 104"
    mat.derssaati="14:00"

    turkce = Ders()
    turkce.dersadi="Türkçe 1"
    turkce.dersbolumu="Bilgisayar prog"
    turkce.dershocaadi="Ahmet"
    turkce.dersicerik="Temel dil bilgisi"
    turkce.derskredi=2
    turkce.derslabadi="Lab 105"
    turkce.derssaati="10:00" 

    ingilizce = Ders()
    ingilizce.dersadi="ingilizce 1"
    ingilizce.dersbolumu="Bilgisayar prog"
    ingilizce.dershocaadi="Ayşe"
    ingilizce.dersicerik="Temel ingilizce bilgisi"
    ingilizce.derskredi=3
    ingilizce.derslabadi="Lab 100"
    ingilizce.derssaati="10:00" 

    ogrenci1.dersler=[mat,turkce,ingilizce]
    ogrenci2.dersler=[turkce]

    for i in ogrenci1.dersler:
        print(i.dersadi)
    
 
        