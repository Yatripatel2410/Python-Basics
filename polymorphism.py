#polymorphism means many forms
#best ex in python is operator over loading
#when the same operator is allowed to have diff meaning according to the context

print(1+3) #yahan + 4 add kar raha hai
print("yanna"+"patel") #yahan + yanna patel concatenate kar raha hai
print([1,2,3]+[4,5,6]) #yahan + merge kar raha hai
#to isse operator overloading kahete hai
#python me class int,string,list sab ke liye + operatoer ka matalab alag hai

class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img 

    def showNumber(self):
        print(self.real,"i +",self.img,"j")    
    """
    def add(self,num2):
        newReal=self.real+num2.real
        newImag=self.img+num2.img
        return complex(newReal,newImag)
    """
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImag=self.img+num2.img
        return complex(newReal,newImag)
    
num1=complex(19,3)
num1.showNumber()

num2=complex(2,1)
num2.showNumber()
#ye num1+num2 karne ke liye ab hum dunder function ka use karenge aage 2 time __ lagane se wo dundar function baan jata hai
"""
num3=num1.add(num2)
num3.showNumber()
"""
# but mujhe aisa chahiye ki me direct print(num1+num2) kar saku to ab iss ke liye dunder function karenge to ab add ke aage and piche 2 time __ kar dete hai
