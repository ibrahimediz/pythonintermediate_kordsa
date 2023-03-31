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
#####################################
class Sinif:
    def __init__(self,a,b): #  initialize Constructor Yapıcı 
        """ self parametresi self ifadesi olarak ele alındığında bir gelenektir. 
        self parametresi ya da değişkeni instance attribute ve instance methodlara sınıf içerisinde 
        erişmek için kullanılır"""
        self.a = a
        self.b = b
        self.sayA()
    
    def sayA(self):
        return self.a

obj1 = Sinif(2,3)
print(obj1.sayA())

print(type(obj1)) # <class '__main__.Sinif'>
print(type(2.0)) # <class 'float'>

print(__name__)