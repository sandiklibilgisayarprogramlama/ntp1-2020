"""
author: caner balim
date: 30.12.2020
desc: ogrenci nesnelerinin ozelliklerinin bulundugu bir sinif
"""
class Ogrenci:
    _ad=None
    __soyad=None
    __tcno=None
    """
    parameters:

    ad (str): ogrenci ismi
    soyad (str): ogrenci soyadi
    tcno (str): ogrenci id

    returns:
    None
    """
    def __init__(self,ad,soyad,tcno):
        self._ad=ad
        self.__soyad=soyad
        self.__tcno=tcno

    def adyaz(self):
        print(self._ad)