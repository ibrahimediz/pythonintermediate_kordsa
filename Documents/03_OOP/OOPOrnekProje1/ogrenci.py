class Ogrenci:
    def __init__(self,isim,ogrno,not1,not2): # constructor-initialize
        self.isim = isim
        self.ogrno = ogrno
        self.not1 = not1
        self.not2 = not2

    def onaylama(self,isim,ogrno,not1,not2):
        og = Ogrenci(isim, ogrno, not1, not2)
        ls.append(og)
    
    def goruntuleme(self,ob):
        print(f"İsim : {ob.isim}") # 
        print(f"Ogrenci No : {ob.ogrno}")
        print(f"Not 1 : {ob.not1}")
        print(f"Not 2: {ob.not2}")

    def arama(self,ogrno):
        for i in range(ls.__len__()):
            if ls[i].ogrno == ogrno:
                return i
    
    def silme(self,ogrno):
        i = obj.arama(ogrno)
        del ls[i]

    def guncelleme(self,ogrno,No):
        i = obj.arama(ogrno)
        ogr = No
        ls[i].ogrNo = ogr

ls = []
obj = Ogrenci("", 0, 0, 0)

# menu = """
# 1. Onaylama
# 2. Görüntüleme
# 3. Arama
# 4. Silme
# 5. Güncelleme
# 6. Çıkış
# """
# anahtar = 1
# while anahtar == 1:
#     giris = input(menu)
#     if giris and giris.isdigit():
#         giris = int(giris)
#         if giris-1 in range(0,4):
#             if giris == 1:
#                 pass 
#                 # TODO öğrenci bilgileri girişi istenecek
#             elif giris == 2:
#                 pass
#                 # TODO öğrenci id si istenecek
#                 ......
from banka import BankaHesabi
obj = BankaHesabi("Ali",2000)