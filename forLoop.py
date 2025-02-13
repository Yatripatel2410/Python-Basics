#for loop: for sequential traversal. for traversing list,string,tuple etc

num=[1,2,3,4,5]
for val in num:
    print(val)

num1=(6,7,8,9,0)
for val1 in num1:
    print(val1)    

str="ApnaGhar" 
for char in str:
    print(char)  
else:
    print("END")
#for loop with else(optional else): it is use for when we use break in short aise kaam jo hum completly loop ke end per karva na chahte hai uss ko end me likh dene ka
str1="hloyanna" 
for char1 in str1:
    if(char1=='o'):
        print("o Found")
        break
    print(char1)
else:
    print("End")    

num2=(1,2,3,4,5,3)
x=3
i2=0
for val2 in num2:
    if(val2==x):
        print("No found at index",i2)
        break
    i2+=1

#factorial 
number=5
fact=1
for ii in range(1,number+1):
    fact*=ii
print("factorial is:",fact)