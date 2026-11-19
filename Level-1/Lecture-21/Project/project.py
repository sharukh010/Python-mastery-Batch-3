students = [
    {
        "id": 1,
        "name": "Alex",
        "age": 13,
        "marks": None 
    },
    {
        "id": 2, 
        "name": "Bob",
        "age": 14,
        "marks": None 
    },
    {
        "id": 3, 
        "name": "Charlie",
        "age": 15,
        "marks": None 
    }
] # no student in the dictionary 
next_id = 4
subjects = ("Math","Science","Computer Science","History")

def add_student(student):
    students.append(student.copy()) 

def display_student(student): 
    for key in student: 
        print(f"{key.capitalize()}: {student[key]}")

def display_students(): 
    if len(students) == 0: 
        print("No student in database")
    else: 
        for student in students: 
            display_student(student)
            print("="*15)

def search_student(student_id: int | None = None,name: str | None = None): 
    if student_id is None: 
        for student in students: 
            if student["name"].lower() == name.lower(): 
                return student 
    elif name is None: 
        for student in students: 
            if student["id"] == student_id: 
                return student 
    return None 

menu = """
====================================
       STUDENT MANAGEMENT SYSTEM
====================================

1. Add Student
2. View All Students
3. Search Student
4. Update Student Details
5. Delete Student
6. Enter Student Marks
7. Calculate Student Grade
8. Display Class Performance
9. Display Topper
10. Display Subject Statistics
11. Generate Student Report
12. Exit"""
while True: 
    print(menu)
    choice = int(input("Enter your choice: "))
    match choice: 
        case 1: 
            print("Student Registration: ")
            name = input("Name: ")
            age = int(input("Age: "))
            student = {
                "id": next_id,
                "name": name,
                "age": age,
                "marks": None 
            }
            next_id += 1 
            add_student(student)
            print(f"Student added succesfully...")
        case 2:
            print("Students: ") 
            display_students()
        case 3: 
            print("Search a Student:")
            print("Options:")
            print("1. Search by Student ID")
            print("2. Search by student Name")
            search_choice = int(input("Enter your choice: "))
            if search_choice == 1: 
                student_id = int(input("Student ID: "))
                student = search_student(student_id=student_id)
                if student is None: 
                    print("Student Not found")
                else: 
                    display_student(student)
            else: 
                name = input("Student Name: ")
                student = search_student(name=name)
                if student is None: 
                    print("Student Not found")
                else: 
                    display_student(student)
        case 4: 
            print("Update Student Details: ")
            student_id = int(input("Student ID: "))
            student = search_student(student_id=student_id)
            if student is None: 
                print("Student does not exists")
            else: 
                print("Options:")
                print("1. Update Name")
                print("2. Update Age")
                update_choice = int(input("Enter your choice: "))
                if update_choice == 1: 
                    name = input("Student updated Name: ")
                    student["name"] = name 
                else: 
                    age = int(input("Student updated Age: "))
                    student["age"] = age 

        case 5: 
            print("Deleting a Student: ")
            student_id = int(input("Student ID: "))
            student = search_student(student_id=student_id)
            if student is None: 
                print("Student not found")
            else: 
                students.remove(student)
                print("Student deleted Successfully")

        case 6: 
            print("Marks Assignment: ")
            student_id = int(input("Student ID: "))
            student = search_student(student_id=student_id)
            if student is None: 
                print("Student does not exists")
            else: 
                print("Enter the marks (0-100)")
                count = 0
                marks = dict.fromkeys(subjects,None) 
                while count < len(subjects):  
                    print(f"Subject: {subjects[count]}")
                    score = int(input("Score: "))
                    if score < 0 or score > 100: 
                        print("Invalid marks. Please try again...")
                        continue 
                    else: 
                        marks[subjects[count]] = score 
                        count += 1 # moving to next subject
                student["marks"] = marks.copy() 
                print("Completed marks assignment")


                    