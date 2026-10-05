f = open("demo.txt","w")
f.write("I want to learn js tommorow 123")#Overwrites the entire file
f = open("demo.txt","a")
f.write("\n After that NextJS")
f.close()
