import random
class Urun:
    id= random.randint(1,100) 
    def __init__(self,ad,stok,aciklama,pakettur,uruntur,fiyat) :
        self.ad=ad
        self.stok=stok
        self.aciklama=aciklama
        self.pakettur=pakettur
        self.uruntur=uruntur
        self.fiyat=fiyat
    
    def urunBilgiYazdir(self):
        print(self.id)
        print(self.ad)
        print(self.aciklama)
        print(self.pakettur)
        print(self.uruntur)
        print(self.fiyat)
        print(self.stok)
    
    

        