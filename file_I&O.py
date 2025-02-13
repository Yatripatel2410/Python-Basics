#file input and output
#python can be perform operations on a file.(read and write data is major operation)
#types of all file:
#1)text file: .txt , .docx , .log etc
#2)binary files: .mp4 , .mov , .png , .jpeg etc

#open,read & close file
#we have to open a file before reading or writing
# f=open("file_name","mode")  mode=> r:read mode and w:write mode and file_name=>sample.txt and demo.docx
"""
f=open("demo.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()
"""
"""
'r':open for reading(default)
'w':open for writing,truncating the file first
'x':create a new file and open it for writing
'a':open for writing,appending to the end of the file if it exists
'b':binary mode
't':text mode(default)
'+':open a disk file for updating(reading and writing)
"""
"""
f=open("demo.txt","r")
data=f.read(5)
print(data)
f.close()
"""

"""
f=open("demo.txt","r")
#data=f.read()
#print(data)

line1=f.readLine()
print(line1)

line2=f.readline()
print(line2)

f.close()
"""
 #write data
"""
f=open("demo.txt","w")
f.write("1 bye guyss...! ")
f.close()
"""
#append data
"""
f=open("demo.txt","a")
f.write("\nthen i'll move to home\n")
f.write("take care guyssssss..........\n")
f.close()
"""
#jab file folder me available nhi hoti toh python automatic file create kar deta hai
"""
f=open("Sample.txt","w")    #f=open("Sample.txt","a")
f.close()
"""
#r+ : overwrite hoga
"""
f=open("Sample.txt","r+")
f.write("asf")
print(f.read())
f.close()
"""

#with syntax
"""
with open("demo.txt","a")as f:   #f is alias
    data=f.read()
    print(data)   #yahan with automaticaly fine ko close kar dega
"""

#deleting a file
#using the os module
#module(like a code library) is a file writeen by another programmer that generally has a function we can use
#import os ye built-in hai so error nhi aayega nut
#import tensorflow me error aayega so uss me pip(or)pip3 install tensorflow install karna padega
"""
import os
os.remove("Sample.txt")  #ye ran se humari Samplefile delete ho jayegi
"""
