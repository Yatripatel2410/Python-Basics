#if-elif-else (SYNTAX) (EXAMPLE)
"""
light=input("Light color is: ")
if(light == "red"):
    print("------------STOP------------")
elif(light == "orange"):
    print("-----------Ready-----------")
elif(light == "green"):
    print("----------go---------")
else:
    print("light is broken")        
"""

#grade of student
"""
marks=int(input("Enter Your Marks: "))
if(marks>=90):
    print("You Got 'A' Grade")
elif(marks>=80 and marks<90):
    print("you got 'B' Grade")
elif(marks>=70 and marks<80):
    print("you got 'C' Grade")    
elif(marks>=60 and marks<70):
    print("you got 'D' Grade")    
elif(marks>=50 and marks<60):
    print("you got 'E' Grade") 
else:
    print("You Are Fali Better Luck Next Time")
"""

#single line if/ternary operator
#<var> = <var1> if <condition> else <var2>
"""
food=input("food: ")
eat="yes" if food=="cake" else "no"
print(eat)
"""

#<stt1> if <condition> else <stt2>
"""
food=input("food:")
print("sweet") if food=="cake" or food=="jalebi" else print('not sweet') 
"""

#clever if/ ternary operator
#<var>=(false_val,true_value)[<condition>]
"""
age=int(input("age: "))
vote=("No","Yes") [age>=18]
print(vote)
"""

"""
sal=float(input("salary:"))
tax=sal*(0.1,0.2) [sal>50000]
print(tax)
"""
