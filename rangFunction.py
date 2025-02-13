#range()
#range fun returns a sequence of numbers,starting from 0 by default, and increments by 1(by default), and stop before a specified number
#range(start?,stop,step?)
seq=range(10)    #range(stop)
#range(2,10) range(start,stop) means start at 2 and end at 10
#range(1,10,2) means range(start,stop,step) start at 1 and print increase by 2 and stop at 10 
#yahan hum step size ko -ve bhi kar sakte hai for decrising order like range(10,0,-1)
for i in seq:   #for i in range(10)
    print(i)

#even number
for i1 in range(2,101,2):
    print(i1)    

print("-----------------------------------")
#print table
n=int(input("enter number:"))
for index in range(1, 11):
    print(n * index)    