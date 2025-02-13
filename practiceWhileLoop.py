#print the multiplication table of a number n
"""
n=int(input("Number:"))
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1
"""    

#print the elements of the following list using a loop
""" 
num=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(num):
    print(num[idx])
    idx+=1
""" 

#search for a number x in this tuple using loop
""" 
num1=(1,4,9,16,25,36,49,64,81,36,100)
x=36
i=0
while i<len(num1):
    if(num1[i]==x):
        print("found at index",i)
    else:
        print("finding...")    
    i+=1
""" 

#WAP to find the sum of 1st n natural num
number=int(input("Enter the number:"))
sum=0
for ii in range(1,number+1):
    sum+=ii
print("total sum is:",sum)   

#factorial
"""
number=5
fact=1
ii=1
while ii<=number:
   fact*=ii
   ii+=1
print("factorial is:",fact)  
"""