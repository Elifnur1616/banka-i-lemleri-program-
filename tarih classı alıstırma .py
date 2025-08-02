class bankaSinifi():
    def __init__(self,isim,soyisim):
        if(self.isimSoyisimKontrol(isim)==True and self.isimSoyisimKontrol(soyisim)==True):
            self.isim=isim
            self.soyisim=soyisim
            self.bakiye=0
        else:
            raise ValueError("Isim veya soyisim sadece karakter icerebilir!")
    @staticmethod
    def isimSoyisimKontrol(isimVeyaSoyisim):
        for karakter in isimVeyaSoyisim:
            if not karakter.isalpha():
                return False
        return True
    
    def profilGoruntule(self):
        print("Hesap Sahibi:{} {}".format(self.isim,self.soyisim))
        print("Hesap Bakiyesi:{}₺".format(self.bakiye))
    
    def paraYatirma(self,yatirilacakParaMiktari):
        if yatirilacakParaMiktari<=0:
            print("Para Yatirma Basarisiz!")
        else:
            self.bakiye+=yatirilacakParaMiktari
            print("Yeni Bakiye:{}".format(self.bakiye))
    
    def paraCekme(self,cekilecekParaMiktari):
        if cekilecekParaMiktari>self.bakiye:
            print("Para Cekme Basarisiz!")
        else:
            self.bakiye-=cekilecekParaMiktari
            print("Yeni Bakiye:{}".format(self.bakiye))

    def paraGonderme(self,gonderilecekParaMiktari,gonderilecekHesap):
        if gonderilecekParaMiktari>self.bakiye:
            print("Para Gonderme Basarisiz!")
        else:
            self.bakiye-=gonderilecekParaMiktari
            gonderilecekHesap.bakiye+=gonderilecekParaMiktari
            print("Yeni Bakiye:{}".format(self.bakiye))
            hesap1=bankaSinifi("Ogun","Birinci")
hesap2=bankaSinifi("Elifnur","Atici")
hesap1.profilGoruntule()
hesap2.profilGoruntule()
hesap1.paraYatirma(200)
hesap1.profilGoruntule()
hesap1.paraCekme(100)
hesap1.profilGoruntule()
hesap1.paraGonderme(100,hesap2)
hesap1.profilGoruntule()
hesap2.profilGoruntule()
