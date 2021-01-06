class Takim:
    def __init__(self,ad,puan) :
        self._ad=ad
        self._puan=puan

    
    def get_takim_ad(self):
        """[summary]

        Returns:
            [type]: takim adını geriye döndürür.
        """
        return self._ad


    #setter
    def set_puan(self,yenipuan):
        """ puanı yenisiyle günceller.

        Args:
            yenipuan ([type]): [description]
        """
        self._puan=yenipuan

    #getter
    def get_puan(self):
        return self._puan