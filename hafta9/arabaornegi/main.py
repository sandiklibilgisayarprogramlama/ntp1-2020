from araba import Araba
from yakitturu import YakitTuru

yakit1=YakitTuru()
yakit1.yakitadi="Dizel"
yakit1.yakitlitreucreti=6.5
yakit1.tum_bilgileri_yazdir()

araba1=Araba()
araba1.marka="Opel astra"
araba1.model=2020
araba1.yakit=yakit1
araba1.kmbasinayaktigilitre=0.2

print(araba1.araba_marka_dondur())
araba1.modelini_ekrana_yazdir()
print(araba1.kmyegöreyakitucretihesapla(100))
print("---------------------")
araba1.tum_bilgileri_yazdir()
