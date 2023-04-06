import random as rnd
import time

class Hero:
    def __init__(self,name,power,health):
        self.name = name
        self.power = power
        self.health = health

    def impact1(self,power):
        self.health -= power//2
    def impact2(self,power):
        self.health -= power//3
    def impact3(self,power):
        self.health -= power

    def impact(self,obj):
        rnd.choice((self.impact1,self.impact2,self.impact3))(obj.power)
        obj.health -= self.power//2
    
    def hit1(self):
        return self.power//2
    def hit2(self):
        return self.power//3
    def hit3(self):
        return self.power

    def hit(self):
        return rnd.choice((self.hit1,self.hit2,self.hit3))()

    def status(self):
        return f"{self.name} {self.health}"

class MarvelHero(Hero):
    def __init__(self, name, power, health):
        super().__init__(name, power, health)
        self.supPower = 0

    def impact(self, obj):
        super().impact(obj)
        self.supPower += 1
        if self.supPower == rnd.randint(5, 10):
            print(f"{self.name} Süper Güç Kullandı")
            self.health += obj.power
            self.supPower = 0


class DCHero(Hero):
    def __init__(self, name, power, health):
        super().__init__(name, power, health)
        self.supPower = 0

    def hit(self):
        self.supPower += 1
        if self.supPower == rnd.randint(5, 10):
            self.supPower = 0
            print(f"{self.name} Süper Güç Kullandı")
            return self.power * 2
        return self.power

class TurkishHero(Hero):
    def __init__(self, name, power, health):
        super().__init__(name, power, health)
        self.supPower = 0

    def hit(self):
        self.supPower += 1
        if self.supPower == rnd.randint(5, 10):
            self.supPower == 0
            print(f"{self.name} Sağlam vurdu")
            return self.power * 4
        return self.power

class DeadPool(MarvelHero):
    def __init__(self):
        super().__init__("DeadPool",100,1000)

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk",120,1200)

class IronMan(MarvelHero):
    def __init__(self):
        super().__init__("IronMan",90, 1000)

class SuperMan(DCHero):
    def __init__(self):
        super().__init__("SuperMan",100,1000)

class Batman(DCHero):
    def __init__(self):
        super().__init__("Batman",120,1200)

class Flash(DCHero):
    def __init__(self):
        super().__init__("Flash",90, 1000)

    
class BattalGazi(TurkishHero):
    def __init__(self):
        super().__init__("Battal Gazi",100, 1250)

class KaraMurat(TurkishHero):
    def __init__(self):
        super().__init__("Kara Murat",90, 1450)

class Tarkan(TurkishHero):
    def __init__(self):
        super().__init__("Tarkan",150, 850)

marvelHeroList = [DeadPool,Hulk,IronMan]
dcHeroList = [SuperMan,Batman,Flash]
turkishHeroList = [BattalGazi,KaraMurat,Tarkan]
charList = [marvelHeroList,dcHeroList,turkishHeroList]
# print(rnd.choice(marvelHeroList))

P1 = rnd.choice(rnd.choice(charList))()
P2 = rnd.choice(rnd.choice(charList))()
print(f"P1 için {P1.name} seçildi")
print(f"P2 için {P2.name} seçildi")

# print(rnd.choice(marvelHeroList))

while P1.health >0 and P2.health > 0:
    time.sleep(1)
    P2.impact(P1)
    P1.impact(P2)
    print(P1.status())
    print(P2.status())
else:
    if P1.health > P2.health:
        print(f"{P1.name} Wins")
    elif P1.health < P2.health:
        print(f"{P2.name} Wins")
    else:
        print("Tie")
