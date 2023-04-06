class A: # parent class
    def __init__(self):
        self.a = "A"

    def soyle(self):
        print("A Sınıfından Çalıştım")
    
    def soyleA(self):
        print(self.a)
# objA = A()
# objA.soyle()
# objA.soyleA()

class B(A): # inheritance Kalıtım child class
    def __init__(self): # overloading
        super().__init__() # super ifadesi miras alınan parent class için kullanıldı
        self.b = "B"

    def soyle(self): # overriding
        print("B Sınıfından Çalıştım")

obj1 = B()
obj1.soyle()
obj1.soyleA()