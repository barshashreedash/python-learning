student = {
    "name" : "Barsha",
    "subject" : {
        "phy":97,
        "chem" : 98,
        "math" : 69,
    }

}
print(student.keys()) #dict.keys() -->returns all keys
print(list(student.keys()))
print(len(list(student.keys())))
print(student.values()) # dict.values() -->returns all values
print(student.items()) # dict.items() --> returns the (key,value)pair as tuples
pairs = list((student.items()))
print(pairs[0])
print(student["name"]) # This two gives me the same values.
print(student.get("name")) # returns the key according to the values
print(student.get("name2"))#no error -->NONE
# print("Before")
# print(student["name2"]) #error
# print("After") Before the error the code is execute but after the error code isnot execute that's why we prefer getmethod().
student.update({"City": "Balasore"}) # insert the specified items to the dictionary .
print(student)
