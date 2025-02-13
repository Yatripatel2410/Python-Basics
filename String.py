str1="this is a string.\nwe are creating in python.\tit is in double cote"   #yahan har sentance ko next line me print kar ne ke liye escape sequence char ka use kar te hai jiska kaam hota hai formatting dena
str2='it is also a string with single comma'
str3="""This a string in triple cote"""
print(str1)
s1="kim"
s2="teahyung"
print(s1+" "+s2)
print(len(str2))   #space bhi count hoga
print(len(s1))
print(len(s1+" "+s2))
print(s1[2])
print(str1[4])      #s1[1]=y ---> it is not allow to assign another value

#slicing = accessing parts of a string
print(s2[2:4])
print(str2[0:5])    #print(str2[:5])  same output
print(str3[17:len(str3)])    #or str3[17:] same output

# -ve index backword counting
print(s2[-4:-1])

#string function
print(s2.endswith("ung"))  #return true if string ends with substring
print(s1.capitalize())     #capitalizes 1st char
print(str2.replace("comma","cote"))   #replaces all occurences of old with new word (old,new)
print(str1.find("in"))             #return 1st index of 1st occurrence   
print(str1.count("in"))              #counts the occurrence of substr in string
