class Meyve:
    cins=""

    # kurucu metod: sınıftan nesne türetildiğinde çalıştıralan ilk metoddur. initialize
    def __init__(self,ad,renk,kgFiyat,mevsim):
        self.ad=ad
        self.renk=renk
        self.kgFiyat=kgFiyat
        self.mevsim=mevsim

    def adiEkranaYaz(self):
        print(self.ad)
    
    def fiyatHesapla(self,alinankg):
        return self.kgFiyat*alinankg