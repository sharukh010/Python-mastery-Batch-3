"""
Dictionary are similar to list which can hold multiple data 
the only difference is dictionary you can add you're on indexes 
in dictionary you can store the data as key-value pairs 
syntax of dictionary 
{key:value}
"""
# creation of dictionary 
person = {"name":"Vijay","age":16,"height":5.8}
# accessing elements in dictionary 
# print(person)
# print(person["age"])
# print(person["height"])
# print(person["name"])
# print(person["school"]) # this gives you error 
person["school"] = "XYZ school"
# print(person)
# print(person.keys())
# print(person.values())
# acesssing each element using keys and loops 
for key in person.keys(): 
    print(person[key])