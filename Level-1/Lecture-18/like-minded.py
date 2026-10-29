print("Like Minded")
print("Find your buddy")

options = """
1. create an account 
2. Find your buddies
3. Exit 
"""
users = []
user_id = 1 

def get_person(target:int)->dict[str]: 
    for user in users: 
        if user["id"] == target: 
            return user 
    return None 

while True: 
    print(options)
    choice = int(input("Enter your choice(1-3): "))
    match choice: 
        case 1: 
            print("Creating account: ")
            print("Enter your details: ")
            name = input("Name: ")
            interests = set(input("Interests (seperated by ,): ").split(","))
            users.append({"id":user_id,"name":name,"interests":interests})
            print(f"Your id is {user_id}")
            user_id += 1 
        case 2: 
            print("Finding Buddies: ")
            target = int(input("Enter your ID: "))
            person = get_person(target)
            if person == None: 
                print("Person Not found")
            else: 
                print("Buddies:")
                for user in users: 
                    if person["interests"].intersection(user["interests"]) != set({}): 
                        print(user["name"])
        case 3: 
            print("Exiting...")
            break 