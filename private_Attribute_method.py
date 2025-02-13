#private(like)attribute & methods 
#conceptual implementations in python
#private attributes & methods are meant to be used only within the class and are not accessible from outside the class
"""
class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.acc__pass=acc_pass    #2 _ means wo chiz private hai
    def reset_pass(self):   #aisa karne se private ko access kar sakte hai and acc_pass ko print karva sakte hai
        print(self.__acc_pass)
acc1=account("12345","abcde")
print(acc1.acc_no)   #koi bhi aise kuch bhi information print karva sakta hai so hume private karne ki jarurat hai bcz kuch chizze sencitive hoti hai jise private rakh ne ki jarurat hai
print(acc1.acc__pass)  #error aayega
"""

class person:
    __name="yanna"

    def __heloo(self):     #ye function ko obj se use nhi kar sakte but humane isse iss liye banaya hai taki iss ko ho hum internaly dusare function me use kar sakte hai
        print("hello person...!")

    def wlcome(self):
        self.__heloo(self.name)
p1=person()
#print(p1.__name)   
print(p1.wlcome())