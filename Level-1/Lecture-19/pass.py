light = "green"

if light == "green": 
    pass 

for i in range(10): 
    pass 

def draw(shape:str): 
    pass 


def display(name:str,age:int,gender:str)->str: 
    """
    generate formated string of given details.

    Args
    - name (str) : it is the name of the person 
    - age (int)  : it is the age of the person 
    - gender (str) : it is the gender of the person (Male/Female)

    Returns
    - formated (str) : it is the formated string 

    Example 
    ```
    display("Aryan",13,"Male")
    ```
    Returns
    ```
    Name: Aryan
    Age: 13 
    Gender: Male
    ```    
    """
    formated = f"Name: {name}\nAge: {age}\nGender: {gender}"
    return formated 


# positional and keyword arguments 
# positional arguments 
# print(display("Aryan",13,"Male"))
# keyword arguments 
print(display(name="Aryan",age=13,gender="Male"))

# positional + keyword argument 

print(display("Akshaya",age=13,gender="Female"))