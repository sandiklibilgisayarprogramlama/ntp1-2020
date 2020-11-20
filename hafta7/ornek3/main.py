"""
parametre olarak ad ve soyad girilen bir fonksiyon tanımlayıp ad ın sadece ilk harfini büyük
soyadın ise hepsini büyük yapan fonksiyonu yazınız.

edebiyatın başlangıcı -> capitalize -> Edebiyat başlangıcı
edebiyatın başlangıcı -> title -> Edebiyat Başlangıcı
edebiyatın başlangıcı -> upper -> EDEBİYAT BAĞLANGICI


"""

def adsoyadYazdir(ad,soyad):
    print(str(ad).title()," ",str(soyad).upper())


def adsoyadbicimlendirDondur(ad,soyad):
    return str(ad).title()+" "+str(soyad).upper()

#adsoyadAyarla("ahmet veli","uzun")
