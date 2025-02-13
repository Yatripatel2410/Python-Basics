#Guess the number

import random   #random module is use to generate random values 

target=random.randint(1,100)   #i se 5 ke bich me koi bhi random number generate karega
#print(target) --> ye ans batayega

while True:
    userChoice=int(input("Guess Any Number OR Quit(Q):"))
    
    if(userChoice=="Q"):
        break

    userChoice=int(userChoice)

    if(userChoice == target):
        print("Success : Correct Guess...!")
        break
    elif(userChoice < target):
        print("OOPS...! Your Number Was Too Small. Take A Bigger Guess...")   
    else:
        print("OOPS...! Your Number Was Too Big. Take A Smaller Guess...")    

print("----GAME OVER----")    