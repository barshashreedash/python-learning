list = [5,4,1,2,6]
list.append(8)#add one element at the end [5,4,1,2,6,8] 
print(list)
list.sort()#sorts in ascending order of the updated list
print(list)#show the updated list
print(list.sort()) # this method will changes the original list.
list1 = ['a','c', 'k','i','o']
list1.sort(reverse=True)# shorts is descending order
print(list1)
list1.reverse() # reverse the list1
print(list1)
list3 = [2,1,3]
list3.insert(1,5)#insert element in index , here we insert 5 element in the index no. 1 means before 1 elements are same but after 5 including index 1 the value are same in order  
print(list3)     
list4 = [2,1,3,1]
list4.remove(1) # remove 1st occurence of element [2,3,1]
print(list4)
list.pop(5) # remove at index 
print(list)