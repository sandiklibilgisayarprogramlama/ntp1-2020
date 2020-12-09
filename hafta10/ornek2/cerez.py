class Cerez:
    def __init__(self,ad,kgfiyat) :
        self.ad=ad
        self.kgfiyat=kgfiyat
    
    def adfiyatyaz(self,alinankg):
        """
        bu fonksiyon alınan kg ve çerez adını ekrana yazar
        """
        print(self.ad+"-"+"toplam tutar:"+alinankg*self.kgfiyat)