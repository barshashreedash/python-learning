#WAP to check if a list contains a palindrome elements or not . 
list= ["M","A","A","M"]
copylist=list.copy()
copylist.reverse()
if(copylist == list):
    print("It's a palindrome ")
else:
    print("Not a palindrome ")        