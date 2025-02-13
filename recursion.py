#recursion: when a fun calls itself repeatedly
#call stack banega during recursion
"""
def show(n):
    if(n==0):    #base case
        return
    print(n)
    show(n-1)
show(5)    
"""

#factorial 
"""
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(4))
"""

#calculate sum
"""
def calc_sum(n):
    if(n==0):
        return 0
    else:
        return calc_sum(n-1)+n
sum=calc_sum(5)
print(sum)
"""

#print all elemnt in list
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
f=["mango","apple","bannana","lichi"]    
print_list(f)