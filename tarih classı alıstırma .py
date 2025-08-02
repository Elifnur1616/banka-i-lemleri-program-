class tarih:
    aylaraGöreGünler=[31,29,31,30,31,30,31,30,31,31,30,31]
    aylistesi=["ocak","subat","mart","nisan","mayıs","haziran","temmuz","agustos","eyül","ekim","kasim","aralik"]
    def __init__(self,gün,ay,yil):
       self.ay=int()
       self.gün=int() 
       self.yil=int()
       if ay>=1 and ay<=12:
          self.ay=ay
       else:
          self.ay=1
       if gün>=1 and gün<=self.aylaraGöreGünler[ay-1]:
          self.gün=gün   
       else:
        self.gün=1    
       if yil>=1900:
          self.yil=yil
       else:
          self.yil=1900

    def günArttir (self)  :
      if self.gün<self.aylaraGöreGünler[self.ay-1]:
       self.gün+=1
      else:
         self.gün=1
         if self.ay<12:
          self.ay+=1  
         else:
          self.ay=1
          self.yil+=1

    def tarihYazdir(self):
       print("{} {} {}".format(self.gün,self.aylistesi[self.ay-1],self.yil))


    def tarihKarsilastir(self,ikinciTarih)   :
       if self.yil>ikinciTarih.yil or (self.yil==ikinciTarih.yil and self.ay>ikinciTarih.ay) or(self.ay==ikinciTarih.ay and self.gün>ikinciTarih.gün):
          print("ilk tarih daha büyüktür")                                                                                      
       elif self.yil ==ikinciTarih.yil and self.ay==ikinciTarih.ay and self.gün==ikinciTarih.gün :
           print("iki tarih de esittir")   
       else:
          print("ikinci tarih daha büyüktür")
            
tarih1=tarih(30,7,1999)
tarih2=tarih(31,7,1999)
tarih1.tarihYazdir()
tarih1.günArttir()
tarih1.tarihYazdir()
tarih2.tarihYazdir()
tarih2.günArttir()
tarih2.tarihYazdir()
tarih1.tarihKarsilastir(tarih2)