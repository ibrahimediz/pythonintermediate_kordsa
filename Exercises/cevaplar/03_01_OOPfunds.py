class Dog:
    def __init__(self,name,spiece,age,gender):
        self.name = name
        self.spiece = spiece
        self.age = age
        self.gender = gender

    def sayMyName(self):
        print(self.name)

    def makeNoise(self):
        print(self.name,"says Waff Waff")
        # Kedi için bir sınıf oluşturup bu sınıf üzerinden iki kedinin nesne olarak tanımını yapınız

dog1 = Dog("Biber","Husky",22,"Male")
dog2 = Dog("Çilek","King Charles",20,"Female")