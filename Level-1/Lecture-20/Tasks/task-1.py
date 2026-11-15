menu = []
menu.append({
    "id": 1,
    "name": "Chicken Burger",
    "price": 20
})
menu.append({
    "id": 2,
    "name": "Chicken Nuggets",
    "price": 30
})
menu.append({
    "id": 3,
    "name": "Pizza",
    "price": 25
})
menu.append({
    "id": 4,
    "name": "Mushroom Pizza",
    "price": 35
})
menu.append({
    "id": 5,
    "name": "Coke",
    "price": 10
})
menu.append({
    "id": 6,
    "name": "Smoothie",
    "price": 23
})

print("Welcome to Python Restaurant!")
print("Available Menu: ")
for item in menu: 
    item_id,item_name,item_price = item.values()
    print(f"{item_id}. {item_name} - ${item_price}")

print("Order by entering the ids...")
orders = input("Enter item IDs: ")
if orders == "": 
    print("Cannot generate bill Order is empty...")
else: 
    orders = set(map(int,orders.split(",")))
    