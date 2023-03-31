
# Kedi için bir sınıf oluşturup bu sınıf üzerinden iki kedinin nesne olarak tanımını yapınız
class Cat:
        def __init__(self,name,spiece,gender,age,nat):
                self.name = name
                self.spiece = spiece
                self.gender = gender
                self.age = age
                self.nat = nat #nationality
        
        def shoutMyName(self):
                print(self.name)

        def makeSound(self):
                print(self.name,"says Meawwww")

cat1 = Cat("Matsko","Tekir","Female",3, "Turkish")
cat2 = Cat("Cassie","British Shorthair","Female",4,"England")

