def hello(name): 
    return f"Hello, {name}"


names = ["Vinuja","Akshaya","Aryan"]
# output = []
# for name in names: 
#     output.append(hello(name))
# int(value)->value 
# print(value)->none 
output = list(map(hello,names))
print(output)