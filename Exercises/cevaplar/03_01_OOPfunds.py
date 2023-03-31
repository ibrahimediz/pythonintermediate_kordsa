class Dog:
    classAttribute = "Canis lupus familiaris"
    def __init__(self,name,specie,age,gender):
        self.name = name
        self.specie = specie
        self.age = age
        self.gender = gender

    def sayMyName(self):
        print(self.name)

    def makeNoise(self):
        print(self.name,"says Waff Waff")
        # Kedi için bir sınıf oluşturup bu sınıf üzerinden iki kedinin nesne olarak tanımını yapınız

dog1 = Dog("Biber","Husky",22,"Male")
dog2 = Dog("Çilek","King Charles",20,"Female")
dog1.makeNoise() # Biber says Waff Waff
dog2.makeNoise() # Çilek says Waff Waff
print(dog1.classAttribute)
print(dog2.classAttribute)
print(Dog.classAttribute)