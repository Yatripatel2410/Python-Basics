#tuples ---> a built in data type that lets us create immutable sequences of values
#immutable means ek baar tuple bana diya FIR uss ki value chasnge nhi kar sake same as string
#i.e tup[0]=43 is not allow
tup=(87,64,33,95,76,33)
print(tup)
print(type(tup))
print(tup[2])
tup1=()  #empty tuple it is a valid tuple
tup3=(5)   
print(tup3)  
print(type(tup3))
tup2=(1,) #single element tup=(1) is not right bcz python fill (1) is just an integer jisse parenthisses me likha hai sane as string and float me bhi hoga
print(tup1)
print(type(tup1))
print(tup2)
print(type(tup2))

print(tup[1:3])

#methods in tuple
print(tup.index(76))
print(tup.count(33))

#enter 3 movide by user and add(store) in list
movies=[]
mov1=input("Enter 1st Movie:")
mov2=input("Enter 2nd Movie:")
mov3=input("Enter 3rd Movie:")
movies.append(mov3)
mov3=input("enter m0vieee:")
movies.append(mov3)
movies.append(mov1)
movies.append(mov2)
movies.append(input("enter movie:"))
print(movies)

#WAP to check if a list contains a palindrome of elements
#ex of palindrom is [1,2,3,2,1] ,121 ,yaasaay
list1=[1,2,1]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrom")
else:
    print("not palindrom")    

#WAP to count the num of student with the "A" grade in following tuple
grades=("C","D","A","A","B","C","A")
print(grades.count("A"))    
#atore above values in list and sort them from A to D
grades1=["C","D","A","A","B","C","A"]
print(grades1.sort()) 
print(grades1)