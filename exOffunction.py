#print length of any list
"""
cities=["delhi","gurgaon","noida","pune","bombe","chennai"]
heroes=["thor","ironman","naruto","V"]
def print_len(list):
    print(len(list))
print_len(cities)
print_len(heroes)    

def print_list(list):
    for item in list:
        print(item,end=" ")
        #print(cities,end="\n")
print_list(heroes)
print_list(cities)
"""

#factorial
"""
def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)   
calc_fact(6) 
"""

#convert the number USD to INR
def convert(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD=",inr_val,"INR")
convert(73)
convert(100)    