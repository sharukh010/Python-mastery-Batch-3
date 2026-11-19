def display(*names): 
    for name in names: 
        print(name)

# display("Alex","Bob","Charlie")

def display_family(*first_names,last_name):
    for name in first_names: 
        print(name,last_name)

display_family("Harry","Alex","Bob",last_name="Potter")