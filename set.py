#set in python 
#set is the collection of the unordered items
#each element in the set must be unique and immutable
#dictonaries and list ko hum set ke andar store nhi kara sakte
collection={1,2,2,2,"hello","hello","yanna",4}
print(collection)
print(type(collection))
print(len(collection))
collection1={} #empty dictionary
print(type(collection1))
#made empty set
collection2=set()
print(type(collection2))

#set is mutable
#set elements immutable
#method of set
collection2.add(1)
collection2.add(2)
collection2.add("Hieee")
print(collection2)
collection2.remove(1)
print(collection2)
collection2.add((11,22,33,"biee"))
print(collection2)
print(len(collection2))
print(collection2.pop())
print(collection2.pop())
print(collection2)
#collection2.clear()
#print(len(collection2))

set1={1,2,3}
set2={2,3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))