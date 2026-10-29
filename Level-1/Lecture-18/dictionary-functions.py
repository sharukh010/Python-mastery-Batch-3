student = {"name": "aryan","age":"13"}

# to create copy 
# student_copy = student.copy()
# print(student_copy)

# get value from dictionary 
# print(student.get("gender"))
# print(student.get())
# print(student.get("roll_no",0))

# print(student.keys()) # returns all the keys in the dictionary
# print(student.values())

# snacks = dict.fromkeys(["name","calories","price","ingredients"])
# # it will create a dictionary with None as default value 
# print(snacks)

# print(student.items())
# student.pop("age")
# print(student)
# student.popitem()
student.setdefault("gender","male")
print(student)