class Ogrenci:
    ad=""
    OKUL_AD="Sandıklı MYO"

    def __init__(self,ad,soyad,yas,ogrno) :
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.ogrno=ogrno

    def adiEkranaYaz(self):
        print(self.ad+" "+self.soyad)
    
    @classmethod
    def okulAdiYazdir(cls):
        print(cls.OKUL_AD)

if __name__ == "__main__":
    ogrenci=Ogrenci("ahmet","uzun",12,"13182371")
    print(dir(ogrenci))
    Ogrenci.okulAdiYazdir()