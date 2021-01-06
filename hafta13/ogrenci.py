"""
author: caner balim
date: 30.12.2020
desc: ogrenci nesnelerinin ozelliklerinin bulundugu bir sinif
"""
class Ogrenci:
    __ad=None
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
        self.__ad=ad
        self.__soyad=soyad
        self.__tcno=tcno
        self.__ad=str(self.__ad).capitalize()

    def adyaz(self):
        print(self.__ad)
    
    def adDegistir(self,ad):
        """
        bu metodu ogrenci adi değiştirmekte kullanınız.

        Args:
            ad ([type]): [description]
        """
        self.__ad=ad
    
    def soyad_degistir(self,soyad):
        self.__soyad=soyad