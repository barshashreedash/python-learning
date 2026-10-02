f = open("demo.txt","r")
# data = f.read()
# print(data) # After reading whole file then in readline there is nothing to read so,spaces are in output. 
line1= f.readline()
print(line1)
line2= f.readline()
print(line2)
f.close()
