#super Method
class car:
    def __init__(self,type):
        self.type=type
        
    color="black"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped....!")

class toyotaCar(car):
    def __init__(self,name,type):
        super().__init__(type)   #super class ke andar constructor call ho gaya to ab print(car1.type) me error nhi aayega
        self.name=name
        #self.type=type  #ye toyota kar ke andar attribute create hoga but mujhe toyota car ke liye nhi chahiye mujhe to parent class ke andar attribut chahiye to super ka use karte hai hum
        super().start()

car1=toyotaCar("prius","electric")
print(car1.type)