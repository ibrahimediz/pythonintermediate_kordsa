# DRY => Don't Repeat Yourself
# class 
# instance
## attribute özellik
## method   fonksiyon
# class Sinif: # class
#     pass

# Sinif() # instance object

############################
# class Sinif:
#     sinifOzelligi = "Sınıf Özelliği" # class attribute
#     def __init__(self,a):
#         self.ornekOzellik = "Örnek Özellik " + a # instance attribute

#     def ornekMethod(self): # instance Method Örnek Metod
#         print(self.ornekOzellik) 

#     @classmethod
#     def sinifMethod(cls): # class method sınıf metot
#         print(cls.sinifOzelligi) 

# nesne1 = Sinif("nesne 1")
# nesne2 = Sinif("nesne 2")
# nesne1.ornekMethod() # Örnek Özellik nesne 1
# nesne2.ornekMethod() # Örnek Özellik nesne 2
# nesne1.sinifMethod() # Sınıf Özelliği
# nesne2.sinifMethod() # Sınıf Özelliği
# Sinif.sinifMethod() # Sınıf Özelliği