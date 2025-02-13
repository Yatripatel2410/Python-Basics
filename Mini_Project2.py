#Random Password Generator With N Length
#hum git hub ya koi aur app me aacount banate hai to kai baar wo pass sujest karta hai 
#pass. me 0-9 & A to Z & a to z and punctuators(@#$%^&*/*+-(){}[]~:;<>?'",\) use hote hai

import random
import string  

#print(string.ascii_letters)
#print(string.punctuation)
#print(string.digits)

#koi bhi num select karta hai list me se
"""
val=random.choice([1,"b",2,3,"a"])
print(val)
"""

pass_length=12
charValues=string.ascii_letters + string.digits + string.punctuation
print(charValues)

#list comprehension  [function for i in range(n)]--> list ko baar baar call karana chahte hai
result=  "".join([random.choice(charValues) for i in range(pass_length)])   #"".join list kostring me convert karta hai
print("Your Password Is:",result)

"""
password=""
for i in range(pass_length):
    password+=random.choice(charValues)

print("Your Random Password Is:",password)
"""