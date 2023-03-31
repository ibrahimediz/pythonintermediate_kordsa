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