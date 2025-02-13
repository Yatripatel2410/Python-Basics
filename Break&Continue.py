#break and continue
#break: used to terminate the loop when encountered
#continue: terminates execution in the current iteration & continues exicution of the loop with the next iteration

i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("End OF LOop")    


num1=(1,4,9,16,25,36,49,64,81,36,100)
x=36
i=0
while i<len(num1):
    if(num1[i]==x):
        print("found at index",i)
        break
    else:
        print("finding...")    
    i+=1
print("End of loop")    

#print odd numbers
i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue  #skip
    print(i)
    i+=1
