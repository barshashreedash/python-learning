collection = set()
collection.add(1)
collection.add(4)# adds an element
collection.add(2)
collection.add(2)
collection.add("GITAM")
collection.add((8,9,5))
collection.remove(2)#removes the elements
print(collection)
print(len(collection))
collection.clear() # empties the set
print(len(collection))
collection1 = {"hello","GITAM","coding","world","python"}
print(collection1.pop())
print(collection1.pop())#removes a random variables
set1= {1,2,3}
set2= {2,3,4}
print(set1.union(set2))#set.union(set2)-->combines both set values & returns  new 
print(set1.intersection(set2))#set.intersection(set2)-->combines common value and returns new  

