#single line comment 
"""
multiline comments
"""
print("Yanna Patel")   #here print is a function
#Python Character Set:- 
# letters=A to Z , a to z
#Digits=0 to 9
#Special Symbol= +,-,*,/ etc
#whiteSpace=blank space,tab,carriage return,newline,formfeed
#other characters=ASCII and Unicode characters 
print("i am ","yanna")
print(23)
print(45)
print(10+5)
print(10-5)
print(10*2)
print(10/5)
print(10%3)
name="yans"
age=19
a=age+0.5
print(a)
print("I am ",name,".My age is:",age)
print(type(name))
print(type(a))
print(type(age))
a1=False
print(type(a1))
a2=True
print(type(a2))
z=None
print(z)
print(type(z))

#python is case-sencitive lang
#Identifiers:-kind of variable`s name 
#KeyWords:-Reserved words in python 

#sum of 2 num
n1=2
n2=5
sum=n1+n2
print(sum)

#python is implicit not explicit bcz hum variable define karte time uss ka type nhi batate wo khud se hi usska type difine kar dega

#expression execution
#String and numeric value can opearte together with *
A,B=2,4
Txt="@"
print(2*Txt*4)  #here 2*4=8 hota hai but yahan 2 and 4 ke sath ek string ko multiply kiya hai toh yahan 2*4=8 time @ print hoga

#string and string can operate with + 
C,D="2",3
print((C+Txt)*D)  #yahan 2+@ 3 bar print hoga bcz *3 hai so

#numeric values can operate with all arithmetic operators
E,F=2,3
G=4
print(E+F*G)

#arithmetic expression with int and float will result in float
H,I=10,5.0
J=H*I
print(J)

#result of divison operator with two interers will be float
K,L=1,2
M=K/L
print(M)

#int divison with float & int will give int display as float
N,O=1.5,3
P=N//O    #yahan ans 0.5 aayega but round fig kar ke int me stir katega so 0.5 ka chota stor karega means 0.0 ans aayega
print(P,N/O)

#floor give cllosest int,which is lesser than or equal than or equal to the float value
#result of (N//O) same as floor(N/O)
V,S=-12,5
W=V//S
print(W)

V2,S2=12,5
W2=V2//S2
print(W2)

V1,S1=12,-5
W1=V1//S1
print(W1)

#remainder is -ve when denominator is -ve
#n/d ---> (+/+)=+ve ,(-/-)=+ve ,(-/+)=+ve ,(+/-)=-ve
A1,B1=-5,2
C1=A1%B1
print(C1)

A2,B2=5,2
C2=A2%B2
print(C2)

A3,B3=5,-2
C3=A3%B3
print(C3)

num1,num2=2,4   #a**b means (a)^b a to the power b 
num3=num1**num2
print(num3)

T1=True
T2=False
T3=not True
T4=T3&T2|T1
print(T4)
