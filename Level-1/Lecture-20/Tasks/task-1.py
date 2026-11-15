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

"""
item.keys() -> ["id","name","price"]
item.values() -> [6,"Smoothie",23]
item_id,item_name,item_price = [6,"Smoothie",23]
item_id = 6 
item_name = "Smoothie"
item_price = 23 

name = "Aryan"
print("{name}") -> {name}
print(f"{name}") -> Aryan 
in normal it is treated as {name}
"""
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
    """
    "1,2,3,4,5".split(",") -> "1","2","3","4","5"
    map(function,sequence)
    it applies the function on this sequence and returns the result
    
    """
    # 1. spliting the item ids 
    # 2. converting item ids into int using map 
    # 3. removing duplicate item ids using set 
    orders = set(map(int,orders.split(",")))
    total_price = 0 
    discount_price = 0 
    final_price = 0

    for order in orders: 
        if order <1 or order >6: 
            print(f"Invalid order ID: {order}")
    
    print("Your order: ")
    for item in menu: 
        if item["id"] in orders:
            item_id,item_name,item_price = item.values() 
            print(f"{item_id}. {item_name} - $ {item_price}")
            total_price = total_price + item_price 

    if len(orders) > 3: 
        discount_price = total_price * 0.1 

    final_price = total_price - discount_price 
    print(f"Total Price: ${total_price}")
    print(f"Discount Price: ${discount_price}")
    print(f"Final Price: ${final_price}")