class Dog:
    classAttribute = "Canis lupus familiaris"
    def __init__(self,name,specie,age,gender):
        self.name = name
        self.specie = specie
        self.age = age
        self.gender = gender
        self.__idNum = gender[:2] + name[:2] # private attribute

    @property
    def Id(self): # getter fonksiyonu
        if  self.age < 13:
            return "Yetki Hatası"
        return self.__idNum

    @Id.setter
    def Id(self,param):
        if len(param) == 5:
            self.__idNum = param
        else:
            raise ValueError("Değer Hatası")

    @Id.deleter
    def Id(self):
        self.__idNum = "-"+self.__idNum

    def sayMyName(self):
        print(self.name)

    def makeNoise(self):
        print(self.name,"says Waff Waff")


dog1 = Dog("Biber", "Saint Bernand", 12, "Male")
print(dog1.Id)
dog1.Id = "AAAAA"
dog1.age = 14
print(dog1.Id)
del dog1.Id
print(dog1.Id)
"""
__gizli # erişilemez
__gizli_  # erişilemez
__gizli__ # erişilir
"""