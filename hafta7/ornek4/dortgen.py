class Dortgen:
    kenar1=0
    kenar2=0

    def alanHesapla(self,sekilad):
        if (sekilad=="kare"):
            return self.kenar1**2
        elif(sekilad=="dikdortgen"):
            return self.kenar1*self.kenar2
        else:
            return 0


    def cevreHesapla(self,sekilad):
        if sekilad=="kare":
            return self.kenar1*4
        elif sekilad=="dikdortgen":
            return (self.kenar1+self.kenar2)*2
        else:
            return 0