#Grade student based on marks
# marks>=90,grade="A"
# 90>marks>=80,grade"B"
# 80>marks>=70,grade"C"
# 70>marks,grade"D"

mark =int( input("Enter Student marks: "))
if(mark >= 90):
    print("Grade 'A'")
elif(90 > mark>= 80 ): # elif(mark >= 80 && mark<90)
    print("Grade 'B'")
elif(80 > mark >= 70 ):
    print("Grade 'C'")  
else:
    print("Grade 'D'")



