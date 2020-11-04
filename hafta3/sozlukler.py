
sozluk ={} # boş sözlük
# sozluk={anahtar:deger}
sozluk={"soyad":"uzun","ad":"ahmet","yas":10}

print(sozluk["yas"])

print(type(sozluk))

"""
liste
for eleman in liste:
    pass
sozluk 
for anahtar,deger in sozluk.items():
    pass

"""

for a,d in sozluk.items():
    print(a," ",d)

sozluk2 = {}
sozluk2 = dict()

# sozluk[anahtar] 

# deger değiştirme
# listt[0]="dsada"
# sozluk[anahtar]="dada"
sozluk["ad"]="hüseyin"
sozluk["soyad"]="işler"
sozluk["yas"]=20

for a,d in sozluk.items():
    print(a," ",d)

sozluk.pop("yas")
print("-------------------")
for a,d in sozluk.items():
    print(a," ",d)

print("--------------------------")
kisi = {"ad":"veli","soyad":"uzun"}
"""
internet sitesine üye olan veli ad ve soyadını küçük yazmıştır. Programcı ise bu eksikliği düzeltmek
istemektedir.
bilgilerden ad' ın sadece ilk harfinin büyük soyadın ise hepsinin büyük olmasını sağlayınız.
"""
print(kisi["ad"]+" "+kisi["soyad"])

kisi["ad"]=kisi["ad"].capitalize()
kisi["soyad"]=kisi["soyad"].upper()

print(kisi["ad"]+" "+kisi["soyad"])