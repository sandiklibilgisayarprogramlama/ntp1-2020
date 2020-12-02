class YakitTuru:
    yakitadi=""
    yakitlitreucreti=0.0

    def yakit_adini_yazdir(self):
        print(self.yakitadi)

    def yakit_litre_ucreti_getir(self):
        return self.yakitlitreucreti

    def tum_bilgileri_yazdir(self):
        self.yakit_adini_yazdir()
        print(self.yakit_litre_ucreti_getir())
