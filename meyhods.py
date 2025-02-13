class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def hello(self):
        print("wlc student",self.name)    

    def get_marks(self):  #without parameter error aayega so hum static method banayenge
        return self.marks    

#methods that don't use the self parameter (work at class level)
    @staticmethod  #decorator
    def hello():
        print("hello student.....")
s1=student("yanna",98)
s1.hello()
print(s1.get_marks())