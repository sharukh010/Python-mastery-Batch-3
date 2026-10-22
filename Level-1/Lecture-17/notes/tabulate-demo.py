# install tabulate module using command "pip install tabulate"
import tabulate 

shopping_list = [
    {"name":"apple","quantity":12,"price":60,"purchased":False},
    {"name":"Keyboard","quantity":1,"price":99,"purchased":False},
    {"name":"Chocolate","quantity":1,"price":5,"purchased":False},
    {"name":"Chips","quantity":2,"price":20,"purchased":False},
    {"name":"Coke","quantity":2,"price":20,"purchased":False},
]

table = tabulate.tabulate(shopping_list,headers="keys",tablefmt="grid")
print(table)