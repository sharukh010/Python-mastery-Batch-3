from tabulate import tabulate 
"""
Add element to list 
Display all the items in the list 
Display a single item in the list 
mark an item as purchased 
delete an item from the list 
exit
"""
shopping_list = [] 
def add_item(item: dict[str])->None:
    shopping_list.append(item)
def find_item(target: int)->dict[str]: 
    for item in shopping_list: 
        if item["id"] == target: 
            return item 
    return None 
print("Shopping List:")
options="""Options: 
1) Add an item 
2) Display all the items 
3) Display single item
4) Mark an item as purchased 
5) Delete an item 
6) Exit application
"""
item_id = 1 
while True: 
    print(options)
    choice = int(input("Enter a choice(1-6): "))
    match choice: 
        case 1: 
            print("Adding an item: ")
            name = input("Name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            item = {
                "id": item_id,
                "name": name,
                "quantity": quantity,
                "price": price,
                "purchased": False
            }
            item_id += 1 # incrementing item id so the next item will have different id 
            add_item(item)
            print("ITEM ADDED SUCCESSFULLY")
        case 2: 
            print("Displaying Items: ")
            table = tabulate(shopping_list,headers="keys",tablefmt="grid")
            print(table)
        case 3: 
            print("Item Details: ")
            target = int(input("Enter an item ID: "))
            item = find_item(target)
            if item == None: 
                print("Item not found")
            else: 
                table = tabulate([item],headers="keys",tablefmt="grid")
                print(table)
        case 4: 
            print("Marking as Purchased: ")
        case 5: 
            print("Deleting an Item: ")
        case 6: 
            print("Exiting..")
            break 
    print("#"*30)