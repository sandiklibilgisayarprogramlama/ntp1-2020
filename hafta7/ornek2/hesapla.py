class Hesap:
    s1=0
    s2=0

    def topla(self):
        print(self.s1," ile ",self.s2," nin toplam sonucu: ",(self.s1+self.s2))
    
    def cikar(self):
        print(self.s1," ile ",self.s2," nin fark sonucu: ",(self.s1-self.s2))

    def carp(self):
        print(self.s1," ile ",self.s2," nin çarpım sonucu: ",(self.s1*self.s2))

    def bol(self):
        print(self.s1," ile ",self.s2," nin bölüm sonucu: ",(self.s1/self.s2))
    
    def adGoreIslemYap(self,islemadi):
        if islemadi=="+":
            print(self.s1," ile ",self.s2," nin toplam sonucu: ",(self.s1+self.s2))
        elif islemadi=="-":
            print(self.s1," ile ",self.s2," nin cikar sonucu: ",(self.s1-self.s2))
        elif islemadi=="*":
            print(self.s1," ile ",self.s2," nin carpım sonucu: ",(self.s1*self.s2))

