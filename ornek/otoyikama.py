class Yikamaci():
    def __init__(self,ad,adres,randevu_txt_ad):
        self._yikamaci_ad=ad
        self._yikamaci_adres=adres
        randevu_liste=[]
        with open(randevu_txt_ad,"r") as f:
            randevu_liste=f.readlines()
            f.close()
        self._randevu_listesi=randevu_liste
    
    def set_randevu_list(self,randevu_saati,randevu_bilgi):
        basariliMI=False
        yeni_belge=[]
        for i in self._randevu_listesi:
            if i.split("-")[0] == randevu_saati:
                if i.split("-")[1]=="\n":
                    i=randevu_saati+"-"+randevu_bilgi+"\n"
                    print("Sayın",randevu_bilgi,"randevunuz istediniz saat olan",randevu_saati, "için ayarlanmıştır.")
                    basariliMI=True
                else:
                    print("Üzgünüz istediğiniz randevu saati dolu")
            yeni_belge.append(i)
        if basariliMI:
            basariliMI=False
            open("randevusaat.txt","w").writelines(yeni_belge)


    def get_randevu_list(self):
        for i in self._randevu_listesi:
            print(i,end="")


