"""[summary]
Dortgen adında bir sınıf oluşturup içerisine kenar1,kenar2 özellikleri ve
alanHesapla, çevrehesapla metodları oluşturunuz. Daha sonra main sınıfında iki tane örnek tanımlayıp
ornelerin cevre ve alanlarını ekrana yazdırınız.  
"""

from dortgen import Dortgen

kare = Dortgen()
kare.kenar1=int(input("kare kenar gir"))
print("Karenin alanı",kare.alanHesapla("kare"))
print("Karenin çevresi",kare.cevreHesapla("kare"))


dikdortgen= Dortgen()
dikdortgen.kenar1=int(input("dikdortgen kenar 1 gir"))
dikdortgen.kenar2=int(input("dikdortgen kenar 2 gir"))
print("dikdörtgen alan",dikdortgen.alanHesapla("dikdortgen"))
print("dikdörtgen çevresi",dikdortgen.cevreHesapla("dikdortgen"))