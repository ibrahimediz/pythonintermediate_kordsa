from abc import ABC,abstractmethod

class Vehicle(ABC): # abstract base class
    @abstractmethod
    def ornekMethod(self):
        pass 

class LandVehicles(Vehicle):
    def ornekMethod(self): # override işlemi yapılmalı çünkü kalıtım alınan sınıf bir Abstract sınıf
        print("Örnek Method Çalıştı")

obj = LandVehicles()