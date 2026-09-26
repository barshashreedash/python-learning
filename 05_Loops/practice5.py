# print the elements the list using a loop 
nums = [1,6,7,78,89,90,5,0]
for el in nums:
    print(el)

#Search for a number x in your tuple using loop 
tup = (1,6,7,78,89,90,5,0)
x = 89 
# for el in tup:
#     if(el == x):
#         print("Found")  
#i want index no. 
idx = 0 
for el in tup:
    if(el == x ):
        print("number found at idx : ",idx)
    idx += 1       
       