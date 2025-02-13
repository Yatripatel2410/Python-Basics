#del keyword
#used to delete object properties or object itself
class student:
    def __init__(self,name):
        self.name=name
s1=student("yatri")
print(s1)
print(s1.name)
del s1
#print(s1)      error aayega bcz s1 kp delete kar diya hai
#print(s1.name)   