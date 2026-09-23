#WAP to enter marks of 3 subjects from the user and store them in a dictonary.start with an empty dictionary and add one by one.Use subject name as key & marks as a value. 
dict = {}
x = int(input("Enter phy marks : "))
dict.update({"phy" : x})
y = int(input("Enter chem marks : "))
dict.update({"chem" : y})
z = int(input("Enter math marks : "))
dict.update({"math" : z})
print(dict)
