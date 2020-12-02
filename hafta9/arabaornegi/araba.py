"""
Araba nesnesini yazılım ortamına özellikleri ve fonksiyonları ile aktarınız. 
(özellik: tekersayisi, silindir,marka,model )
"""

class Araba:
    marka=""
    model=0
    yakit=None
    kmbasinayaktigilitre=0

    # markasını döndüren metot
    def araba_marka_dondur(self):
        return self.marka
    
    def kmyegöreyakitucretihesapla(self,gidilenkm):
        return self.yakit.yakitlitreucreti*self.kmbasinayaktigilitre*gidilenkm
    
    def modelini_ekrana_yazdir(self):
        print(self.model)

    def tum_bilgileri_yazdir(self):
        print(self.marka)
        print(self.model)
        print(self.yakit.yakitadi)
        print(self.yakit.yakitlitreucreti)
        print(self.kmbasinayaktigilitre)

    

