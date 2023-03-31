# class A: # parent class
#     def __init__(self):
#         self.a = "A"

#     def soyle(self):
#         print("A Sınıfından Çalıştım")
    
#     def soyleA(self):
#         print(self.a)
# # objA = A()
# # objA.soyle()
# # objA.soyleA()

# class B(A): # inheritance Kalıtım child class
#     def __init__(self):
#         super().__init__() # super ifadesi miras alınan parent class için kullanıldı
#         self.b = "B"
# obj1 = B()
# obj1.soyle()
# obj1.soyleA()

#################################

class A: # parent class
    def __init__(self):
        self.a = "A"

    def soyle(self):
        print("A Sınıfından Çalıştım")
    
    def soyleA(self):
        print(self.a)

class B: # parent class
    def __init__(self):
        self.b = "B"

    def soyle(self):
        print("B Sınıfından Çalıştım")
    
    def soyleB(self):
        print(self.b)

class C(A,B): # Multiple Inheritance
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.c = "C"

objC = C()
objC.soyleA()
objC.soyleB()
objC.soyle() # A Sınıfından Çalıştım

