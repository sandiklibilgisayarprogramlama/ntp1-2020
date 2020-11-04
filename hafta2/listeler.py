"""
liste = [12,12,32,44,45,"dasd"]
for eleman in liste:
    print(eleman)


liste2 = list()  #[]
kelime="merhaba"
print(len(liste2))

kelimeListe = list(kelime)
print(kelimeListe)


kelime2="merhaba Dünya"

son karakter -1, len(kelime)-1

print(kelime2[len(kelime2)-1])

meyveler = ["elma","armut","çilek","şeftali"]
print(meyveler[-2])
print("---------------------------")
for meyve in meyveler:
    print(meyve)

print(meyveler[2:3])

[soru] ahmet poşete sevdiği meyvelerden ekleyip spor sonrası yemek istiyor. Daha sonra yanlışlıkla sevmediği
    armut meyvesinde poşete yanlışlıkla koydugunu görüyor. poşetten armutu çıkarıp yerine elma koymak istiyor.
    Bu örneği listelerde gösteriniz.


poset = ["armut","muz","çilek","üzüm"]

print(poset)
print("----------------------")
poset[0]="elma"
print(poset)


for i,k in enumerate(poset):
    if poset[i]=="armut":
        poset[i]="elma"

print(poset)

poset.append("kavun") # poset+["kavun"]
print(poset)


poset1=["armut","elma"]

poset2 = ["kavun","karpuz","elma"]

tumPoset = poset1+poset2
print(tumPoset)

del poset1
print(poset1)
tumPoset.remove("elma")
print(tumPoset)
print(tumPoset.index("elma"))


print(tumPoset)
tumPoset.insert(1,"muz")
print(tumPoset.count("elma"))
print(tumPoset)

yeniListe=[]
for eleman in tumPoset:
    if eleman!="elma":
        yeniListe.append(eleman)

print(yeniListe)

tumPoset.remove("elma")

del tumPoset[0]
"""

"""
['a','h','m','e','t'] listeden str ye çevirme 

ahmet = ['a','h','m','e','t']
print(type(ahmet))
ahmetstr=""
for eleman in ahmet:
    ahmetstr+=eleman

print(ahmetstr)
print(type(ahmetstr))
"""

cepNumListe = ["5069032322","050690323","50690332","050690323","5069033331"]
""" yukarıdaki listedeki cep numaralarından geçerli olanları ekrana yazdırınız.
şart 1 başında 0 olmasını istemiyoruz
şart iki cep numarası uzunluğunun 10 olmasını istiyoruz
 """
for i in cepNumListe:
    if i[0]!="0" and len(i)==10:
        print(i)
""" 
adam asmaca basit

kişiye 5 hak verilsin
ve iki tane boşluk olsun
"""
import random
kelimeler = ["araba","gemi","motor","armut","elma","tursu"]
ind = random.randint(0,len(kelimeler)-1)
sorulacakKelime = kelimeler[ind]

boslukInd = random.randint(0,len(sorulacakKelime)-1)
kelimeCevap =sorulacakKelime
sorulacakKelimeList=list(sorulacakKelime)
sorulacakKelimeList[boslukInd]="_"

sorulacakKelime=""
for eleman in sorulacakKelimeList:
    sorulacakKelime+=eleman

print("aşağıdaki kelimeyi tahmin ediniz")
print(sorulacakKelime)
klavye = input("karakter giriniz")

if (klavye==kelimeCevap):
    print("tebrikler doğru yanıtı buldunuz")
else:
    print("yanlış karakter girdiniz")

print(kelimeCevap)
