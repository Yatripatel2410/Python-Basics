#constuctor
#all classes have a function called_int_(),which is always executed when the class is being initiated
#constructor always ek self perameter leta hai 
class student:
    clg_name="ldrp"  #ye sab ke liye same hai so aise declare kiya taki ek hi baar memory me store hoga
    name="Asha" #class attribute same hai obj attribute na so always obj attribute vala hi print hoga
    def __inti__(self):
        print("it ia a default constructor")
        #parameteraized constructor
    def __init__(self,fullname,marks):   #self is a reference and it is use to exess the variables self means s1 hai isse hum self kahete hai
        print(self)
        self.name=fullname   #it is instance attribute sab ke liye alag hoge
        self.marks=marks
        print("adding new student in database")

  #s1 and s2 alag space occupy karenge memory me  
s1=student("karan",75)
print(s1)
print(s1.name)
print(s1.marks)
s2=student("yanna",98)
print(s2)
print(s2.name)
print(s2.marks)

print(s2.clg_name)