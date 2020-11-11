from karaktertip import KarakterTip
from silah import Silah
from karakter import Karakter

kilic=Silah()
kilic.silahad="Kılınç"
kilic.silahvurus=10

ok=Silah()
ok.silahad="Ok"
ok.silahvurus=7

yaya = KarakterTip()
yaya.tipadi="Yayalı Asker"
yaya.tipsilah=kilic

atli =KarakterTip()
atli.tipadi="Atlı okçu"
atli.tipsilah=ok

viking=Karakter()
viking.ad="viking savaşçısı"
viking.karakterTip=yaya

mogol = Karakter()
mogol.karakterTip=atli
print("Merhaba Hoşgeldin")
print("mogol ve viking savaşı burda olacak")
print("karakterini seç ve savaç")

while True:

    k=input("mogol için 1, viking için 2yı tuşla böylece savaççılar güç kullanabilisin")
    
    if k=="1":
        viking.karakterTip.can=viking.karakterTip.can-mogol.karakterTip.tipsilah.silahvurus
        print("vikjing kalan can",viking.karakterTip.can)
    elif k=="2":
        mogol.karakterTip.can=mogol.karakterTip.can-viking.karakterTip.tipsilah.silahvurus
        print("Mogol kalan can: ",mogol.karakterTip.can)
    else:
        continue

    if mogol.karakterTip.can <= 0:
        print("viking kazandı")
        break
    elif viking.karakterTip.can <=0:
        print("mogol kazandi")
        break