
"""
Bir galeri için tasarlanan bir yazılım içerisinde arabalar bir sınıf üzerinden nesne üretilerek kaydedilmek istenmektedir.
En az üç örnek özelliği olan (instance attribute ) bir araba sınıfı tasarlayınız
"""

class Galeri:
        def __init__(self,marka,model,renk):
                self.marka = marka
                self.model = model
                self.renk = renk

        def yazMarka(self):
                print(self.marka)

        def yazmodel(self):
                print(self.model)
        
        def yazrenk(self):
                print(self.marka)


araba1 = Araba("Toyota","Corolla","Gri")
araba2 = Araba("Toyota","Chr","Kırmızı")
araba3 = Araba("Toyota","Yaris","Kırmızı")


        