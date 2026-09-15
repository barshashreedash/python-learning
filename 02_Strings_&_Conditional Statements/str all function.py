str = "I am studying python from Privatecollege"
str1 = "i am studying python from Privatecollege"
print(str.endswith("ege")) #endswith function --> returns true if string ends with substr 
str1 = str1.capitalize() # capitalize function --> capitalize 1st char 
print(str1)
str2 = "My name is Barshreee Dash "
print(str2.replace("Barshreee","Barshashree")) # replace function 
print(str2.find("a")) # find function
print(str2.find("name")) # find function and return 1st index of 1st occrrer 
print(str2.find("q")) # find function --> output is -1 due to -1 is not a valid index. And -ve indexing only for slicing not for original string .
print(str.count("from"))
