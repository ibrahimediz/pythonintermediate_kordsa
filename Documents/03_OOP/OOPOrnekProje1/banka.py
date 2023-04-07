class BankaHesabi:
    varsayilanHesapNum = 1 # class attribute

    def __init__(self,isim,bakiye=0):
        self.isim = isim
        self.bakiye = bakiye
        self.hesapNumarasi = BankaHesabi.varsayilanHesapNum
        BankaHesabi.varsayilanHesapNum = BankaHesabi.varsayilanHesapNum + 1

    def yatirma(self,tutar):
        self.bakiye += tutar

    def cekme(self,tutar):
        if self.bakiye < tutar:
            print("Yetersiz Bakiye")
        else:
            self.bakiye -= tutar
        
    def bakiyeAl(self):
        return self.bakiye
print("#"*30,__name__,"#"*30)
if __name__ == "__main__":
    hesap1 = BankaHesabi("Paribu",1000)
    hesap1.yatirma(1000)
    print(hesap1.bakiyeAl())
    hesap1.cekme(500)
    print(hesap1.bakiyeAl())