info = {
    "key" : "value",
    "name" : "Barsha",
    "learning" : "coding",
    "subjects" : ["python","c"],
    "age" : 20, 
    "is_adult" : True,
    "marks" : 94.4
}
print(info)
print(type(info))
print(info["is_adult"]) #value access by the key name
info["name"]="Shardha" # if we want to change the key value 
info["surname"]="Khapra" # if we want to add a new key value pair 
print(info)
null_dict={}
print(null_dict)#null dictionary 