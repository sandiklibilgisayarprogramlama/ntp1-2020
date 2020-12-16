from uruntur import UrunTur
from pakettur import PaketTur
from urun import Urun

# ürün tür oluşturma
meyve=UrunTur(1,"meyve")
sebze=UrunTur(2,"sebze")
cerez=UrunTur(3,"Cerez")

# paket tür oluşturma
adet=PaketTur(1,"adet")
demet=PaketTur(2,"demet")
kg=PaketTur(3,"kg")

urunListe=[]
dosya="stok.txt"

print("**********************************")
print("stok takip programı v.0.1")
print("***********************************")
print(
"""hoşgeldiniz 
    stok goruntulemek için 1
    ürün eklemek için 2
    ürün silmek için 3
""")
def dosyayaYaz(urun):
    with open("stok.txt","a") as dosya:
        dosya.write(str(urun.id)+"|"+urun.ad+"|"+urun.aciklama+"|"+str(urun.pakettur.ad)+"|"+str(urun.uruntur.ad)+"|"+str(stok)+"|"+str(fiyat)+"\n")
        dosya.close()

def stokGoruntule():
    pass

def urunekle(ad,aciklama,fiyat,pakettur,uruntur,stok):
    paket=None
    urun=None
    if pakettur=="1":
        paket=adet
    elif pakettur=="2":
        paket=demet
    elif pakettur=="3":
        paket=kg

    if uruntur=="1":
        urun=meyve
    elif uruntur=="2":
        urun=sebze
    elif uruntur=="3":
        urun=cerez

    yUrun=Urun(ad,stok,aciklama,paket,urun,fiyat)
    dosyayaYaz(yUrun)
    print("ürün başarıyla eklendi. id: ",str(yUrun.id))

def urunsil():
    pass


while True:
    girilen=input("seçeneği giriniz")
    if girilen=="1":
        stokGoruntule()
    elif girilen=="2":
        ad=input("ad giriniz")
        aciklama=input("aciklama")
        fiyat=input("fiyat giriniz")
        print("adet için 1,demet için 2, kg için 3 e basınız")
        pakettur=input("pakettur giriniz")
        print("meyve için 1,sebze için 2, cerez için 3 e basınız")
        uruntur=input("uruntur giriniz")
        stok=input("stok giriniz")
        urunekle(ad=ad,aciklama=aciklama,fiyat=fiyat,pakettur=pakettur,uruntur=uruntur,stok=stok)
    elif girilen=="3":
        urunsil()
    else:
        print("yanlış seçenek girdiniz")





