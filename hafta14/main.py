from typing import Dict
from fikstur import Fikstur
from takim import Takim

benimtakimim=Takim("read madrid",30)

rakip1 = Takim("barcelona",27)
rakip2= Takim("Valencia",20)
rakip3=Takim("Deportivo",18)


takimimin_fiksturu=dict()
takimimin_fiksturu["12.01.2021 19:00"]=rakip1
takimimin_fiksturu["19.01.2021 20:00"]=rakip2
takimimin_fiksturu["23.01.2021 21:00"]=rakip3

t_fiktur=Fikstur(benimtakimim,takimimin_fiksturu)

t_fiktur.print_fikstur()

t_fiktur.yeni_mac_ekle("29.01.2021 20:00",Takim("Celta Vigo",15))

t_fiktur.print_fikstur()

"""
maç tarihi geçtikten sonra puanları kazanana göre güncelleyin ve bunu kapsüllemeye uygun bir şekilde yapın.
"""