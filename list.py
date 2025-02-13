#list in python
marks=[12.20,53.34,78.67,54.5,90.0,76.43,54.8]
print(marks)
print(type(marks))
print(marks[1])
marks[2]=66.66
print(marks)
student=["yanna",90.07,"ldrp"]
print(student)
print(len(student))
print(marks[1:5])
print(student[:2])
print(student[1:])
print(marks[5:len(marks)])
print(marks[-3:-1])

#methods in list
marks1=[21,34,65]
print(marks1)
marks1.reverse()       #reverses list
print(marks1)
marks1.append(22.22)  #adds one element at the end
print(marks1)
marks1.sort()         #sort in ascending order return none uss ke baad print karva na padega
print(marks1)
marks1.sort(reverse=True)  #sorts in descending order
print(marks1)
marks1.reverse()       #reverses list
print(marks1)
student.insert(0,"patel")   #insert element at index 
print(student)
s=['e','a','d','z','p']
s.sort()         #sort in ascending order return none uss ke baad print karva na padega
print(s)
s.remove('e')
print(s)
s.pop(2)
print(s)
s.copy()
print(s)
s.clear()
print(s)
