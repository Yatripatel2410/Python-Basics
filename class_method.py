#class method
#a class method is bound to the class & receives the class as an implicit first argument
#note---> static method can1t access or modify class state and generally for utility

class person:
    name='yanna'

    """
    def changename(self,name):
        #self.name=name    #obj ke andar ek name create ho gaya so yahan person.name=name karke class attribute ko change kar sake hai to sab me yatri print hoga
        #person.name=name
        self.__class__.name="yans"
    """
        
    @classmethod   #ye change direct class ke attributes me hoga
    def changename(cls,name):    
        cls.name=name

p1=person()
p1.changename("yatri")
print(p1.name)
print(person.name)  #iss me purana name hi store hai jab sel.name=name hai tab

#ab humare pass 3 methods hai 1)static method jiss me class and instance kissi ke bhi argument ko change nhi kar rahe  2)class method jiss me cls as a arument aata hai 3)instance method jiss me self as a argument aata hai
