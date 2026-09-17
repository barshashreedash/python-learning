#WAP to find the greatset number entered by the user .
num1 = int (input("Enter 1st number :"))
num2 = int (input("Enter 2nd number :"))
num3 = int (input("Enter 3rd number :"))
if(num1 >= num2 and num1 >= num3):
    print("num 1 is greater than all 3 numbers.",num1)
elif(num2 >= num1 and num2 >= num3   )  :  
    print("num 2 is greater than all 3 numbers.",num2)
else:    
    print("num 3 is greater than all 3 numbers.",num3)