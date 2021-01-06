class Fikstur:
    def __init__(self,takim,rakipDict):
        self._rakipDict=rakipDict
        self._takim=takim

    def print_fikstur(self):
        """
        fikturu ekrana yazar
        """
        print(self._takim.get_takim_ad()+" adlı takimin fikstürü")
        for tarih,takim in self._rakipDict.items():
            print(self._takim.get_takim_ad()+" - "+takim.get_takim_ad()+" "+tarih)

    def yeni_mac_ekle(self,tarih,takim):
        """ maç listesine yeni ekleman ekler

        Args:
            tarih ([type]): maç gününün tarihi ve saati
            takim ([type]): takim nesnesi
        """
        self._rakipDict[tarih]=takim