class Util:
    @staticmethod
    def kareal(sayi):
        return sayi**2
    
    @staticmethod
    def ucegoremodal(sayi):
        return sayi%3
    
    @staticmethod
    def adsoyadduzenle(adsoyad):
        gelen=adsoyad.lower()
        gelendizi=gelen.split(" ")
        geriyedonecek=""
        for i,k in enumerate(gelendizi):
            gelendizi[i]=str(gelendizi[i]).strip()
            if gelendizi[i] == gelendizi[-1]:
                gelendizi[i]=gelendizi[i].upper()
            else:
                gelendizi[i]=gelendizi[i].capitalize()
        
            geriyedonecek=geriyedonecek+" "+gelendizi[i]
        
        return geriyedonecek


if __name__ == "__main__":
    girilen = input("ad soyad giriniz")
    print(Util.adsoyadduzenle(girilen))