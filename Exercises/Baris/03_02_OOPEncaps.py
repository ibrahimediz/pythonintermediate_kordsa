
     

class Car:
    classAttribute = ""
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        

    def getBrand(self):
        print(self.brand)

    def getModel(self):
        print(self.model)

    def getYear(self):
        print(self.year)       
        