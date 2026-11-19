students = [
    {
        "id": 1,
        "name": "Alex",
        "age": 13,
        "marks": 60
    },
    {
        "id": 2, 
        "name": "Bob",
        "age": 14,
        "marks": 75
    },
    {
        "id": 3, 
        "name": "Charlie",
        "age": 15,
        "marks": 80
    }
] # no student in the dictionary 
next_id = 1 

def add_student(student):
    students.append(student.copy()) 

def display_students(): 
    if len(students) == 0: 
        print("No student in database")
    else: 
        for student in students: 
            for key in student: 
                print(f"{key.capitalize()}: {student[key]}")
            print("="*15)

# print("Student Registration: ")
# name = input("Name: ")
# age = int(input("Age: "))
# marks = int(input("Marks: "))
# student = {
#     "id": next_id,
#     "name": name,
#     "age": age,
#     "marks": marks
# }
# next_id += 1 
# add_student(student)
# print(f"Student added succesfully...")

display_students()