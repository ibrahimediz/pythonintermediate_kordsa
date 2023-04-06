# https://www.analyticsvidhya.com/blog/2021/08/explore-the-magic-methods-in-python/
class A:
    def __init__(self,a,b,*args,**kwargs):
        self.a = a
        self.b = b
    
    def __le__(self,obj): # less  equal >=
        return self.a >= obj.a

    def __eq__(self,obj): # equal ==
        return self.a == obj.a

    def __str__(self):
        return self.b
obj1 = A(2,"a")
obj2 = A(3,"b")

print(obj2) # str veri tipine dönüştürerek yazar ya da repr özelliği devreye girer 