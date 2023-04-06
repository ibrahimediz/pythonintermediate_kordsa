import random as rnd
import time

class Hero:
    def __init__(self,name,power,health):
        self.name = name
        self.power = power
        self.health = health

    def impact(self,power):
        self.health -= power
    
    def hit(self):
        return self.power

    def status(self):
        return f"{self.name} {self.health}"

class MarvelHero(Hero):
    def __init__(self, name, power, health):
        super().__init__(name, power, health)
        self.supPower = 0

    def impact(self, power):
        super().impact(power)
        self.supPower += 1
        if self.supPower == 5:
            self.health += 100
            self.supPower = 0


class DCHero(Hero):
    def __init__(self, name, power, health):
        super().__init__(name, power, health)
        self.supPower = 0

    def hit(self):
        self.supPower += 1
        if self.supPower == 5:
            self.supPower = 0
            return self.power * 2
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

marvelHeroList = [DeadPool,Hulk,IronMan]
dcHeroList = [SuperMan,Batman,Flash]

# print(rnd.choice(marvelHeroList))

P1 = rnd.choice(marvelHeroList)()
P2 = rnd.choice(dcHeroList)()
while P1.health >0 and P2.health > 0:
    time.sleep(1)
    P2.impact(P1.hit())
    P1.impact(P2.hit())
    print(P1.status())
    print(P2.status())
else:
    if P1.health > P2.health:
        print(f"{P1.name} Wins")
    elif P1.health < P2.health:
        print(f"{P2.name} Wins")
    else:
        print("Tie")
