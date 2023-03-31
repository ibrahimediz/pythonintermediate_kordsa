
class Cat:
        def __init__(self,name,spiece,age,gender):
                self.name = name
                self.spiece = spiece
                self.age = age
                self.gender = gender

        def sayMyName(self):
                print(self.name)

        def makeNoise(self):
                print(self.name ,"Meow") 

cat1 =Cat("Boncuk","Tekir","3","Female") 
cat2 =Cat("Paşa","Scottish","3","Male")      

cat1.sayMyName()