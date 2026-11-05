# a function is a piece of code with a name which can be accessed whenever you want 

# function definition 
# def display(name: str,age: int,gender: str): # function signature (name+parameters)
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Gender: {gender}")

"""
calling is a function when you are calling you need the other person's 
mobile number so mobile number it is the parameter for the function calling 
now without mobile number a call cannot be placed 
by this we can understand that you cannot call a function without passing its parameters 
"""
# # reusability 
# display("Vinuja",14,"Female")
# display("Aryan",13,"Male")
# display("Akshaya",13,"Female")

# print()
"""
functions without parameters: 
ex: 
a power on button doesnt take any parameters you can press / call 
it directly 


functions with parameters: 
whenever you want to change a channel in TV,Radio you need to provide the channel number 
here the change function takes a channel number as parameter 

functions which can return some data: 
ex: printout - takes the document and provide printout 
- whenever you want to share the data out side the function you will return the result / data 

functions which cannot return some data: 
ex: texting - takes data and make changes in the screen it doesn't give any in return 
- whenever you don't want to share the data outside the function you will no return anyting 

Imagine two functions in google meet 
1. Join -> you need meeting link / code 
- here meeting link / code is the parameter 
2. end -> you don't need to pass any data 
- here it doen't need any parameter
"""
def join(meeting_code: str)->None: 
    print(f"Joining meeting {meeting_code}")

def end()->None: 
    print("Ending meeting...")

def display(name:str,age:int,gender:str)->str: 
    formated = f"Name: {name}\nAge: {age}\nGender: {gender}"
    return formated 

# join("xds-ksdo-max")
# end()

text = display("Vinuja",14,"Female")
# when a function returns its output you will have more flexibility and control over the output 
text = text.replace("Vinuja","Akshaya")
text = text.replace("14","13")
print(text)