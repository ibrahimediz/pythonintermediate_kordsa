class Cat():
        def __init__(self,name,specie,age,gender):
                self.name = name
                self.specie = specie
                self.age = age
                self.gender = gender

        def SayMyName(self):
                print(self.name)

        def talk(self):
                print(self.name,"a")

cat1 = Cat("Venüs", "Tekir", 6, "Male")
cat2 = Cat("Jelly", "Scotish", 1, "Male")
