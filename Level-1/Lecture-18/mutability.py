# name = "aryan"
# print(f"ID aryan: {id(name)}")
# name = "Vinuja"
# print(f"ID vinuja: {id(name)}")
# name[2] = "u"

# list are mutable but string is not mutable 
ages = [12,13,14]
print(f"Before ID: {id(ages)}")
ages[1] = 14 
print(f"After ID: {id(ages)}")