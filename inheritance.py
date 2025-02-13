#inharitance
#when one class(child/derived) derives the properties & methods of another class(parent/base)
#type of inheritance:>1.single 2.multi-level  3.multiple
"""
class car:
    color="black"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped....!")

class toyotaCar(car):
    def __init__(self,name):
        self.name=name

car1=toyotaCar("fortunar")
car2=toyotaCar("prius")

print(car1.name)
print(car1.start())
print(car1.color)
"""

#multi-level -----> car ki property toyotaCar me ja rahi hai and toyota car ki sari property fortunar exess kar raha hai
"""
class car:
    color="black"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped....!")

class toyotaCar(car):
    def __init__(self,brand):
        self.brand=brand

class fortunar(toyotaCar):
    def __inti__(self,type):
        self.type=type

car1=fortunar("diesel")
print(car1.start())
"""

#multiple inheritance yahan multiple class ki property inherite ki ja sakti hai 
#for ex 2 base class hai and uss ka 1 derive class hai

class A:
    varA="wlc to class A"

class B:
    varB="wlc to class B"

class C(A,B):
    varC="wlc to class C"        

c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)