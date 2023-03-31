
"""
Bir galeri için tasarlanan bir yazılım içerisinde arabalar bir sınıf üzerinden nesne üretilerek kaydedilmek istenmektedir.
En az üç örnek özelliği olan (instance attribute ) bir araba sınıfı tasarlayınız
"""

class Araba:
        classAttribute = "Hibrit"
        def __init__(self,marka,model,renk,şase):
                self.marka = marka
                self.model = model
                self.renk = renk
                self.__sase = şase

        def yazmarka(self):
                print(self.marka)

        def yazmodel(self):
                print(self.model)
        
        def yazrenk(self):
                print(self.renk)

        def getId(self): # getter fonksiyonu
                if  len(self.__sase) == 17:
                        return şase
                else:
                        print("Eksik veya fazla numara tuşladınız.")


araba1 = Araba("Toyota","Corolla","Gri",102)
araba2 = Araba("Toyota","Chr","Kırmızı",10236548975315643)
araba3 = Araba("Toyota","Yaris","Kırmızı",10236548975315645)

print(araba1.getId())


        