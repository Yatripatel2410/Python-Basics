#property
#we use @property decorator an any method in the class to use the method as a property
class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        #self.persentage=str((self.phy+self.chem+self.math)/3)+"%"
    """
    def calc_persentage(self):
        self.persentage=str((self.phy+self.chem+self.math)/3)+"%"
    """
    @property
    def persentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"

stu1=student(98,97,99)
print(stu1.persentage)    

#ab realize hua ki stu1 ke phy me marks 65 the to ab hum change kar ke print karenge to wo aa bhi jayega but stu1 ki persentage change nhi hongi to iss ke liye ek method banayenge calc_persentage uss ko call karenge to iss ke badale me hum property ka use kar sakte hai
stu1.phy=86
print(stu1.phy)
#print(stu1.calc_persentage())
print(stu1.persentage)