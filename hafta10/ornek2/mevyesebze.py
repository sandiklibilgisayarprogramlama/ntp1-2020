class MeyveSebze:
    
    def __init__(self,kategori,ad,kgfiyat,renk):
        self.ad=ad
        self.kgfiyat=kgfiyat
        self.renk=renk
        self.kategori=kategori
    
        
    def adrenkfiyatyaz(self,alinankg):
        """
        bu fonksiyon alınan kg ve renk ve meyve adını ekrana yazar
        """
        print(self.ad+"-"+self.renk+"-"+"toplam tutar:"+alinankg*self.kgfiyat)
