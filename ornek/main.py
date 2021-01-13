from otoyikama import Yikamaci

yikamaci=Yikamaci("Sürat Yıkama","sandıklı afyon","randevusaat.txt")


print("oto yıkama rezervasyon programı")
print("Aşağıda listelenen boş randevulardan birinin saatini yazınız")
yikamaci.get_randevu_list()
print()
kisiad=input("adınızı yazınız")
rsaat=input("Randevu saatini giriniz")
yikamaci.set_randevu_list(rsaat,kisiad)
